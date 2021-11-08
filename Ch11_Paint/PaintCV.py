from header.paint_init import *
from header.paint_utils import *

def onMouse(event, x, y, flags, param):

    global pt1, pt2, mouse_mode, draw_mode

    if event == cv.EVENT_LBUTTONUP:
        for i, (x0, y0, w, h) in enumerate(icons):
            if x0 <= x < x0+ w and y0 <= y < y0 + h: 
                if i < 6:
                    mouse_mode = 0
                    draw_mode = i
                else:
                    command(i)
                return

        pt2 = (x, y)
        mouse_mode = 1

    elif event == cv.EVENT_LBUTTONDOWN:
        pt1 = (x, y)
        mouse_mode = 2

    if mouse_mode >= 2:
        mouse_mode = 0 if x < 125 else 3
        pt2 = (x, y)

def draw(image, color=(200, 200, 200)):
    global draw_mode, thickness, pt1, pt2

    if draw_mode == DRAW_RECTANGLE:
        cv.rectangle(image, pt1, pt2, color, thickness)

    elif draw_mode == DRAW_LINE:
        cv.line(image, pt1, pt2, color, thickness)

    elif draw_mode == DRAW_BRUSH:
        cv.line(image, pt1, pt2, color, thickness * 3)
        pt1 = pt2

    elif draw_mode == ERASE:
        cv.line(image, pt1, pt2, (255, 255, 255), thickness * 5)
        pt1 = pt2

    elif draw_mode == DRAW_CIRCLE:
        d = np.subtract(pt1, pt2)
        radius = int(np.sqrt(d[0] ** 2 + d[1] ** 2))
        cv.circle(image, pt1, radius, color, thickness)

    elif draw_mode == DRAW_ECLIPSE:
        center = np.abs(np.add(pt1, pt2)) // 2
        size = np.abs(np.subtract(pt1, pt2)) // 2
        cv.ellipse(image, tuple(center), tuple(size), 0, 0, 360, color, thickness)

    cv.imshow("PaintCV", image)

def command(mode):
    global icons, image, canvas, Color, hue, mouse_mode

    if mode == PALETTE:
        pixel = image[pt2[::-1]]
        x, y, w, h = icons[COLOR]
        image[y:y + h - 1, x:x + w - 1] = pixel
        Color = tuple(map(int, pixel))

    elif mode == HUE_IDX:
        create_colorPlatte(image, pt2[0], icons[PALETTE])

    elif mode == OPEN:
        tmp = cv.imread("images/my_picture.jpg", cv.IMREAD_COLOR)
        cv.resize(tmp, canvas.shape[1::-1], canvas)

    elif mode == SAVE:
        cv.imwrite("images/my_save.jpg", canvas)

    elif mode == PLUS:
        val = np.full(canvas.shape, 10, np.uint8)
        cv.add(canvas, val, canvas)

    elif mode == MINUS:
        val = np.full(canvas.shape, 10, np.uint8)
        cv.subtract(canvas, val, canvas)

    elif mode == CREAR:
        canvas[:] = (255, 255, 255)
        mouse_mode = 0

    cv.imshow("PaintCV", image)

def onTrackbar(value):
    global mouse_mode, thickness
    mouse_mode = 0
    thickness = value

image = np.full((500, 800, 3), 255, np.uint8)
icons = place_icons(image, (60, 60))
x, y, w, h = icons[-1]

icons.append((0, y + h + 2  , 120, 120) )
icons.append((0, y + h + 124, 120, 15))
create_colorPlatte(image, 0, icons[PALETTE])
create_hueIndex(image, icons[HUE_IDX])

cv.imshow("PaintCV", image)
cv.setMouseCallback("PaintCV", onMouse)
cv.createTrackbar("Thickness", "PaintCV", thickness, 255, onTrackbar)
 
canvas = image[:, w*2:image.shape[1]]

while True:
    if mouse_mode == 1:
        draw(image, Color)
    elif mouse_mode == 3:
        if draw_mode == DRAW_BRUSH or draw_mode == ERASE:
            draw(image, Color)
        else:
            draw(np.copy(image), (200, 200, 200))
    if cv.waitKey(30) == 27:
        break