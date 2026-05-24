# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QCheckBox
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import *
from PySide6.QtCore import QCoreApplication, Qt

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow
import os
import time


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Software Part
        self.TotalFile = 0
        self.programPath = os.getcwd()
        self.IMGFolder = r''
        self.FileList = []
        self.newNameList = []
        self.FileSelection = False
        self.RenamedCount = 0

        # Remove Title Bar
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)

        self.ui.centralwidget.setGraphicsEffect(self.shadow)

        self.setWindowIcon(QtGui.QIcon(u"icon/logo.png"))
        self.setWindowTitle("Rename Software")
        QSizeGrip(self.ui.sizeGrip)

        # Window App Control
        self.ui.Minimize.clicked.connect(lambda: self.showMinimized())
        self.ui.Close.clicked.connect(lambda: self.close())
        self.ui.FullScreen.clicked.connect(self.restoreMaximize)
        self.ui.Pin.clicked.connect(self.pinTop)

        # CheckFolder
        self.ui.CheckFolder.clicked.connect(self.checkFolder)
        self.ui.OpenFolder.clicked.connect(self.DirectOpenFolder)
        self.ui.SelectAllFile.stateChanged.connect(self.selectAll)

        #  Rename Control
        self.ui.RenameBtn.clicked.connect(self.RenameStep)
        self.ui.StartRename.clicked.connect(self.RenameNow)

    def RenameNow(self):
        History = fr'{self.ui.FolderLocation.text()}\\Rename_File_History.txt'

        backup = open(f"{History}", 'a')
        backup.write(f'FileLocation = " {self.ui.FolderLocation.text()}\n')
        backup.write('Rename History (Delete this file if you dont need \'Rename Backup\')\nSn : Old Name : New Name\n')
        backup.write('-------------------------------------------------------------\n')
        ChangedName = self.findChildren(QTextEdit)
        count = 1
        for i in ChangedName:
            for j in self.FileList:
                if i.objectName() == str(j[0]):
                    index = int(i.objectName())
                    OldName = self.FileList[index][1]
                    ext = OldName.split('.')[1]
                    if ext != 'jpg':
                        ext = 'py'
                    NewName = i.toPlainText()
                    # if len(OldName.split('.')) == 2:
                    #     NewName = NewName + f'.{ext}'
                    # else:
                    #     NewName = NewName
                    if len(OldName.split('.')) == 2:
                        Name = NewName + str(count) + f'.{ext}'
                        NewName = Name
                    else:
                        NewName = NewName
                    print(
                        f"i: {i} | j:{j} | i.objectName(): {i.objectName()} | OldName: {OldName} | NewName: {NewName}")
                    pathN = self.IMGFolder + f'\\{NewName}'
                    pathO = self.IMGFolder + f'\\{OldName}'
                    text = f"{self.RenamedCount + 1} : {OldName} : {NewName}\n"
                    print(pathO)
                    print(pathN)
                    try:
                        os.rename(pathO, pathN)
                        backup.write(text)
                        self.RenamedCount += 1
                        self.ui.Status.setText(f'{self.RenamedCount}. {OldName} is Renamed as {NewName}.')
                    except Exception as e:
                        self.ui.Status.setText(f"Error Occurred in {OldName}")
                        pass
                    time.sleep(1)
                    count += 1

        backup.write('------------------------\'Created By - Rabib\'------------------------\n\n\n\n\n')
        backup.close()
        self.ui.Status.setText(f'{self.RenamedCount} Files are Renamed. All Rename History are saved in'
                               f' {History}.')

    def DirectOpenFolder(self):
        location = self.ui.FolderLocation.text()
        if location:
            os.startfile(location)

    def AddSelectItem(self, Index, Filename):
        self.file = QCheckBox(self.ui.FileCheckBody)
        self.file.setObjectName(Index)
        self.ui.verticalLayout_15.addWidget(self.file)
        self.file.setText(QCoreApplication.translate("MainWindow", Filename, None))

    def selectAll(self, state):
        CheckBoxList = self.findChildren(QCheckBox)
        for checkbox in range(2, len(CheckBoxList)):
            CheckBoxList[checkbox].setChecked(state == 2)

    def clearLayout(self, layout):
        for i in reversed(range(layout.count())):
            layout.itemAt(i).widget().setParent(None)

    def checkFolder(self):
        if len(self.FileList) != 0:
            self.clearLayout(self.ui.verticalLayout_15)
            self.clearLayout(self.ui.verticalLayout_13)
            self.clearLayout(self.ui.verticalLayout_14)
            self.ui.SelectAllFile.setChecked(False)
            self.FileList.clear()
            self.TotalFile = 0

        location = self.ui.FolderLocation.text()
        self.IMGFolder = fr'{location}'
        if location:
            self.ui.Status.setText("Please Wait... Scanning All File")
            Folder = os.listdir(location)
            for sl, File in enumerate(Folder):
                if len(File.split(".")) >= 2:
                    self.AddSelectItem(str(sl), File)
                    self.FileList.append([sl, File])
                    self.TotalFile += 1
            self.ui.FileCount.setText(str(self.TotalFile))
            self.FileSelection = True
            self.ui.Status.setText("Select File To Rename, Then Click 'Rename' Button.")
        else:
            self.ui.Status.setText('No Location Given')

    def SeparateSelectedFile(self):
        CheckBoxList = self.findChildren(QCheckBox)
        checked = []
        # checked.Remove('')
        for i in range(2, len(CheckBoxList)):
            if CheckBoxList[i].objectName() == 'PinTop':
                pass
            fileIndex = int(CheckBoxList[i].objectName())
            if CheckBoxList[i].isChecked():
                FileName = self.FileList[fileIndex][1]
                checked.append([fileIndex, FileName])
        return checked

    def RenameStep(self):
        if self.FileSelection:
            self.ui.Status.setText("Change File Name From 'New Rename Box'. If there is Extension Keep then It")
            self.resize(900, self.height())
            self.ui.RightSide.setMinimumWidth(500)
            x = self.SeparateSelectedFile()
            for i, name in enumerate(x):
                # print('101- ', name)
                self.addTOChange(i + 1, name[0], name[1])
        else:
            self.ui.Status.setText("Give Folder Location & Click 'Check Folder' Button")

    def addTOChange(self, sn, Index, name):
        # Add to old List
        FileName = f"{sn} {name}"
        # print('A2C-125- ', FileName)
        self.File = QLabel(self.ui.OldFileList)
        self.File.setObjectName(str(Index))
        self.File.setWordWrap(True)
        self.ui.verticalLayout_13.addWidget(self.File, 0, Qt.AlignTop)
        self.File.setText(QCoreApplication.translate("MainWindow", FileName, None))

        # Add To Change list
        self.RenamePlace = QTextEdit(self.ui.NewFileList)
        self.RenamePlace.setObjectName(str(Index))
        self.ui.verticalLayout_14.addWidget(self.RenamePlace)
        self.RenamePlace.setAcceptRichText(False)
        fName = name.split('.')
        if len(fName) == 2:
            self.RenamePlace.setMarkdown(QCoreApplication.translate("MainWindow", fName[0], None))
        else:
            NameFound = name
            # CheckName = fName[:-1]
            # NameFound = str('.'.join(CheckName))
            # print('check: ', NameFound)
            self.RenamePlace.setMarkdown(QCoreApplication.translate("MainWindow", NameFound, None))

    def pinTop(self, state):
        if state:
            self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
            self.show()
            self.ui.Status.setText(f'Pinned On Top Window ')

        else:
            self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint, False)
            self.show()
            self.ui.Status.setText(f'Unpinned On Top Window ')
        self.ui.Status.setWordWrap(False)

    def restoreMaximize(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
        self.dragPos = event.globalPosition().toPoint()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
