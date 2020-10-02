#使用Qt Designer
#方法一：在命令行中（此工作目录下）敲下面的命令
# python -m PyQt5.uic.pyuic gg.ui -o demo.py

#方法二:
# pyuic5 gg.ui -o demo.py

#方法三:增加扩展工具PyUIC


#下面是调用生成的python代码的例子
import sys
from 自己敲的部分代码 import gg

from PyQt5.QtWidgets import QApplication,QMainWindow
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = gg.Ui_MainWindow()###!!!!!!!!!!!!!!!!注意想看其他的生成ui ,改这里就行了
    #向主窗口上添加控件
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())



