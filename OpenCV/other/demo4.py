import cv2

# 读取图像
img = cv2.imread('../img/test14.bmp')

#对图像进行均值滤波
img_mean = cv2.blur(img, (5, 5))

#对图像进行中值滤波
img_median = cv2.medianBlur(img, 5)

#对图像进行高斯滤波
img_Guassian = cv2.GaussianBlur(img,(5,5),0)

#对图像进行高斯边缘检测
laplacian = cv2.Laplacian(img_Guassian, cv2.CV_16S, ksize=5)
dst = cv2.convertScaleAbs(laplacian)
# dst = cv2.bilateralFilter(img, 0, 100, 15)  # 高斯双边

#图像显示
cv2.imshow("img",img)
cv2.imshow("img_mean",img_mean)
cv2.imshow("img_median",img_median)
cv2.imshow("img_Guassian",img_Guassian)
cv2.imshow("img_bilater",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
