import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QTextEdit, QVBoxLayout
from PyQt6 import uic


class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()

        # Load the UI file
        uic.loadUi('GuestLog.ui', self)

        # Define the widgets
        self.button = self.findChild(QPushButton, "pushButton")
        self.input = self.findChild(QLineEdit, "lineEdit")
        self.output = self.findChild(QTextEdit, "textEdit")


        self.setWindowTitle('Epstein Hillel Guest Log')
    #     self.button.clicked.connect(self.sayHello())
    #
    # def sayHello(self):
    #     inputText = self.input.text()
    #     self.output.setText(f'Hello {inputText}')


app = QApplication(sys.argv)
app.setStyleSheet('''
        QWidget {
            font-size: 25px;
        }

        QPushButton {
            font-size: 20px;
        }

    ''')
myApp = MyApp()
myApp.show()

app.exec()
