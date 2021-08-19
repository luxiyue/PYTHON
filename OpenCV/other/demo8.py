import cv2
import numpy as np

#读取图片
image = cv2.imread('../img/dip_switch_03.bmp')

image1 = image.copy()
rect = image1[80:220, 114:206]
gray = cv2.cvtColor(rect, cv2.COLOR_BGR2GRAY)  # face彩色图片变成灰度图片
retval, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)#二值化
fanse = cv2.bitwise_not(binary)#反色
bianyuan = cv2.bitwise_not(cv2.Canny(fanse,80,255))
section = cv2.cvtColor(bianyuan, cv2.COLOR_GRAY2BGR)
image1[80:220, 114:206] = section

#画线
image2 = image1.copy()
ptStart = (114, 112)
ptEnd = (204, 112)
point_color = (0, 0, 255) # BGR 红色
thickness = 2
lineType = 4
cv2.line(image2, ptStart, ptEnd, point_color, thickness, lineType)
#----------------------------------------



#显示
cv2.imshow("image",image)
cv2.imshow("image1",image1)
cv2.imshow("image2",image2)

cv2.waitKey()
cv2.destroyAllWindows()