import cv2
import numpy as np
from scipy import signal

#读取图片
src_s = cv2.imread('../img/dip_switch_02.bmp', 0)
#对图片进行反色
src = cv2.bitwise_not(src_s)


# Sobel边缘检测算子
x = cv2.Sobel(src, cv2.CV_16S, 1, 0)
y = cv2.Sobel(src, cv2.CV_16S, 0, 1)
# cv2.convertScaleAbs(src[, dst[, alpha[, beta]]])
# 可选参数alpha是伸缩系数，beta是加到结果上的一个值，结果返回uint类型的图像
Scale_absX = cv2.convertScaleAbs(x)  # convert 转换  scale 缩放
Scale_absY = cv2.convertScaleAbs(y)
edgesobel = cv2.addWeighted(Scale_absX, 0.5, Scale_absY, 0.5, 0)
edgesobel2 = cv2.bitwise_not(edgesobel)
cv2.putText(edgesobel2,"Sobel",(50,50),cv2.FONT_HERSHEY_SIMPLEX,1.5,(0,0,255),4)



# Scharr算子
# x = cv2.Sobel(src, cv2.CV_16S, 1, 0, ksize=-1)
# y = cv2.Sobel(src, cv2.CV_16S, 0, 1, ksize=-1)
# # ksize=-1 Scharr算子
# # cv2.convertScaleAbs(src[, dst[, alpha[, beta]]])
# # 可选参数alpha是伸缩系数，beta是加到结果上的一个值，结果返回uint类型的图像
# Scharr_absX = cv2.convertScaleAbs(x)  # convert 转换  scale 缩放
# Scharr_absY = cv2.convertScaleAbs(y)
# edgerobert = cv2.addWeighted(Scharr_absX, 0.5, Scharr_absY, 0.5, 0)
# edgerobert2 = cv2.bitwise_not(edgerobert)
# cv2.putText(edgerobert2,"robert",(50,50),cv2.FONT_HERSHEY_SIMPLEX,1.5,(0,0,255),4)


#robert边缘检测算子
def roberts(I, _boundary='fill', _fillvalue=0):
    # 图像的高，宽
    H1, W1 = I.shape[0:2]
    # 卷积核的尺寸
    H2, W2 = 2, 2
    # 卷积核1 和 锚点的位置
    R1 = np.array([[1, 0], [0, -1]], np.float32)
    kr1, kc1 = 0, 0
    # 计算full卷积
    IconR1 = signal.convolve2d(I, R1, mode='full', boundary=_boundary, fillvalue=_fillvalue)
    IconR1 = IconR1[H2 - kr1 - 1:H1 + H2 - kr1 - 1, W2 - kc1 - 1:W1 + W2 - kc1 - 1]
    # 卷积核2 和 锚点的位置
    R2 = np.array([[0, 1], [-1, 0]], np.float32)
    kr2, kc2 = 0, 1
    # 再计算full卷积
    IconR2 = signal.convolve2d(I, R2, mode='full', boundary=_boundary, fillvalue=_fillvalue)
    IconR2 = IconR2[H2 - kr2 - 1:H1 + H2 - kr2 - 1, W2 - kc2 - 1:W1 + W2 - kc2 - 1]
    return (IconR1, IconR2)
IconR1, IconR2 = roberts(src, 'symm')
# 45度方向上的边缘强度的灰度级显示
IconR1 = np.abs(IconR1)
edge45 = IconR1.astype(np.uint8)
# 135度方向上的边缘强度的灰度级显示
IconR2 = np.abs(IconR2)
edge135 = IconR2.astype(np.uint8)
# 用平方和的开方来衡量最后输出的边缘
edge = np.sqrt(np.power(IconR1, 2.0) + np.power(IconR2, 2.0))
edge = np.round(edge)
edge[edge > 255] = 255
edge = edge.astype(np.uint8)
edge2 = cv2.bitwise_not(edge)
cv2.putText(edge2,"robert",(50,50),cv2.FONT_HERSHEY_SIMPLEX,1.5,(0,0,255),4)

#拉普拉斯算子（高斯）
laplacian = cv2.Laplacian(src, cv2.CV_16S, ksize=5)
dst = cv2.convertScaleAbs(laplacian)
lap = cv2.bitwise_not(dst)
cv2.putText(lap,"guass",(50,50),cv2.FONT_HERSHEY_SIMPLEX,1.5,(0,100,255),4)





cv2.imshow("lap",lap)
cv2.imshow('robert', edge2)
cv2.imshow('src', src)
cv2.imshow('sobel', edgesobel2)
cv2.waitKey(0)
cv2.destroyAllWindows()
