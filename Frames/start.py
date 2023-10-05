from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QMovie


class Starting_Screen(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.frame_index = 0
        movie = QMovie("assets\mygif.gif")
        movie_label = QtWidgets.QLabel(self)
        movie_label.setMovie(movie)
        movie_label.setFixedSize(1000, 600)
        movie.start()

        header_font = self.create_font('Times New Roman', 40, True, True)
        button_font = self.create_font('Arial', 30, True, True)

        self.pushButton = self.create_button(QtCore.QRect(0, 70, 800, 600), button_font, '\nPRESS TO START', 'pushButton', 'background-color: transparent;')

        header = self.create_label(QtCore.QRect(260, 10, 290, 100), header_font, 'EasyWash', 'header')
        logo = self.create_label(QtCore.QRect(316, 150, 150, 150), header_font, '', 'logo')
        pixmap = QPixmap('assets/favicon.png')
        pixmap = pixmap.scaled(logo.size(), aspectRatioMode=True)
        logo.setPixmap(pixmap)

    def create_font(self, family, size, bold: bool, italic: bool):
        font = QtGui.QFont()
        font.setFamily(family)
        font.setPointSize(size)
        font.setBold(bold)
        font.setItalic(italic)
        return font

    def create_button(self, geom, font, text, name, style_sheet):
        pushButton = QtWidgets.QPushButton(self)
        pushButton.setGeometry(QtCore.QRect(geom))
        pushButton.setFont(font)
        pushButton.setObjectName(name)
        pushButton.setStyleSheet(style_sheet)
        pushButton.setText(text)
        return pushButton
    
    def create_label(self, geom, font, text, name):
        label = QtWidgets.QLabel(self)
        label.setGeometry(geom)
        label.setFont(font)
        label.setText(text)
        label.setObjectName(name)
        return label
    
