import numpy as np
import cv2 as cv

def preprocessing(no):
    image = cv.imread('images/face/%02d.jpg' %no, cv.IMREAD_COLOR)
    if image is None:
        return None, None
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    gray = cv.equalizeHist(gray)
    return image, gray

def correct_image(image, face_center, eye_centers):
    pt0, pt1 = eye_centers
    if pt0[0] > pt1[0]: pt0, pt1 = pt1, pt0

    dx, dy = np.subtract(pt1, pt0).astype(float)
    angle = cv.fastAtan2(dy, dx)
    rot_mat = cv.getRotationMatrix2D(face_center, angle, 1)

    size = image.shape[1::-1]
    corr_image = cv.warpAffine(image, rot_mat, size, cv.INTER_CUBIC)

    eye_centers = np.expand_dims(eye_centers, axis=0)
    corr_centers = cv.transform(eye_centers, rot_mat)
    corr_centers = np.squeeze(corr_centers, axis=0)

    return corr_image, corr_centers

def define_roi(pt, size):
    return np.ravel([pt, size]).astype(int)

def detect_object(center, face):
    w, h = face[2:4]
    center = np.array(center)
    gap1 = np.multiply((w,h), (0.45, 0.65))
    gap2 = np.multiply((w,h), (0.20, 0.1))

    pt1 = center - gap1
    pt2 = center + gap1
    hair = define_roi(pt1, pt2-pt1)

    size = np.multiply(hair[2:4], (1, 0.4))
    hair1 = define_roi(pt1, size)
    hair2 = define_roi(pt2-size, size)

    lip_center = center + (0, h * 0.3)
    lip1 = lip_center - gap2
    lip2 = lip_center + gap2
    lip = define_roi(lip1, lip2-lip1)

    return [hair1, hair2, lip, hair]

