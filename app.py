import cv2
from tracking import *

tracker = find_eucledian_dist()

cap = cv2.VideoCapture(r"C:\Users\jayas\Downloads\object_tracking\highway.mp4")

if not cap.isOpened():
    print("Please load the File")
    exit()

background_remover = cv2.createBackgroundSubtractorMOG2(varThreshold = 40,history = 100)

while True:
    ret,frame = cap.read()

    if not ret:
        print("Frame is Not Loaded")
        break

    roi = frame[340:720,500:800]
    mask = background_remover.apply(roi)
    _,mask = cv2.threshold(mask,200,255,cv2.THRESH_BINARY)
    boundaries,_ = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    detections = []

    for cnt in boundaries:
        area = cv2.contourArea(cnt)
        if area > 100:
            x,y,w,h = cv2.boundingRect(cnt)
            detections.append([x,y,w,h])

    box_id = tracker.update(detections)
    for id1 in box_id:
        x,y,w,h,id = id1
        cv2.putText(roi,f"{id}",(x,y-15),cv2.FONT_HERSHEY_PLAIN,2,(255,255,0),2)
        cv2.rectangle(roi,(x,y),(x+w,y+h),(255,0,0),3)
    
    cv2.imshow("Region of Intrest",roi)
    cv2.imshow("original frame",frame)
    cv2.imshow("Mask or Background",mask)

    if cv2.waitKey(30) == 27:
        break
        
cap.release()
cv2.destroyAllWindows()
