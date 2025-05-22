import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk
import cv2
import numpy as np
import os
import uuid
from supabase import create_client, Client

# Initialize Supabase client
SUPABASE_URL = "https://fjcmkchoonqougedgbtv.supabase.co"  # Replace with your Supabase URL
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZqY21rY2hvb25xb3VnZWRnYnR2Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDc4OTY4NDcsImV4cCI6MjA2MzQ3Mjg0N30.YR0NtZWzgjCrgLPXziLBs7Tt4RhDhvP4v5UckdvJPnc"     # Replace with your API Key

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Directory to store images
IMAGE_DIR = "student_images"
os.makedirs(IMAGE_DIR, exist_ok=True)

class StudentManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition Student Management System")
        self.root.geometry("900x600")

        # ========== GUI Layout ==========
        title = tk.Label(root, text="Student Management System", font=("Helvetica", 20, "bold"))
        title.pack(pady=10)

        frame = tk.Frame(root)
        frame.pack(pady=10)

        # Labels & Entries
        tk.Label(frame, text="Student ID").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        tk.Label(frame, text="Name").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        tk.Label(frame, text="Email").grid(row=2, column=0, padx=10, pady=5, sticky="w")

        self.entry_id = tk.Entry(frame, width=30)
        self.entry_name = tk.Entry(frame, width=30)
        self.entry_email = tk.Entry(frame, width=30)

        self.entry_id.grid(row=0, column=1, padx=10)
        self.entry_name.grid(row=1, column=1, padx=10)
        self.entry_email.grid(row=2, column=1, padx=10)

        # Buttons
        tk.Button(frame, text="Add Student", command=self.add_student).grid(row=3, column=0, pady=10)
        tk.Button(frame, text="Capture Face", command=self.capture_face).grid(row=3, column=1, pady=10)
        tk.Button(frame, text="Train Model", command=self.train_model).grid(row=4, column=0, pady=10)
        tk.Button(frame, text="Recognize Face", command=self.recognize_face).grid(row=4, column=1, pady=10)

        # Student Table
        self.tree = ttk.Treeview(root, columns=("id", "name", "email"), show='headings')
        self.tree.heading("id", text="Student ID")
        self.tree.heading("name", text="Name")
        self.tree.heading("email", text="Email")
        self.tree.pack(pady=20)

        self.fetch_students()

    def add_student(self):
        student_id = self.entry_id.get()
        name = self.entry_name.get()
        email = self.entry_email.get()

        if not student_id or not name or not email:
            messagebox.showerror("Error", "All fields are required.")
            return

        data = {
            "student_id": student_id,
            "name": name,
            "email": email
        }

        response = supabase.table("students").insert(data).execute()
        if response.status_code == 201:
            messagebox.showinfo("Success", "Student added successfully.")
            self.fetch_students()
        else:
            messagebox.showerror("Error", "Failed to add student.")

    def fetch_students(self):
        self.tree.delete(*self.tree.get_children())
        response = supabase.table("students").select("*").execute()
        for student in response.data:
            self.tree.insert("", "end", values=(student['student_id'], student['name'], student['email']))

    def capture_face(self):
        student_id = self.entry_id.get()
        if not student_id:
            messagebox.showerror("Error", "Enter Student ID to capture face.")
            return

        cam = cv2.VideoCapture(0)
        detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        count = 0

        while True:
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)

            for (x, y, w, h) in faces:
                count += 1
                face = gray[y:y+h, x:x+w]
                filename = os.path.join(IMAGE_DIR, f"{student_id}_{count}.jpg")
                cv2.imwrite(filename, face)
                cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

            cv2.imshow('Capturing Face', img)
            if cv2.waitKey(1) == 27 or count >= 20:  # ESC key
                break

        cam.release()
        cv2.destroyAllWindows()

    def train_model(self):
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        faces, ids = [], []

        for filename in os.listdir(IMAGE_DIR):
            if filename.endswith(".jpg"):
                path = os.path.join(IMAGE_DIR, filename)
                img = Image.open(path).convert('L')
                img_np = np.array(img, 'uint8')
                id_ = int(filename.split('_')[0])
                faces.append(img_np)
                ids.append(id_)

        recognizer.train(faces, np.array(ids))
        recognizer.save("trainer.yml")
        messagebox.showinfo("Info", "Model trained successfully.")

    def recognize_face(self):
        if not os.path.exists("trainer.yml"):
            messagebox.showerror("Error", "Model not trained yet.")
            return

        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read("trainer.yml")
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

        cam = cv2.VideoCapture(0)
        font = cv2.FONT_HERSHEY_SIMPLEX

        while True:
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.2, 5)

            for (x, y, w, h) in faces:
                id_, conf = recognizer.predict(gray[y:y+h, x:x+w])
                if conf < 70:
                    response = supabase.table("students").select("name").eq("student_id", str(id_)).execute()
                    name = response.data[0]["name"] if response.data else "Unknown"
                else:
                    name = "Unknown"

                cv2.putText(img, str(name), (x, y-10), font, 0.75, (255, 255, 255), 2)
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

            cv2.imshow("Recognizing Face", img)
            if cv2.waitKey(10) & 0xFF == 27:
                break

        cam.release()
        cv2.destroyAllWindows()

# Launch app
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManagementSystem(root)
    root.mainloop()
