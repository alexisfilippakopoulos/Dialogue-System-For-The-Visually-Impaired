from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QMovie, QCursor, QIcon
import sys


class First_Frame(QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        movie = QMovie("assets\mygif.gif")
        movie_label = QtWidgets.QLabel(self)
        movie_label.setMovie(movie)
        movie_label.setFixedSize(800, 600)
        movie.start()

        washer_icon = QIcon('assets/washer.png')
        dryer_icon = QIcon('assets/dryer1.png')

        header_font = self.create_font('Arial', 15, True, True, 75)
        button_font = self.create_font('Arial', 10, True, True, 75)

        pushButton = self.create_button(QtCore.QRect(70, 100, 261, 360), header_font, 'WASHER' , 'pushButton', washer_icon)
        pushButton2 = self.create_button(QtCore.QRect(470, 100, 251, 360), header_font, 'DRYER', 'pushButton2', dryer_icon)

        label = QtWidgets.QLabel(self)
        label.setGeometry(QtCore.QRect(280, 20, 271, 41))
        label.setFont(header_font)
        label.setObjectName("label")
        label.setText('WASHER OR DRYER ?')

        pushButton_3 = self.create_button(QtCore.QRect(330, 490, 141, 51), button_font, 'VOICE\nASSISTANT', 'pushButton3')


    def create_font(self, family, size, bold: bool, italic: bool, weight):
        font = QtGui.QFont()
        font.setFamily(family)
        font.setPointSize(size)
        font.setBold(bold)
        font.setItalic(italic)
        font.setWeight(weight)
        return font
    
    def create_button(self, geom, font, text, name, icon=None):
        pushButton = QtWidgets.QPushButton(self.centralwidget)
        pushButton.setGeometry(QtCore.QRect(geom))
        pushButton.setIcon(icon) if icon != None else None
        pushButton.setFont(font)
        pushButton.setObjectName(name)
        pushButton.setStyleSheet("background-color: #D3D3D3")
        pushButton.setText
        return pushButton
    
if __name__ == '__main__':
