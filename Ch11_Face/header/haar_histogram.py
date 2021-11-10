import numpy as np
import cv2 as cv

def draw_ellipse(image, roi, ratio, color, thickness=cv.FILLED):
    x, y, w, h = roi
    center = (x + w // 2, y + h // 2)
    size = (int(w * ratio), int(h * ratio))
    cv.ellipse(image, center, size, 0, 0, 360, color, thickness)
    return image

def make_masks(rois, correct_shape):
    base_mask = np.full(correct_shape, 255, np.uint8)
    hair_mask = draw_ellipse(base_mask, rois[3], 0.45, 0,  -1)
    lip_mask = draw_ellipse(np.copy(base_mask), rois[2], 0.45, 255)

    masks = [hair_mask, hair_mask, lip_mask, ~lip_mask]
    masks = [mask[y:y+h,x:x+w] for mask,(x,y, w,h) in zip(masks, rois)]

    return masks

def calc_histo(image, rois, masks):
    bsize = (64, 64,64)
    ranges = (0,256, 0,256, 0,256)

    subs = [image[y:y+h, x:x+w] for x, y, w, h in rois]
    hists = [cv.calcHist([sub], [0,1,2], mask, bsize, ranges) for sub, mask in zip(subs, masks)]
    hists = [ h/np.sum(h) for h in hists]

    sim1 = cv.compareHist(hists[2], hists[3], cv.HISTCMP_CORREL)
    sim2 = cv.compareHist(hists[0], hists[1], cv.HISTCMP_CORREL)
    return  sim1, sim2