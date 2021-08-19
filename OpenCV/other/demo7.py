import cv2
import numpy as np

#读取图片
image1 = cv2.imread('../img/car1.png')
#灰度处理
gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
#对灰度处理进行反色
fanse = cv2.bitwise_not(gray)
#二值化
retval, binary = cv2.threshold(fanse, 0, 255, cv2.THRESH_OTSU)


(h,w) = binary.shape# 返回高和宽

#垂直投影
vproject = binary.copy()
a = [0 for x in range(0,w)]
#记录每一列的波峰
for j in range(0,w):#遍历一列
    for i in range(0,h):#遍历一行
        if vproject[i,j]==0:#如果改点为黑点
            a[j]+=1#该列的计数器加1计数
            vproject[i,j]=255#记录完后将其变为白色
for j in range(0,w):#遍历每一列
    for i in range((h-a[j]),h):#从该列应该变黑的最顶部的点开始向最底部涂黑
        vproject[i,j]=0 #涂黑

#水平投影
hproject = binary.copy()
b = [0 for x in range(0,w)]
for j in range(0,h):
    for i in range(0,w):
        if hproject[j,i] == 0:
            b[j] += 1
            hproject[j,i] = 255
for j in range(0,h):
    for i in range(0,b[j]):
        hproject[j,i]=0



#分割字符
def measure_object(image):
    outimg,contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for i, contour in enumerate(contours):
        area = cv2.contourArea(contour)  # 计算轮廓面积
        print("contour area:", area)
        # 轮廓周长,第二参数可以用来指定对象的形状是闭合的（True）,还是打开的（一条曲线）。
        perimeter = cv2.arcLength(contour, True)
        print("contour perimeter:", perimeter)
        x, y, w, h = cv2.boundingRect(contour)  # 用矩阵框出轮廓
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 255), 1)
        rate = min(w, h)/max(w, h)  # 计算矩阵宽高比
        print("rectangle rate",rate)

        mm = cv2.moments(contour)  # 函数 cv2.moments() 会将计算得到的矩以一个字典的形式返回
        # 计算出对象的重心
        cx = mm['m10']/mm['m00']
        cy = mm['m01']/mm['m00']
        # cv2.circle(image, (np.int(cx), np.int(cy)), 2, (0, 255, 255), -1)  # 用实心圆画出重心

    cv2.imshow("measure_object", image)
image = binary.copy()
measure_object(image)

#分割字符
# th = binary.copy()
# image = binary.copy()#拷贝一份，用于在上面修改
# h_h = b
# start = 0
# h_start,h_end = [],[]
# position = []
# #根据水平投影获取垂直分割
# for i in range(len(h_h)):
#     if h_h[i] >0 and start==0:
#         h_start.append(i)
#         start=1
#     if h_h[i] ==0 and start==1:
#         h_end.append(i)
#         start = 0
# for i in range(len(h_start)):
#     cropImg = th[h_start[i]:h_end[i],0:w]
#     if i==0:
#         pass
#     w_w = a
#     wstart,wend,w_start,w_end = 0,0,0,0
#     for j in range(len(w_w)):
#         if w_w[j]>0 and  wstart==0:
#             w_start = j
#             wstart = 1
#             wend = 0
#         if w_w[j] ==0 and wstart==1:
#             w_end = j
#             wstart = 0
#             wend = 1
#         #当确定了起点和终点之后保存坐标
#         if wend ==1:
#             position.append([w_start,h_start[i],w_end,h_end[i]])
#             wend = 0
# #确定分割位置
# for p in position:
#     cv2.rectangle(image,(p[0],p[1]),(p[2],p[3]),(0,255,0),2)



#显示
cv2.imshow("image1",image1)
cv2.imshow("gray",gray)
cv2.imshow("fanse",fanse)
cv2.imshow("binary",binary)
cv2.imshow("vproject",vproject)
cv2.imshow("hproject",hproject)
cv2.imshow("image",image)

cv2.waitKey()
cv2.destroyAllWindows()
