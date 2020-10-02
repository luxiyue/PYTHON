#QLabel控件
'''基本方法
setAlignment():设置文本的对齐方式
setIndent():设置文本缩进
text():获取文本内容
setBuddy():设置伙伴关系
setText():设置文本内容
selectedText():返回所选择的字符
setWordWrap():设置是否允许换行
'''
'''QLabel常见的信号（事件）
1.当鼠标划过QLabel控件时触发:linkHovered
2.当鼠标单击QLabel控件时触发:linkActivated
3.
'''

import sys
from PyQt5.QtWidgets import QHBoxLayout, QWidget, QLabel, QVBoxLayout, QApplication
from PyQt5.QtCore import  Qt
from PyQt5.QtGui import QPalette,QPixmap


class QLabelDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        label1.setText("<font color='yellow'>这是一个文本标签</font>")
        label1.setAutoFillBackground(True)#开启背景的调色
        patette = QPalette()
        patette.setColor(QPalette.Window,Qt.blue)
        label1.setPalette(patette)
        label1.setAlignment(Qt.AlignCenter)#文本居中对齐

        label2.setText("<a href='#'> 欢迎使用Python GUI程序</a>")

        label3.setAlignment(Qt.AlignCenter)#文本居中对齐
        label3.setToolTip('这是一个图片标签')
        label3.setPixmap(QPixmap("E:\\文件\\web\\img\\1.jpg"))#放置图片


        label4.setText("<a href='https://space.bilibili.com/397055729/favlist'>即可将看就看</a>")
        label4.setOpenExternalLinks(True)#开启点击超链接进入网页的功能
        label4.setAlignment(Qt.AlignRight)#向右对齐
        label4.setToolTip('这是一个超级连接')

        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)

        label2.linkHovered.connect(self.linkHovered)
        label4.linkActivated.connect(self.linkClicked)

        self.setLayout(vbox)
        self.setWindowTitle('QLabel控件演示')

    def linkHovered(self):
        print('当鼠标滑过label2标签时，触发事件')
    def linkClicked(self):
        print('当鼠标单击Label4标签时，触发事件')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLabelDemo()
    main.show()
    sys.exit(app.exec_())
