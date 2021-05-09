import time
import random
import sys
import webbrowser

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import *

#UI 파일 연결하기
form_class = uic.loadUiType("midtestProjectUI.ui")[0]

class WindowClass(QMainWindow, form_class) :#윈도우 클래스 선언
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

    #-----------여기서부터---------------------#
    def printForCheck(self):
        return (self.calendarWidget.firstDayOfWeek)

    def clickDate(self):
        return 0;

    #def 
    #---------------여기까지---------------------#
        

if __name__ == "__main__" :#메인 함수 선언
    
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    print(type(myWindow.printForCheck()))
    app.exec_()

#달력 UI
#오늘 날짜는 Bold 또는 눈에 보이는 방식으로
#날짜 클릭했을때 팝업창 (토스트메세지로 환율
#input창으로 숫자입력 후 함수호출 시 날짜마다 색변환
