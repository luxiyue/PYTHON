import cv2 as cv
import numpy as np

def video_demo():
    capture = cv.VideoCapture(0)
    while True:
        ret,frame = capture.read()
        frame = cv.flip(frame,1)#让摄像头正过来
        cv.imshow("video",frame)
        c = cv.waitKey(50)
        if c == 27:#esc建的ascii为27
            break

def get_image_info(image):
    print(type(image))
    print(image.shape)
    print(image.size)
    print(image.dtype)
    pixel_data = np.array(image)
    print(pixel_data)


print("----------------hello python-------------------")
src = cv.imread("../../img/cloud.jpg")
#下面两行的第一个参数必须一致！不一致就会出现两个窗口
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)

# video_demo()
get_image_info(src)

#保存图像
gray = cv.cvtColor(src,cv.COLOR_BGR2GRAY)#灰度处理
cv.imshow("111",gray)
# cv.imwrite("E:/文件/python/OpenCV/bilibili/自己敲的/a.png",gray)

cv.waitKey(0)
cv.destroyAllWindows()
