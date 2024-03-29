'''
滑块控件(QSlider)
'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class QSliderDemo(QWidget):
    def __init__(self):
        super(QSliderDemo, self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('滑块控件演示')
        self.resize(300,700)
        layout = QVBoxLayout()
        self.label = QLabel('你好PyQt5')
        self.label.setAlignment(Qt.AlignCenter)#文本居中
        layout.addWidget(self.label)
        self.slider = QSlider(Qt.Horizontal)#让滑块水平拜访   如果是Qt.Vertical 则是竖直
        #设置最小值
        self.slider.setMinimum(12)
        #设置最大值
        self.slider.setMaximum(48)

        #步长
        self.slider.setSingleStep(3)

        #设置当前值
        self.slider.setValue(18)

        #设置刻度的位置,刻度在下方
        self.slider.setTickPosition(QSlider.TicksBelow)
        #设置刻度的间隔
        self.slider.setTickInterval(6)
        layout.addWidget(self.slider)
        self.slider.valueChanged.connect(self.valueChange)
        self.setLayout(layout)

    def valueChange(self):
        print('当前值: %s' % self.slider.value())
        size = self.slider.value()
        self.label.setFont(QFont('Arial',size))






if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QSliderDemo()
    main.show()
    sys.exit(app.exec_())