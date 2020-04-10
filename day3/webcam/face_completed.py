## Realtime face detection with webcam and opencv

#import packages
import cv2
import sys

# initialize detection variable
detect = 0

# load cascade file
cascPath = 'haarcascade_frontalface_default.xml'
cascade = cv2.CascadeClassifier(cascPath)

#start video capture
video_capture = cv2.VideoCapture(0)

# loop the caputre till keypress 
while True:
    # Capture frame-by-frame  and covert to gray scale
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # run the detectmutliscale function
    detect = cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30))
        
    # Draw a rectangle around the faces
    if len(detect) > 0:
        for (x, y, w, h) in detect:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            
    # Display the resulting frame
    cv2.imshow('Video', frame)

    # press q for 1 sec to stop the application
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
