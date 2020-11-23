import cv2
import numpy as np
# 读取图像
img = cv2.imread('../img/test14.bmp')
print(img.shape)

#对图像进行均值滤波
img_mean = cv2.blur(img, (5, 5))
cv2.putText(img_mean,"img_mean",(50,50),cv2.FONT_HERSHEY_SIMPLEX,1.5,(255,0,0),4)

#对图像进行中值滤波
img_median = cv2.medianBlur(img, 5)
cv2.putText(img_median,"img_median",(50,50),cv2.FONT_HERSHEY_SIMPLEX,1.5,(255,0,0),4)

#对图像进行高斯滤波
img_Guassian = cv2.GaussianBlur(img,(5,5),0)
cv2.putText(img_Guassian,"img_Guassian",(50,50),cv2.FONT_HERSHEY_SIMPLEX,1.5,(255,0,0),4)

#对图像进行高斯边缘检测  下面的三行是我自己乱写的，我实际上用的是拉普拉斯算子
laplacian = cv2.Laplacian(img_Guassian, cv2.CV_16S, ksize=5)
dst = cv2.convertScaleAbs(laplacian)
cv2.putText(dst,"img_bilater",(50,50),cv2.FONT_HERSHEY_SIMPLEX,1.5,(255,0,0),4)


#李昂写的高斯边缘检测 ,我不知道对不对
gau_matrix = np.asarray([[-2/28,-5/28,-2/28],[-5/28,28/28,-5/28],[-2/28,-5/28,-2/28]])
img1 = np.zeros(img.shape)
hight,width,v = img.shape
for i in range(1,hight-1):
    for j in range(1,width-1):
        img1[i-1,j-1] = np.sum(img[i-1:i+2,j-1:j+2]*gau_matrix)
gas = img1.astype(np.uint8)
cv2.putText(gas,"gussianEdgeDetection",(50,50),cv2.FONT_HERSHEY_SIMPLEX,1.5,(255,0,0),4)


#图像显示
cv2.imshow("img_bilater",dst)
cv2.imshow("gussianEdgeDetection",gas)
cv2.imshow("img",img)
cv2.imshow("img_mean",img_mean)
cv2.imshow("img_median",img_median)
cv2.imshow("img_Guassian",img_Guassian)
cv2.waitKey(0)
cv2.destroyAllWindows()
