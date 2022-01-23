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
        send(self, self.token, self.channel_id, self.message, self.delay, self.image)



class formwindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(formwindow, self).__init__()
        self.mainui = Ui_MainWindow()
        self.mainui.setupUi(self)
        self.mainui.start_Button.installEventFilter(self)
        self.mainui.start_Button.clicked.connect(self.start_sending)

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
    
    def start_sending(self):
        def logs_update(value: str):
            self.mainui.logs_text.append(value)
        token = self.mainui.token.text()
        channel_id = self.mainui.channel_id.text()
        message =self.mainui.message.toPlainText()
        delay = self.mainui.delay.text()
        image = self.mainui.image.text()
        if token == '':
            self.mainui.token.setStyleSheet("""background: #C4C4C4;
                                    border: 2px solid #BC2E3F;
                                    border-radius: 10px;
                                    font-family: Sitara;
                                    font-style: normal;
                                    font-weight: normal;
                                    font-size: 18px;
                                    line-height: 29px;
                                    color: #000000;""")
        elif channel_id == '':
             self.mainui.channel_id.setStyleSheet("""background: #C4C4C4;
                                    border: 2px solid #BC2E3F;
                                    border-radius: 10px;
                                    font-family: Sitara;
                                    font-style: normal;
                                    font-weight: normal;
                                    font-size: 18px;
                                    line-height: 29px;
                                    color: #000000;""")
        elif message == '':
            self.mainui.message.setStyleSheet("""background: #C4C4C4;
                                    border: 2px solid #BC2E3F;
                                    border-radius: 10px;
                                    font-family: Sitara;
                                    font-style: normal;
                                    font-weight: normal;
                                    font-size: 18px;
                                    line-height: 29px;
                                    color: #000000;""")
        elif delay == '':
            self.mainui.delay.setStyleSheet("""background: #C4C4C4;
                                    border: 2px solid #BC2E3F;
                                    border-radius: 10px;
                                    font-family: Sitara;
                                    font-style: normal;
                                    font-weight: normal;
                                    font-size: 18px;
                                    line-height: 29px;
                                    color: #000000;""")
        else:
            self.worker = Worker(token, channel_id, message, delay, image)
            self.worker.start()
            self.worker.logsbeep.connect(logs_update)
            self.mainui.logs_text.append('Program started! Don\'t close!')
def main():
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = formwindow()
    mainwindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()