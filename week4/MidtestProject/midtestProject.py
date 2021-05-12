import time
import random
import sys
import webbrowser
import requests
import openpyxl

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import *

#엑셀 파일에서 사용할 상수 선언
FULL_DATE=0; YEAR=1; MONTH=2; DAY=3; MONEY=4;

#UI 파일 연결하기
form_class = uic.loadUiType("midtestProjectUI.ui")[0]

class WindowClass(QMainWindow, form_class) :#윈도우 클래스 선언
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

    #-----------여기서부터---------------------#
        self.inputBtn.clicked.connect(self.inputBtnClick)
        #self.dateLabel
        #self.calendar = QCalendarWidget(self)
        #self.calender.selectionChanged.connect(self.calendar_change)

    def inputBtnClick(self):
        colorBackground(self.degreeInput.value())
        
    def loadData(self): #엑셀에 담겨있는 날짜와 원화 데이터 가져오기 
        excel_file = openpyxl.load_workbook('data.xlsx')
        excel_sheet = excel_file.active

        global date_dict, dolloar_dict
        date_dict={}
        dollar_dict={}

        for row in excel_sheet.rows:
            date_dict[row[FULL_DATE].value]={int(row[YEAR].value),int(row[MONTH].value),int(row[DAY].value)}
            dollar_dict[row[FULL_DATE].value]=int(row[MONEY].value)
        
        excel_file.close()

    def colorBackground(data):
        format=QTextCharFormat()
        for date in date_dict.keys():
            if dollar_dict[date][0] <data : format.setBackground(QBrush(QColor(Qt.Blue)))
            else : format.setBackground(QBrush(QColor(Qt.Red)))
            date=QDate(data_dict[date][YEAR-1],data_dict[date][MONTH-1],data_dict[date][DAY-1])
            self.calendar.setDateTextFormat(date, format)
    
    #---------------여기까지---------------------#
        

if __name__ == "__main__" :#메인 함수 선언
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.loadData()
    myWindow.show()
    a=input()
    app.exec_()

#달력 UI
#오늘 날짜는 Bold 또는 눈에 보이는 방식으로
#날짜 클릭했을때 팝업창 (토스트메세지로 환율
#input창으로 숫자입력 후 함수호출 시 날짜마다 색변환
