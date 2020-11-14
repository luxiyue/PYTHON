#描绘云朵
import cv2

img = cv2.imread('../img/cloud.jpg')
# 灰度图像
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 二值化
ret, binary = cv2.threshold(gray, 175, 255, cv2.THRESH_BINARY)
img1, contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 以圆形框出云朵
# for i in range(len(contours)):
#   (x, y), radius = cv2.minEnclosingCircle(contours[i])
#   center = (int(x), int(y))
#   radius = int(radius)
#   img = cv2.circle(img, center, radius, (0, 255, 0), 2)

#以云朵边界轮廓框出云朵
cv2.drawContours(img, contours, -1, (0, 0, 255), 3)

cv2.imshow("img", img)
cv2.imshow("gray", gray)
cv2.imshow("img1", img1)
cv2.waitKey(0)