from functools import partial
from PySide6.QtCore import Qt, QThreadPool
from PySide6.QtWidgets import QFileDialog
import os

from widgets.DragDrop.Dragdrop import DragDrop
class Drag:
    def __init__(self):
        from ui.ui_main import Ui_Form

        self.ui = Ui_Form()
        self.ui.setupUi(self)

    def init(self, main):
        self.main = main
        self.drag_frame = DragDrop(main)
        #####################################
        Drag.buttons_actions(self)
        
        self.ui.gridLayout_7.addWidget(self.drag_frame, 0, 1)

    def buttons_actions(self):
       # filter button
        self.drag_frame.browse_file.clicked.connect(
            partial(Drag.showDialog,self )
            # partial(self.showDialog )
        )

  
    def showDialog(self):
        self.fileName = QFileDialog.getOpenFileName(self, "Chose media", "/","Media Files (*.mp3 *.mp4 *.avi *.mov *.mkv *.ogv *.webm *.MPEG *.WMV *.FLV .*3GP .*FLAC .*DSD .*AIFF .*ALAC .*AAC )")
        if len(self.fileName[0])> 10:
            self.start_media(self.fileName[0])
