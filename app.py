import sys
from datetime import datetime, timedelta
from functools import partial

from PySide6.QtWidgets import QApplication, QMainWindow,QFileDialog , QLabel, QLineEdit, QSpacerItem, QSizePolicy, QCompleter, QPushButton
from PySide6.QtCore import Qt, QThreadPool, QRegularExpression,QSize
from PySide6.QtGui import QRegularExpressionValidator, QCursor,QIcon
from ui.ui_main import Ui_MainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # init always the main window to the welcome page
        self.ui.stackedWidget.setCurrentIndex(0)
        # get started function 
        self.ui.get_started.clicked.connect(self.get_started_Fun)
        # sign up and login function
        self.ui.logIn_btn.clicked.connect(self.log_in_fun)
        # drag and drop files 
        # get the drag and drop frame to accept drag and drop behavior
        self.fileName = None #it holds the video path 
        self.ui.drag_frame.setAcceptDrops(True)
        self.ui.browse_file.clicked.connect(self.showDialog)
    def get_started_Fun(self):
        self.ui.stackedWidget.setCurrentIndex(1)
    def log_in_fun(self):
        self.ui.stackedWidget.setCurrentIndex(2)
    # drag and drop events
    def dragEnterEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()
    def dragMoveEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()
    def dropEvent(self, event):
        if event.mimeData().hasImage:
            event.setDropAction(Qt.CopyAction)
            file_path = event.mimeData().urls()[0].toLocalFile()
            print(file_path)

            event.accept()
        else:
            event.ignore()
    def showDialog(self):
        self.fileName = QFileDialog.getOpenFileName(self, "Open Image", "/","Image Files (*.mp4 *.avi *.mov *.mkv)")
        print(self.fileName[0])
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
