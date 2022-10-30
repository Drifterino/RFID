from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *


class GuestLog(QWidget):
    def __init__(self):
        super(GuestLog, self).__init__()
        self.title = "Epstein Hillel Guest Log"
        self.left = 50
        self.top = 50
        self.width = 600
        self.height = 500
        self.icon = "epstein-hillel-logo-color.svg"
        self.grid = QGridLayout()
        self.RFID_Dictionary = {}
        self.People_Present = ['Devon Barker']
        self.Greetings = ['Good Bye', 'Welcome']
        self.Greet = True
        self.scanning = True
        self.createUI()

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
        self.logo = QLabel()
        self.logo.setPixmap((self.imageLogo))
        self.logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.grid.addWidget(self.logo,0,0)

        # Greeting Text
        self.welcome_text = QLabel(f"{self.Greetings[self.Greet]},\n{self.People_Present[0]}")
        self.welcome_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.welcome_text.setStyleSheet('''
            font-size: 20px;
            ''')
        self.grid.addWidget(self.welcome_text,1,0)

        # Roster
        self.roster =QLabel(f"People")
        self.roster.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.roster.setStyleSheet("""
            font-size: 15px;
            """)
        self.grid.addWidget(self.roster,2,0)


    def csv_to_dict(csv_file):
        with open(csv_file, mode='r') as in_file:
            reader = csv.reader(in_file)
            with open('parsed_csv.csv', mode='w') as out_file:
                writer = csv.writer(out_file)
                RFID_dict = {rows[0]: rows[1] for rows in reader}
                os.remove('parsed_csv.csv')
                return RFID_dict

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