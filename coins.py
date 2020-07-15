import numpy as np
import cv2


frame = cv2.imread("coins.jpg")
frame = cv2.resize(frame, (480,640))

gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


thresh = cv2.threshold(gray, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

kernel = np.ones((5, 5), np.uint8)
closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE,
 	kernel, iterations=4)

closing_img = closing.copy()

contours, hierarchy = cv2.findContours(closing_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

total=0

for cnt in contours:
    

    area = cv2.contourArea(cnt)
   
    if area < 100:
        continue
    
    if area > 3000 and area < 4000:
        total = total + 0.5
        
    if area > 4000 and area < 5000:
        total = total + 1
    
   
    print("Toplam Tutar: "+str(total)+"TL")
    ellipse = cv2.fitEllipse(cnt)
    cv2.ellipse(frame, ellipse, (0,255,0), 2)


cv2.imshow("Morphological Closing", closing)
cv2.imshow('Contours', frame)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()




