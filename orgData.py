import glob
import os
from shutil import copyfile

print("======PROGRAM START======")

emotions = ["neutral", "anger", "contempt", "disgust", "fear", "happy", "sadness", "surprise"]

participants = glob.glob("source_emotion/*") 

items = len(participants)

print("Identified " + str(items) + " items to parse")

print("======PARSING START======")
for x in participants:
    part = "%s" %x[-4:]
    for sessions in glob.glob("%s/*" %x):
        for files in glob.glob("%s/*" %sessions):
            current_session = files[20:-30]
            sfile = open(files, 'r')
            
            emotion = int(float(sfile.readline()))
            
            sourcefile_emotion = glob.glob("source_images/%s/%s/*" %(part, current_session))[-1]
            sourcefile_neutral = glob.glob("source_images/%s/%s/*" %(part, current_session))[0]
            
            dest_neut = "sorted_set/neutral/%s" %sourcefile_neutral[30:]
            dest_emot = "sorted_set/%s/%s" %(emotions[emotion], sourcefile_emotion[30:])
            
            copyfile(sourcefile_neutral, dest_neut)
            copyfile(sourcefile_emotion, dest_emot)


print("======PARSING END======")
print("======PROGRAM END======")


