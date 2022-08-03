from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 
from rainy import check_winter
import sys
import os

def resource_path(relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 500)
        MainWindow.setStyleSheet("background-color: black;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # create label
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 200, 200))
        self.label.setMinimumSize(QtCore.QSize(500, 500))
        self.label.setMaximumSize(QtCore.QSize(500, 500))
        self.label.setObjectName("label")

        # add label to main window
        MainWindow.setCentralWidget(self.centralwidget)

        gif1 = resource_path('stars.gif')
        gif2 = resource_path('rain_a.gif')
        res = check_winter(resource_path('cities.txt'), resource_path('citylocs.txt'))
        if res == 0:
            result = QLabel(" No winter weather this week :(", self.label)
            self.movie = QMovie(gif1)
            self.label.setMovie(self.movie)
            self.movie.start()
        else:
            result = QLabel(' '+ res, self.label)
            self.movie = QMovie(gif2)
            self.label.setMovie(self.movie)
            self.movie.start()
        pal = result.palette()
        pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("cyan"))
        result.setPalette(pal)
        result.setStyleSheet("background-color: rgba(0,0,0,0%)")
        result.setFont(QFont('Arial', 21))

            

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())