'''
按钮控件（QPushButton）
QPushButton
AToolButton
QRadioButton
QCheckBox
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class QPushButtonDemo(QDialog):
    def __init__(self):
        super(QPushButtonDemo, self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('QPushButton')
        self.resize(300,320)
        layout = QVBoxLayout()
        self.button1 = QPushButton('第一个按钮 ')
        self.button2 = QPushButton()
        self.button2.setText('第二个按钮')
        #给按钮加上图片
        self.button2.setIcon(QIcon('E:\\文件\\web\\img\\5.png'))

        self.button3 = QPushButton('不可用按钮')
        self.button3.setEnabled(False)

        self.button4 = QPushButton('&MyButton')#按Alt+M  即可点击
        self.button4.setDefault(True)


        #让按钮1点击后不会自动弹起
        self.button1.setCheckable(True)
        self.button1.toggle()

        self.button1.clicked.connect(lambda :self.wichButton(self.button1))
        self.button2.clicked.connect(lambda :self.wichButton(self.button2))
        self.button4.clicked.connect(lambda :self.wichButton(self.button4))
        self.button1.clicked.connect(self.buttonState)

        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)
        self.setLayout(layout)

    def wichButton(self,btn):
        print('被单击的按钮是<'+btn.text()+">")
    def buttonState(self):
        if self.button1.isChecked():
            print('按钮1已经被选中')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QPushButtonDemo()
    main.show()
    sys.exit(app.exec_())