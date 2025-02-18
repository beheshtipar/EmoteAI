import cv2
import glob
import random
import os
import numpy as np

emotions = ["neutral", "anger", "disgust", "happy", "surprise"] #Emotion list
fishface = cv2.createFisherFaceRecognizer() #Initialize fisher face classifier

data = {}

def get_files(emotion): #Define function to get file list, randomly shuffle it and split 80/20
   files = glob.glob("dataset/%s/*" %emotion)
   random.shuffle(files)
   training = files[:int(len(files)*0.8)] #get first 80% of file list
   prediction = files[-int(len(files)*0.2):] #get last 20% of file list
   return training, prediction

def make_sets():
    training_data = []
    training_labels = []
    prediction_data = []
    prediction_labels = []
    for emotion in emotions:
        training, prediction = get_files(emotion)
        #Append data to training and prediction list, and generate labels 0-7
        for item in training:
            image = cv2.imread(item) #open image
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #convert to grayscale
            training_data.append(gray) #append image array to training data list
            training_labels.append(emotions.index(emotion))
   
        for item in prediction: #repeat above process for prediction set
            image = cv2.imread(item)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            prediction_data.append(gray)
            prediction_labels.append(emotions.index(emotion))

    return training_data, training_labels, prediction_data, prediction_labels

def run_recognizer():
   training_data, training_labels, prediction_data, prediction_labels = make_sets()
   
   print "size of training set is:", len(training_labels), "images"
   fishface.train(training_data, np.asarray(training_labels))

   print "predicting classification set"
   cnt = 0
   correct = 0
   incorrect = 0
   for image in prediction_data:
       pred, conf = fishface.predict(image)
       if pred == prediction_labels[cnt]:
           correct += 1
           cnt += 1
       else:
           diffPath = ("difficult/" + str(emotions[prediction_labels[cnt]]) + "_" + str(emotions[pred]) + "_" + str(cnt) + ".jpg")
           print(diffPath)
           
           cv2.imwrite("difficult/%s_%s_%s.jpg" %(emotions[prediction_labels[cnt]], emotions[pred], cnt), image)
           incorrect += 1
           cnt += 1
   return ((100*correct)/(correct + incorrect))

#Now run it
metascore = []
trainingRuns = 12
for i in range(0, trainingRuns):
    print("Run: " + str(i) + "/" + str(trainingRuns))
    correct = run_recognizer()
    print str(correct) + "% correct"
    metascore.append(correct)

fishface.save("trainedML.xml")
print "\n\nend score:", np.mean(metascore), "% correct"
