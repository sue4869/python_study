
from PyQt5.QtWidgets import *
import sys
from PyQt5 import uic
import math #로그랑 여러가지 수학 쓸수있게 한다.
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

# CalUI = "./calculator.ui"
CalUI = resource_path("./calculator.ui")

class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(CalUI, self)

        self.button_equal.clicked.connect(self.calculate)


    def calculate(self):
        foo = self.lineEdit.text()
        result = eval(foo) #eval : 문자열로 된 계산식을 계산하게 도와줌
        result_for_history = "{}\n= {}\n".format(foo,result)
        self.history.append(result_for_history) #result는 float타입이라서 append함수가 받아들이지 않아짐
        self.lineEdit.clear()            #문자열로 바꿈

QApplication.setStyle("fusion")
app =QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()

sys.exit(app.exec_())
