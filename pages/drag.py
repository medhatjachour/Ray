from functools import partial
from PySide6.QtCore import Qt, QThreadPool
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
            partial(self.showDialog )
        )

  
