'''
QLineEdit控件与回显模式
基本功能：输入单行的文本
EchoMode(回显模式):4种
1.Normal
2.NoEcho
3.Password
4.PasswordEchoOnEdit

'''
from PyQt5.QtWidgets import *
import sys

class QLineEditEchoMode(QWidget):
    def __init__(self):
        super(QLineEditEchoMode, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('文本输入框的回显模式')
        formLayout = QFormLayout()

        normalLineEdit = QLineEdit()
        noEchoLineEdit = QLineEdit()
        passwordLineEdit = QLineEdit()
        passwordEchoOnEditLineEdit = QLineEdit()
        #将文本框加入到表单布局器中
        formLayout.addRow("Normal1",normalLineEdit)
        formLayout.addRow("NoEcho1",noEchoLineEdit)
        formLayout.addRow("Password1",passwordLineEdit)
        formLayout.addRow("PasswordEchoOnEdit1",passwordEchoOnEditLineEdit)

        #设置文本框的提示值
        normalLineEdit.setPlaceholderText("Normal")
        noEchoLineEdit.setPlaceholderText("NoEcho")
        passwordEchoOnEditLineEdit.setPlaceholderText("passwordEchoOnEdit")
        passwordLineEdit.setPlaceholderText("password")
        #设置文本框格式
        normalLineEdit.setEchoMode(QLineEdit.Normal)
        noEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
        passwordLineEdit.setEchoMode(QLineEdit.Password)
        passwordEchoOnEditLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.setLayout(formLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLineEditEchoMode()
    main.show()
    sys.exit(app.exec_())











