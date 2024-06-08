import sys
from datetime import datetime, timedelta
from functools import partial

from PySide6.QtWidgets import QApplication, QMainWindow,QFileDialog , QGraphicsScene, QGraphicsView, QSpacerItem, QSlider, QCompleter, QPushButton
from PySide6.QtCore import Qt, QThreadPool, QSize, Slot,QUrl,QPoint,QSizeF
from PySide6.QtGui import QRegularExpressionValidator, QCursor,QIcon
from PySide6.QtMultimedia import (QAudioOutput,
                            QMediaPlayer)
from PySide6.QtMultimediaWidgets import QVideoWidget,QGraphicsVideoItem


from ui.ui_main import Ui_MainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #/////////// media player 

        self.player = QMediaPlayer()
        

        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)
        # test graphics

        # self._scene =  QGraphicsScene(self)
        # self._gv =   QGraphicsView(self._scene)
        # self._videoitem = QGraphicsVideoItem()
        # self.ui.gridLayout_7.addWidget(self._gv)
        # self._scene.addItem(self._videoitem)
        # self._gv.fitInView(self._videoitem)



        self.view =   QGraphicsView(self.ui.frame_41)
        self._scene =  QGraphicsScene(self.view )
        self.view.setScene(self._scene) 
        self._videoitem = QGraphicsVideoItem()
        self.ui.verticalLayout_13.addWidget(self.view)
        self._scene.addItem(self._videoitem)
        self.view.fitInView(self._scene.sceneRect(), Qt.KeepAspectRatio)
        # self.view.fitInView(self._videoitem)
        self._videoitem.setSize(self.ui.frame_23.size())
        # print(f'_scene  {self._scene.size()}')
        print(f'view  == {self.view.size()}')
        print(f'video_player == {self._videoitem.size()}')
        print(f'frame_41 == {self.ui.frame_41.size()}')
  




        self.player.setVideoOutput(self._videoitem)
        # init always the main window to the welcome page
        self.ui.stackedWidget.setCurrentIndex(0)
        # get started function 
        self.ui.get_started.clicked.connect(self.get_started_Fun)
        # sign up and login function
        self.ui.signUp_tab.clicked.connect(self.open_singUp)
        self.ui.logIn_tab.clicked.connect(self.open_logIn)
        self.ui.logIn_btn.clicked.connect(self.log_in_fun)
        # drag and drop files 
        # get the drag and drop frame to accept drag and drop behavior
        self.fileName = None #it holds the video path 
        self.ui.drag_frame.setAcceptDrops(True)
        self.ui.browse_file.clicked.connect(self.showDialog)
        # ,media player 
        # self.ui.stop_play.clicked.connect(self.play_pause)
        # # position
        # self.ui.position_control.sliderMoved.connect(self.set_position)
        # self.ui.sound_control.setToolTip("Position")
        # self.player.positionChanged.connect(self.change_position)
        # self.player.durationChanged.connect(self.duration_position)
        # # sound
        # self.ui.sound_control.setValue(self.audio_output.volume()*100)
        # self.ui.sound_control.setTickInterval(10)
        # self.ui.sound_control.setTickPosition(QSlider.TicksBelow)
        # self.ui.sound_control.setToolTip("Volume")
        # self.ui.sound_control.valueChanged.connect(self.adjust_audio_volume)
        # # choose subtitle 
        # self.ui.gridLayout_13.removeWidget(self.ui.sub_floating)
        # self.ui.sub_floating.hide()
        # self.ui.choseSub.clicked.connect(self.choose_subtitle)    
    def get_started_Fun(self):
        self.ui.stackedWidget.setCurrentIndex(1)
    def open_singUp(self):
        self.ui.stackedWidget_2.setCurrentIndex(1)
    def open_logIn(self):
        self.ui.stackedWidget_2.setCurrentIndex(0)
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
        self.fileName = QFileDialog.getOpenFileName(self, "Chose the movie", "/","Image Files (*.mp4 *.avi *.mov *.mkv)")
        self.ui.stackedWidget.setCurrentIndex(3)
        print(self.fileName[0])
        self.player.setSource(QUrl(self.fileName[0]))
        # self.player.setVideoOutput(self.videoWidget)
        # self.videoWidget.show()
        self.player.play()
        # self.floating_video_control()
    @Slot()
    def floating_video_control(self):
        # self.ui.frame_23.hide()
        self.ui.frame_32.raise_()
        self.ui.gridLayout_8.removeWidget(self.ui.frame_32)
        self.ui.frame_32.setMinimumWidth(self.width())
        self.ui.frame_32.setMinimumHeight(100)
        self.ui.frame_32.raise_()
        R = QPoint(0, self.height())- QPoint(0, self.ui.frame_32.height() + 85)
        self.ui.frame_32.move(R)
    @Slot()
    def _ensure_stopped(self):
        if self.player.playbackState() != QMediaPlayer.StoppedState:
            self.player.stop()
    @Slot()
    def play_pause(self):
        if self.player.playbackState() == QMediaPlayer.PlayingState:
            self.player.pause()
            icon = QIcon()
            icon.addFile(u"../assets/icons/equal-pause.png", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.stop_play.setIcon(icon)
            self.ui.stop_play.setIconSize(QSize(21, 21))
        else:
            self.player.play()
            icon4 = QIcon()
            icon4.addFile(u":/icons/assets/icons/play.png", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.stop_play.setIcon(icon4)
            self.ui.stop_play.setIconSize(QSize(21, 21))
    @Slot()
    def set_position(self,position):
        self.player.setPosition(position)
    @Slot()
    def change_position(self,position):
        self.ui.position_control.setValue(position)
    @Slot()
    def duration_position(self,d):
        self.ui.position_control.setRange(0,d)
    @Slot()
    def adjust_audio_volume(self,volume):
        self.audio_output.setVolume(volume/100)
    @Slot()
    def choose_subtitle(self):
        width = self.ui.frame_32.width()
        # height = self.ui.frame_32.height()

        R = QPoint(width, 0) - QPoint(600, 350)
        # print(f"{R} is r")
        self.ui.sub_floating.setMinimumWidth(300)
        self.ui.sub_floating.setMinimumHeight(300)
        self.ui.sub_floating.move(R)
        self.ui.sub_floating.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
