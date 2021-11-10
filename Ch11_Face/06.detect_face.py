import cv2 as cv
import numpy as np

def preprocessing(no):
    image = cv.imread("images/face/%2d.jpg" %no, cv.IMREAD_COLOR)
    if image is None:
        return None, None
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    gray = cv.equalizeHist(gray)
    return image, gray

face_cascade = cv.CascadeClassifier("haarcascade_frontalface_alt2.xml")
eye_cascade = cv.CascadeClassifier("haarcascade_eye.xml")
image, gray = preprocessing(34)
if image is None:
    raise Exception("Error READIMAGE")

faces = face_cascade.detectMultiScale(gray, 1.1, 2, 0, (100, 100))
if(faces.any()):
    x, y, w, h = faces[0]
    face_image = image[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(face_image, 1.15, 7, 9, (25, 20))
    if len(eyes) == 2:
        for ex, ey, ew, eh in eyes:
            center = (x + ex + ew//2, y + ey + eh//2)
            cv.circle(image, center, 10, (0, 255, 0), 2)
    else:
        print("Not detected eyes")
        
    cv.rectangle(image, faces[0], (255, 0, 0), 2)
    cv.imshow("image", image)
else:
    print("Not detected face")
    
cv.waitKey()