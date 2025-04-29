from tkinter import *
from PIL import Image, ImageTk

class FaceRecognitionSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # -----------------------------------
        # Top Banner Images (Height: 130 pixels)
        # -----------------------------------

        # Load and resize the first image
        img1 = Image.open(r"C:\Users\KIIT\Desktop\face_recongition system\ChatGPT Image Apr 26, 2025, 10_23_56 AM.png")
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=0, y=0, width=500, height=130)

        # Load and resize the second image (Title)
        img2 = Image.open(r"C:\Users\KIIT\Desktop\face_recongition system\TITLE.png")
        img2 = img2.resize((500, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=510, y=0, width=500, height=130)

        # Load and resize the third image
        img3 = Image.open(r"C:\Users\KIIT\Desktop\face_recongition system\ChatGPT Image Apr 26, 2025, 10_26_48 AM.png")
        img3 = img3.resize((500, 130), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        f_lbl3 = Label(self.root, image=self.photoimg3)
        f_lbl3.place(x=1020, y=0, width=500, height=130)

        # -----------------------------------
        # Background Image (Below Banner)
        # -----------------------------------
        img4 = Image.open(r"C:\Users\KIIT\Desktop\face_recongition system\ad0d8f16-8480-49fc-ab26-b76ddc06332b.png")
        img4 = img4.resize((1530, 660), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=130, width=1530, height=660)

        # Title Label
        title_lbl = Label(bg_img, text="Smart Face Recognition Attendance System Software",
                          font=("sans-serif", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # -----------------------------------
        # Buttons with Images & Labels
        # -----------------------------------

        # Student Details Button
        img5 = Image.open(r"C:\Users\KIIT\Desktop\face_recongition system\d2a03de0-a62c-40c7-8a52-3ac7b12ab154.png")
        img5 = img5.resize((200, 200), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg5, cursor="hand2")
        b1.place(x=200, y=100, width=200, height=200)

        b1_1 = Button(bg_img, text="Student Details", cursor="hand2",
                      font=("Sans-serif", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=200, y=300, width=200, height=40)

        # Face Detector Button
        img6 = Image.open(r"C:\Users\KIIT\Desktop\face_recongition system\istockphoto-1138172609-612x612.png")
        img6 = img6.resize((200, 200), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b2 = Button(bg_img, image=self.photoimg6, cursor="hand2")
        b2.place(x=500, y=100, width=200, height=200)

        b2_1 = Button(bg_img, text="Face Detector", cursor="hand2",
                      font=("Sans-serif", 15, "bold"), bg="darkblue", fg="white")
        b2_1.place(x=500, y=300, width=200, height=40)

        # Attendance Details Button
        img7 = Image.open(r"C:\Users\KIIT\Desktop\face_recongition system\istockphoto-1447132233-612x612.png")
        img7 = img7.resize((200, 200), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b3 = Button(bg_img, image=self.photoimg7, cursor="hand2")
        b3.place(x=800, y=100, width=200, height=200)

        b3_1 = Button(bg_img, text="Attendance Details", cursor="hand2",
                      font=("Sans-serif", 15, "bold"), bg="darkblue", fg="white")
        b3_1.place(x=800, y=300, width=200, height=40)




        #Helpdesk
        img8 = Image.open(r"C:\Users\KIIT\Desktop\face_recongition system\7928625.png")
        img8 = img8.resize((200, 200), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b4 = Button(bg_img, image=self.photoimg8, cursor="hand2")
        b4.place(x=1100, y=100, width=200, height=200)

        b4_1 = Button(bg_img, text="Helpdesk", cursor="hand2",
                      font=("Sans-serif", 15, "bold"), bg="darkblue", fg="white")
        b4_1.place(x=1100, y=300, width=200, height=40)

        #Train face
        img9 = Image.open(r"C:\Users\KIIT\Desktop\face_recongition system\2985134-200.png")
        img9 = img9.resize((200, 200), Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b5 = Button(bg_img, image=self.photoimg9, cursor="hand2")
        b5.place(x=200, y=380, width=200, height=200)

        b5_1 = Button(bg_img, text="Train Data", cursor="hand2",
                      font=("Sans-serif", 15, "bold"), bg="darkblue", fg="white")
        b5_1.place(x=200, y=580, width=200, height=40)


         #photos face button
        img10 = Image.open(r"C:\Users\KIIT\Desktop\face_recongition system\563d0201e4359c2e890569e254ea14790eb370b71d08b6de5052511cc0352313.jpg")
        img10 = img10.resize((200, 200), Image.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b6 = Button(bg_img, image=self.photoimg10, cursor="hand2")
        b6.place(x=500, y=380, width=200, height=200)

        b6_1 = Button(bg_img, text="Photos", cursor="hand2",
                      font=("Sans-serif", 15, "bold"), bg="darkblue", fg="white")
        b6_1.place(x=500, y=580, width=200, height=40)


        #Devloper face button
        img11 = Image.open(r"C:\Users\KIIT\Desktop\face_recongition system\developer-working-icon-free-vector.png")
        img11 = img11.resize((200, 200), Image.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b7 = Button(bg_img, image=self.photoimg11, cursor="hand2")
        b7.place(x=800, y=380, width=200, height=200)

        b7_1 = Button(bg_img, text="Devloper", cursor="hand2",
                      font=("Sans-serif", 15, "bold"), bg="darkblue", fg="white")
        b7_1.place(x=800, y=580, width=200, height=40)

         #Exit face button
        img12 = Image.open(r"C:\Users\KIIT\Desktop\face_recongition system\5b33590a6b88e7972ba33358cacd3a966e50738c140565c29037ccd73bf63426.jpg")
        img12 = img12.resize((200, 200), Image.LANCZOS)
        self.photoimg12 = ImageTk.PhotoImage(img12)

        b8 = Button(bg_img, image=self.photoimg12, cursor="hand2")
        b8.place(x=1100, y=380, width=200, height=200)

        b8_1 = Button(bg_img, text="Exit", cursor="hand2",
                      font=("Sans-serif", 15, "bold"), bg="darkblue", fg="white")
        b8_1.place(x=1100, y=580, width=200, height=40)






# -----------------------------------
# Run the Application
# -----------------------------------
if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognitionSystem(root)
    root.mainloop()