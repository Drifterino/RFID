from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import os
import csv


class GuestLog(QWidget):
    def __init__(self):
        super(GuestLog, self).__init__()
        self.title = "Epstein Hillel Guest Log"
        self.left = 50
        self.top = 50
        self.width = 600
        self.height = 500
        self.header_image = 1000
        self.icon = "epstein-hillel-logo-color.svg"
        self.grid = QGridLayout()
        self.RFID_Dictionary = {}
        self.People_Present = ['Devon Barker']
        self.Greetings = ['Good Bye', 'Welcome']
        self.Greet = True
        self.scanning = True
        self.button = QPushButton('&Load Names', clicked=self.open)
        self.entry = QLineEdit()
        self.createUI()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            self.close()
        if event.key() == Qt.Key.Key_F11:
            if self.isFullScreen():
                self.showNormal()
            else:
                self.showFullScreen()

    def createUI(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon(self.icon))
        self.resize(self.width, self.height)
        self.setStyleSheet('format.css')
        self.setLayout(self.grid)
        self.drawItems()

    def drawItems(self):

        # Logo
        self.imageLogo = QPixmap(self.icon)
        self.imageLogo.scaled(self.header_image, self.header_image, Qt.AspectRatioMode.KeepAspectRatio)
        self.logo = QLabel()
        self.logo.setPixmap((self.imageLogo))
        self.logo.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.grid.addWidget(self.logo,0,0,1,3)
        #self.grid.setRowMinimumHeight(200,200)

        # Greeting Text
        self.welcome_text = QLabel(f"{self.Greetings[self.Greet]},\n{self.People_Present[0]}")
        self.welcome_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.welcome_text.setStyleSheet('''
            font-size: 20px;
            ''')
        self.grid.addWidget(self.welcome_text,1,0,1,3)

        # Roster
        self.roster = QLabel(f"{self.People_Present}")
        self.roster.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.roster.setStyleSheet("""
            font-size: 15px;
            """)
        self.grid.addWidget(self.roster,2,0,1,3)

        # File Select Button

        self.grid.addWidget(self.button,3,2,1,1)

        self.grid.addWidget(self.entry, 4, 0, 1, 3)



    def open(self):
        file = QFileDialog.getOpenFileName(self, "Open Personnel ID CSV File", "", "CSV Files (*.csv)")
        if file:
            self.RFID_Dictionary = csv_to_dict(str(file[0]))
            print(f'{len(self.RFID_Dictionary)} RFID Tags Loaded')



def csv_to_dict(csv_file):
    with open(csv_file, mode='r') as in_file:
        reader = csv.reader(in_file)
        with open('parsed_csv.csv', mode='w') as out_file:
            writer = csv.writer(out_file)
            RFID_dict = {rows[0]: rows[1] for rows in reader}
            os.remove('parsed_csv.csv')
            return RFID_dict