## 01.move_window.py
#import numpy as np
#import cv2  as cv

#image = np.zeros((200, 400), np.uint8)
#image[:] = 200

#title1, title2 = 'pos1', 'pos2'
#cv.namedWindow(title1, cv.WINDOW_AUTOSIZE)
#cv.namedWindow(title2)
#cv.moveWindow(title1, 150, 150)
#cv.moveWindow(title2, 400, 50)

#cv.imshow(title1, image)
#cv.imshow(title2, image)
#cv.waitKey(0)
#cv.destroyAllWindows()



## 02.window_resize.py
#import numpy as np
#import cv2 as cv

#image = np.zeros((200, 400), np.uint8)
#image[:] = 200

#title1, title2 = 'pos1', 'pos2'
#cv.namedWindow(title1, cv.WINDOW_AUTOSIZE)
#cv.namedWindow(title2, cv.WINDOW_NORMAL)        # 윈도우 크기 변경 가능
#cv.moveWindow(title1, 150, 150)
#cv.moveWindow(title2, 400, 50)

#cv.imshow(title1, image)
#cv.imshow(title2, image)
#cv.waitKey(0)
#cv.destroyAllWindows()



## 03.event_key.py
#import numpy as np
#import cv2 as cv

#switch_case = {
#    ord('a'): "a키 입력",              # ord() : 문자->아스키코드
#    ord('b'): "b키 입력",
#    0x41: "A키 입력",
#    int('0x42', 16): "B키 입력",
#    2424832: "왼쪽 화살표키 입력",      # 0x250000
#    2490368: "윗쪽 화살표키 입력",      # 0x260000
#    2555904: "오른쪽 화살표키 입력",    # 0x270000
#    2621440: "아래쪽 화살표키 입력"     # 0x280000
#}


#image = np.ones((200, 300), np.float)
#cv.namedWindow('Keyboard Event')
#cv.imshow('Keyboard Event', image)

#while True:
#    key = cv.waitKeyEx(100)
#    if key == 27:
#        break

#    try:
#        result = switch_case[key]
#        print(result)
#    except KeyError:
#        result = -1

#cv.destroyAllWindows()



## 04.event_mouse.py
#import numpy as np
#import cv2 as cv

#def onMouse(event, x, y, flags, param):
#    if event == cv.EVENT_LBUTTONDOWN:
#        print("마우스 왼쪽 버튼 누르기")-
#    elif event == cv.EVENT_RBUTTONDOWN:
#        print("오른쪽 버튼 누르기")
#    elif event == cv.EVENT_RBUTTONUP:
#        print("오른쪽 버튼 떼기")
#    elif event == cv.EVENT_LBUTTONDBLCLK:
#        print("마우스 왼쪽 버튼 더블클릭")


#image = np.full((200, 300), 255, np.uint8)

#title1, title2 = "Mouse Event1", "Mouse Event2"
#cv.imshow(title1, image)
#cv.imshow(title2, image)

#cv.setMouseCallback(title2, onMouse)
#cv.waitKey(0)
#cv.destoryAllWindows()



## 05.event_trackbar.py
#import numpy as np
#import cv2 as cv

#def onChange(value):
#    global image, title

#    add_value = value - int(image[0][0])
#    print("추가 화소값:", add_value)
#    image = image + add_value
#    cv.imshow(title, image)

#image = np.zeros((300, 500), np.uint8)

#title = 'trackbar Event'
#cv.imshow(title, image)

#cv.createTrackbar('Brightness', title, image[0][0], 255, onChange)
#cv.waitKey(0)
#cv.destroyAllWindows()



# 06.event_mouse_trackbar.py
#import numpy as np
#import cv2 as cv

#def onChange(value):
#    global image, title

#    add_value = value - int(image[0][0])
#    print("추가 화소값:", add_value)
#    image = image + add_value
#    cv.imshow(title, image)

#def onMouse(event, x, y, flags, param):
#    global image, bar_name

#    if event == cv.EVENT_RBUTTONDOWN:
#        if(image[0][0] < 246):
#            image = image + 10
#        cv.setTrackbarPos(bar_name, title, image[0][0])
#        cv.imshow(title, image)

#    elif event == cv.EVENT_LBUTTONDOWN:
#        if(image[0][0] >= 10):
#            image = image - 10
#        cv.setTrackbarPos(bar_name, title, image[0][0])
#        cv.imshow(title, image)

#image = np.zeros((300, 500), np.uint8)
#title = "Trackbar & Mouse Event"
#bar_name = 'Brightness'
#cv.imshow(title, image)

#cv.createTrackbar(bar_name, title, image[0][0], 255, onChange)
#cv.setMouseCallback(title, onMouse)
#cv.waitKey(0)
#cv.destroyAllWindows()



## 07.draw =_line_rect.py
#import numpy as np
#import cv2 as cv

#blue, green, red = (255, 0, 0), (0, 255, 0), (0, 0, 255)
#image = np.zeros((400, 600, 3), np.uint8)
#image[:] = (255, 255, 255)

#pt1, pt2 = (50, 50), (250, 150)
#pt3, pt4 = (400, 150), (500, 50)
#roi = (50, 200, 200, 100)

#cv.line(image, pt1, pt2, red)
#cv.line(image, pt3, pt4, green, 3, cv.LINE_AA)

#cv.rectangle(image, pt1, pt2, blue, 3, cv.LINE_4)
#cv.rectangle(image, roi, red, 3, cv.LINE_8)
#cv.rectangle(image, (400, 200, 100, 100), green, cv.FILLED)

#cv.imshow("LINE & RECTANGE", image)
#cv.waitKey(0)
#cv.destroyAllWindows()



## 08.put_text.py
#import numpy as np
#import cv2 as cv

#olive, violet, brown = (128, 128, 0), (221, 160, 221), (42, 42, 165)
#pt1, pt2 = (50, 230), (50, 310)

#image = np.zeros((350, 500, 3), np.uint8)
#image.fill(255)

#cv.putText(image, 'SIMPLEX', (50, 50), cv.FONT_HERSHEY_SIMPLEX, 2, brown)
#cv.putText(image, 'DUPLEX', (50, 130), cv.FONT_HERSHEY_DUPLEX, 3, olive)
#cv.putText(image, 'TRIPLEX', pt1, cv.FONT_HERSHEY_TRIPLEX, 2, violet)
#fontFace = cv.FONT_HERSHEY_PLAIN | cv.FONT_ITALIC
#cv.putText(image, 'ITALIC', pt2, fontFace, 4, violet)

#cv.imshow('Put Text', image)
#cv.waitKey(0)



## 09.draw_circle.py
#import numpy as np
#import cv2 as cv

#orange, blue, cyan = (0, 165, 255), (255, 0, 0), (255, 255, 0)
#white, black = (255, 255, 255), (0, 0, 0)

#image = np.full((300, 550, 3), white, np.uint8)

#center = (image.shape[1]//2, image.shape[0]//2)
#pt1, pt2 = (300, 50), (100, 220)
#shade = (pt2[0] + 2, pt2[1] + 2)

#cv.circle(image, center, 100, blue)
#cv.circle(image, pt1, 50, orange, 2)
#cv.circle(image, pt2, 70, cyan, -1)

#font = cv.FONT_HERSHEY_COMPLEX
#cv.putText(image, 'center_blue', center, font, 1.0, blue)
#cv.putText(image, 'pt1_orange', pt1, font, 0.8, orange)
#cv.putText(image, 'pt2_cyan', pt2, font, 1.2, black, 2)
#cv.putText(image, 'pt2_cyan', pt2, font, 1.2, cyan, 1)

#cv.imshow("Draw circles", image)
#cv.waitKey(0)



## 10.draw_ellipse.py
#import numpy as np
#import cv2 as cv

#orange, blue, white = (0, 165, 255), (255, 0, 0), (255, 255, 255)
#image = np.full((300, 700, 3), white, np.uint8)

#pt1, pt2 = (180, 150), (550, 150)
#size = (120, 60)

#cv.circle(image, pt1, 1, 0, 2)
#cv.circle(image, pt2, 1, 0, 2)

#cv.ellipse(image, pt1, size, 0, 0, 360, blue, 1)
#cv.ellipse(image, pt2, size, 90, 0, 360, blue, 1)
#cv.ellipse(image, pt1, size, 0, 30, 270, orange, 4)
#cv.ellipse(image, pt2, size, 90, -45, 90, orange, 4)

#cv.imshow("문자열", image)
#cv.waitKey(0)



## 11.event_draw.py
#import numpy as np
#import cv2 as cv

#def onMouse(event, x, y, flags, param):
#    global title, pt

#    if event == cv.EVENT_LBUTTONDOWN:
#        if pt[0] < 0:
#            pt = (x, y)
#        else:
#            cv.rectangle(image, pt, (x, y), (255, 0, 0), 2)
#            cv.imshow(title, image)
#            pt = (-1, -1)
#    elif event == cv.EVENT_RBUTTONDOWN:
#        if pt[0] < 0:
#            pt = (x, y)
#        else:
#           dx, dy = pt[0] - x, pt[1] - y
#           radius = int(np.sqrt(dx*dx + dy*dy))
#           cv.circle(image, pt, radius, (0, 0, 255), 2)
#           cv.imshow(title, image)
#           pt = (-1, -1)

#image = np.full((300, 500, 3), (255, 255, 255), np.uint8)

#pt = (-1, -1)
#title = "Draw Event"
#cv.imshow(title, image)
#cv.setMouseCallback(title, onMouse)
#cv.waitKey(0)



## 12.read_image1.py
#import cv2 as cv

#def print_matInfo(name, image):
#    if image.dtype == 'uint8':
#        mat_type = "CV_8U"
#    elif image.dtype == 'int8':
#        mat_type = "CV_8S"
#    elif image.dtype == 'uint16':
#        mat_type = "CV_16U"
#    elif image.dtype == 'float32':
#        mat_type = "CV_32F"
#    elif image.dtype == 'float64':
#        mat_type = "CV_64F"
#    nch = 3 if image.ndim == 3 else 1

#    print("%12s: depth(%s), channels(%s) -> mat_type(%sC%d)" 
#          % (name, image.dtype, nch, mat_type, nch))
    
#title1, title2 = 'gray2gray', 'gray2color'
#gray2gray = cv.imread("D:\\study\\RYS\\Ch2_OpenCV\\1.jpg", cv.IMREAD_GRAYSCALE)
#gray2color = cv.imread("D:\\study\\RYS\\Ch2_OpenCV\\1.jpg", cv.IMREAD_COLOR)

#if gray2gray is None or gray2color is None :
#    raise Exception("Error IMREAD")

#print("arr(100,100) value")
#print("%s %s" % (title1, gray2gray[100, 100]))
#print("%s %s" % (title2, gray2color[100, 100]))

#print_matInfo(title1, gray2gray)
#print_matInfo(title2, gray2color)

#cv.imshow(title1, gray2gray)
#cv.imshow(title2, gray2color)
#cv.waitKey(0)



## 13.read_image2.py
#import cv2 as cv
##from Common.utils import print_matInfo
#import Common.utils as ut

#title1, title2 = 'gray2gray', 'gray2color'
#gray2gray = cv.imread("D:\\study\\RYS\\Ch2_OpenCV\\1.jpg", cv.IMREAD_GRAYSCALE)
#gray2color = cv.imread("D:\\study\\RYS\\Ch2_OpenCV\\1.jpg", cv.IMREAD_COLOR)

#if gray2gray is None or gray2color is None :
#    raise Exception("Error IMREAD")

#print("arr(100,100) value")
#print("%s %s" % (title1, gray2gray[100, 100]))
#print("%s %s" % (title2, gray2color[100, 100]))

#ut.print_matInfo(title1, gray2gray)
#ut.print_matInfo(title2, gray2color)

#cv.imshow(title1, gray2gray)
#cv.imshow(title2, gray2color)
#cv.waitKey(0)



## 14.read_image3.py
#import cv2 as cv
#from Common.utils import print_matInfo

#title1, title2 = '16 bit unchaged', '32 bit unchanged'
#color2unchanged1 = cv.imread("D:\\study\\RYS\\Ch2_OpenCV\\1.jpg", cv.IMREAD_UNCHANGED)
#color2unchanged2 = cv.imread("D:\\study\\RYS\\Ch2_OpenCV\\1.jpg", cv.IMREAD_UNCHANGED)
#if color2unchanged1 is None or color2unchanged2 is None :
#    raise Exception("Error IMREAD")

#print("16/32 bit (10, 10) value")
#print(title1, '원소 자료형', type(color2unchanged1[10][10][0]))
#print(title1, '화소값(3원소)', color2unchanged1[10, 10])
#print(title2, '원소 자료형', type(color2unchanged2[10][10][0]))
#print(title2, '화소값(3원소)', color2unchanged2[10, 10])
#print()

#print_matInfo(title1, color2unchanged1)
#print_matInfo(title2, color2unchanged2)
#cv.imshow(title1, color2unchanged1)
#cv.imshow(title2, (color2unchanged2 * 255).astype('uint8'))
#cv.waitKey(0)



## 15.write_image1.py
#import cv2 as cv

#image = cv.imread("D:\\study\\RYS\\Ch2_OpenCV\\1.jpg", cv.IMREAD_COLOR)
#if image is None :
#    raise Exception("Error IMREAD")

#params_jpg = (cv.IMWRITE_JPEG_QUALITY, 10)
#params_png = [cv.IMWRITE_PNG_COMPRESSION, 9]

#cv.imwrite("images/write_test1.jpg", image)
#cv.imwrite("images/write_test2.jpg", image, params_jpg)
#cv.imwrite("images/write_test3.png", image, params_png)
#cv.imwrite("images/write_test4.bmp", image)
#print("complate save")



## 16.write_image2.py
#import numpy as np
#import cv2 as cv

#image8 = cv.imread("D:\\study\\RYS\\Ch2_OpenCV\\1.jpg", cv.IMREAD_COLOR)
#if image8 is None:
#    raise Exception("Error IMREAD")
#image16 = np.uint16(image8 * (65535/255))
#image32 = np.float32(image8 * (1/255))

#print("image8 행렬의 일부\n %s\n" % image8[10:12, 10:13])
#print("image16 행렬의 일부\n %s\n" % image16[10:12, 10:13])
#print("image32 행렬의 일부\n %s\n" % image32[10:12, 10:13])

#cv.imwrite('images/image16.tif', image16)
#cv.imwrite('images/image32.tif', image32)

#cv.imshow('image16', image16)
#cv.imshow('image32', image32)
#cv.imshow('image32_', (image32*255).astype('uint8'))
#cv.waitKey(0)




## 17.read_pcamera.py
#import cv2 as cv

#def put_string(frame, text, pt, value, color=(120, 200, 90)):
#    text += str(value)
#    shade = (pt[0] + 2, pt[1] + 2)
#    font = cv.FONT_HERSHEY_SIMPLEX
#    cv.putText(frame, text, shade, font, 0.7, (0, 0, 0), 2)
#    cv.putText(frame, text, pt, font, 0.7, color, 2)

#capture = cv.VideoCapture(0)
#if capture.isOpened() == False:
#    raise Exeption("Error VIDEOCAPTER")

#print("wid %d" % capture.get(cv.CAP_PROP_FRAME_WIDTH))
#print("hei %d" % capture.get(cv.CAP_PROP_FRAME_HEIGHT))
#print("Exp %d" % capture.get(cv.CAP_PROP_EXPOSURE))
#print("Bri %d" % capture.get(cv.CAP_PROP_BRIGHTNESS))


#while True:
#    ret, frame = capture.read()
#    if not ret:
#        break
#    if cv.waitKey(30) >= 0:
#        break

#    exposure = capture.get(cv.CAP_PROP_EXPOSURE)
#    put_string(frame, 'EXPOS: ', (10, 40), exposure)
#    title = "View Frame from Camera"
#    cv.imshow(title, frame)

#capture.release()




## 18.set_camera_attr.py
#import cv2 as cv
#from Common.utils import put_string

#def zoom_bar(value):
#    global capture
#    capture.set(cv.CAP_PROP_ZOOM, value)

#def focus_bar(value):
#    global capture
#    capture.set(cv.CAP_PROP_FOCUS, value)

#capture = cv.VideoCapture(0)
#if capture.isOpened() == False :
#    raise Exception("Error VIDEOCAPTURE")

#capture.set(cv.CAP_PROP_FRAME_WIDTH, 400)
#capture.set(cv.CAP_PROP_FRAME_HEIGHT, 300)
#capture.set(cv.CAP_PROP_AUTOFOCUS, 0)
#capture.set(cv.CAP_PROP_BRIGHTNESS, 100)

#title = "Change Camera Properties"
#cv.namedWindow(title)
#cv.createTrackbar("zoom", title, 0, 10, zoom_bar)
#cv.createTrackbar("focus", title, 0, 10, focus_bar)

#while True:
#    ret, frame = capture.read()
#    if not ret:
#        break;
#    if cv.waitKey(30) >= 0:
#        break;

#    zoom = int(capture.get(cv.CAP_PROP_ZOOM))
#    focus = int(capture.get(cv.CAP_PROP_FOCUS))
#    put_string(frame, 'zoom : ', (10, 240), zoom)
#    put_string(frame, 'focus : ', (10, 270), focus)
#    cv.imshow(title, frame)

#capture.release()



## 19.write_camera_frame.py
#import cv2 as cv

#capture = cv.VideoCapture(0)
#if capture.isOpened() == False:
#    raise Exception("Error VIDEOCAPTURE")

#fps = 29.97
#delay = round(1000/fps)
#size = (640, 360)
#fourcc = cv.VideoWriter_fourcc(*'DX50')

#print("width x height: ", size)
#print("VideoWriterfourcc: %s" % fourcc)
#print("delay: %2d ms" % delay)
#print("fps: %2f" % fps)

#capture.set(cv.CAP_PROP_ZOOM, 1)
#capture.set(cv.CAP_PROP_AUTOFOCUS, 0)
#capture.set(cv.CAP_PROP_FRAME_WIDTH, size[0])
#capture.set(cv.CAP_PROP_FRAME_HEIGHT, size[1])

#writer = cv.VideoWriter("image/video_file.avi", fourcc, fps, size)
#if writer.isOpened() == False:
#    raise Exception("Error VIDEOWRITER")

#while True:
#    ret, frame = capture.read()
#    if not ret:
#        break;
#    if cv.waitKey(delay) >= 0:
#        break;

#    writer.write(frame)
#    cv.imshow("View Frame from Camera", frame)

#writer.release()
#capture.release()



## 20.read_video_file.py
#import cv2 as cv
#from Common.utils import put_string

#capture = cv.VideoCapture("image/video_file.avi")
#if not capture.isOpened():
#    raise Exception("Error VIDEOCAPTURE")

#frame_rate = capture.get(cv.CAP_PROP_FPS)
#delay = int(1000 / frame_rate)
#frame_cnt = 0

#while True:
#    ret, frame = capture.read()
#    if not ret or cv.waitKey(delay) >= 0:
#        break;
#    blue, green, red = cv.split(frame)
#    frame_cnt += 1

#    if 100 <= frame_cnt < 200:
#        cv.add(blue, 100, blue)
#    elif 200 <= frame_cnt < 300:
#        cv.add(green, 100, green)
#    elif 300 <= frame_cnt < 400:
#        cv.add(red, 100, red)

#    frame = cv.merge([blue, green, red])
#    put_string(frame, 'frame_cnt: ', (20, 30), frame_cnt)
#    cv.imshow("Read Video File", frame)

#capture.release()




## 21.matplotlib.py
#import cv2 as cv
#import matplotlib.pyplot as plt

#image = cv.imread("images\\write_test1.jpg", cv.IMREAD_COLOR)
#if image is None:
#    raise Exception("Error IMREAD")

#rows, cols = image.shape[:2]
#rgb_img = cv.cvtColor(image, cv.COLOR_BGR2RGB)
#gray_img = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

#fig = plt.figure(num=1, figsize=(3,4))
#plt.imshow(image)
#plt.title('figure1- original(bgr)')
#plt.axis('off')
#plt.tight_layout()

#fig = plt.figure(figsize=(6,4))
#plt.suptitle('figure2- pyplot image display')
#plt.subplot(1, 2, 1)
#plt.imshow(rgb_img)
#plt.axis([0, cols, rows, 0])
#plt.title('rgb color')
#plt.subplot(1, 2, 2)
#plt.imshow(gray_img, cmap='gray')
#plt.title('gray_img2')
#plt.show()




## 22.interpolation.py
#import matplotlib.pyplot as plt
#import numpy as np

#methods = ['none', 'nearest', 'bilinear', 'bicubic', 'spline16', 'spline36']
#grid = np.random.rand(5, 5)

#fig, axs = plt.subplots(nrows=2, ncols=3, figsize=(8, 6))

#for ax, method in zip(axs.flat, methods):
#    ax.imshow(grid, interpolation=method, cmap='gray')
#    ax.set_title(method)
#plt.tight_layout()
#plt.imshow()




# 23.plot.py
#import matplotlib.pyplot as plt
#import numpy as np

#x = np.arange(10)
#y1 = np.arange(10)
#y2 = np.arange(10)**2
#y3 = np.random.choice(50, size=10)

#plt.figure(figsize=(5,3))
#plt.plot(x, y1, 'b--', linewidth=2)
#plt.plot(x, y2, 'go-', linewidth=3)
#plt.plot(x, y3, 'c+', linewidth=5)

#plt.title('Line examples')
#plt.axis([0, 10, 0, 80])
#plt.tight_layout()
#plt.savefig(fname='sample.png', dpi=300)
#plt.show()




## example 5
#import numpy as np
#import cv2 as cv

#image = np.zeros((300, 400), np.uint8)
#image[:] = 100

#title = 'Window'
#cv.namedWindow(title, cv.WINDOW_NORMAL)
#cv.moveWindow(title, 100, 200)
#cv.imshow(title, image)
#cv.waitKey(0)
#cv.destroyAllWindows()

############################################

#import numpy as np
#import cv2 as cv

#image = np.zeros((400, 600, 3), np.uint8)
#image[:] = (255, 255, 255)
#pt1, pt2 = (50, 100), (200, 300)

#cv.line(image, pt1, pt2, (0, 255, 0), 5)
#cv.rectangle(image, pt2, (300, 400), (0, 0, 255), -1, cv.LINE_4, 1)


#title = 'Line & Rectangle'
#cv.imshow(title, image)
#cv.waitKey(0)
#cv.destroyAllWindows()



# example 7
import numpy as np
import cv2 as cv


image = np.zeros((300, 400, 3), np.uint8)
image[:] = (255, 255, 255)

pt1, pt2 = (50, 130), (200, 300)

#cv.line(image, pt1, (100, 200))
cv.line(image, pt1, pt2, (100, 100, 100))
cv.rectangle(image, pt1, pt2, (255, 0, 255))
cv.rectangle(image, pt1, pt2, (0, 0, 255))

title = "Line & Ractangle"
cv.namedWindow(title)
cv.imshow(title, image)
cv.waitKey(0)

cv.destroyAllWindows()

