#gui : grapic user interface
# 사용자에게 시각적으로 인터페이스 해주는 환경
# 기본 템플릿

from PyQt5.QtWidgets import *
import sys
from PyQt5 import uic

TestUI = "./test.ui"

class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(TestUI, self)

        #puchbutton을 누르면 showString을 호출
        self.pushButton.clicked.connect(self.showString)#pushButton을 불러오기 이름이 변수가 됨됨

    def showString(self):
        result = self.lineEdit.text() #사용자가 입력한 문자열을 result에 들어감
        self.label.setText(result) #라벨에 result가 들어감

QApplication.setStyle("fusion")
app =QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()

sys.exit(app.exec_())
