import cv2
import cv2 as cv
import numpy as np
from PIL import Image, ImageDraw, ImageFont

rgbimage_std = cv.imread("../img/0.bmp")

rgb2grayimage_std = cv2.cvtColor(rgbimage_std, cv2.COLOR_RGB2GRAY)



for i in range(1,6,1):
    imagename = "../img/" +str(i) + '.bmp'
    rgbimage_defect = cv.imread(imagename)
    # 将每次imagename对应图像在图像窗口显示出来
    # cv.imshow(imagename, rgbimage_defect)

    # 将24位rgbimage_defect彩色图像转换8位rgb2grayimage_defect灰度图
    # gray = np.array(rgbimage_defect)
    # gray = gray[:, :, 0]
    gray = cv2.cvtColor(rgbimage_defect, cv2.COLOR_RGB2GRAY)
    print(np.array(gray))
    rgb2grayimage_defect = np.array([gray, gray, gray])
    # 转 置
    rgb2grayimage_defect = np.transpose(rgb2grayimage_defect, (1, 2, 0))

    name = str(i) + '_rgb2grayimage_defect.bmp'
    # cv.imshow(name, rgb2grayimage_defect)

    # 缺陷比较
    # 直方图计算的函数，反应灰度值的分布情况
    be_compare_image = cv2.calcHist([rgb2grayimage_std], [0], None, [256], [0.0, 255.0])
    compare_image = cv2.calcHist([rgb2grayimage_defect], [0], None, [256], [0.0, 255.0])

    # 相关性计算，采用相关系数的方式
    # result = cv2.compareHist(be_compare_image,compare_image,method=cv2.HISTCMP_CORREL)
    result = sum(be_compare_image - compare_image)[0]
    # 打开PIL创建的图像
    ss = Image.open("../img/" + str(i) + ".bmp")
    # 创建一个操作对象
    draw = ImageDraw.Draw(ss)
    # 字体对象为simsun，字大小为50号
    fnt = ImageFont.truetype(r'C:\Windows\Fonts\simsun.ttc', 50)
    # 如果图片对比原图相似度小于7，则合格；否则不合格。
    if result < 7:
        draw.text((5, 10), u'合格', fill='red', font=fnt)
        th_str = str(i) + '.bmp'
        draw.text((5, 350), th_str, fill='red', font=fnt)
    else:
        draw.text((5, 10), u'不合格', fill='red', font=fnt)
        th_str = str(i) + '.bmp'
        draw.text((5, 350), th_str, fill='red', font=fnt)
    ss.show("result" + str(i) + ".png")
cv.waitKey(0)

