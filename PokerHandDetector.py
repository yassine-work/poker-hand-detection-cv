from ultralytics import YOLO
import cv2
import cvzone
import math
import torch
import PokerHandFunction

print("CUDA Available:", torch.cuda.is_available())

cap=cv2.VideoCapture(1)  #for webcam
cap.set(3, 1280)
cap.set(4, 720)
cap.set(cv2.CAP_PROP_FPS, 15)  # Lower FPS to reduce processing

#cap=cv2.VideoCapture("../videos/motorbikes-1.mp4")    #for videos
model=YOLO("../models/playingCards.pt").to('cuda')
classNames= ['10C', '10D', '10H', '10S', '2C', '2D', '2H', '2S', '3C', '3D', '3H', '3S', '4C', '4D', '4H', '4S', '5C', '5D', '5H', '5S', '6C', '6D', '6H', '6S', '7C', '7D', '7H', '7S', '8C', '8D', '8H', '8S', '9C', '9D', '9H', '9S', 'AC', 'AD', 'AH', 'AS', 'JC', 'JD', 'JH', 'JS', 'KC', 'KD', 'KH', 'KS', 'QC', 'QD', 'QH', 'QS']
myColor=(0,0,255)


while True:
    success,img=cap.read()
    results=model(img,stream=True)#stream for optimisation
    hand = []
    for r in results:
        boxes=r.boxes
        for box in boxes:
            #Bounding Box
            x1,y1,x2,y2=box.xyxy[0]
            x1, y1, x2, y2=int(x1),int(y1),int(x2),int(y2)
            # print(x1,y1,x2,y2)
            # cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,255),3)
            w,h=x2-x1,y2-y1
            cvzone.cornerRect(img,(x1,y1,w,h))
            # Confidence
            conf=math.ceil((box.conf[0]*100))/100
            #class name
            cls=int(box.cls[0])
            cvzone.putTextRect(img,f'{classNames[cls]} {conf}',(max(0,x1),max(35,y1-35)),
            1, 1, offset = 5, colorB = myColor,
            colorT = (255, 255, 255), colorR = myColor)
            if conf > 0.5:
                hand.append(classNames[cls])


    hand=list(set(hand))
    if len(hand)==5:
        res=PokerHandFunction.find_poker_hand(hand)
        print(res)
        cvzone.putTextRect(img, f'Your Hand:{res} ', (300, 75),
                           3, 5)
    cv2.imshow("Image",img)
    cv2.waitKey(1)

