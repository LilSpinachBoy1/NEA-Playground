"""
CREATE THE MAIN WINDOW FOR THE PYQT APPLICATION
"""

# Imports from PyQT
from PyQt5.QtWidgets import QMainWindow, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import QSize

# Subclass for customising main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fun Fact Generator!")
        self.setFixedSize(QSize(400, 300))


# Subclass for the username input screen
class LoginPage(QWidget):
    def __init__(self):
        super().__init__()

        # Create a line edit for username input
        self.username_label = QLabel("Enter your username:", self)
        self.username_input = QLineEdit(self)
        self.inp_layout = QHBoxLayout()
        self.inp_layout.addWidget(self.username_label)
        self.inp_layout.addWidget(self.username_input)
        
        # Create the button to submit
        self.submit_button = QPushButton("Submit", self)

        # Create the main layout
        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(self.inp_layout)
        self.main_layout.addWidget(self.submit_button)

        # Set the main layout for the widget
        self.setLayout(self.main_layout)

# Subclass to display once the user has logged in
class UserNamePage(QWidget):
    def __init__(self, username):
        super().__init__()

        # Create a label to display the username
        self.username_label = QLabel(f"Welcome, {username}!", self)

        # Create the main layout
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.username_label)

        # Set the main layout for the widget
        self.setLayout(self.main_layout)

    def update_username(self, new_username):
        self.username_label.setText(f"Welcome, {new_username}!")