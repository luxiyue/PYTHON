import cv2

# 读取图像
img = cv2.imread('../img/test.png')

# 变微灰度图
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 大津法二值化
retval, dst = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)

#反色
fanse = cv2.bitwise_not(dst)

#描述轮廓后再反色
lunkuo = cv2.bitwise_not(cv2.Canny(dst,80,255)) #设置80为低阈值，255为高阈值

cv2.imshow('img',img)
cv2.imshow('binary', dst)
cv2.imshow("fanse",fanse)
cv2.imshow("lunkuo",lunkuo)

cv2.waitKey(0)


