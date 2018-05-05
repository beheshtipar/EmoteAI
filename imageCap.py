import cv2
import string
import time

def open_cam_onboard(width, height):
    gst_str = ("nvcamerasrc ! "
               "video/x-raw(memory:NVMM), width=(int)2592, height=(int)1458, format=(string)I420, framerate=(fraction)30/1 ! "
               "nvvidconv ! video/x-raw, width=(int){}, height=(int){}, format=(string)BGRx ! "
               "videoconvert ! appsink").format(width, height)
    return cv2.VideoCapture(gst_str, cv2.CAP_GSTREAMER)

cap = open_cam_onboard(1920, 1080)
cv2.namedWindow("HackWescam2018")
ret, frame = cap.read()
img_counter = str(time.time())
img_counter = img_counter.replace('.','_')

img_name = "HackWescam_frame_{}.png".format(img_counter)
cv2.imwrite(img_name, frame)
cap.release()        




	
