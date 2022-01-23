from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(QtCore.QSize(1280, 720))
        MainWindow.setStyleSheet("""background: #424549;""")
        MainWindow.setWindowTitle("Discord AutoPoster")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 640, 720))
        self.background.setStyleSheet("""background: #36393E;""")
        self.background.setObjectName("background")

        self.titletext = QtWidgets.QLabel(self.centralwidget)
        self.titletext.setGeometry(QtCore.QRect(192, 54, 433, 70))
        self.titletext.setStyleSheet("""background: rgba(0, 0, 0, 0);
                                        font-family: Sitara;
                                        font-style: normal;
                                        font-weight: normal;
                                        font-size: 40px;
                                        line-height: 65px;
                                        color: #FFFFFF;""")
        self.titletext.setObjectName("titletext")
        self.titletext.setText("Discord Auto Poster")

        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(50, 41, 115, 83))
        self.logo.setStyleSheet("""background: rgba(0, 0, 0, 0);
                                    background-image: url(img/logo.png);""")
        self.logo.setObjectName("logo")

        self.info_text = QtWidgets.QLabel(self.centralwidget)
        self.info_text.setGeometry(QtCore.QRect(34, 161, 570, 155))
        self.info_text.setStyleSheet("""background: #424549;
                                        border-radius: 20px;
                                        font-family: Sitara;
                                        font-style: normal;
                                        font-weight: normal;
                                        font-size: 16px;
                                        line-height: 23px;
                                        text-align: center;
                                        color: #FFFFFF;""")
        self.info_text.setObjectName("info_text")
        self.info_text.setText("Software for automatically sending messages to discord channels \nGuide: https://github.com/discord-camp/discord-autoposter \n\nMade by RusTNT \nvk.com/rustnt \ndiscord: RusTNT#7271")
        self.info_text.setAlignment(QtCore.Qt.AlignCenter)

        self.logs_name = QtWidgets.QLabel(self.centralwidget)
        self.logs_name.setGeometry(QtCore.QRect(276, 315, 104, 70))
        self.logs_name.setStyleSheet("""background: rgba(0, 0, 0, 0);
                                        font-family: Sitara;
                                        font-style: normal;
                                        font-weight: normal;
                                        font-size: 36px;
                                        line-height: 58px;
                                        color: #FFFFFF;""")
        self.logs_name.setObjectName("logs_name")
        self.logs_name.setText("Logs")
        
        self.logs_text = QtWidgets.QTextEdit(self.centralwidget)
        self.logs_text.setGeometry(QtCore.QRect(33, 381, 570, 301))
        self.logs_text.setStyleSheet("""background: #C4C4C4;
                                        border-radius: 20px;
                                        font-family: Sitara;
                                        font-style: normal;
                                        font-weight: normal;
                                        font-size: 16px;
                                        line-height: 58px;
                                        color: #000000;
                                        padding: 10px""")
        self.logs_text.setObjectName("logs_text")
        self.logs_text.setAlignment(QtCore.Qt.AlignHCenter)
        self.logs_text.setReadOnly(True)
        self.token_text = QtWidgets.QLabel(self.centralwidget)
        self.token_text.setGeometry(QtCore.QRect(675, 13, 125, 35))
        self.token_text.setStyleSheet("""font-family: Sitara;
                                        font-style: normal;
                                        font-weight: normal;
                                        font-size: 18px;
                                        line-height: 29px;
                                        color: #FFFFFF;""")
        self.token_text.setObjectName("token_text")
        self.token_text.setText("Your token:")

        self.token = QtWidgets.QLineEdit(self.centralwidget)
        self.token.setGeometry(QtCore.QRect(675, 51, 578, 35))
        self.token.setStyleSheet("""background: #C4C4C4;
                                    border-radius: 10px;
                                    font-family: Sitara;
                                    font-style: normal;
                                    font-weight: normal;
                                    font-size: 18px;
                                    line-height: 29px;
                                    color: #000000;""")
        self.token.setObjectName("token")
        self.token.setPlaceholderText("Enter discord token")

        self.channel_id_text = QtWidgets.QLabel(self.centralwidget)
        self.channel_id_text.setGeometry(QtCore.QRect(675, 91, 125, 35))
        self.channel_id_text.setStyleSheet("""font-family: Sitara;
                                        font-style: normal;
                                        font-weight: normal;
                                        font-size: 18px;
                                        line-height: 29px;
                                        color: #FFFFFF;""")
        self.channel_id_text.setObjectName("channel_id_text")
        self.channel_id_text.setText("Channel id:")

        self.channel_id = QtWidgets.QLineEdit(self.centralwidget)
        self.channel_id.setGeometry(QtCore.QRect(675, 129, 578, 35))
        self.channel_id.setStyleSheet("""background: #C4C4C4;
                                    border-radius: 10px;
                                    font-family: Sitara;
                                    font-style: normal;
                                    font-weight: normal;
                                    font-size: 18px;
                                    line-height: 29px;
                                    color: #000000;""")
        self.channel_id.setObjectName("channel_id")
        self.channel_id.setPlaceholderText("Enter channel id")

        self.message_text = QtWidgets.QLabel(self.centralwidget)
        self.message_text.setGeometry(QtCore.QRect(675, 169, 125, 35))
        self.message_text.setStyleSheet("""font-family: Sitara;
                                        font-style: normal;
                                        font-weight: normal;
                                        font-size: 18px;
                                        line-height: 29px;
                                        color: #FFFFFF;""")
        self.message_text.setObjectName("message_text")
        self.message_text.setText("Message:")

        self.message = QtWidgets.QTextEdit(self.centralwidget)
        self.message.setGeometry(QtCore.QRect(675, 207, 578, 222))
        self.message.setStyleSheet("""background: #C4C4C4;
                                    border-radius: 10px;
                                    font-family: Sitara;
                                    font-style: normal;
                                    font-weight: normal;
                                    font-size: 18px;
                                    line-height: 29px;
                                    color: #000000;""")
        self.message.setObjectName("message")
        self.message.setPlaceholderText("Enter message")
        self.message.setAlignment(QtCore.Qt.AlignHCenter)

        self.delay_text = QtWidgets.QLabel(self.centralwidget)
        self.delay_text.setGeometry(QtCore.QRect(675, 440, 220, 35))
        self.delay_text.setStyleSheet("""font-family: Sitara;
                                        font-style: normal;
                                        font-weight: normal;
                                        font-size: 18px;
                                        line-height: 29px;
                                        color: #FFFFFF;""")
        self.delay_text.setObjectName("delay_text")
        self.delay_text.setText("Delay: every          minutes")

        self.delay = QtWidgets.QLineEdit(self.centralwidget)
        self.delay.setGeometry(QtCore.QRect(780, 448, 45, 22))
        self.delay.setStyleSheet("""background: #C4C4C4;
                                    border-radius: 10px;
                                    font-family: Sitara;
                                    font-style: normal;
                                    font-weight: normal;
                                    font-size: 18px;
                                    line-height: 29px;
                                    color: #000000;""")
        self.delay.setObjectName("delay")
        self.delay.setPlaceholderText("5")

        self.image_text = QtWidgets.QLabel(self.centralwidget)
        self.image_text.setGeometry(QtCore.QRect(675, 486, 125, 35))
        self.image_text.setStyleSheet("""font-family: Sitara;
                                        font-style: normal;
                                        font-weight: normal;
                                        font-size: 18px;
                                        line-height: 29px;
                                        color: #FFFFFF;""")
        self.image_text.setObjectName("image_text")
        self.image_text.setText("Image:")

        self.image = QtWidgets.QLineEdit(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(675, 524, 578, 35))
        self.image.setStyleSheet("""background: #C4C4C4;
                                    border-radius: 10px;
                                    font-family: Sitara;
                                    font-style: normal;
                                    font-weight: normal;
                                    font-size: 18px;
                                    line-height: 29px;
                                    color: #000000;""")
        self.image.setObjectName("image")
        self.image.setPlaceholderText("Enter path: (img/yourimage.png)")

        self.start_Button = QtWidgets.QPushButton(self.centralwidget)
        self.start_Button.setGeometry(QtCore.QRect(796, 584, 287, 91))
        self.start_Button.setStyleSheet("""background: #7289DA;
                                        border-radius: 15px;
                                        font-family: Sitara;
                                        font-style: normal;
                                        font-weight: normal;
                                        font-size: 36px;
                                        line-height: 58px;
                                        text-align: center;
                                        color: #FFFFFF;""")
        self.start_Button.setObjectName("start_Button")
        self.start_Button.setText("START")



        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.error_dialog = QtWidgets.QErrorMessage()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate