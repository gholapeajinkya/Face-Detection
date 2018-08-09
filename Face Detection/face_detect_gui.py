#Author: Ajinkya Gholape
#Face Detection using opencv & tkinter

from Tkinter import *
from PIL import Image
from PIL import ImageTk
import tkFileDialog
import cv2

def select_image():
	#background color
	color="#00ff00"
	#background color
	lcolor="#ffffcc"
	cascPath = "haarcascade_frontalface_default.xml"
	global panelA, panelB
	path = tkFileDialog.askopenfilename()
	
	
	if len(path) > 0:
		image = cv2.imread(path)
		rimage = cv2.imread(path)
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		
		faceCascade = cv2.CascadeClassifier(cascPath)
		faces = faceCascade.detectMultiScale(
		gray,
		scaleFactor=1.1,
		minNeighbors=5,
		minSize=(30, 30)
		    #flags = cv2.cv.CV_HAAR_SCALE_IMAGE
		)
		# Draw a rectangle around the faces
		for (i,(x, y, w, h)) in enumerate(faces):
			cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
			cv2.putText(image, "{}#".format(i + 1), (x - 4, y - 10),
			cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 255, 0), 2)

		
		image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
		rimage = cv2.cvtColor(rimage, cv2.COLOR_BGR2RGB)
		# convert the images to PIL format...
		image = Image.fromarray(image)
		rimage = Image.fromarray(rimage)
		#edged = Image.fromarray(edged)

		# ...and then to ImageTk format
		image = ImageTk.PhotoImage(image)
		rimage = ImageTk.PhotoImage(rimage)
		#edged = ImageTk.PhotoImage(edged)
	
		# if the panels are None, initialize them
		if panelA is None or panelB is None:
			# the first panel will store our original image
			lo = Label(text="Original Image",font=("Helvetica", 16),fg=color, bg=lcolor)
			lo2 = Label(text="Face Detected Image", font=("Helvetica", 16),fg=color, bg=lcolor)
			lo2.pack(pady=25)
			lo2.place(x=1400,y=0)
			panelA = Label(image=rimage)
			panelA.image = rimage
			panelA.lo=lo.pack(padx=200, expand="yes",side="top")
			lo.place(x=400,y=0)
			panelA.pack(side="left", padx=20, pady=50, expand="yes")
			# while the second panel will store the edge map
			panelB = Label(image=image)
			panelB.image = image
			#panelB.lo2=lo2.pack(expand="yes",side="top")
			panelB.pack(side="right", padx=20, pady=50, expand="yes")

		# otherwise, update the image panels
		else:
			# update the pannels
			panelA.configure(image=image)
			panelB.configure(image=image)
			panelA.image = image
			panelB.image = image

# initialize the window toolkit along with the two image panels
root = Tk()
panelA = None
panelB = None
#background color
bgcolor="#ffffcc"

root.configure(background=bgcolor)
root.resizable(FALSE,FALSE)

# create a button, then when pressed, will trigger a file chooser
# dialog and allow the user to select an input image; then add the
# button the GUI
btn = Button(root, text="Select an image", command=select_image, fg="red", bg="skyblue",font=("Helvetica", 16))
btn.pack(side="bottom", fill="both", padx="10", pady="10", expand="yes")

# kick off the GUI
root.mainloop()


