import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QHBoxLayout, QWidget
from PyQt5.QtGui import QIcon
#此代码QMainWindow 的基本使用
class FirstMainWin(QMainWindow):
    # def __init__(self,parent=None):
    #     super(FirstMainWin,self).__init__(parent)
    #！！！！上面的两行也可以用下面的代替
    def __init__(self):
        super(FirstMainWin, self).__init__()
        #设置主窗口的标题
        self.setWindowTitle("第一个主窗口应用")
        #设置窗口的尺寸
        self.resize(400,300)
        self.status = self.statusBar()
        self.status.showMessage("只存在5s的消息",5000)
        # self.button1 = QPushButton('退出',self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("E:\\文件\\web\\img\\5.png"))
    main = FirstMainWin()
    main.show()
    sys.exit(app.exec_())
