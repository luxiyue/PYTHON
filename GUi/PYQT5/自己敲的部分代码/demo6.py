#此代码讲述屏幕坐标系
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow


def onClick():
    print("1")
    print("窗口x坐标为  :%d"  % widget.x() )#窗口横坐标
    print("窗口y坐标为  :%d"  % widget.y())#窗口纵坐标
    print("窗口宽度为  :%d"  % widget.width())#  工作区宽度
    print("窗口高度为  :%d"  % widget.height())# 工作区高度
    print("2")
    print("窗口x坐标为  :%d"  % widget.geometry().x() ) # 工作区横坐标
    print("窗口y坐标为  :%d"  % widget.geometry().y())#   工作区纵坐标 因为他没有算标题栏宽度，所以数值要比上面的大
    print("窗口宽度为  :%d"  % widget.geometry().width())#工作区宽度
    print("窗口高度为  :%d"  % widget.geometry().height())#240 工作区高度
    print("3")
    print("窗口x坐标为  :%d"  % widget.frameGeometry().x() )# 窗口横坐标
    print("窗口y坐标为  :%d"  % widget.frameGeometry().y())# 窗口纵坐标
    print("窗口宽度为  :%d"  % widget.frameGeometry().width())
    print("窗口高度为  :%d"  % widget.frameGeometry().height())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # widget = QMainWindow()
    widget = QWidget()
    btn = QPushButton("按钮",widget)#如果加了第一个参数，则不需要下面的一行代码,第二个参数是指控件放入的位置
    # btn.setText("按钮")
    btn.move(24,52)
    btn.clicked.connect(onClick)
    widget.resize(300,240)
    widget.move(100,200)
    widget.setWindowTitle('屏幕坐标系')
    widget.show()
    sys.exit(app.exec_())