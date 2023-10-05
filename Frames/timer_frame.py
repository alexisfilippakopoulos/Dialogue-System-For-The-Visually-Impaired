from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QMovie
from PyQt5.QtCore import QTimer, QTime, Qt, QMetaObject
from PyQt5.QtWidgets import QWidget


class TimerFrame(QWidget, QtCore.QObject):
    timer_signal = QtCore.pyqtSignal()
    def __init__(self):
        super().__init__()
        self.frame_index = 10
        movie = QMovie("assets\mygif.gif")
        movie_label = QtWidgets.QLabel(self)
        movie_label.setMovie(movie)
        movie_label.setFixedSize(800, 600)
        movie.start()

        self.timer = QTimer()

        header_font = self.create_font('Times New Roman', 40, True, True, 75)
        font = self.create_font('Arial', 18, True, True, 75)

        #header = self.create_label(QtCore.QRect(270, 20, 281, 41), font, "TIME LEFT", 'header')

        header = self.create_label(QtCore.QRect(260, 10, 290, 100), header_font, 'EasyWash', 'header')
        logo = self.create_label(QtCore.QRect(330, 150, 150, 150), header_font, '', 'logo')
        pixmap = QPixmap('assets/favicon.png')
        pixmap = pixmap.scaled(logo.size(), aspectRatioMode=True)
        logo.setPixmap(pixmap)

        timer_font = self.create_font('MS Shell Dig 2', 40, False, False, 75)
        self.label = self.create_label(QtCore.QRect(230, 380, 350, 80), timer_font,"","")


    def start_timer(self, hours, minutes, seconds):
        self.timer.timeout.connect(self.update_timer)
        self.remaining_time = QTime(hours, minutes, seconds)
        self.update_label()
        # Start the timer indirectly from the main thread
        QMetaObject.invokeMethod(self.timer, "start", QtCore.Qt.QueuedConnection, QtCore.Q_ARG(int, 1000))

        
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
        label.setAlignment(Qt.AlignCenter)
        label.setObjectName(name)
        label.setStyleSheet(stylesheet)
        return label
    

    def update_timer(self):
        self.remaining_time = self.remaining_time.addSecs(-1)  # Decrement the time by 1 second
        self.update_label()
        if self.remaining_time == QTime(0, 0):  # Timer has reached 0
            self.timer.stop()
            self.timer_signal.emit()

    def update_label(self):
        self.label.setText(self.remaining_time.toString("hh:mm:ss"))











