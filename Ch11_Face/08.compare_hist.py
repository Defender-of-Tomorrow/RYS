from header.haar_utils import *
from header.haar_histogram import *

face_cascade = cv.CascadeClassifier("haarcascade_frontalface_alt2.xml")
eye_cascade = cv.CascadeClassifier("haarcascade_eye.xml")
image, gray = preprocessing(34)
if image is None: 
    raise Exception("Error READ_IMAGE")

faces = face_cascade.detectMultiScale(gray, 1.1, 2, 0, (100, 100));
if faces.any():
    x, y, w, h = faces[0]
    face_image = image[y:y + h, x:x + w]
    eyes = eye_cascade.detectMultiScale(face_image, 1.15, 7, 0, (25, 20))

    if len(eyes) == 2:
        face_center = (x + w // 2, y + h // 2)
        eye_centers = [(x + ex + ew // 2, y + ey + eh // 2) for ex, ey, ew, eh in eyes]
        corr_image, corr_center = correct_image(image, face_center, eye_centers)

        rois = detect_object(face_center, faces[0])
        masks = make_masks(rois, corr_image.shape[:2])
        sim = calc_histo(corr_image, rois, masks)

        print("lip-face sim: %4.2f" % sim[0])
        print("top-down hair sim: %4.2f" % sim[1])
    else:
        print("Not detected eyes")
else:
    print("Not detected face")