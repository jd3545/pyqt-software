from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1450, 778)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        font = QFont()
        font.setFamily(u"MS")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet(u"*{Background:\"Black\";Border:0.5px solid \"green\";color: \"White\";font: bold;font-family:\"MS\"}\n"
"QPushButton:Hover{Color: \"Green\";Border:0.5px solid \"White\";Font-Size:10pt}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 35))
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame_4)
        self.verticalLayout_10 = QVBoxLayout(self.frame_4)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_10.addWidget(self.label_6)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_8)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_8)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_5)


        self.verticalLayout_4.addWidget(self.frame_8)

        self.frame_11 = QFrame(self.frame_6)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_11)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame_11)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton_5 = QPushButton(self.frame_9)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.frame_9)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.pushButton_6)


        self.verticalLayout_8.addWidget(self.frame_9)

        self.pushButton_3 = QPushButton(self.frame_11)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)

        self.verticalLayout_8.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame_11)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)

        self.verticalLayout_8.addWidget(self.pushButton_4)


        self.verticalLayout_4.addWidget(self.frame_11)


        self.verticalLayout_2.addWidget(self.frame_6)


        self.horizontalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 35))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_2)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 90))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frame_5)
        self.verticalLayout_11 = QVBoxLayout(self.frame_5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_7 = QLabel(self.frame_5)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_11.addWidget(self.label_7)

        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_7)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_7)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 35))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_3)

        self.frame_10 = QFrame(self.frame_7)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_10)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.frame_10)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 379, 225))
        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        #       start class data frame scroll list
        # self.frame_12 = QFrame(self.scrollAreaWidgetContents)
        # self.frame_12.setObjectName(u"frame_12")
        # self.frame_12.setMinimumSize(QSize(0, 45))
        # self.frame_12.setMaximumSize(QSize(16777215, 0))
        # self.frame_12.setFrameShape(QFrame.StyledPanel)
        # self.frame_12.setFrameShadow(QFrame.Raised)
        # self.horizontalLayout_2 = QHBoxLayout(self.frame_12)
        # self.horizontalLayout_2.setSpacing(0)
        # self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        # self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        # self.label_4 = QLabel(self.frame_12)
        # self.label_4.setObjectName(u"label_4")
        #
        # self.horizontalLayout_2.addWidget(self.label_4)
        #
        # self.pushButton = QPushButton(self.frame_12)
        # self.pushButton.setObjectName(u"pushButton")
        # sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        # self.pushButton.setSizePolicy(sizePolicy)
        #
        # self.horizontalLayout_2.addWidget(self.pushButton)
        #
        # self.pushButton_2 = QPushButton(self.frame_12)
        # self.pushButton_2.setObjectName(u"pushButton_2")
        # sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        # self.pushButton_2.setSizePolicy(sizePolicy)
        #
        # self.horizontalLayout_2.addWidget(self.pushButton_2)


        #self.verticalLayout_7.addWidget(self.frame_12, 0, Qt.AlignTop)
        # end

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_6.addWidget(self.scrollArea)


        self.verticalLayout_5.addWidget(self.frame_10)


        self.verticalLayout_3.addWidget(self.frame_7)


        self.horizontalLayout.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"IMAGE [0]/[100]", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"STATUS", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"[PREVIOUS]", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"[NEXT]", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"[LOAD CLASSES AND IMAGES]", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"[LOAD CHECKPOINT]", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"LABEL NUMBER BELOW! LABEL EACH!", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"CLASSES LOADED [0] |  TO LABEL[0]/[#NUMBER TO BE LABELED]", None))
        #self.label_4.setText(QCoreApplication.translate("MainWindow", u"[0] [BLACK_BALL][FALSE]", None))
        #self.pushButton.setText(QCoreApplication.translate("MainWindow", u"[REMOVE]", None))
        #self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"[ADD]", None))
    # retranslateUi

