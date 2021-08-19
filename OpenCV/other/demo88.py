import cv2
import cv2 as cv
import numpy as np
import imutils


#读取图片
img = cv2.imread('../img/dip_switch_03.bmp')

img = imutils.resize(img, width=500)
roi = cv2.selectROI(windowName="image1", img=img, showCrosshair=True, fromCenter=False)
x, y, w, h = roi
cv2.rectangle(img=img, pt1=(x, y), pt2=(x + w, y + h), color=(0, 0, 255), thickness=2)
s = img[y:y+h,x:x+w]

gray = cv2.cvtColor(s, cv2.COLOR_BGR2GRAY)  # face彩色图片变成灰度图片
retval, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)  # 二值化
fanse = cv2.bitwise_not(binary)#反色
bianyuan = cv2.bitwise_not(cv2.Canny(fanse,80,255))
section = cv2.cvtColor(bianyuan, cv2.COLOR_GRAY2BGR)
img[y:y+h,x:x+w] = section


img1 = img.copy()
# 输出鼠标选择点的坐标
# setMouseCallback使用的回调函数，这个回调函数在捕获到鼠标左键点击事件时，就在图片上点击处绘制一个实心的圆、并显示出坐标。
def on_EVENT_LBUTTONDOWN(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        xy = "%d,%d" % (x, y)
        print (xy)
        cv2.circle(img1, (x, y), 1, (255, 0, 0), thickness = -1)
        cv2.putText(img1, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,
                    1.0, (0,0,0), thickness = 1)
        cv2.imshow("image2", img1)

# 绘制线段
s = cv2.line(img1,(161, 150), (275, 150), (0, 255, 0), 2)
d = cv2.line(img1,(161, 235), (275, 235), (0,255, 0), 2)
lens = 235 - 150
#
# # 输出图形
text = "宽为：{0}".format(lens)
cv.putText(img1, text, (30, 30), cv.FONT_HERSHEY_COMPLEX, 2.0, (0, 255, 0), 1)



cv2.namedWindow("image2")
cv2.setMouseCallback("image2", on_EVENT_LBUTTONDOWN)
cv2.imshow("image2", img1)

cv2.imshow("img",img)



cv2.waitKey()
cv2.destroyAllWindows()