from skimage import data,color,morphology
import cv2 as cv
import cv2

#读取图片
img1 = cv2.imread('../img/vas0 .bmp')
img11 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)


laplacian = cv2.Laplacian(img11, cv2.CV_16S, ksize=5)
dst = cv2.convertScaleAbs(laplacian)
img2 = cv2.bitwise_not(dst)

#反色


#显示图片
cv2.imshow("img1",img1)
cv2.imshow("img2",img2)

print(img1.shape)
print(img2.shape)


cv2.waitKey()
cv2.destroyAllWindows()