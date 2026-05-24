# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(339, 600)
        MainWindow.setMinimumSize(QSize(339, 600))
        MainWindow.setMaximumSize(QSize(914, 16777215))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#centralwidget QWidget{\n"
"	background: #0f3f74;\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.Header = QFrame(self.centralwidget)
        self.Header.setObjectName(u"Header")
        self.Header.setStyleSheet(u"QFrame{\n"
"	background: #020344;\n"
"	padding: 2px;\n"
"	border-top-left-radius: 10px;\n"
"	border-top-right-radius: 10px;\n"
"}")
        self.Header.setFrameShape(QFrame.StyledPanel)
        self.Header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Header)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.Header)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 16pt \"MS Serif\";\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(25, 25))
        self.label.setStyleSheet(u"")
        self.label.setPixmap(QPixmap(u"icon/Logo.png"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)

        self.horizontalLayout_2.addWidget(self.label, 0, Qt.AlignLeft)

        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.frame_3, 0, Qt.AlignLeft)

        self.frame_4 = QFrame(self.Header)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"#frame_4 QPushButton{\n"
"	background: white;\n"
"	border-radius: 5px;\n"
"	padding: 2px;\n"
"	margin-left: 6px;\n"
"}\n"
"\n"
"#frame_4 QPushButton::hover{\n"
"	background: #28b8d5;\n"
"	border-radius: 5px;\n"
"\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_4.setLineWidth(-1)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 2, 10, 2)
        self.Minimize = QPushButton(self.frame_4)
        self.Minimize.setObjectName(u"Minimize")
        icon = QIcon()
        icon.addFile(u"icon/minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Minimize.setIcon(icon)
        self.Minimize.setIconSize(QSize(18, 18))

        self.horizontalLayout_3.addWidget(self.Minimize)

        self.FullScreen = QPushButton(self.frame_4)
        self.FullScreen.setObjectName(u"FullScreen")
        icon1 = QIcon()
        icon1.addFile(u"icon/Fullscreen.png", QSize(), QIcon.Normal, QIcon.Off)
        self.FullScreen.setIcon(icon1)
        self.FullScreen.setIconSize(QSize(18, 18))

        self.horizontalLayout_3.addWidget(self.FullScreen)

        self.Close = QPushButton(self.frame_4)
        self.Close.setObjectName(u"Close")
        icon2 = QIcon()
        icon2.addFile(u"icon/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Close.setIcon(icon2)
        self.Close.setIconSize(QSize(18, 18))

        self.horizontalLayout_3.addWidget(self.Close)


        self.horizontalLayout.addWidget(self.frame_4, 0, Qt.AlignRight)


        self.verticalLayout_4.addWidget(self.Header)

        self.Body = QFrame(self.centralwidget)
        self.Body.setObjectName(u"Body")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Body.sizePolicy().hasHeightForWidth())
        self.Body.setSizePolicy(sizePolicy)
        self.Body.setFrameShape(QFrame.StyledPanel)
        self.Body.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.Body)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.LeftSide = QFrame(self.Body)
        self.LeftSide.setObjectName(u"LeftSide")
        self.LeftSide.setMinimumSize(QSize(300, 0))
        self.LeftSide.setMaximumSize(QSize(336, 16777215))
        self.LeftSide.setStyleSheet(u"#LeftSide QFrame{\n"
"	background-color: rgb(34, 154, 189);\n"
"}")
        self.LeftSide.setFrameShape(QFrame.StyledPanel)
        self.LeftSide.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.LeftSide)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.LeftHeader = QFrame(self.LeftSide)
        self.LeftHeader.setObjectName(u"LeftHeader")
        self.LeftHeader.setStyleSheet(u"QLabel{\n"
"	color: rgb(0, 0, 0);\n"
"	font: 13pt \"Comic Sans MS\";\n"
"}\n"
"\n"
"QLineEdit {\n"
"	 background: white; \n"
"     color: black; \n"
"     border: 2 px solid black; \n"
"     border-radius: 5px; \n"
"     padding: 4px;  \n"
"\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border: 3px solid rgb(13, 57, 103); \n"
"}")
        self.LeftHeader.setFrameShape(QFrame.StyledPanel)
        self.LeftHeader.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.LeftHeader)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(9, 0, 9, 0)
        self.label_3 = QLabel(self.LeftHeader)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"")
        self.label_3.setMargin(10)

        self.horizontalLayout_5.addWidget(self.label_3)

        self.FolderLocation = QLineEdit(self.LeftHeader)
        self.FolderLocation.setObjectName(u"FolderLocation")
        font = QFont()
        font.setFamilies([u"Open Sans Light"])
        font.setPointSize(11)
        self.FolderLocation.setFont(font)

        self.horizontalLayout_5.addWidget(self.FolderLocation)


        self.verticalLayout_2.addWidget(self.LeftHeader, 0, Qt.AlignTop)

        self.frame_9 = QFrame(self.LeftSide)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"QPushButton{\n"
"	border: 1px solid white;\n"
"	font: 11pt \"Nexa Heavy\";\n"
"	color: white;\n"
"	padding: 6px;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	border: 2px solid white;\n"
"	font: 700 10pt \"Comic Sans MS\";\n"
"	color: rgb(2, 3, 68);\n"
"	background: white;\n"
"	padding: 3px;\n"
"\n"
"}")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.CheckFolder = QPushButton(self.frame_9)
        self.CheckFolder.setObjectName(u"CheckFolder")

        self.horizontalLayout_6.addWidget(self.CheckFolder, 0, Qt.AlignHCenter)

        self.RenameBtn = QPushButton(self.frame_9)
        self.RenameBtn.setObjectName(u"RenameBtn")

        self.horizontalLayout_6.addWidget(self.RenameBtn, 0, Qt.AlignHCenter)

        self.OpenFolder = QPushButton(self.frame_9)
        self.OpenFolder.setObjectName(u"OpenFolder")

        self.horizontalLayout_6.addWidget(self.OpenFolder, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.frame_9, 0, Qt.AlignTop)

        self.FolderCheck = QFrame(self.LeftSide)
        self.FolderCheck.setObjectName(u"FolderCheck")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.FolderCheck.sizePolicy().hasHeightForWidth())
        self.FolderCheck.setSizePolicy(sizePolicy1)
        self.FolderCheck.setFrameShape(QFrame.StyledPanel)
        self.FolderCheck.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.FolderCheck)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.scrollArea = QScrollArea(self.FolderCheck)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"QWidget{\n"
"	background-color: #1b7ca5;\n"
"	border-radius: 10px;\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 312, 412))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.scrollAreaWidgetContents)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"QLabel{\n"
"	font: 700 10pt \"Comic Sans MS\";\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(10, 10, 8, -1)
        self.label_6 = QLabel(self.frame_8)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_10.addWidget(self.label_6, 0, Qt.AlignLeft)

        self.FileCount = QLabel(self.frame_8)
        self.FileCount.setObjectName(u"FileCount")

        self.horizontalLayout_10.addWidget(self.FileCount)

        self.line = QFrame(self.frame_8)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"border: 2px solid black")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_10.addWidget(self.line)

        self.Pin = QCheckBox(self.frame_8)
        self.Pin.setObjectName(u"Pin")
        self.Pin.setStyleSheet(u"QCheckBox{\n"
"	background: transparent;\n"
"	spacing: 10px;\n"
"	font: 700 10pt \"Comic Sans MS\";\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.horizontalLayout_10.addWidget(self.Pin, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.frame_8, 0, Qt.AlignTop)

        self.frame_15 = QFrame(self.scrollAreaWidgetContents)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setStyleSheet(u"QLabel{\n"
"	font: 700 11pt \"Comic Sans MS\";\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(10, 5, 8, -1)
        self.label_7 = QLabel(self.frame_15)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_9.addWidget(self.label_7)

        self.SelectAllFile = QCheckBox(self.frame_15)
        self.SelectAllFile.setObjectName(u"SelectAllFile")
        self.SelectAllFile.setStyleSheet(u"QCheckBox {\n"
"    spacing: 5px;\n"
"	color: white;\n"
"	font: 700 10pt \"Comic Sans MS\";\n"
"	margin-right: 5px;\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"	background-color: black;\n"
"	border: 2px solid Black;\n"
"	border-radius: 10px;\n"
"	padding: 1px;\n"
"	\n"
"}\n"
"QCheckBox::indicator:checked{\n"
"	background-color:white;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.SelectAllFile.setChecked(False)

        self.horizontalLayout_9.addWidget(self.SelectAllFile, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.frame_15)

        self.FileCheckBody = QFrame(self.scrollAreaWidgetContents)
        self.FileCheckBody.setObjectName(u"FileCheckBody")
        sizePolicy1.setHeightForWidth(self.FileCheckBody.sizePolicy().hasHeightForWidth())
        self.FileCheckBody.setSizePolicy(sizePolicy1)
        self.FileCheckBody.setStyleSheet(u"#FileCheckBody QCheckBox {\n"
"    spacing: 7px;\n"
"	color: white;\n"
"	font: 700 10pt \"Comic Sans MS\";\n"
"	margin-right: 5px;\n"
"}\n"
"#FileCheckBody QCheckBox::indicator {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"	background-color: black;\n"
"	border: 2px solid Black;\n"
"	border-radius: 10px;\n"
"	padding: 1px;\n"
"	\n"
"}\n"
"#FileCheckBody QCheckBox::indicator:checked{\n"
"	background-color:white;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.FileCheckBody.setFrameShape(QFrame.StyledPanel)
        self.FileCheckBody.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_15 = QVBoxLayout(self.FileCheckBody)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(14, -1, 9, 14)

        self.verticalLayout.addWidget(self.FileCheckBody)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)


        self.verticalLayout_2.addWidget(self.FolderCheck)


        self.horizontalLayout_4.addWidget(self.LeftSide)

        self.RightSide = QFrame(self.Body)
        self.RightSide.setObjectName(u"RightSide")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.RightSide.sizePolicy().hasHeightForWidth())
        self.RightSide.setSizePolicy(sizePolicy2)
        self.RightSide.setMaximumSize(QSize(0, 16777215))
        self.RightSide.setFrameShape(QFrame.StyledPanel)
        self.RightSide.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.RightSide)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.RightSide)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.frame)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy2.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy2)
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_11)
        self.verticalLayout_5.setSpacing(4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 0, 0, 5)
        self.label_5 = QLabel(self.frame_11)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"QLabel{\n"
"	font: 700 14pt \"Comic Sans MS\";\n"
"	color: rgb(255, 255, 255);\n"
"	padding: 2px;\n"
"}")

        self.verticalLayout_5.addWidget(self.label_5, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.frame_13 = QFrame(self.frame_11)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy1.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy1)
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_13)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.frame_13)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 20, 415))
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.OldFileList = QFrame(self.scrollAreaWidgetContents_2)
        self.OldFileList.setObjectName(u"OldFileList")
        self.OldFileList.setStyleSheet(u"QLabel{\n"
"	font: 600 11pt \"Open Sans SemiBold\";\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.OldFileList.setFrameShape(QFrame.StyledPanel)
        self.OldFileList.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.OldFileList)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")

        self.verticalLayout_9.addWidget(self.OldFileList)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_7.addWidget(self.scrollArea_2)


        self.verticalLayout_5.addWidget(self.frame_13)


        self.horizontalLayout_7.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.frame)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_12)
        self.verticalLayout_6.setSpacing(4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 5, 5)
        self.label_4 = QLabel(self.frame_12)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"QLabel{\n"
"	font: 700 14pt \"Comic Sans MS\";\n"
"	color: rgb(255, 255, 255);\n"
"	padding: 2px;\n"
"}")

        self.verticalLayout_6.addWidget(self.label_4, 0, Qt.AlignHCenter)

        self.frame_14 = QFrame(self.frame_12)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy1.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy1)
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_14)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_3 = QScrollArea(self.frame_14)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 20, 415))
        self.verticalLayout_10 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.NewFileList = QFrame(self.scrollAreaWidgetContents_3)
        self.NewFileList.setObjectName(u"NewFileList")
        self.NewFileList.setStyleSheet(u"#NewFileList QTextEdit{\n"
"	font: 600 10pt \"Open Sans SemiBold\";\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid white;\n"
"	border-radius: 15px;\n"
"	padding: 2px;\n"
"}")
        self.NewFileList.setFrameShape(QFrame.StyledPanel)
        self.NewFileList.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.NewFileList)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(9, 9, 9, 9)

        self.verticalLayout_10.addWidget(self.NewFileList)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_8.addWidget(self.scrollArea_3)


        self.verticalLayout_6.addWidget(self.frame_14)


        self.horizontalLayout_7.addWidget(self.frame_12)


        self.verticalLayout_11.addWidget(self.frame)

        self.frame_2 = QFrame(self.RightSide)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.StartRename = QPushButton(self.frame_2)
        self.StartRename.setObjectName(u"StartRename")
        self.StartRename.setMinimumSize(QSize(150, 0))
        self.StartRename.setLayoutDirection(Qt.LeftToRight)
        self.StartRename.setStyleSheet(u"QPushButton{\n"
"	border: 1px solid white;\n"
"	font: 11pt \"Nexa Heavy\";\n"
"	color: Black;\n"
"	padding: 6px;\n"
"	border-radius: 10px;\n"
"	background: rgb(46, 210, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	border: 2px solid Black;\n"
"	font: 700 13pt \"Comic Sans MS\";\n"
"	color: rgb(255, 255, 255);\n"
"	background: black;\n"
"	padding: 3px;\n"
"\n"
"}")

        self.verticalLayout_12.addWidget(self.StartRename)


        self.verticalLayout_11.addWidget(self.frame_2)


        self.horizontalLayout_4.addWidget(self.RightSide)


        self.verticalLayout_4.addWidget(self.Body)

        self.frame_6 = QFrame(self.centralwidget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(5, 5, 7, 5)
        self.frame_10 = QFrame(self.frame_6)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy2.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy2)
        self.frame_10.setMinimumSize(QSize(0, 0))
        self.frame_10.setMaximumSize(QSize(16777215, 16777215))
        self.frame_10.setStyleSheet(u"\n"
"QLabel{\n"
"	font: 500 8pt \"Open Sans SemiBold\";\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.Report = QLabel(self.frame_10)
        self.Report.setObjectName(u"Report")
        font1 = QFont()
        font1.setFamilies([u"Open Sans SemiBold"])
        font1.setPointSize(8)
        font1.setWeight(QFont.Medium)
        font1.setItalic(False)
        self.Report.setFont(font1)

        self.horizontalLayout_11.addWidget(self.Report, 0, Qt.AlignLeft)

        self.Status = QLabel(self.frame_10)
        self.Status.setObjectName(u"Status")
        sizePolicy2.setHeightForWidth(self.Status.sizePolicy().hasHeightForWidth())
        self.Status.setSizePolicy(sizePolicy2)
        self.Status.setLayoutDirection(Qt.LeftToRight)
        self.Status.setWordWrap(False)

        self.horizontalLayout_11.addWidget(self.Status, 0, Qt.AlignLeft)


        self.horizontalLayout_8.addWidget(self.frame_10)

        self.sizeGrip = QFrame(self.frame_6)
        self.sizeGrip.setObjectName(u"sizeGrip")
        self.sizeGrip.setMaximumSize(QSize(15, 15))
        self.sizeGrip.setStyleSheet(u"QFrame{\n"
"	background-color: white;\n"
"	border: 2px solid white;\n"
"	padding: 2px;\n"
"}")
        self.sizeGrip.setFrameShape(QFrame.StyledPanel)
        self.sizeGrip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.sizeGrip)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_8 = QLabel(self.sizeGrip)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_12.addWidget(self.label_8)


        self.horizontalLayout_8.addWidget(self.sizeGrip)


        self.verticalLayout_4.addWidget(self.frame_6)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Rename App", None))
        self.Minimize.setText("")
        self.FullScreen.setText("")
        self.Close.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Folder Location", None))
        self.FolderLocation.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Past Your Folder Location", None))
        self.CheckFolder.setText(QCoreApplication.translate("MainWindow", u"Check Folder", None))
        self.RenameBtn.setText(QCoreApplication.translate("MainWindow", u"Rename", None))
        self.OpenFolder.setText(QCoreApplication.translate("MainWindow", u"Open Folder", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Total Files Found :", None))
        self.FileCount.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Pin.setText(QCoreApplication.translate("MainWindow", u"Pin", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Select Files To Rename", None))
        self.SelectAllFile.setText(QCoreApplication.translate("MainWindow", u"All File", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Old File Name", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"New File Name", None))
        self.StartRename.setText(QCoreApplication.translate("MainWindow", u"Start Renaming", None))
        self.Report.setText(QCoreApplication.translate("MainWindow", u"Report: ", None))
        self.Status.setText(QCoreApplication.translate("MainWindow", u"Give Folder Location & Click \"Check Folder\"", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

