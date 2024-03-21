import pandas as pd

df = pd.DataFrame({'name':[], 'enc':[]})
fname = 'features.csv'
df.to_csv(fname)
# # Import Libraries
# import cv2
# import time
# import mediapipe as mp
# # Grabbing the Holistic Model from Mediapipe and
# # Initializing the Model
# mp_holistic = mp.solutions.holistic
# holistic_model = mp_holistic.Holistic(
# 	min_detection_confidence=0.5,
# 	min_tracking_confidence=0.5
# )
# # Code to access landmarks
# for landmark in mp_holistic.HandLandmark:
# 	print(landmark, landmark.value)

# print(mp_holistic.HandLandmark.WRIST.value)