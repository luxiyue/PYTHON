#灰度处理图片
import cv2

# 读入原始图像
img = cv2.imread('../img/cloud.jpg', 1)

# 灰度化处理1：直接读入灰度化图像
img1 = cv2.imread('../img/cloud.jpg', 0)

# 灰度化处理2：
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 通过窗口展示图片 第一个参数为窗口名 第二个为读取的图片变量
cv2.imshow('img', img)
cv2.imshow('gray1', img1)
cv2.imshow('gray2', gray)

# 暂停cv2模块 不然图片窗口一瞬间即就会消失 观察不到

cv2.waitKey(0)