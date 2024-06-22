from functools import partial


class Log:
    def __init__(self):
        from ui.ui_main import Ui_Form

        self.ui = Ui_Form()
        self.ui.setupUi(self)


    def init(self):
        #####################################
        Log.buttons_actions(self)

    def buttons_actions(self):
       # filter button
        self.ui.signUp_tab.clicked.connect(
            partial(Log.open_singUp, self)
        )
        self.ui.logIn_tab.clicked.connect(
            partial(Log.open_logIn, self)
        )
        self.ui.logIn_btn.clicked.connect(
            partial(Log.log_in_fun, self)
        )




    def open_singUp(self):
        self.ui.stackedWidget_2.setCurrentIndex(1)
    def open_logIn(self):
        self.ui.stackedWidget_2.setCurrentIndex(0)
    def log_in_fun(self):
        self.ui.stackedWidget.setCurrentIndex(2)