# EmoteAI

A collaborative facial recognition and emotion processing project by Parsa Beheshti, Lawrence Liu, Adrian Salvatore, and Natasha Varghese, completed at HackWESCAM 2018.

## Motivation/Background

In light of the growth in popularity of Artificial Intelligence (AI) and improvements in the field of Image Processing in the last few years, many institutions are optimizing their operations using these technologies to enhance the productivity of current employees' operations or make them autonomous with minimal human supervision. Inspired by the theme of the Hackathon and the technological focus of L3 Wescam, a project combining the strengths of AI and Image Processing was chosen to be pursued.

## Hack Overview

EmoteAI is a facial detection and recognition program with an additional capability to analyze the expression of the face detected and determine the emotion of the human using a pre-trained Cascade Classifier data set. 

The algorithm has been trained to distinguish 5 different emotions: 'Neutral, 'Anger', 'Disgust', 'Happy' and 'Surprise'. We utilized the Haas Cascade Classifier to pre-process the photos and crop them. This reduces noise that could be picked up by the Fisherfaces algorithm that is used for training and detection of emotions. After cropping, the images are converted into greyscale before they are used to train the Fisherfaces algorithm.

Facial photo raw data was collected from the internet, and was manually sorted into the pre-defined moods. During training of the algorithm, erronous sorting by the algorithm was manually re-classified and used to re-train the algorithm in order to achieve a higher degree of accuracy.

## Potential Applicaitons

EmoteAI's concept can be applied to a wide variety of settings:

- **Self-Checkout POS Terminals**: A large number of restaurants and supermarkets have been adding self-checkout point-of-sale (POS) terminals to their locations. Since this is new technology, there can be a number of flaws that will degrade the user's experience. Installing this technology at these terminals can help identify where improvements can be made to the software, and by extension, the user's experience.

- **Body Cameras for Police Officers**: In an effort to maintain consistency in criminal proceedings, demand for police officers to wear body cameras is at an all-time high. Furthermore, with AI and image processing technology improving, there is potential for this technology to be used to enhance the tools available to the police; Using image processing to determine further information about persons in the frame of the video feed from their body camera. This could allow the officer on-site to make more informed decisions and maximize non-lethal methods of de-escalation.   

## Dependencies
This project was written in Python 3.x, and uses the Open Source Computer Vision (OpenCV) libraries. Early iterations of the hack were ran successfully on OpenCV 3.4.0, but the facial recognition portion of the program only ran successfully using OpenCV 2.4.9.1.


