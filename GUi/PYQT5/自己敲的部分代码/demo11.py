'''
QLineEdit控件的输入(校验器)
如限制只能输入整数、浮点或满足一定条件的字符串
'''

from PyQt5.QtWidgets import *
import sys
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QRegExpValidator
from PyQt5.QtCore import QRegExp

class QLineEditValidator(QWidget):
    def __init__(self):
        super(QLineEditValidator, self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("校验器")
        #创建表单布局
        formLayout = QFormLayout()

        intLineEdit = QLineEdit()
        doubleLineEdit = QLineEdit()
        validatorLineEdit = QLineEdit()

        #将上面的三个组件加入布局管理器
        formLayout.addRow('整数类型',intLineEdit)
        formLayout.addRow('浮点类型',doubleLineEdit)
        formLayout.addRow('数字和字母',validatorLineEdit)

        intLineEdit.setPlaceholderText('整数类型')
        doubleLineEdit.setPlaceholderText('浮点类型')
        validatorLineEdit.setPlaceholderText('字母和数字')

        #整数校验器【1,99】
        intValidator = QIntValidator(self)
        intValidator.setRange(1,99)

        #浮点校验器【-360,360】,精度：小数点后2位
        doubleValidator = QDoubleValidator(self)
        doubleValidator.setRange(-360,360)
        doubleValidator.setNotation(QDoubleValidator.StandardNotation)
        #设置精度，小数点后2位
        doubleValidator.setDecimals(2)

        #字符和数字
        reg = QRegExp('[a-zA-Z0-9]+$')
        validator = QRegExpValidator(self)
        validator.setRegExp(reg)

        #设置校验器
        intLineEdit.setValidator(intValidator)
        doubleLineEdit.setValidator(doubleValidator)
        validatorLineEdit.setValidator(validator)

        self.setLayout(formLayout)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLineEditValidator()
    main.show()
    sys.exit(app.exec_())


