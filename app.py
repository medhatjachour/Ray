import sys
import os
import time 
from datetime import datetime, timedelta
from functools import partial

os.environ["QT_GSTREAMER_PLAYBIN_FLAGS"] = str(0x00000017)

from PySide6.QtWidgets import QApplication, QMainWindow,QFileDialog , QGraphicsScene, QGraphicsView, QGraphicsSceneHoverEvent, QSlider, QCompleter, QGraphicsTextItem
from PySide6.QtCore import Qt, QThreadPool, QSize, Slot,QUrl,QPoint,QTimer,QEvent
from PySide6.QtGui import QMouseEvent, QCursor,QIcon,QFont, QColor
from PySide6.QtMultimedia import (QAudioOutput,
                            QMediaPlayer)
from PySide6.QtMultimediaWidgets import QGraphicsVideoItem

from widgets.worker.Worker import Worker
from widgets.PySubBtn.PySubBtn import PySubBtn
from widgets.toggleBtn.py_toggle import PyToggle

from ui.ui_main import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) 
        self.threadpool = QThreadPool()

 
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.toggle_full_screen()
        self.ui.close_btn.clicked.connect(self.close_fun)
        self.ui.max_btn.clicked.connect(self.toggle_full_screen)
        self.ui.min_btn.clicked.connect(self.showMinimized)
        self.ui.top_bar.mouseMoveEvent = self.move_window1
        self.ui.verticalLayout.removeWidget(self.ui.top_bar)
        self.ui.verticalLayout_8.setContentsMargins(-1, 50, -1, 30)
        self.Hovered = False
        

        #/////////// media player 
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)
        # test graphics

        self.view =   QGraphicsView(self)
        self._scene =  QGraphicsScene(self.view )
        self.view.setScene(self._scene) 
        self._videoitem = QGraphicsVideoItem()
        self.ui.gridLayout_8.addWidget(self.view)

        # Set up window resizing
        self.view.resizeEvent = self.handleResize
        # 
        self._playlist = []  # FIXME 6.3: Replace by QMediaPlaylist?
        self._playlist_index = -1
        self.subtitles_text = []
        # Set up timer to display subtitles
        self.sub_timer = QTimer()
        self.sub_timer.timeout.connect(self.display_subtitle)

        self.subHolder = QGraphicsTextItem('')
        font = QFont("Proxima Nova", 24) 
        self.subHolder.setFont(font)
        self.subHolder.setDefaultTextColor(QColor(Qt.white))
        self.ui.choseSub.clicked.connect(self.choose_subtitle)   
        self.subWindowShown = False 
        self.subtitles = "/" # it's for local subtitle 
        self.subtitle_content = None # the content of the subtitle
        self.available_subs =[
                "English", "Mandarin Chinese", "Hindi", "Spanish", "French",
                "Modern Standard Arabic", "Bengali", "Russian", "Portuguese",
                "Urdu", "Indonesian", "German", "Japanese", "Swahili",
                "Marathi", "Telugu", "Turkish", "Tamil", "Vietnamese",
                "Italian", "Korean", "Punjabi", "Polish", "Dutch",
                "Thai", "Greek", "Persian (Farsi)", "Gujarati", "Romanian",
                "Ukrainian", "Uzbek", "Sindhi", "Amharic", "Oromo",
                "Kurdish", "Serbo-Croatian",
                "Malagasy", "Nepali", "Sinhalese (Sinhala)", 
                "Khmer (Cambodian)", "Somali"
            ]
        self.show_available_subs()
        self.ui.playSub.clicked.connect(self.view_local_sub_window)
        self.localSubWindowShown = False 
        self.ui.search_sub.returnPressed.connect(self.filter_sub)
        self.isSub = False 
        # return self.subtitles_text
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
        self.fileName = "/" #it holds the video path 
        self.ui.drag_frame.setAcceptDrops(True)
        self.ui.browse_file.clicked.connect(self.showDialog)
        # ,media player 
        self.ui.stop_play.clicked.connect(self.play_pause)
        # position
        self.ui.position_control.sliderMoved.connect(self.set_position)
        self.ui.position_control.setTickInterval(100)
        self.ui.position_control.setTickPosition(QSlider.TicksBelow)
        self.ui.position_control.setToolTip("Position")
        self.player.positionChanged.connect(self.change_position)
        self.player.durationChanged.connect(self.duration_position)
        self.ui.forward.clicked.connect(self.forward_Ten)
        self.ui.backward.clicked.connect(self.backward_Ten)
        # timer = QTimer()
        # # timer.timeout.connect(self.display_subtitle())
        # timer.start(100)  # Check every 100 ms
        # sound
        self.isMuted = False
        self.audio_value = self.audio_output.volume()*100
        self.ui.sound_control.setValue(self.audio_output.volume()*100)
        self.ui.sound_control.setTickInterval(10)
        self.ui.sound_control.setTickPosition(QSlider.TicksBelow)
        self.ui.sound_control.setToolTip("Volume")
        self.ui.sound_control.valueChanged.connect(self.adjust_audio_volume)
        self.ui.mute.clicked.connect(self.mute_fun)

        self.setAttribute(Qt.WidgetAttribute.WA_Hover) 
        self.setMouseTracking(True)  # Enable mouse tracking
        
        self.hoverTimer = QTimer(self)
        self.hoverTimer.setInterval(5000)  # Set timer for 5 seconds
        self.hoverTimer.setSingleShot(True)  # Timer is not reoccurring
        self.hoverTimer.timeout.connect(self.hoverStopped)
        # preference settings
        self.ui.preferences.clicked.connect(self.handle_preference)
        self.pref_shown = False
        #add toggle dark mode 
        self.dark_mode = PyToggle()
        self.ui.horizontalLayout_22.addWidget(self.dark_mode)
    # /////////////////////////////////////////   top bar functions     

    def toggle_controls_bar_visibility(self):
        if self.Hovered:
            self.ui.top_bar.show()
            self.ui.frame_32.show()
            self.ui.frame_32.raise_()
            self.ui.top_bar.raise_()
        else:
            self.ui.top_bar.hide()
            self.ui.frame_32.hide()


    def event(self, event):
        if event.type() == QEvent.HoverMove:
            print("Hover")
            self.hoverTimer.start()  # Restart the timer on every hover move
            self.Hovered = True
            self.toggle_controls_bar_visibility()
        return super().event(event)

    def hoverStopped(self):
        self.Hovered = False
        self.toggle_controls_bar_visibility()
        print("Hover stopped for 5 seconds")

    def showMinimized(self) -> None:
        return super().showMinimized()
    def toggle_full_screen(self):
        is_full = bool(self.windowState() == Qt.WindowFullScreen)
        if is_full:
            self.showNormal()
        else:
            self.showFullScreen()
    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()
    def move_window1(self, event):
        self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
        self.dragPos = event.globalPosition().toPoint()
        event.accept()
    def keyPressEvent(self, event):
        """
        Forward keyPressEvents to plot as long as they are not used in MainApp.
        """
        if event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_Tab:
            # self.ui.stackedWidget_2.setCurrentIndex(self.currentWidgetIndex)
            match self.currentWidgetIndex :
                case  0:
                    self.currentWidgetIndex += 1
                    self.set_status()
                case  1:
                    self.currentWidgetIndex += 1
                    self.set_home()
                case  2:
                    self.currentWidgetIndex += 1
                    self.set_store()
                case  3:
                    self.currentWidgetIndex += 1
                    self.set_sales()
                case  4:
                    self.currentWidgetIndex = 0
                    self.set_settings()
                    # break
    def handleResize(self, event):
        # Update video item size
        self._videoitem.setSize(self.view.size())
        self.floating_video_control()
    def close_fun(self):

        self.close()


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
        if len(self.fileName[0])> 10:
            
            worker = Worker(
                partial(
                    self.media_init,
                )
            )
            worker.signals.result.connect(partial(self.resultFunctionMedia_int))
            self.threadpool.start(worker)
            self.ui.movie_name.setText(os.path.basename(self.fileName[0]))
    @Slot()
    def view_local_sub_window(self):
        if not self.localSubWindowShown:
            self.ui.gridLayout_6.removeWidget(self.ui.localsub)
            width = self.ui.frame_32.width()

            R = QPoint(width, 0) - QPoint(680,-700)
            # print(f"{R} is r")
            self.ui.localsub.setMinimumWidth(216)
            self.ui.localsub.setMinimumHeight(200)
            self.ui.localsub.move(R)
            self.ui.localsub.raise_()
            self.ui.localsub.show()
            self.localSubWindowShown = True
        else:
            self.localSubWindowShown = False
            self.ui.localsub.setMinimumWidth(0)
            self.ui.localsub.setMinimumHeight(0)
            self.ui.localsub.hide()
    def toggle_sub(self):
        if self.isSub:
            
            icon_sub = QIcon()
            icon_sub.addFile(u":/icons/assets/icons/equal-CC.png", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.playSub.setIcon(icon_sub)
            self.ui.playSub.setIconSize(QSize(21, 21))
            self.isSub = not self.isSub
            self.ui.playSub.setText("ON")
        else:
            icon_sub = QIcon()
            icon_sub.addFile(u":/icons/assets/icons/equal-CC-off.png", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.playSub.setIcon(icon_sub)
            self.ui.playSub.setIconSize(QSize(21, 21))
            self.ui.playSub.setText("OFF")
            self.isSub = not self.isSub
             
    def get_local_subtitle(self):
        # Create a QTimer to track video playback time
        self.subName = QFileDialog.getOpenFileName(self, "Chose the subtitle", f"{self.fileName[0]}","Subtitle Files (*.srt *.sbv *.vtt )")
        print(self.subName[0])
        # worker = Worker(
        #     partial(
        #         self.parse_srt,
        #     )
        # )
        # worker.signals.result.connect(partial(self.resultSub_tile))
        # self.threadpool.start(worker)
        self.parse_srt() 
  
    def parse_srt(self):
        with open(self.subName[0], 'r', encoding='utf-8') as file:
            content = file.read()
            entries = content.split('\n\n')
            for entry in entries:
                if entry.strip():
                    parts = entry.split('\n')
                    times = parts[1].split(' --> ')
                    start_time =self.convert_to_ms(times[0])
                    end_time = self.convert_to_ms(times[1])
                    text = ' '.join(parts[2:])
                    self.subtitles_text.append((start_time, end_time, text))
        self.isSub = True
        self._scene.addItem(self.subHolder)
  
        self.subHolder.setPos((self.width()-self.subHolder.boundingRect().width() )/2, self.height() - 300)
        self.sub_timer.start(100)  # Check every 100 ms

    @Slot()
    def choose_subtitle(self):
        if not self.subWindowShown:
            self.ui.gridLayout_6.removeWidget(self.ui.sub_floating)
            width = self.ui.frame_32.width()
            # height = self.ui.frame_32.height()
            print(self.ui.choseSub.pos())
            print(self.ui.frame_32.pos())
            print(self.height()-self.ui.sub_floating.height())
            R = QPoint(width, 0) - QPoint(800,-525)
            # print(f"{R} is r")
            self.ui.sub_floating.setMinimumWidth(216)
            self.ui.sub_floating.setMinimumHeight(400)
            self.ui.sub_floating.move(R)
            self.ui.sub_floating.raise_()
            self.ui.sub_floating.show()
            self.subWindowShown = True
        else:
            self.subWindowShown = False
            self.ui.sub_floating.setMinimumWidth(0)
            self.ui.sub_floating.setMinimumHeight(0)
            self.ui.sub_floating.hide()

    def show_available_subs(self):
        for i in self.available_subs:
            self.PySubBtn_ = PySubBtn(i)
            self.ui.verticalLayout_13.addWidget(self.PySubBtn_)

    def filter_sub(self):
        print("Filter Sub")
    

    # Function to convert SRT time format to milliseconds
    def convert_to_ms(self, srt_time):
        h, m, s_ms = srt_time.split(':')
        s, ms = s_ms.split(',')
        return int(h) * 3600000 + int(m) * 60000 + int(s) * 1000 + int(ms)

    # Function to display the current subtitle based on the video time
    def display_subtitle(self):
        if self.isSub == True:
            if self.player.playbackState() == QMediaPlayer.PlayingState and len(self.subtitles_text) > 1:#TODO: this needs more accurate condtions 
                current_time = self.player.position()
                for start_time, end_time, text in self.subtitles_text:
                    if start_time <= current_time <= end_time:
                        # Display subtitle text
                        self._scene.removeItem(self.subHolder)
                        self.subHolder.setPlainText(text)
                        self.subHolder.setHtml(f"<div style='background: rgba(0, 0, 0, 0.4);color:white'>{text}</div>")

                        self._scene.addItem(self.subHolder)
                        self.subHolder.setPos((self.width()-self.subHolder.boundingRect().width() )/2, self.height() - 300)
                        break
        else:
            self.subHolder.setPlainText(" ")
    @Slot()
    def topBarFloating(self):
        self.ui.verticalLayout.removeWidget(self.ui.top_bar)
        self.ui.top_bar.hide()
    @Slot()
    def floating_video_control(self):
        # self.ui.frame_23.hide()
        self.ui.frame_32.raise_()
        self.ui.gridLayout_6.removeWidget(self.ui.frame_32)
        self.ui.frame_32.setMinimumWidth(self.width())
        self.ui.frame_32.setMinimumHeight(100)
        self.ui.frame_32.raise_()
        R = QPoint(0, self.height())- QPoint(0, self.ui.frame_32.height() + 85)
        self.ui.frame_32.move(R)
        self._videoitem.setSize(self.ui.frame_23.size())
    def media_init(self,progress_callback):
        self.player.setSource(QUrl(self.fileName[0]))
        self.player.play()
        self._scene.addItem(self._videoitem)
        self.view.fitInView(self._scene.sceneRect())
        # self.view.fitInView(self._scene.sceneRect(), Qt.KeepAspectRatio)
        # self.view.fitInView(self._videoitem)
        self._videoitem.setSize(self.ui.frame_23.size())
        # print(f'_scene  {self._scene.size()}')
        print(f'view  == {self.view.size()}')
        print(f'video_player == {self._videoitem.size()}')
    def resultFunctionMedia_int(self,result):
        print(result)
        self.ui.stackedWidget.setCurrentIndex(3)
        self.player.setVideoOutput(self._videoitem)
        subtitle_tracks = self.player.subtitleTracks()
        print(f'the subtitles tracked are { subtitle_tracks}')
        if subtitle_tracks:
            self.player.setSubtitleTrack(subtitle_tracks[0])

    @Slot()
    def _ensure_stopped(self):
        if self.player.playbackState() != QMediaPlayer.StoppedState:
            self.player.stop()
    @Slot()
    def play_pause(self):
        if self.player.playbackState() == QMediaPlayer.PlayingState:
            icon_play = QIcon()
            icon_play.addFile(u":/icons/assets/icons/play_.png", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.stop_play.setIcon(icon_play)
            # self.ui.stop_play.setIconSize(QSize(21, 21))
            self.player.pause()
        else:
            icon4_pause = QIcon()
            icon4_pause.addFile(u":/icons/assets/icons/equal-pause.png", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.stop_play.setIcon(icon4_pause)
            # self.ui.stop_play.setIconSize(QSize(21, 21))
            self.player.play()
    @Slot()
    def set_position(self,position):
        self.player.setPosition(position)
    @Slot()
    def change_position(self,position):
        played = time.strftime('%H:%M:%S', time.gmtime(position / 1000))
        duration = time.strftime('%H:%M:%S', time.gmtime(self.player.duration() / 1000))
        self.ui.time.setText(f'{played} / {duration}')
        self.ui.position_control.setValue(position)
    @Slot()
    def duration_position(self,d):
        self.ui.position_control.setRange(0,d)
    @Slot()
    def forward_Ten(self):
        current_position  = self.player.position() 
        # To skip forward by 10 seconds
        self.player.setPosition(current_position + 10000)
        self.ui.position_control.setValue((current_position+10000) // 1000)
    @Slot()
    def backward_Ten(self):
        current_position  = self.player.position() 
        # To skip forward by 10 seconds
        self.player.setPosition(current_position - 10000)
        self.ui.position_control.setValue((current_position-10000) // 1000)
    @Slot()
    def adjust_audio_volume(self,volume):
        self.audio_output.setVolume(volume/100)
        self.audio_value = volume/100
        if self.isMuted:
            print(self.audio_value)
            icon_sound = QIcon()
            icon_sound.addFile(u":/icons/assets/icons/volume-max.png", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.mute.setIcon(icon_sound)
    @Slot()
    def mute_fun(self):
        if self.isMuted:
            print(self.audio_value)
            self.isMuted = not self.isMuted
            self.audio_output.setVolume(self.audio_value)
            icon_sound = QIcon()
            icon_sound.addFile(u":/icons/assets/icons/volume-max.png", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.mute.setIcon(icon_sound)
        else:
            self.isMuted = not self.isMuted
            self.audio_output.setVolume(0)
            icon_mute = QIcon()
            icon_mute.addFile(u":/icons/assets/icons/Mute.png", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.mute.setIcon(icon_mute)

    # preferences
    @Slot()
    def handle_preference(self): 
        if not self.pref_shown:
            self.ui.verticalLayout.removeWidget(self.ui.preferences_frame)
            print(self.ui.preferences_frame.pos())
            R = QPoint(0, 0)+  QPoint(15, 50)
            # print(f"{R} is r")
            self.ui.preferences_frame.setMinimumWidth(265)
            self.ui.preferences_frame.setMinimumHeight(260)
            self.ui.preferences_frame.move(R)
            self.ui.preferences_frame.raise_()
            self.ui.preferences_frame.show()
            self.pref_shown = True
        else:
            self.pref_shown = False
            self.ui.preferences_frame.setMinimumWidth(0)
            self.ui.preferences_frame.setMinimumHeight(0)
            self.ui.preferences_frame.hide()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
