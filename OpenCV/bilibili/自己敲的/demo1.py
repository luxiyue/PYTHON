import cv2 as cv

src = cv.imread("../../img/cloud.jpg")
#下面两行的第一个参数必须一致！不一致就会出现两个窗口
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)
cv.waitKey(0)
cv.destroyAllWindows()
print("hello world")
