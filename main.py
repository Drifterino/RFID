import sys
import csv
import os

from PyQt6.QtWidgets import *
from PyQt6.QtGui import QIcon, QFont, QFontDatabase
from PyQt6 import QtCore

from window import guest_log



RFID_Dictionary = {}

#TODO Find out how to open a PyQt6 UI file

class MyApp(QWidget):
    def __init__(self):
        super(MyApp, self).__init__()
        self.setWindowTitle('Epstein Hillel Guest Log')
        self.setWindowIcon(QIcon('epstein-hillel-logo-color.svg'))
        self.resize(500, 350)
        #self.setContentsMargins(20, 20, 20, 20)
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.RFID_Dictionary = {}
        self.People_Present = []
        self.scanning = True

        id = QFontDatabase.addApplicationFont("/home/deck/Documents/RFID/Res/Metropolis-Medium.otf")
        if id < 0: print("Error")

        families = QFontDatabase.applicationFontFamilies(id)
        print(families[0])

        label = QLabel("Hello World", self)
        label.setFont(QFont(families[0]))
        #label.move(50, 100)

        # Widgets
        self.inputField = QLineEdit()
        button = QPushButton('&Say Hello', clicked=self.open)
        self.output = QTextEdit()

        # layout.addWidget(self.inputField)
        # layout.addWidget(button)
        # layout.addWidget(self.output)

    def sayhello(self):
        inputText = self.inputField.text()
        inputText = self.RFID_Dictionary[10055]
        self.output.setText(f'Hello {inputText}')

    def open(self):
        file = QFileDialog.getOpenFileName(self, "Open Personnel ID CSV File", "", "CSV Files (*.csv)")
        if file:
            self.RFID_Dictionary = csv_to_dict(str(file[0]))
            self.output.setText(self.RFID_Dictionary[str(10053)])

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key.Key_Escape:
            self.close()
        if event.key() == QtCore.Qt.Key.Key_F11:
            if self.isFullScreen():
                self.showNormal()
            else:
                self.showFullScreen()


    def drawItems(self):
        self.imageLogo = QPixmap("epstein-hillel-logo-color.svg")


def csv_to_dict(csv_file):
    with open(csv_file, mode='r') as in_file:
        reader = csv.reader(in_file)
        with open('parsed_csv.csv', mode='w') as out_file:
            writer = csv.writer(out_file)
            RFID_dict = {rows[0]:rows[1] for rows in reader}
            os.remove('parsed_csv.csv')
            return RFID_dict


app = QApplication(sys.argv)
app.setStyleSheet('''
        QWidget {
            font-size: 25px;
        }
        
        QPushButton {
            font-size: 20px;
        }

    ''')

window = MyApp()
window.show()

# scanned_id = input()
# if scanned_id in window.People_Present:
#     window.People_Present.remove(scanned_id)
#     print(f"Good Bye, {RFID_Dictionary[scanned_id]}")
# else:
#     window.People_Present.append(scanned_id)
#     print(f"Welcome, {RFID_Dictionary[scanned_id]}")
# for people in window.People_Present:
#     print(RFID_Dictionary[people])

sys.exit(app.exec())