from functools import partial
from PySide6.QtCore import Qt, QThreadPool
import os

from widgets.DragDrop.Dragdrop import DragDrop
class Drag:
    def __init__(self):
        from ui.ui_main import Ui_Form

        self.ui = Ui_Form()
        self.ui.setupUi(self)

    def init(self):
        self.drag_frame = DragDrop(Drag)
        #####################################
        Drag.buttons_actions(self)
        
        self.ui.gridLayout_7.addWidget(self.drag_frame, 0, 1)

    def buttons_actions(self):
       # filter button
        self.drag_frame.browse_file.clicked.connect(
            partial(self.showDialog )
        )

  

    def dragg(self,file_name):
        worker = Worker(
                partial(
                    self.media_init,file_name
                )
            )
        worker.signals.result.connect(partial(self.resultFunctionMedia_int))
        self.threadpool.start(worker)
        self.ui.movie_name.setText(os.path.basename(self.fileName[0]))
  