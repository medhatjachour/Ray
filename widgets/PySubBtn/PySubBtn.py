from PySide6.QtWidgets import QRadioButton
from PySide6.QtGui import QCursor
from PySide6.QtCore import Qt
# STYLE
# ///////////////////////////////////////////////////////////////
style = '''
QRadioButton {{
    background-color :  transparent;
    border : none ;
    color: rgba(36, 43, 46, 1);
    font-family: Proxima Nova;
    font-size: 12px;
    font-weight: 400;
    line-height: 12px;
    margin-top:10px;
}}
QRadioButton:hover {{
  /*background: rgba(0, 0, 0, 0.1);*/
  background: rgba(242, 242, 242, 1);

    margin-left:10px;
}}
QRadioButton:checked {{	
    background-color : rgb(255, 255, 255) ;
    color: rgb(0, 0, 0);
    font-family: Proxima Nova;
    font-size: 12px;
    font-weight: 700;
    line-height: 14.62px;
    text-align: left;
}}
QRadioButton::indicator {{
	width : 0px ;
    height: 0px ;
    background-color:transparent;
 }}
  QRadioButton::indicator:checked {{
	margin-left:5px;
	width : 25px ;
    height: 25 px ;
	image:  url(:/icons/assets/icons/check.png);
 }}
'''

class PySubBtn(QRadioButton):
    def __init__(
        self,
        text="None",
    ):
        super(PySubBtn, self).__init__()

        # FORMAT STYLE
        # ///////////////////////////////////////////////////////////////
        adjust_style = style.format(

        )
        self.setMinimumHeight(35)
        
        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.setText(text)
        # APPLY CUSTOM STYLE
        # ///////////////////////////////////////////////////////////////
        self.setStyleSheet(adjust_style)