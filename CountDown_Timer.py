from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QTextEdit, QPushButton, QLineEdit
from PyQt5 import uic
import sys
import time
from PyQt5.QtCore import QTimer
import res

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the ui file
        uic.loadUi("CountDown Timer.ui", self)

        # Define Our Widgets
        self.min_lineEdit = self.findChild(QLineEdit, "m_lineEdit")
        self.sec_lineEdit = self.findChild(QLineEdit, "s_lineEdit")
        self.Timer_lineEdit = self.findChild(QLineEdit, "Timer_lineEdit")
        self.textEdit = self.findChild(QTextEdit, "textEdit")
        self.set_timer_bt = self.findChild(QPushButton, "set_timer_bt")


        # Do something
        self.set_timer_bt.clicked.connect(self.check)

        self.timer = QTimer()
        self.timer.timeout.connect(self.check_timer)
        self.remaining_time = 0

        self.textEdit.setText('WellCome\nPlease inter timer')

        # Show The App
        self.show()


    def check(self):
        minutes = self.min_lineEdit.text()
        seconds = self.sec_lineEdit.text()

        try:
            minutes = int(minutes)
            seconds = int(seconds)
            self.textEdit.setText('Timer Started!')
            self.remaining_time = minutes * 60 + seconds
            self.show_timer()
            self.timer.start(1000)
        except ValueError:
            self.textEdit.setText("Invalid input")

    def check_timer(self):
        if self.remaining_time > 0:
            self.remaining_time -= 1
            self.show_timer()
        else:
            self.timer.stop()
            self.textEdit.setText("Timer Finish!")

    def show_timer(self):
        minutes, seconds = divmod(self.remaining_time, 60)
        self.Timer_lineEdit.setText(f"{minutes:02d}:{seconds:02d}")

# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
