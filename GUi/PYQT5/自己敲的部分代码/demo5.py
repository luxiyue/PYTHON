import sys
from PyQt5.QtWidgets import QHBoxLayout, QMainWindow, QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
#此代码展示如何退出应用程序
class QuitApplication(QMainWindow):
    def __init__(self):
        super(QuitApplication, self).__init__()
        self.resize(300,120)
        self.setWindowTitle("退出应用程序")
        #添加Button
        self.button1 = QPushButton('退出')
        #将信号与曹关联
        self.button1.clicked.connect(self.onClick_Button)#注意onClick_Button方法后面不需要加上（）
        layout = QHBoxLayout()
        layout.addWidget(self.button1)
        #在创建一个子窗口
        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        #将子窗口放进容器
        self.setCentralWidget(mainFrame)

    #按钮单击事件的方法
    def onClick_Button(self):
        sender = self.sender()
        print(sender.text()+' 按钮被按下  ')
        app = QApplication.instance()
        #退出应用程序
        app.quit()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("E:\\文件\\web\\img\\5.png"))
    main = QuitApplication()
    main.show()
    sys.exit(app.exec_())
