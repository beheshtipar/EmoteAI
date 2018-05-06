import cv2
import glob

faceDet = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
faceDet_two = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
faceDet_three = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
faceDet_four = cv2.CascadeClassifier("haarcascade_frontalface_alt_tree.xml")

emotions = ["neutral", "anger", "contempt", "disgust", "fear", "happy", "sadness", "surprise"]

def process_faces(emotion):
    print("====Detecting: " + emotion)
    pathway = "sorted_set/%s/*" %emotion
    print(pathway)
    files = glob.glob(pathway)
    
    filenumber = 0
    for f in files:
        print("File: " + f)
        frame = cv2.imread(f)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
       
        face = faceDet.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10, minSize=(5, 5), flags=cv2.CASCADE_SCALE_IMAGE)   
        face_two = faceDet_two.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10, minSize=(5, 5), flags=cv2.CASCADE_SCALE_IMAGE)
        face_three = faceDet_three.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10, minSize=(5, 5), flags=cv2.CASCADE_SCALE_IMAGE)
        face_four = faceDet_four.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10, minSize=(5, 5), flags=cv2.CASCADE_SCALE_IMAGE)

        if len(face) == 1:
            facefeatures = face
        elif len(face_two) == 1:
            facefeatures = face_two
        elif len(face_three) == 1:
            facefeatures = face_three
        elif len(face_four) == 1:
            facefeatures = face_four
        else:
            facefeatures = ""
       
        for (x, y, w, h) in facefeatures: 
            print ("face found in file: " + str(f))
            gray = gray[y:y+h, x:x+w]
           
            try:
                out = cv2.resize(gray, (400, 400)) 
                cv2.imwrite("dataset/%s/%s.jpg" %(emotion, filenumber), out)
            except:
                pass
        filenumber += 1

for emotion in emotions:
    process_faces(emotion)
