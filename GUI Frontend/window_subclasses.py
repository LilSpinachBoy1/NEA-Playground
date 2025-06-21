"""
CREATE THE MAIN WINDOW FOR THE PYQT APPLICATION
"""

# Imports from PyQT
from PyQt5.QtWidgets import QMainWindow, QWidget, QLineEdit
from PyQt5.QtCore import QSize

# Subclass for customising main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fun Fact Generator!")


# Subclass for an input widget
class InputWidget1Field(QWidget):
    def __init__(self):
        super().__init__()
        id_input = QLineEdit(parent=self)
