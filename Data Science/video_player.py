import cv2

filepath=r'C:'
video= cv2.VideoCapture(0)
while True:
    status,frame =video.read()
    if not status:
        break
    cv2.imshow('webcam 0',frame)
    if cv2.waitKey(1)==ord('q'):
        break

video.release()
cv2.destroyAllWindows()

