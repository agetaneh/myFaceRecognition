"""
ECE196 Face Recognition Project
Author: W Chen

Adapted from:
http://www.pyimagesearch.com/2015/03/30/accessing-the-raspberry-pi-camera-with-opencv-and-python/

Use this code as a template to process images in real time, using the same techniques as the last challenge.
You need to display a gray scale video with 320x240 dimensions, with box at the center
"""


# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import argparse

imNum = 0
def detectAndDisplay(frame):
    global imNum
    faces = face_cascade.detectMultiScale(frame)
    for (x,y,w,h) in faces:
        frame = cv2.rectangle(frame,(x, y+h), ( x+w, y),(255,255,255), 0)
         
        faceROI = frame[y:y+h,x:x+w]
        cv2.imwrite('/home/pi/myFaceRecognition/Data/Validation/18/{0:03d}.jpg'.format(imNum),faceROI)
        imNum += 1
    cv2.imshow('Capture - Face detection', frame)
 
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.color_effects = (128,128)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

# allow the camera to warmup
time.sleep(0.1)
number = 0

# Face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

#Load the cascades
  
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    image = frame.array

    # Resize the image
    image = cv2.resize(image, (160,120), interpolation=cv2.INTER_AREA)

    # Drawing rectangle on image
    #image = cv2.rectangle(image, (30,10), (130, 110), (255,255,255), 4)
    
    detectAndDisplay(image)
    # show the frame
    #cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF


    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break

   
