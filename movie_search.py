import sys
import csv
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("movie.ui")[0]


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_search.clicked.connect(self.search)

        file = open('movie.csv', 'r')
        self.movie = csv.reader(file)
        self.movie_list = []
        for i in self.movie:
            self.movie_list.append(i)
        self.movie_table.setRowCount(len(self.movie_list))

        for i in range(len(self.movie_list)):
            for j in range(0, 7):
                self.movie_table.setItem(i, j, QTableWidgetItem(self.movie_list[i][j]))

    def search(self):
        movie_title = self.lineEdit.text()
        print(movie_title)
        search_result = []
        for a_title in self.movie_list:
            print(a_title)
            if movie_title in a_title[0] or a_title[1]:
                print('yeah')
                self.movie_table.clearContents()
                search_result.append(a_title)
                self.movie_table.setRowCount(3)
                self.movie_table.setColumnCount(7)
        print(search_result)

        for i in range(len(search_result)):
            for j in range(len(search_result[0])):
                # i번째 줄의 j번째 칸에 데이터를 넣어줌
                self.movie_table.setItem(i, j, QTableWidgetItem(search_result[i][j]))




if __name__ == "__main__":
    app = QApplication(sys.argv)

    main = WindowClass()

    main.show()

    app.exec_()
