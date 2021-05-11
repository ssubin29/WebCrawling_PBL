import time
import random
import sys
import webbrowser
import requests
from bs4 import BeautifulSoup

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
    def takeCrawling():
        exchange_rate={}
        for page_num in range(10):
            res = requests.get
            ('https://finance.naver.com/marketindex/exchangeDailyQuote.nhn?marketindexCd=FX_USDKRW&page=' + str(page_num + 1))
            soup = BeautifulSoup(res.content, 'html.parser')
            data = soup.select('table.tbl_exchange.today tbody tr')
            for item in data:
                exchange_rate[item.find('td',{'class':'date'}).get_text().strip()] = float(item.find('td',{'class':'num'}).get_text().strip().replace(',',''))   
        print(exchange_rate)
    
    def printC(self,**er):
        print(er)
    #---------------여기까지---------------------#
        

if __name__ == "__main__" :#메인 함수 선언
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    #printC(takeCrawling())
    app.exec_()

#달력 UI
#오늘 날짜는 Bold 또는 눈에 보이는 방식으로
#날짜 클릭했을때 팝업창 (토스트메세지로 환율
#input창으로 숫자입력 후 함수호출 시 날짜마다 색변환
