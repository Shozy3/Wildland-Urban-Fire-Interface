import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # set window title and size
        self.setWindowTitle("Google Maps in PyQt5")
        self.setGeometry(100, 100, 800, 600)

        # create a QWebEngineView widget to display the map
        self.map_box = QGroupBox("Map")
        self.browser = QWebEngineView()
        map_layout = QVBoxLayout()
        map_layout.addWidget(self.browser)
        self.map_box.setLayout(map_layout)
        self.map_box.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.map_box.setStyleSheet("QGroupBox { padding: 10px; }")

        # load the map using the Google Maps Embed API
        map_url = "https://www.google.com/maps/embed/v1/place?key=YOUR_API_KEY&q=Edmonton"
        self.browser.setHtml(f"<iframe id='map_iframe' frameborder='0' style='border:0' src='{map_url}' allowfullscreen></iframe>")
        self.map_box.resizeEvent = self.on_map_box_resized  # connect resizeEvent to slot

        # create a group box for the other elements
        self.other_box = QGroupBox("Other Elements")
        other_layout = QVBoxLayout()

        # create a button
        self.button = QPushButton("Click me")
        other_layout.addWidget(self.button)

        # create a dropdown menu
        self.dropdown = QComboBox()
        self.dropdown.addItems(["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"])
        other_layout.addWidget(self.dropdown)

        # create a calendar widget
        self.calendar = QCalendarWidget()
        self.calendar.setSelectedDate(QDate.currentDate())
        other_layout.addWidget(self.calendar)

        self.other_box.setLayout(other_layout)

        # create a main widget and add the map and other elements to it
        main_widget = QWidget(self)
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.map_box)
        main_layout.addWidget(self.other_box)
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    def on_map_box_resized(self, event):
        # get the new size of the map box
        width = event.size().width()
        height = event.size().height()

        # update the width and height of the iframe tag
        self.browser.page().runJavaScript(f"document.getElementById('map_iframe').width='{width}px';")
        self.browser.page().runJavaScript(f"document.getElementById('map_iframe').height='{height}px';")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
