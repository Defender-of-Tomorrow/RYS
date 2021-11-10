from header.haar_utils import *

face_cascade = cv.CascadeClassifier("haarcascade_frontalface_alt2.xml")
eye_cascade = cv.CascadeClassifier("haarcascade_eye.xml")
image, gray = preprocessing(34)
if image is None:
    raise Exception("Error READ_IMAGE")

faces = face_cascade.detectMultiScale(gray, 1.1, 2, 0, (100, 100));
if faces.any() :
    x, y, w, h = faces[0]
    face_image = image[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(face_image, 1.15, 7, 0, (25, 20))

    if len(eyes) == 2:
        face_center = (x + w//2, y + h//2)
        eye_centers  = [[x+ex+ew//2, y+ey+eh//2] for ex,ey,ew,eh in eyes]
        corr_image, corr_center = correct_image(image, face_center, eye_centers )

        rois = detect_object(face_center, faces[0])

        cv.rectangle(corr_image, rois[0], (255, 0, 255), 2)
        cv.rectangle(corr_image, rois[1], (255, 0, 255), 2)
        cv.rectangle(corr_image, rois[2], (255, 0, 0), 2)
        cv.circle(corr_image, tuple(corr_center[0]), 5, (0, 255, 0), 2)
        cv.circle(corr_image, tuple(corr_center[1]), 5, (0, 255, 0), 2)
        cv.circle(corr_image, face_center, 3, (0, 0, 255), 2)
        cv.imshow("correct_image", corr_image)
    else:
        print("No detected eyes")
else:
    cv.imshow("image", image)
cv.waitKey(0)