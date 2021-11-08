import numpy as np
import cv2 as cv

def place_icons(image, size):
    icon_name = ["rect", "circle", "eclipe", "line", "brush", "eraser", "open", "save", "plus", "minus", "clear", "color"]
    icons = [(i%2, i//2, 1, 1) for i in range(len(icon_name))]
    icons = np.multiply(icons, size*2)

    for roi, name in zip(icons, icon_name):
        icon = cv.imread("images/icon/%s.jpg" % name, cv.IMREAD_COLOR)
        if icon is None:
            continue
        x, y, w, h = roi

        image[y:y+h, x:x+w] = cv.resize(icon, size)
    return list(icons)

def create_hueIndex(image, roi):
    x, y, w, h = roi
    index = [[(j, 1, 1) for j in range(w)] for i in range(h)]
    ratios = (180/w, 255, 255)
    hueIndex = np.multiply(index, ratios).astype("uint8")
    image[y:y+h, x:x+w] = cv.cvtColor(hueIndex, cv.COLOR_HSV2BGR)

def create_colorPlatte(image, idx, roi):
    x, y, w, h = roi
    hue = idx - x
    palette = [[(hue, j , h-i-1) for j in range(w)] for i in range(h)]

    ratios = (180/w, 255/w, 255/h)
    palette = np.multiply(palette, ratios).astype("uint8")

    image[y:y+h, x:x+w] = cv.cvtColor(palette, cv.COLOR_HSV2BGR)

def create_colorPlatte1(image, hueidx, roi):
    x, y, w, h = roi
    ratio1 = 180 / h
    ratio2 = 255 / w
    ratio3 = 255 / h
    hue = ((hueidx - x) * ratio1)

    palatte = [[(hue, j, (h-i-1)) for j in range(w)] for i in range(h)]
    palatte = np.multiply(palatte, (1, ratio2, ratio3)).astype('uint8')

    image[y:y+h, x:x+w] = cv.cvtColor(palatte, cv.COLOR_HSV2BGR)

def create_colorPlatte2(image, hueidx, roi):
    x, y, w, h = roi
    ratio1 = 180 / w
    ratio2 = 256 / w
    ratio3 = 256 / h

    hue = round((hueidx - x) * ratio1)
    palatte = [[(hue, j * ratio2, (h - i - 1) * ratio3)
                for j in range(w)] for i in range(h)]
    palatte = np.array(palatte, np.uint8)

    image[y:y + h, x:x + w] = cv.cvtColor(palatte, cv.COLOR_HSV2BGR)

    return hue
