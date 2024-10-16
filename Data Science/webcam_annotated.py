# import cv2

# video= cv2.VideoCapture(0)
# while True:
#     status,frame =video.read()
#     #print(frame.shape)
#     #frame=cv2.resize(frame,(frame.shape[1]//2,frame.shape[0]//2))
    
#     cv2.rectangle(frame,(100,100),(200,200),(0,25,0),-1)
#     cv2.putText(frame,'Live',(120,150),
#             cv2.FONT_HERSHEY_PLAIN,2,(0,0,0),1,cv2.LINE_AA,False)
#     cv2.imshow('webcam 0',frame)
#     if cv2.waitKey(1)==ord('q'):
#         break

# video.release()
# cv2.destroyAllWindows()


import cv2

video= cv2.VideoCapture(0)
while True:
    status,frame =video.read()
    #print(frame.shape)
    #frame=cv2.resize(frame,(frame.shape[1]//2,frame.shape[0]//2))
    
    cv2.flip(frame,1,frame)

    cv2.rectangle(frame,(0,0),(frame.shape[1],40),(255,255,255),-1)

    cv2.putText(frame,'Live',(10,30),
        cv2.FONT_HERSHEY_PLAIN,2,(0,0,0),2)

    cv2.putText(frame,'webcam 0',(frame.shape[1]//2-100,30),
        cv2.FONT_HERSHEY_PLAIN,2,(120,0,230),2)

    cv2.imshow('webcam 0',frame)
    if cv2.waitKey(1)==ord('q'):
        break

video.release()
cv2.destroyAllWindows()

