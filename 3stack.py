import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("stack.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        # ui 불러오기. 객체생성
        self.setupUi(self)
        # stack의 페이지를 첫 페이지로 고정
        self.stackedWidget.setCurrentIndex(0)
        # 버튼의 클릭이벤트와 함수 연결
        self.button0.clicked.connect(self.to_second_page)
        self.button1.clicked.connect(self.to_third_page)
        self.button2.clicked.connect(self.to_first_page)

    def to_second_page(self): # stack인덱스1로 연결할 버튼함수
        self.stackedWidget.setCurrentIndex(1)

    def to_third_page(self): # stack인덱스2로 연결할 버튼함수
        self.stackedWidget.setCurrentIndex(2)

    def to_first_page(self): # stack인덱스0로 연결할 버튼함수
        self.stackedWidget.setCurrentIndex(0)

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()