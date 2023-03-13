import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QWidget, QCalendarWidget, QComboBox, QGridLayout, QHBoxLayout, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtWebKitWidgets import QWebView

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create the Google Maps box
        map_box = QWebView(self)
        api_key = "YOUR_API_KEY"  # Replace with your own API key
        map_box.setUrl(QUrl(f"https://www.google.com/maps/embed/v1/place?key={api_key}&q=Space+Needle,Seattle+WA"))

        # Create the button
        button = QPushButton("Click me", self)
        button.setToolTip("This is a button")

        # Create the calendar
        calendar = QCalendarWidget(self)

        # Create the drop-down menu
        drop_down = QComboBox(self)
        drop_down.addItem("1")
        drop_down.addItem("2")
        drop_down.addItem("3")
        drop_down.addItem("4")
        drop_down.addItem("5")

        # Create the layout
        hbox = QHBoxLayout()
        hbox.addWidget(QLabel("Drop-down menu:"))
        hbox.addWidget(drop_down)

        vbox = QVBoxLayout()
        vbox.addWidget(map_box)
        vbox.addWidget(button)
        vbox.addWidget(calendar)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 500, 400)
        self.setWindowTitle("My Window")
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())
