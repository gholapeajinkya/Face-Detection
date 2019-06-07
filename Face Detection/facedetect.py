# Face detecting by giving an image as input
import cv2
#import sys

imagePath = "selena.jpg"
cascPath = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"

# Creating the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Reading the image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
    #flags = cv2.cv.CV_HAAR_SCALE_IMAGE
)

print("Found {0} faces!".format(len(faces)))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Faces", image)
cv2.waitKey(0)
