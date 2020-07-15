# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 20:51:33 2020

@author: sefa
"""


import cv2
cap = cv2.VideoCapture('videoplayback.mp4')
count = 0
while cap.isOpened():
    ret,frame = cap.read()
    frame = cv2.resize(frame, (480,640))
    cv2.imshow('window-name',frame)
    count = count + 1
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()  # destroy all the opened windows