from PyQt5 import QtWidgets, QtCore
from form import Ui_MainWindow
from sender import *
from datetime import datetime
import sys


class Worker(QtCore.QThread):
    logsbeep=QtCore.pyqtSignal(str)

    def __init__(self, token, channel_id, message, delay, image):
        super(Worker, self).__init__()
        self.token = token
        self.channel_id = channel_id
        self.message = message
        self.delay = delay
        self.image = image
    def run(self):
        try:
            send(self, self.token, self.channel_id, self.message, self.delay, self.image)
        except:
            pass


class formwindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(formwindow, self).__init__()
        self.mainui = Ui_MainWindow()
        self.mainui.setupUi(self)
        self.mainui.start_Button.installEventFilter(self)

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.MouseButtonPress and source is self.mainui.start_Button:
            self.mainui.start_Button.setStyleSheet("""background: #23272A;
                                        border-radius: 15px;
                                        font-family: Sitara;
                                        font-style: normal;
                                        font-weight: normal;
                                        font-size: 36px;
                                        line-height: 58px;
                                        text-align: center;
                                        color: #FFFFFF;""")
            return False
        if event.type() == QtCore.QEvent.MouseButtonRelease and source is self.mainui.start_Button:
            self.mainui.start_Button.setStyleSheet("""background: #7289DA;
                                        border-radius: 15px;
                                        font-family: Sitara;
                                        font-style: normal;
                                        font-weight: normal;
                                        font-size: 36px;
                                        line-height: 58px;
                                        text-align: center;
                                        color: #FFFFFF;""")
            return False
        return super(formwindow, self).eventFilter(source, event)
    

def main():
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = formwindow()
    mainwindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()