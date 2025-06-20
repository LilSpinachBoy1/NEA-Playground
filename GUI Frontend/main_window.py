"""
CREATE THE MAIN WINDOW FOR THE PYQT APPLICATION
"""

# Imports from PyQT
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QWidget
from PyQt5.QtCore import QSize

# Subclass for customising main window
class FactWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fun Fact Generator!")
        self.setFixedSize(QSize(400, 300))

        # Create widgets
        

