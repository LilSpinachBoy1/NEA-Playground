from PyQt5.QtWidgets import QApplication, QPushButton, QLabel
from window_subclasses import MainWindow, InputWidget1Field
import sys

# Create the app
app = QApplication(sys.argv)

# Create main window
window = MainWindow()

# Procedure to change the current acive widget
def change_widget(widget):
    window.setCentralWidget(widget)

# Fill main window
button = QPushButton("Change le window!")
confirm_text = QLabel("You clicked the button!")
button.clicked.connect(lambda: change_widget(confirm_text))
window.setCentralWidget(button)
window.show()

app.exec()  # Event loop