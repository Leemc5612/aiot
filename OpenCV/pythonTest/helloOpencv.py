import cv2

def main():
    img =  cv2.imread("/home/lmc/aiot/OpenCV/cppTest/build/lena.bmp")
    cv2.imshow("image", img)
    cv2.waitKey(0)

if __name__ == "__main__":
    main()