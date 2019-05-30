from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
import numpy as np
import cv2
import datetime
from tkinter import messagebox

def getImage():
    filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    return filename

def destroyPanel():
    panel.destroy()
    panel.pack_forget()
    print("control in destroyPanel function\n")

def saveImage():
    try:
        img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        file = filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        print(file)
        cv2.imwrite(file,img)
        print("image saved")
    except:
        messagebox.showinfo("Message", "first browse an image using Browse Image button")
def proceessImage():
    messagebox.showinfo("Message", "If you are pressing this button for second time, first press the Delete Image button")
    filename = getImage()
    print(filename)
    if filename:                                   
        img = cv2.imread(filename)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cascPath = "haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + cascPath)
        faces = faceCascade.detectMultiScale(gray,1.1,5)
        for (i,(x, y, w, h)) in enumerate(faces):
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(img, "{}#".format(i + 1), (x - 4, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 255, 0), 2)

        global image
        image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        img = Image.fromarray(image)
        img = img.resize((500, 400), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        global panel
        panel = Label(window, image = img)
        panel.image = img
        panel.place(x=0, y=0)
        panel.pack()
        

if __name__ == '__main__':
    window = Tk()
    window.iconbitmap('face-detection.ico')
    window.title("Face Detection")
    
    btn1 = Button(window, text = "Browse Image",activebackground="#2896F6",command=proceessImage)
    btn1.pack()
    btn1.place(x=100,y=450)
    btn2 = Button(window, text = "Delete Image",activebackground="#2896F6",command=destroyPanel)
    btn2.pack()
    btn2.place(x=200,y=450)
    btn3 = Button(window, text = "Save Image",activebackground="#2896F6",command=saveImage)
    btn3.pack()
    btn3.place(x=300,y=450)
    window.geometry("505x500")
    window.resizable(False, False)
    window.mainloop()
