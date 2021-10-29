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



# 04.event_mouse.py
import numpy as np
import cv2 as cv

def onMouse(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        print("마우스 왼쪽 버튼 누르기")
    elif event == cv.EVENT_RBUTTONDOWN:
        print("오른쪽 버튼 누르기")
    elif event == cv.EVENT_RBUTTONUP:
        print("오른쪽 버튼 떼기")
    elif event == cv.EVENT_LBUTTONDBLCLK:
        print("마우스 왼쪽 버튼 더블클릭")


image = np.full((200, 300), 255, np.uint8)

title1, title2 = "Mouse Event1", "Mouse Event2"
cv.imshow(title1, image)
cv.imshow(title2, image)

cv.setMouseCallback(title2, onMouse)
cv.waitKey(0)
cv.destoryAllWindows()