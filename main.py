from PyQt5 import QtWidgets, QtCore
from form import Ui_MainWindow
from sender import *
from slash_sender import *
import sys
import json

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

class SlashWorker(QtCore.QThread):
    logsbeep=QtCore.pyqtSignal(str)

    def __init__(self, token, channel_id, application_id, guild_id, version_id, command_id, command, delay):
        super(SlashWorker, self).__init__()
        self.token = token
        self.channel_id = channel_id
        self.application_id = application_id
        self.guild_id = guild_id
        self.version_id = version_id
        self.command_id = command_id
        self.command = command
        self.delay = delay
    def run(self):
        slash_send(self, self.token, self.channel_id, self.application_id, self.guild_id, self.version_id, self.command_id, self.command, self.delay)



class formwindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(formwindow, self).__init__()
        self.mainui = Ui_MainWindow()
        self.mainui.setupUi(self)
        self.mainui.start_Button.installEventFilter(self)
        self.mainui.slash_Button.installEventFilter(self)
        self.mainui.start_slash_Button.installEventFilter(self)
        self.mainui.start_Button.clicked.connect(self.start_sending)
        self.mainui.slash_Button.clicked.connect(self.show_slash)
        self.mainui.start_slash_Button.clicked.connect(self.start_slash_sending)
        try:
            with open('data.json') as json_file:
                data = json.load(json_file)
                self.mainui.token.setPlainText(data['token'])
                self.mainui.channel_id.setText(data['channelid'])
                self.mainui.guild_id.setText(data['guild_id'])
                self.mainui.application_id.setText(data['application_id'])
                self.mainui.version_id.setText(data['version_id'])
                self.mainui.command_id.setText(data['command_id'])
                self.mainui.command.setText(data['command'])
                self.mainui.delay.setText(data['delay'])
                self.mainui.image.setText(data['image'])
                self.mainui.message.setPlainText(data['message'])
        except Exception as e: 
            print(e)
            pass


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
        if event.type() == QtCore.QEvent.MouseButtonPress and source is self.mainui.slash_Button:
            self.mainui.slash_Button.setStyleSheet("""background-image: url(img/slash_active.png);
                                                    border: 0;""")
            return False
        if event.type() == QtCore.QEvent.MouseButtonRelease and source is self.mainui.slash_Button:
            self.mainui.slash_Button.setStyleSheet ("""background-image: url(img/slash.png);
                                                    border: 0;""")
            return False
        if event.type() == QtCore.QEvent.MouseButtonPress and source is self.mainui.start_slash_Button:
            self.mainui.start_slash_Button.setStyleSheet("""background: #23272A;
                                        border-radius: 15px;
                                        font-family: Sitara;
                                        font-style: normal;
                                        font-weight: normal;
                                        font-size: 36px;
                                        line-height: 58px;
                                        text-align: center;
                                        color: #FFFFFF;""")
            return False
        if event.type() == QtCore.QEvent.MouseButtonRelease and source is self.mainui.start_slash_Button:
            self.mainui.start_slash_Button.setStyleSheet("""background: #7289DA;
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
        def red_color(element):
            element.setStyleSheet("""background: #C4C4C4;
                                    border: 2px solid #BC2E3F;
                                    border-radius: 10px;
                                    font-family: Sitara;
                                    font-style: normal;
                                    font-weight: normal;
                                    font-size: 18px;
                                    line-height: 29px;
                                    color: #000000;""")
        def logs_update(value: str):
            self.mainui.logs_text.append(value)
        token = self.mainui.token.toPlainText()
        channel_id = self.mainui.channel_id.text()
        message =self.mainui.message.toPlainText()
        delay = self.mainui.delay.text()
        image = self.mainui.image.text()
        guild_id = self.mainui.guild_id.text()
        application_id = self.mainui.application_id.text()
        version_id = self.mainui.version_id.text()
        command_id = self.mainui.command_id.text()
        command = self.mainui.command.text()
        if token == '':
            red_color(self.mainui.token)
        elif channel_id == '':
            red_color(self.mainui.channel_id)
        elif message == '':
            red_color(self.mainui.message)
        elif delay == '':
            red_color(self.mainui.delay)
        else:
            data = {'token': token,
                    'channelid': channel_id,
                    'guild_id': guild_id,
                    'application_id': application_id,
                    'version_id': version_id,
                    'command_id': command_id,
                    'command': command,
                    'delay': delay,
                    'image':image,
                    'message': message
                    }
            with open('data.json', 'w') as outfile:
                json.dump(data, outfile)
            self.mainui.logs_text.append('Program started! Don\'t close!')
            self.worker = Worker(token, channel_id, message, delay, image)
            self.worker.logsbeep.connect(logs_update)
            self.worker.start()
    def start_slash_sending(self):
        def red_color(element):
            element.setStyleSheet("""background: #C4C4C4;
                                    border: 2px solid #BC2E3F;
                                    border-radius: 10px;
                                    font-family: Sitara;
                                    font-style: normal;
                                    font-weight: normal;
                                    font-size: 18px;
                                    line-height: 29px;
                                    color: #000000;""")
        def logs_update(value: str):
            self.mainui.logs_text.append(value)
        token = self.mainui.token.toPlainText()
        channel_id = self.mainui.channel_id.text()
        guild_id = self.mainui.guild_id.text()
        application_id = self.mainui.application_id.text()
        version_id = self.mainui.version_id.text()
        command_id = self.mainui.command_id.text()
        command = self.mainui.command.text()
        delay = self.mainui.delay.text()
        message =self.mainui.message.toPlainText()
        image = self.mainui.image.text()
        
        if token == '':
            red_color(self.mainui.token)
        elif channel_id == '':
            red_color(self.mainui.channel_id)
        elif guild_id == '':
            red_color(self.mainui.guild_id)
        elif application_id == '':
            red_color(self.mainui.application_id)
        elif application_id == '':
            red_color(self.mainui.application_id)
        elif version_id == '':
            red_color(self.mainui.version_id)
        elif command_id == '':
            red_color(self.mainui.command_id)
        elif command == '':
            red_color(self.mainui.command)
        elif delay == '':
            red_color(self.mainui.delay)
        else:
            data = {'token': token,
                    'channelid': channel_id,
                    'guild_id': guild_id,
                    'application_id': application_id,
                    'version_id': version_id,
                    'command_id': command_id,
                    'command': command,
                    'delay': delay,
                    'image':image,
                    'message': message
                    }
            with open('data.json', 'w') as outfile:
                json.dump(data, outfile)
            self.mainui.logs_text.append('Program started! Don\'t close!')
            self.worker = SlashWorker(token, channel_id, application_id, guild_id, version_id, command_id, command, delay)
            self.worker.logsbeep.connect(logs_update)
            self.worker.start()

    def show_slash(self):
        if self.mainui.slash_Button.text() == '':
            self.mainui.message.setHidden(True)
            self.mainui.message_text.setHidden(True)
            self.mainui.image.setHidden(True)
            self.mainui.image_text.setHidden(True)
            self.mainui.start_Button.setHidden(True)
            self.mainui.delay_text.setGeometry(QtCore.QRect(675, 629, 220, 35))
            self.mainui.delay.setGeometry(QtCore.QRect(780, 637, 45, 22))
            self.mainui.guild_id_text.setHidden(False)
            self.mainui.guild_id.setHidden(False)
            self.mainui.application_id_text.setHidden(False)
            self.mainui.application_id.setHidden(False)
            self.mainui.version_id_text.setHidden(False)
            self.mainui.version_id.setHidden(False)
            self.mainui.command_id.setHidden(False)
            self.mainui.command_id_text.setHidden(False)
            self.mainui.command_text.setHidden(False)
            self.mainui.command.setHidden(False)
            self.mainui.start_slash_Button.setHidden(False)
            self.mainui.slash_Button.setText(' ')
        else:
            self.mainui.message.setHidden(False)
            self.mainui.message_text.setHidden(False)
            self.mainui.image.setHidden(False)
            self.mainui.image_text.setHidden(False)
            self.mainui.start_Button.setHidden(False)
            self.mainui.delay_text.setGeometry(QtCore.QRect(675, 440, 220, 35))
            self.mainui.delay.setGeometry(QtCore.QRect(780, 448, 45, 22))
            self.mainui.guild_id_text.setHidden(True)
            self.mainui.guild_id.setHidden(True)
            self.mainui.application_id_text.setHidden(True)
            self.mainui.application_id.setHidden(True)
            self.mainui.version_id_text.setHidden(True)
            self.mainui.version_id.setHidden(True)
            self.mainui.command_id.setHidden(True)
            self.mainui.command_id_text.setHidden(True)
            self.mainui.command_text.setHidden(True)
            self.mainui.command.setHidden(True)
            self.mainui.start_slash_Button.setHidden(True)
            self.mainui.slash_Button.setText('')

def main():
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = formwindow()
    mainwindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()