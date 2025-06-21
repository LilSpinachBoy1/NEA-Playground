from PyQt5.QtWidgets import QApplication, QPushButton, QLabel
from window_subclasses import MainWindow, LoginPage, UserNamePage
import sys

# Create a static class to hold the username
class UserDetails:
    username = ""

# Create the app
app = QApplication(sys.argv)

# Create main window
window = MainWindow()

# Instantiate pages
login = LoginPage()
user_page = UserNamePage(UserDetails.username)
window.setCentralWidget(login)  # Set the login page as the central widget
window.show()  # Show the main window

def login_widget_change():
    UserDetails.username = login.username_input.text()  # Get the username from the input field
    user_page.update_username(UserDetails.username)  # Update the username in the user page
    window.setCentralWidget(user_page)  # Change the central widget to the new widget

# Connect the submit button to the login_widget_change function
login.submit_button.clicked.connect(login_widget_change)

app.exec()  # Event loop