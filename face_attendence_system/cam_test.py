import cv2

cam= cv2.VideoCapture(0)
cam.set(3,1280)
cam.set(4,720)
while True:
    suc,ima = cam.read()
    cv2.imshow("Face attend",ima)
    cv2.waitKey(1)