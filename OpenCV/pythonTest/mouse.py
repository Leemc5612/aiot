import cv2
import numpy as np

def on_mouse(event, x, y, flags, param):
    src = param['src']
    if event == cv.cv2.EVENT_LBUTTONDOWN:
        print(x,y)
        cv2.circle(param, (x,y), 10, (255,0,0), -1)
        cv2.imshow("img", param)

def main():
    folder = "/home/lmc/aiot/OpenCV/cppTest/data/"
    src = cv2.imread(folder+ "lenna.bmp", cv2.IMREAD_COLOR)

    param = {'src':src}
    cv2.setMouseCallback("img", on_mouse, param)
    cv2.nameWindow("img")

    cv2.imshow("img", src)
    cv2.waitKey(0)

if __name__ =="__main__":
    main()