import sys
import os
import time 
from datetime import datetime, timedelta
from functools import partial

os.environ["QT_GSTREAMER_PLAYBIN_FLAGS"] = str(0x00000017)

from PySide6.QtWidgets import QApplication, QMainWindow,QFileDialog , QGraphicsScene, QGraphicsView, QGraphicsDropShadowEffect, QSlider, QCompleter, QGraphicsTextItem
from PySide6.QtCore import Qt, QThreadPool, QSize, Slot,QUrl,QPoint,QTimer,QEvent
from PySide6.QtGui import QMouseEvent, QCursor,QIcon,QFont, QColor
from PySide6.QtMultimedia import (QAudioOutput,
                            QMediaPlayer)
from PySide6.QtMultimediaWidgets import QGraphicsVideoItem

from widgets.worker.Worker import Worker
from widgets.PySubBtn.PySubBtn import PySubBtn
from widgets.toggleBtn.py_toggle import PyToggle

from ui.ui_main import Ui_MainWindow
from pages.log import Log
from pages.Drag import Drag
from pages.Controller import Control
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) 
        # remove the old top bar and the frame 
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.toggle_full_screen() #start at full screen
        # init always the main window to the welcome page
        self.ui.stackedWidget.setCurrentIndex(0)
        # threads
        self.threadpool = QThreadPool()

        #/////////// media player 
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)
        
        # pages 
        Log.init(self)
        Drag.init(self,self)
        Control.init(self)

        self.ui.close_btn.clicked.connect(self.close_fun)
        self.ui.max_btn.clicked.connect(self.toggle_full_screen)
        self.ui.min_btn.clicked.connect(self.showMinimized)
        self.ui.top_bar.mouseMoveEvent = self.move_window1
        self.ui.verticalLayout_18.removeWidget(self.ui.top_bar)
        self.Hovered = False
        
        self.ui.verticalLayout_8.setContentsMargins(0, 50, 0, 0) # space for the top bar
        

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
        self.subName = None
        self.sub_timer = QTimer()
        self.sub_timer.timeout.connect(self.display_subtitle)

        self.subHolder = QGraphicsTextItem('')
        self.subHolder.setTextWidth(self.width() - 150)  # Set maximum width to 100
        self.subHolder.setDefaultTextColor(Qt.AlignCenter)  # Align text to center
        font = QFont("Proxima Nova", 20) 
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
        self.ui.button_patiensts.clicked.connect(self.toggle_sub) 
        self.ui.choose_subtitle_file.clicked.connect(self.get_local_subtitle)
        self.localSubWindowShown = False
        self.getLocalSubs = False  
        self.ui.search_sub.returnPressed.connect(self.filter_sub)
        self.isSub = False 
        # return self.subtitles_text
        # get started function 
        self.ui.get_started.clicked.connect(self.get_started_Fun)
        self.ui.p_user.clicked.connect(self.user_fun)
        # drag and drop files 
        # get the drag and drop frame to accept drag and drop behavior
        self.fileName = "/" #it holds the video path 
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
            self.ui.top_bar.setMinimumWidth(self.width())
            self.ui.top_bar.setMaximumWidth(self.width())
            self.ui.top_bar.setMinimumHeight(50)
            self.ui.top_bar.setMaximumHeight(50)
            self.ui.frame_60.setMinimumSize(QSize( 770, 92)) 
            self.ui.frame_60.setMaximumSize(QSize( abs(self.ui.frame_32.width() - 500 ) , 92))
        
        else:
            self.ui.top_bar.hide()
            self.ui.frame_32.hide()
            self.ui.top_bar.setMinimumWidth(0)
            self.ui.top_bar.setMaximumWidth(0)
            self.ui.top_bar.setMinimumHeight(0)
            self.ui.top_bar.setMaximumHeight(0)


    def event(self, event):
        if event.type() == QEvent.HoverMove:
            self.hoverTimer.start()  # Restart the timer on every hover move
            self.Hovered = True
            self.toggle_controls_bar_visibility()
        return super().event(event)

    def hoverStopped(self):
        self.Hovered = False
        self.toggle_controls_bar_visibility()

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
        print(f'event.size(  = = ={event.size()}')
        self._videoitem.setSize(self.view.size())
        self.subHolder.setTextWidth(self.width() - 150)  # Set maximum width to 100
        self.floating_video_control()
    def close_fun(self):

        self.close()


    def get_started_Fun(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def user_fun(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    def showDialog(self):
        self.fileName = QFileDialog.getOpenFileName(self, "Chose media", "/","Media Files (*.mp4 *.avi *.mov *.mkv *.ogv *.webm *.MPEG *.WMV *.FLV .*3GP .*MP3 .*FLAC .*DSD .*AIFF .*ALAC .*AAC )")
        if len(self.fileName[0])> 10:
            self.start_media(self.fileName[0])
    def start_media(self,file_name):
        
        worker = Worker(
            partial(
                self.media_init,file_name
            )
        )
        worker.signals.result.connect(partial(self.resultFunctionMedia_int))
        self.threadpool.start(worker)
        self.ui.movie_name.setText(os.path.basename(file_name))
    @Slot()
    def view_local_sub_window(self):
    
        if not self.localSubWindowShown:
            self.ui.gridLayout_6.removeWidget(self.ui.localsub)
            self.ui.localsub.setMinimumWidth(216)
            self.ui.localsub.setMinimumHeight(200)
            #  get the position related to  the 0, ,0
            # w =self.ui.playSub.mapToGlobal(QPoint(0, 0))
            R = QPoint(self.ui.frame_60.x() + self.ui.frame_52.x()+ 100 , self.ui.frame_32.y() -  self.ui.localsub.height() ) 
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
            self.ui.playSub.setText(" ON")
            self.ui.button_patiensts.setText(" ON")
        else:
            icon_sub = QIcon()
            icon_sub.addFile(u":/icons/assets/icons/equal-CC-off.png", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.playSub.setIcon(icon_sub)
            self.ui.playSub.setIconSize(QSize(21, 21))
            self.ui.playSub.setText(" OFF")
            self.ui.button_patiensts.setText(" OFF")
            self.isSub = not self.isSub

    def auto_local_sub(self):
        #TODO:NEED SOME WORKS
        folder_path = os.path.dirname(self.fileName[0])
        files_in_directory = os.listdir(folder_path)
        # Filter out all files with .srt extension
        srt_files = [os.path.join(folder_path, file) for file in files_in_directory if file.endswith('.srt')]
        sbv_files = [file for file in files_in_directory if file.endswith('.sbv')]
        vtt_files = [file for file in files_in_directory if file.endswith('.vtt')]
        if len (srt_files) > 0:
            self.parse_srt(srt_files[0]) 
        elif len (sbv_files) > 0:
            self.parse_srt(sbv_files[0]) 
        elif len (vtt_files) > 0:
            self.parse_srt(vtt_files[0]) 
      
      
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
        self.parse_srt(self.subName[0]) 
  
    def parse_srt(self, file_name):
        
        with open(file_name, 'r', encoding='utf-8') as file:
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
  
        self.subHolder.setPos((self.width()-self.subHolder.boundingRect().width() )/2, self.height() - 200)
        self.sub_timer.start(100)  # Check every 100 ms

    @Slot()
    def choose_subtitle(self):
        if not self.subWindowShown:
            self.ui.gridLayout_6.removeWidget(self.ui.sub_floating)
            self.ui.sub_floating.setMinimumWidth(216)
            self.ui.sub_floating.setMinimumHeight(400)
            R = QPoint(self.ui.frame_60.x() + self.ui.frame_52.x() , self.ui.frame_32.y() -  self.ui.sub_floating.height() ) 

            # print(f"{R} is r")
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
                    if start_time <= current_time <= end_time :
                        # Display subtitle text
                        self._scene.removeItem(self.subHolder)
                        self.subHolder.setPlainText(text)
                        self.subHolder.setHtml(f"<div style='background: rgba(0, 0, 0, 0.4);color:white;text-align:center;'>{text}</div>")

                        self._scene.addItem(self.subHolder)
                        self.subHolder.setPos((self.width()-self.subHolder.boundingRect().width() )/2, self.height() - 300)
                        break
                    else:
                        self.subHolder.setPlainText(" ")
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
        self.ui.frame_32.setMaximumWidth(self.width())
        self.ui.frame_32.setMinimumHeight(100)
        self.ui.frame_32.raise_()
        R = QPoint(0, self.height())- QPoint(0, self.ui.frame_32.height() + 85)
        self.ui.frame_32.move(R)
        self._videoitem.setSize(self.ui.frame_23.size())
        # top bar top_bar
        # self.ui.top_bar.setMinimumWidth(self.width())
        # self.ui.top_bar.setMaximumWidth(self.width())
        # self.ui.top_bar.setMinimumHeight(50)
        # self.ui.top_bar.setMaximumHeight(50)

    def media_init(self,file_name,progress_callback):
        print(f'file_name =  {file_name}')
        self.player.setSource(QUrl(file_name))
        if self.player.isAvailable():
            self.player.play()
            self._scene.addItem(self._videoitem)
            self.view.fitInView(self._scene.sceneRect())
            # self.view.fitInView(self._scene.sceneRect(), Qt.KeepAspectRatio)
            # self.view.fitInView(self._videoitem)
            self._videoitem.setSize(self.ui.frame_23.size())
        else :
            print('media type is not supported')
    def resultFunctionMedia_int(self,result):
        self.ui.stackedWidget.setCurrentIndex(3)
        self.player.setVideoOutput(self._videoitem)
        subtitle_tracks = self.player.subtitleTracks()
        print(f'the subtitles tracked are { subtitle_tracks}')
        self.auto_local_sub()
        if subtitle_tracks:
            self.player.setSubtitleTrack(subtitle_tracks[0])

    @Slot()
    def _ensure_stopped(self):
        if self.player.playbackState() != QMediaPlayer.StoppedState:
            self.player.stop()
    
    # preferences
    @Slot()
    def handle_preference(self): 
        self.add_box_shadow()
        if not self.pref_shown:
            self.ui.verticalLayout_18.removeWidget(self.ui.preferences_frame)
            R = QPoint(0, 0)+  QPoint(15, 50)
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
    def add_box_shadow(self):
        # Create a shadow effect
        shadow = QGraphicsDropShadowEffect()
        shadow.setColor(QColor(0,0, 0, .9))  # Shadow color (RGBA)
        shadow.setBlurRadius(8)  # Shadow blur radius
        shadow.setOffset(6, 6)  # Shadow offset (x, y)
        # Apply the shadow effect to the widget
        self.ui.preferences_frame.setGraphicsEffect(shadow)

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
