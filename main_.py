import sys
from PyQt6.QtWidgets import *
import window

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = window.GuestLog()
    window.show()
    sys.exit(app.exec())