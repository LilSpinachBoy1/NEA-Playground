from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QWidget
import requests
import sys

# Subclass for customising main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Super Cool Revision App")
        self.setFixedSize(QSize(400, 300))

        # Create a horisontal layout of widgets
        lay = QHBoxLayout()
        butt = QPushButton("I love you Reese")
        lay.addWidget(butt)
        lay.addWidget(QPushButton("im here too"))

        # butt.setCheckable(True) would set the button to be checkable
        # butt.clicked.connect(self.toggled) would then create a slot
        butt.clicked.connect(self.you_love_reese)  # Asign a slot to send the clicked signal to

        # Create inner widget to apply layout to (this has to be done as .setLayout does not work on MainWindow)
        widge = QWidget()
        widge.setLayout(lay)
        self.setCentralWidget(widge)

    def you_love_reese(self):
        rq_url = "http://localhost:8000/api/test_db"
        try:
            response = requests.get(rq_url, timeout=0.5)
            print(response.json())
        except:
            print("ERR: Unable to connect to API")


# Create the app
app = QApplication(sys.argv)

# Create main window
window = MainWindow()
window.show()

# Event loop
app.exec()