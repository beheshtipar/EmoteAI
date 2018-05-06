# Hack-Wescam-2018

A collaborative facial recogition and emotion processing project by Parsa Beheshti, Lawrence Liu, Adrian Salvatore, and Natasha Varghese, completed at HackWescam 2018.

## Motivation/Background
In light of the growth in popularity of Artifical Intelligence (AI) and improvements in the field of Image Processing in the last few years, many institutions are optimizing their operations using these technologies to enhance the productivity of current employees' operations or make them autonomous with minimal human supervision. Inspired by the theme of the Hackathon and the technological focus of L3 Wescam, a project combining the strengths of AI and Image Processing was chosen to be pursued.

## Hack Overview
<name> is a facial detection and recognition program with an additional capibility to analyze the expression of the face detected and determine the emotion of the human using a pre-trained Cascade Classifier data set.
  
## Dependencies
This project was written in Python 3.x, and uses the Open Source Computer Vision (OpenCV) libraries. Early iterations of the hack were ran successfully on OpenCV 3.4.0, but the facial recognition portion of the program only ran sucessfully using OpenCV 4.0.0.

## Summary
The machine has been trained to distinguish 5 different emotions 'Neutral', 'Anger', 'Disgust', 'Happy' and 'Surprise'.
We ultizlied the pre-made OpenCV cascasde to pre-process the dataset (Fisherfaces algotheriem has also been applied)

The raw data (Facial photos) has been collected from Internet. Before the pre-processing, the raw data will be manually classfied into 5 different pre-defined moods. In order to raise the training accuracy, there is a script written to crop and gray style all the training photos. The training script is written in Python leveraging OpenCV Models and Fisherface algorithem to determine the emotion of the input photos. 


## Future Benefits 


