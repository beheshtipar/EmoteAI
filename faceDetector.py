import sys
import cv2


def open_cam_onboard(width, height):
    gst_str = ("nvcamerasrc ! "
               "video/x-raw(memory:NVMM), width=(int)640, height=(int)480, format=(string)I420, framerate=(fraction)24/1 ! "
               "nvvidconv ! video/x-raw, width=(int){}, height=(int){}, format=(string)BGRx ! "
               "videoconvert ! appsink").format(width, height)
    return cv2.VideoCapture(gst_str, cv2.CAP_GSTREAMER)

def new_window(windowName,width,height):
	cv2.namedWindow(windowName, cv2.WINDOW_NORMAL)
	cv2.resizeWindow(windowName, width, height)
	cv2.moveWindow(windowName, 0, 0)
	cv2.setWindowTitle(windowName, "HackWescam 2018")


def main():
	
	windowName = 'HackWescam_demo'
	width = 640
	height = 480

	faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

	video_capture = open_cam_onboard(width, height)
	
	new_window(windowName, width, height)
	
	showHelp = True
	showFullScreen = False
	helpText = "'Q' to Quit, 'H' to Toggle Help, 'F' to Toggle Fullscreen"
	font = cv2.FONT_HERSHEY_PLAIN
	
	

	while True:
		if cv2.getWindowProperty(windowName, 0) < 0: 
			break;
		ret, frame = video_capture.read()
		if showHelp == True:
			cv2.putText(frame, helpText, (11,20), font, 1.0, (32,32,32), 4, cv2.LINE_AA)
			cv2.putText(frame, helpText, (10,20), font, 1.0, (240,240,240), 1, cv2.LINE_AA)
		
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		#cv2.imshow('frame', gray)
		
		faces = faceCascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5,minSize=(10,10))
		
		# Draw a rectangle around the faces
		for (x,y,w,h) in faces:
			cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0),2)
			
		# Display frame
		cv2.imshow(windowName, frame)
		
		key = cv2.waitKey(10)
		if key == ord('Q') or key == ord('q') or key == 27: # Q key: quit program
			break
		elif key == ord('H') or key == ord('h'): # toggle help message
			showHelp = not showHelp
		elif key == ord('F') or key == ord('f'): # toggle fullscreen
			showFullScreen = not showFullScreen
			if showFullScreen == True: 
				cv2.setWindowProperty(windowName, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
			else:
				cv2.setWindowProperty(windowName, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_NORMAL) 
			
	video_capture.release()
	cv2.destroyAllWindows()

main()
	
