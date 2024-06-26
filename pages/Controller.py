from functools import partial
import time 
from PySide6.QtCore import Qt, QThreadPool,Slot,QSize,QUrl
from PySide6.QtWidgets import  QSlider
from PySide6.QtGui import QIcon
from PySide6.QtMultimedia import (QMediaPlayer)
from widgets.worker.Worker import Worker

class Control:
    def __init__(self):
        from ui.ui_main import Ui_Form

        self.ui = Ui_Form()
        self.ui.setupUi(self)

    def init(self):
        #####################################

        # positions 
        self.ui.position_control.setTickInterval(100)
        self.ui.position_control.setTickPosition(QSlider.TicksBelow)
        self.ui.position_control.setToolTip("Position")
        # sound 
        self.audio_value = self.audio_output.volume()*100
        self.ui.sound_control.setValue(self.audio_output.volume()*100)
        self.ui.sound_control.setTickInterval(10)
        self.ui.sound_control.setTickPosition(QSlider.TicksBelow)
        self.ui.sound_control.setToolTip("Volume")

        Control.buttons_actions(self)
    def buttons_actions(self):
       # filter button
       # sound

        
        # play  / stop
        self.ui.stop_play.clicked.connect(
            partial(Control.play_pause, self)
        )
        # position 
        self.player.positionChanged.connect(
            partial(Control.change_position, self)
        )
        self.player.durationChanged.connect(
            partial(Control.duration_position, self)
        )
        self.ui.forward.clicked.connect(
            partial(Control.forward_ten, self)
        )
        self.ui.backward.clicked.connect(
            partial(Control.backward_ten, self)
        )
        self.ui.position_control.sliderMoved.connect(
            partial(Control.set_position, self)
        )
        # next - previous 

        self.ui.next.clicked.connect(
            partial(Control.next, self)
        )
        self.ui.previus.clicked.connect(
            partial(Control.previous, self)
        )
        # sound
        self.ui.sound_control.valueChanged.connect(
            partial(Control.adjust_audio_volume, self)
        )
        self.ui.mute.clicked.connect(
            partial(Control.mute_fun, self)
        )


    @Slot()
    def play_pause(self):
        if self.player.playbackState() == QMediaPlayer.PlayingState:
            self.player.pause()
            
            if self.dark_mode_on:
                icon_play = QIcon()
                icon_play.addFile(u":/icons/assets/icons/play-w.png", QSize(), QIcon.Normal, QIcon.Off)
                self.ui.stop_play.setIcon(icon_play)
            else:
                icon_play_d = QIcon()
                icon_play_d.addFile(u":/icons/assets/icons/play_.png", QSize(), QIcon.Normal, QIcon.Off)
                self.ui.stop_play.setIcon(icon_play_d)
            # self.ui.stop_play.setIconSize(QSize(21, 21))
        else:
            self.player.play()
            if self.dark_mode_on:
                icon4_pause = QIcon()
                icon4_pause.addFile(u":/icons/assets/icons/equal-pause-w.png", QSize(), QIcon.Normal, QIcon.Off)
                self.ui.stop_play.setIcon(icon4_pause)
            else:
                icon4_pause = QIcon()
                icon4_pause.addFile(u":/icons/assets/icons/equal-pause.png", QSize(), QIcon.Normal, QIcon.Off)
                self.ui.stop_play.setIcon(icon4_pause)
            # self.ui.stop_play.setIconSize(QSize(21, 21))
    # position
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
    def forward_ten(self):
        current_position  = self.player.position() 
        # To skip forward by 10 seconds
        self.player.setPosition(current_position + 10000)
        self.ui.position_control.setValue((current_position+10000) // 1000)
    @Slot()
    def backward_ten(self):
        current_position  = self.player.position() 
        # To skip forward by 10 seconds
        self.player.setPosition(current_position - 10000)
        self.ui.position_control.setValue((current_position-10000) // 1000)
  
    # next - previous   
    @Slot()
    def next(self):
        # using the end of video that ends all the states and so 
        self.player.setPosition(self.player.duration() )
    def previous(self):
        self._playlist_index -= 2 
        self.player.setPosition(self.player.duration() )

    # sound
    @Slot()
    def adjust_audio_volume(self,volume):
        self.audio_output.setVolume(volume/100)
        self.audio_value = volume/100

        if self.is_muted:
            icon_sound = QIcon()
            icon_sound.addFile(u":/icons/assets/icons/volume-max.png", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.mute.setIcon(icon_sound)
    @Slot()
    def mute_fun(self):
        if self.is_muted:
            self.is_muted = not self.is_muted
            self.audio_output.setVolume(self.audio_value)
            if self.dark_mode_on:
                icon_sound_d = QIcon()
                icon_sound_d.addFile(u":/icons/assets/icons/volume-max-w.png", QSize(), QIcon.Normal, QIcon.Off)
                self.ui.mute.setIcon(icon_sound_d)
            else:
                icon_sound = QIcon()
                icon_sound.addFile(u":/icons/assets/icons/volume-max.png", QSize(), QIcon.Normal, QIcon.Off)
                self.ui.mute.setIcon(icon_sound)
        else:
            self.is_muted = not self.is_muted
            self.audio_output.setVolume(0)
            if self.dark_mode_on:
                icon_mute = QIcon()
                icon_mute.addFile(u":/icons/assets/icons/NoAudio.png", QSize(), QIcon.Normal, QIcon.Off)
                self.ui.mute.setIcon(icon_mute)
            else:
                icon_mute = QIcon()
                icon_mute.addFile(u":/icons/assets/icons/Mute.png", QSize(), QIcon.Normal, QIcon.Off)
                self.ui.mute.setIcon(icon_mute)
