from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np

DEBUG = True

cam = PiCamera()

cam.resolution=(500,250)
center = (300/2,150/2)
#640 480

#FEAT DEL
img1 = cv2.imread('trash.png',0)
img1 =cv2.resize(img1,(300,150),interpolation=cv2.INTER_AREA)
img2 = cv2.imread('pic.png',0)
orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(img1,None)

#/FEAT DEL
cam.vflip = False
#cam.exposure_mode = 'sports'
#cam.framerate = 20
#cam.shutter_speed = 20000
cam.exposure_mode='antishake'
#cam.iso = 8
cam.awb_mode='auto'
#cam.vlip = True

#cam.shutter_speed = 0
#cam.exposure_mode = 'off'
#g= cam.awb_gains
#cam.awb_mode  = 'off'
#cam.awb_gains = g
#print(str(cam.shutter_speed))
#print(str(cam.awb_gains))
raw= PiRGBArray(cam)
time.sleep(0.1)


time.sleep(0.1)
cam.capture(raw,format="bgr")
frame = raw.array
#cam.saturation=100

raw.truncate(0)

kernal = np.ones((5,5),np.uint8)
kernal1 = np.ones((1,1),np.uint8)
kernals = np.ones((2,2),np.uint8)
for fram in cam.capture_continuous(raw,format='bgr',use_video_port=True):
   
    frame =  fram.array
    
    frame = cv2.medianBlur(frame,3)
    
    timer = cv2.getTickCount()
    #frame = cv2.medianBlur(frame,5)
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    #FEAT DEL
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
   
    kp2, des2 = orb.detectAndCompute(gray,None)
    
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    
    if des2 is not None:
        matches = bf.match(des1,des2)
        matches = sorted(matches, key = lambda x:x.distance)
        frame = cv2.drawMatches(img1,kp1,gray,kp2,matches[:10],None, flags=2)
        
    #/FEAT DEL
    #LASER
   # l = np.array([(int)(0.989*180),   0,   (int)(0.894*255)])
   #u=np.array([180,   (int)(0.119*255),   255])
   # l = np.array([(int)(0.139*180),   0,   (int)(0.597*255)])
  #  u=np.array([(int)(0.416*180),   (int)(0.175*255),   255])
    #l1 = np.array([0,   0,   (int)(0.894*255)])
    #u1=np.array([(int)(0.465*180),   (int)(0.119*255),   255])
  #  print(str(cam.shutter_speed))
  #  print(str(cam.awb_gains))
    
    #l = np.array([70,10,180])
    #u=np.array([85,255,255])
 #   mask = cv2.inRange(hsv,l,u)
    #mask1 = cv2.inRange(hsv,l1,u1)
    #mask = cv2.bitwise_or(mask,mask1)
    
    #mask=cv2.dilate(mask,kernal)
    #mask = cv2.erode(mask,kernal1)
  #  mmmask=mask
  #  masked = cv2.bitwise_and(frame,frame,mask=mask)
  #  im2, contours, hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
  #  if len(contours) > 0:
 #       roundest = max(contours,key = lambda p: cv2.contourArea(p)/cv2.arcLength(p,True) if cv2.arcLength(p,True) != 0 else 0)
 #       cv2.drawContours(frame, roundest, 0, (255,0,0), 2)
    #LASER
 
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);
    

            # Tracking success
        #p1 = (int(bbox[0]), int(bbox[1]))
        #p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        #cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1)
    if DEBUG:
        cv2.putText(frame, "FPS : " + str(int(fps)), (50,50), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (50,170,50), 1)
    
    #frame = cv2.resize(frame,(640,480),interpolation=cv2.INTER_AREA)
        # Display result
    if DEBUG:
        frame = cv2.resize(frame,(640,480))
        cv2.imshow("Tracking", frame)
      #  cv2.imshow("masked", masked)
    
    raw.truncate(0)
        # Exit if ESC pressed
    k = cv2.waitKey(1) & 0xff
    if k == 27 : break

