import sys
import csv

from PySide6.QtWidgets import *
from PySide6.QtGui import QIcon, QFont, QFontDatabase, QPixmap
from PySide6.QtCore import Qt


class GuestApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Epstein Hillel School | Guest Log')
        self.setWindowIcon(QIcon('resources/EHS_star.svg'))
        self.resize(500, 500)
        layout = QGridLayout()
        self.setLayout(layout)
        self.showFullScreen()
        self.data = {}
        self.win_w = 1440
        self.win_h = 2560
        self.guests = []
        self.guest_ids = []
        self.hideui = True
        self.counter = 0


        #Importing fonts
        font = QFontDatabase.addApplicationFont("resources/AvenirLTStd-Roman.otf")
        if font < 0: print("Error")
        families = QFontDatabase.applicationFontFamilies(font)

        layout_title = QVBoxLayout()

        label = QLabel("WELCOME TO", self)
        label.setObjectName("Welcome")
        label.setFont(QFont(families[0]))
        label.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        
        logo_img = QPixmap("Resources/EHS-Logo.png")
        #logo_img = logo_img.scaled(800, 800, Qt.KeepAspectRatio)
        logo = QLabel("Logo", self)
        logo.setObjectName("Logo")
        logo.setPixmap(logo_img)
        logo.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        self.announce = QLabel("", self)
        self.announce.setObjectName("Announce")
        self.announce.setAlignment(Qt.AlignCenter)

        self.entry = QLineEdit("")
        self.entry.setObjectName("Entry")
        self.entry.setFocus()
        self.entry.setAlignment(Qt.AlignCenter)
        self.entry.setEchoMode(QLineEdit.Password)
        self.entry.returnPressed.connect(self.makeEntry)

        self.guest_log = QLabel("", self)
        self.guest_log.setObjectName("Guest")
        self.guest_log.setAlignment(Qt.AlignCenter)
        self.guest_log.setMargin(30)
        self.guest_log.setWordWrap(True)

        logo_wave = QPixmap("Resources/EHS-wave.png")
        #logo_wave = logo_wave.scaled(self.win_w, 1000, Qt.KeepAspectRatio)
        deco = QLabel("Wave", self)
        deco.setObjectName("Wave")
        deco.setPixmap(logo_wave)
        deco.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        deco.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)

        layout_title.addWidget(label)
        layout_title.addWidget(logo)
        layout_title.addWidget(self.announce)
        layout.addLayout(layout_title, 0, 0)
        layout.addWidget(self.guest_log, 1, 0)
        layout.addWidget(deco, 2, 0)
        layout.addWidget(self.entry, 3, 0)


        self.widget = QWidget()
        self.widget.setLayout(layout)
        self.setCentralWidget(self.widget)

    def announcer(self, text):
        self.announce.setText(text)

    def update_guestlist(self):
        self.guests = []
        for guest in self.guest_ids:
            self.guests.append(self.data[guest])
        # TODO Fix the functionality with the join
        guest_list = '\n'.join(sorted(self.guests))
        self.guest_log.setText(guest_list)

    def update_guest(self):
        self.guests = [self.data[x] for x in self.guest_ids]
        guest_list = '\n'.join(sorted(self.guests))
        self.guest_log.setText(str(guest_list))

    def clearEntry(self):
        self.entry.setText("")

    def makeEntry(self):
        scanned_id = str(self.entry.text())
        if scanned_id in self.data:
            name = self.data[scanned_id]
            if scanned_id in self.guest_ids:
                self.guest_ids.remove(scanned_id)
                self.announcer(f"Goodbye, {name}")
                self.update_guest()
                self.clearEntry()
            else:
                self.guest_ids.append(scanned_id)
                self.announcer(f"Welcome, {name}")
                self.update_guest()
                self.clearEntry()
        else:
            self.announcer("Unknown Identification")
            self.clearEntry()

    def clearGuests(self):
        self.guests = []
        self.guest_ids = []
        self.update_guest()


    def open(self):
        file = QFileDialog.getOpenFileName(self, "Select Reference File", "", "CSV Files (*.csv)")
        if file:
            self.counter = 0
            import_file = csv.reader(open(str(file[0]), 'r'))
            for id, name in import_file:
                self.data[id] = name
                self.counter += 1
            del self.data["RFID"]
    
    # Window Key Bindings
    def keyPressEvent(self, event):
        # Closing App
        if event.key() == Qt.Key.Key_Escape:
            self.close()
        # Opening File
        if event.key() == Qt.Key.Key_F10:
            self.open()
            self.announcer(f"~ {self.counter} IDs Loaded ~")
        # Entry Field
        if event.key() == Qt.Key.Key_F9:
            if self.hideui:
                self.entry.setEchoMode(QLineEdit.Normal)
                self.hideui = False
            else:
                self.entry.setEchoMode(QLineEdit.Password)
                self.hideui = True
        # Clear Entries
        if event.key() == Qt.Key.Key_F8:
            self.clearGuests()
            self.announcer("~ Guests Cleared ~")
        # Fullscreen
        if event.key() == Qt.Key.Key_F11:
            if self.isFullScreen():
                self.showNormal()
            else:
                self.showFullScreen()


app = QApplication(sys.argv)
app.setStyleSheet('''
        QPushButton {
            font-size: 20px;
        }

        QLabel#Welcome{
            font-size: 60px;
            color: #00709E;
            margin: 0;
            border: 0px solid red;
            max-height: 100px;
            padding-top: 25px;
        }
        
        QLabel#Logo{
            font-size: 60px;
            color: #00709E;
            margin: 0;
            border: 0px solid blue;
            max-height: 300px;
        }
        
        QLabel#Announce{
            font-size: 60px;
            color: #00709E;
            margin: 0;
            border: 0px solid lime;
            max-height: 200px;
            text-align: center;
        }
        
        QLineEdit#Entry{
            font-size: 20px;
            color: #00709E;
            margin: 0;
            border: 0px solid orange;
            padding-bottom: 10 px;
        }
        
        QLabel#Guest{
            font-size: 40px;
            color: #00709E;
            margin: 0;
            max-height: 1500px;
            min-height: 1500px;
            border: 0px solid purple;
            text-align: center;
            white-space: pre;
        }
        
        QLabel#Wave{
            border: 0px solid green;
            padding-bottom: 30px;
            max-height: 400px;

        }

    ''')


window = GuestApp()
window.show()

sys.exit(app.exec())
