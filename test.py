from sklearn.neighbors import KNeighborsClassifier
import cv2
import pickle
import numpy as np
import os
import csv
import time
from datetime import datetime
from win32com.client import Dispatch

def speak(str1):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str1)

video = cv2.VideoCapture(0)
facedetect = cv2.CascadeClassifier("data/haarcascade_frontalface_default (1).xml")

with open("data/names.pkl", "rb") as w:
    LABELS = pickle.load(w)
with open("data/faces_data.pkl", "rb") as f:
    FACES = pickle.load(f)

print("Shape of Faces matrix --> ", FACES.shape)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(FACES, LABELS)

imgBackground = cv2.imread("data/NewBack2.webp")
if imgBackground is None:
    print("Error: New background image not found!")
    exit()


camera_x = 365  # right
camera_y = 290  # down
camera_width = 350  # Width 
camera_height = 370  # Height 

COL_NAMES = ["NAME", "TIME"]

while True:
    ret, frame = video.read()
    if not ret:
        print("Error: Couldn't read from camera.")
        continue

    frame_resized = cv2.resize(frame, (camera_width, camera_height))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        crop_img = frame[y:y + h, x:x + w, :]
        resized_img = cv2.resize(crop_img, (50, 50)).flatten().reshape(1, -1)
        output = knn.predict(resized_img)
        ts = time.time()
        date = datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
        timestamp = datetime.fromtimestamp(ts).strftime("%H:%M-%S")
        exist = os.path.isfile("Attendance/Attendance_" + date + ".csv")
        cv2.rectangle(frame_resized, (x, y), (x + w, y + h), (0, 0, 255), 1)
        cv2.rectangle(frame_resized, (x, y), (x + w, y + h), (50, 50, 255), 2)
        cv2.rectangle(frame_resized, (x, y - 40), (x + w, y), (50, 50, 255), -1)
        cv2.putText(frame_resized, str(output[0]), (x, y - 15), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)
        attendance = [str(output[0]), str(timestamp)]
    

    imgBackground[camera_y:camera_y + camera_height, camera_x:camera_x + camera_width] = frame_resized
    cv2.imshow("Frame", imgBackground)
    
    k = cv2.waitKey(1)
    if k == ord('o'):
        speak("Attendance Taken..")
        time.sleep(5)
        if not os.path.exists("Attendance"):
            os.makedirs("Attendance")
        if exist:
            with open("Attendance/Attendance_" + date + ".csv", "+a") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(attendance)
        else:
            with open("Attendance/Attendance_" + date + ".csv", "+a") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(COL_NAMES)
                writer.writerow(attendance)
    if k == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
