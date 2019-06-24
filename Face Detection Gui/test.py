from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
import numpy as np
import cv2
from tkinter import messagebox

def getImage():
    filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    return filename

def sel(x):
    try:
        global selection
        selection = var.get()
        img = cv2.imread(filename)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cascPath = "haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + cascPath)
        faces = faceCascade.detectMultiScale(gray,selection,5)
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
    except:
        pass

    
def saveImage():
    try:
        img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        file = filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        print(file)
        cv2.imwrite(file,img)
        print("image saved")
        messagebox.showinfo("Image Saved", "Image Saved at "+file)
    except:
        pass
def proceessImage():
    global filename
    filename = getImage()
    print(filename)
    if filename:
        global img
        img = cv2.imread(filename)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cascPath = "haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + cascPath)
        faces = faceCascade.detectMultiScale(gray,1.1,5)
        for (i,(x, y, w, h)) in enumerate(faces):
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(img, "{}#".format(i + 1), (x - 4, y - 10),
	    cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 255, 0), 2)

        global var
        var = DoubleVar()
        scale = Scale(window,resolution=0.01,variable = var ,orient=HORIZONTAL,command = sel, length=300,from_=0.0, to=2.0)
        scale.place(x=90, y=420)
        scale.set(1.1)
        
        global image
        image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(image)
        img = img.resize((500, 400), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        global panel
        panel = Label(window, image = img)
        panel.image = img
        panel.place(x=0, y=0)	        

if __name__ == '__main__':
    window = Tk()
    window.iconbitmap('face-detection.ico')
    window.title("Face Detection")
    
    btn1 = Button(window, text = "Browse Image",activebackground="#2896F6",command=proceessImage)
    btn1.pack()
    btn1.place(x=100,y=500)
    btn3 = Button(window, text = "Save Image",activebackground="#2896F6",command=saveImage)
    btn3.pack()
    btn3.place(x=300,y=500)
    window.geometry("505x550")
    window.resizable(False, False)
    window.mainloop()
