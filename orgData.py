import glob
from shutil import copyfile

emotions = ["neutral", "anger", "contempt", "disgust", "feat", "happy", "sadness", "surprise"]

participants = glob.glob("Source_emotion\\*") 

for x in participants:
    part = "%s" %x[-4:]
    for sessions in glob.glob("%s\\*" %x):
        for files in glob.glob("%s\\*" %sessions):
            current_session = files[20:-30]
            files = open(files, 'r')
