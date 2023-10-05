from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QMovie, QCursor, QIcon, QPainter, QColor


class Final_Frame(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.frame_index = 11
        movie = QMovie("assets\mygif.gif")
        movie_label = QtWidgets.QLabel(self)
        movie_label.setMovie(movie)
        movie_label.setFixedSize(800, 600)
        movie.start()

        center_button_style = 'QPushButton { border: 2px solid black; border-radius: 10px; background-color: #F0F8FF;}'
        lower_button_style = 'QPushButton { border: 2px solid red; border-radius: 10px; background-color: white;}'

        self.font = self.create_font('Arial', 20, True, True, 75)

        self.yes_button = self.create_button(QtCore.QRect(70, 100, 251, 360), self.font, 'YES' , 'yes_button', center_button_style)
        self.no_button = self.create_button(QtCore.QRect(470, 100, 251, 360), self.font, 'NO' , 'no_button', center_button_style)

        self.back_button = self.create_button(QtCore.QRect(70, 500, 261, 61), self.font, 'BACK', 'back_button', lower_button_style, 'assets/back.png', 50, 40)
        self.exit_button = self.create_button(QtCore.QRect(470, 500, 261, 61), self.font, 'EXIT', 'exit_button', lower_button_style, 'assets/exit.png', 50, 40)

        header = self.create_label(QtCore.QRect(135, 24, 550, 34), self.font, 'START THE PROPOSED CYCLE ?', 'header')
        #recommendation = self.create_label(QtCore.QRect(170, 130, 460, 51), font, '')


    def create_font(self, family, size, bold: bool, italic: bool, weight):
        font = QtGui.QFont()
        font.setFamily(family)
        font.setPointSize(size)
        font.setBold(bold)
        font.setItalic(italic)
        font.setWeight(weight)
        return font
    
    def create_button(self, geom, font, text, name, style_sheet, icon_path=None, icon_width=None, icon_height=None):
        pushButton = QtWidgets.QPushButton(self)
        pushButton.setGeometry(QtCore.QRect(geom))
        if icon_path is not None:
            icon = QtGui.QIcon(icon_path)
            pushButton.setIcon(icon)
            pushButton.setIconSize(QtCore.QSize(icon_width, icon_height))
        pushButton.setFont(font)
        pushButton.setObjectName(name)
        pushButton.setStyleSheet(style_sheet)
        pushButton.setText(text)
        return pushButton
    
    def create_label(self, geom, font, text, name, stylesheet=None):
        label = QtWidgets.QLabel(self)
        label.setGeometry(geom)
        label.setFont(font)
        label.setText(text)
        label.setObjectName(name)
        label.setStyleSheet(stylesheet)
        return label
        
    
