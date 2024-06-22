from functools import partial
from PySide6.QtCore import Qt, QThreadPool
from widgets.DragDrop.Dragdrop import DragDrop
class Drag:
    def __init__(self):
        from ui.ui_main import Ui_Form

        self.ui = Ui_Form()
        self.ui.setupUi(self)

    def init(self):
        self.drag_frame = DragDrop()
        #####################################
        Drag.buttons_actions(self)
        
        self.ui.gridLayout_7.addWidget(self.drag_frame, 0, 1)

    def buttons_actions(self):
       # filter button
        self.ui.signUp_tab.clicked.connect(
            partial(Drag.open_singUp, self)
        )

  

    def open_singUp(self):
        self.ui.stackedWidget_2.setCurrentIndex(1)
  