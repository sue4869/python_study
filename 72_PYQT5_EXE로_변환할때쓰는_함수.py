#1.먼저 pip install pyinstaller 한다
#2. 터미널 창에 pyinstaller --onefile --noconsole ./71_PYQT5_공학용계산기.py
#3.만들어진 파일.spec수정 -  dates=[] --> datas=[("./calculator.ui",".")]로 경로 작성
#                      - console=False

import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

# 위 함수를 exe로 만들려는 파일에 붙여넣기
# 그파일의 CalUI = "./calculator.ui" --> CalUI = resource_path("./calculator.ui")

#터미널 창에 pyinstaller --onefile --noconsole ./71_PYQT5_공학용계산기.spec 입력