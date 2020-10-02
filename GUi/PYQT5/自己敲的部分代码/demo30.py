'''
绘制各种图形
弧
圆形
椭圆
矩形
多边形
绘制图像
'''
import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class DrawAll(QWidget):
    def __init__(self):
        super(DrawAll,self).__init__()
        self.resize(300,300)
        self.setWindowTitle('绘制各种图形')
    def paintEvent(self,event):
        qb = QPainter()
        qb.begin(self)
        qb.setPen(Qt.blue)
        #绘制弧
        rect = QRect(0,10,100,100)#确定区域
        #alen:1个alen等于1/16度
        qb.drawArc(rect,0,50*16) #50度

        #通过弧绘制圆
        qb.setPen(Qt.red)
        qb.drawArc(120,10,100,100,0,360*16)#其实和上面的区别就是这里是360度

        #绘制带弦的弧
        qb.drawChord(10,120,100,100,12,130*16)

        #绘制扇形
        qb.drawPie(10,240,100,100,13,130*16)

        #绘制椭圆
        qb.drawEllipse(120,120,150,100)

        #绘制五边形
        point1 = QPoint(140,380)
        point2 = QPoint(270,420)
        point3 = QPoint(290,512)
        point4 = QPoint(290,588)
        point5 = QPoint(200,533)
        polygon = QPolygon([point1,point2,point3,point4,point5])
        qb.drawPolygon(polygon)

        #绘制图像
        image = QImage('F:\\桌面壁纸\\151222135615-2.jpg')
        rect = QRect(10,600,image.width()/6,image.height()/6)
        qb.drawImage(rect,image)


        # size = self.size()
        qb.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DrawAll()
    main.show()
    sys.exit(app.exec_())