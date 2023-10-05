from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QMovie, QCursor, QIcon
import sys

class Ui_MainWindow(QtWidgets.QDialog):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        movie = QMovie("assets\mygif.gif")
        movie_label = QtWidgets.QLabel(MainWindow)
        movie_label.setMovie(movie)
        movie_label.setFixedSize(800, 600)
        movie.start()

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        washer_icon = QIcon('assets/washer.png')
        dryer_icon = QIcon('assets/dryer1.png')

        header_font = self.create_font('Arial', 15, True, True, 75)
        button_font = self.create_font('Arial', 10, True, True, 75)

        self.pushButton = self.create_button(QtCore.QRect(70, 100, 261, 360), header_font, 'pushButton', washer_icon)
        self.pushButton_2 = self.create_button(QtCore.QRect(470, 100, 251, 360), header_font, 'pushButton2', dryer_icon)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 20, 271, 41))
        self.label.setFont(header_font)
        self.label.setObjectName("label")

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(330, 490, 141, 51))

        self.pushButton_5.setFont(button_font)
        self.pushButton_5.setObjectName("pushButton_5")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EasyWash"))
        MainWindow.setWindowIcon(QIcon("assets/favicon.png"))
        self.pushButton.setText(_translate("MainWindow", "WASHER"))
        self.pushButton_2.setText(_translate("MainWindow", "DRYER"))
        self.label.setText(_translate("MainWindow", "WASHER OR DRYER ?"))
        self.pushButton_5.setText(_translate("MainWindow", "VOICE\nASSISTANT"))

    def create_font(self, family, size, bold: bool, italic: bool, weight):
        font = QtGui.QFont()
        font.setFamily(family)
        font.setPointSize(size)
        font.setBold(bold)
        font.setItalic(italic)
        font.setWeight(weight)
        return font
    
    def create_button(self, geom, font, name, icon=None):
        pushButton = QtWidgets.QPushButton(self.centralwidget)
        pushButton.setGeometry(QtCore.QRect(geom))
        pushButton.setIcon(icon) if icon != None else None
        pushButton.setFont(font)
        pushButton.setObjectName(name)
        pushButton.setStyleSheet("background-color: #D3D3D3")
        return pushButton

                

def main():
    app = QtWidgets.QApplication(sys.argv)
    win = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(win)

    win.show()
    sys.exit(app.exec_())
        
if __name__=='__main__':
    main()
