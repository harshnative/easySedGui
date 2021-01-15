# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SED.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys 
import os 
sys.path.append(os.path.join(os.path.dirname(__file__), '.'))
from PyQt5 import QtCore, QtGui, QtWidgets
import time
from SED import ED, GlobalMethods
import pyperclip
from tkinter import filedialog
from tkinter import *

class GlobalData:
        sedObj = ED()
        file_filePath = None
        file_destPath = None

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1020, 606)
        MainWindow.setMinimumSize(QtCore.QSize(1020, 0))
        MainWindow.setMaximumSize(QtCore.QSize(1020, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 510, 1001, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.stringButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.stringButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"border-style: solid;\n"
"border-color: rgb(0, 0, 0);\n"
"border-width: 2px;\n"
"padding: 16px;")
        self.stringButton.setObjectName("stringButton")
        self.horizontalLayout_2.addWidget(self.stringButton)
        self.fileButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.fileButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"border-style: solid;\n"
"border-color: rgb(0, 0, 0);\n"
"border-width: 2px;\n"
"padding: 16px;")
        self.fileButton.setObjectName("fileButton")
        self.horizontalLayout_2.addWidget(self.fileButton)
        self.folderButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.folderButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"border-style: solid;\n"
"border-color: rgb(0, 0, 0);\n"
"border-width: 2px;\n"
"padding: 16px;")
        self.folderButton.setObjectName("folderButton")






        # password buttons
        self.horizontalLayout_2.addWidget(self.folderButton)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 420, 1001, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.passwordPin = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.passwordPin.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"padding: 8px;")
        self.passwordPin.setObjectName("passwordPin")
        self.horizontalLayout_3.addWidget(self.passwordPin)
        self.passwordInput = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.passwordInput.setMinimumSize(QtCore.QSize(0, 48))
        self.passwordInput.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"padding: 8px;")
        self.passwordInput.setText("")
        self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordInput.setObjectName("passwordInput")
        self.horizontalLayout_3.addWidget(self.passwordInput)
        self.PinInput = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.PinInput.setMinimumSize(QtCore.QSize(48, 48))
        self.PinInput.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"padding: 8px;")
        self.PinInput.setText("")
        self.PinInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PinInput.setObjectName("PinInput")
        self.horizontalLayout_3.addWidget(self.PinInput)
        self.encryptButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.encryptButton_2.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"padding: 8px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 0);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"width: 80px;")
        self.encryptButton_2.setObjectName("encryptButton_2")
        self.horizontalLayout_3.addWidget(self.encryptButton_2)








        # stack widget 1 
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 10, 981, 391))
        self.stackedWidget.setObjectName("stackedWidget")
        self.stringPage = QtWidgets.QWidget()
        self.stringPage.setObjectName("stringPage")
        self.textEdit = QtWidgets.QTextEdit(self.stringPage)
        self.textEdit.setGeometry(QtCore.QRect(70, 20, 512, 243))
        self.textEdit.setMaximumSize(QtCore.QSize(512, 16777215))
        self.textEdit.setStyleSheet("border-style: solid;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"border-width: 2px;\n"
"border-color: rgb(0, 0, 0);\n"
"margin: 16px;")
        self.textEdit.setObjectName("textEdit")
        self.decryptButton = QtWidgets.QPushButton(self.stringPage)
        self.decryptButton.setGeometry(QtCore.QRect(610, 180, 261, 64))
        self.decryptButton.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"padding: 16px;\n"
"background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 87 14pt \"Arial Black\";")
        self.decryptButton.setObjectName("decryptButton")
        self.encryptButton = QtWidgets.QPushButton(self.stringPage)
        self.encryptButton.setGeometry(QtCore.QRect(610, 30, 261, 64))
        self.encryptButton.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"padding: 16px;\n"
"color: rgb(255, 255, 255);\n"
"font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(255, 0, 0);")
        self.encryptButton.setObjectName("encryptButton")
        self.textBrowser = QtWidgets.QTextBrowser(self.stringPage)
        self.textBrowser.setGeometry(QtCore.QRect(20, 270, 781, 101))
        self.textBrowser.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.textBrowser.setObjectName("textBrowser")
        self.encryptButton_3 = QtWidgets.QPushButton(self.stringPage)
        self.encryptButton_3.setGeometry(QtCore.QRect(810, 270, 141, 91))
        self.encryptButton_3.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"padding: 16px;\n"
"color: rgb(255, 255, 255);\n"
"font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(0, 170, 0);")
        self.encryptButton_3.setObjectName("encryptButton_3")
        self.stackedWidget.addWidget(self.stringPage)











        # file page
        self.FilePage = QtWidgets.QWidget()
        self.FilePage.setObjectName("FilePage")
        self.pathInputFile = QtWidgets.QLineEdit(self.FilePage)
        self.pathInputFile.setGeometry(QtCore.QRect(350, 150, 301, 61))
        self.pathInputFile.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.pathInputFile.setObjectName("pathInputFile")
        self.validateFile = QtWidgets.QPushButton(self.FilePage)
        self.validateFile.setGeometry(QtCore.QRect(350, 220, 621, 41))
        self.validateFile.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"color: rgb(255, 255, 255);\n"
"font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(0, 170, 0);")
        self.validateFile.setObjectName("validateFile")
        self.orEnterFile = QtWidgets.QLabel(self.FilePage)
        self.orEnterFile.setGeometry(QtCore.QRect(350, 120, 621, 31))
        self.orEnterFile.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.orEnterFile.setObjectName("orEnterFile")
        self.destInputFile = QtWidgets.QLineEdit(self.FilePage)
        self.destInputFile.setGeometry(QtCore.QRect(660, 150, 311, 61))
        self.destInputFile.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.destInputFile.setObjectName("destInputFile")
        self.textBrowserFile = QtWidgets.QTextBrowser(self.FilePage)
        self.textBrowserFile.setGeometry(QtCore.QRect(10, 10, 321, 371))
        self.textBrowserFile.setObjectName("textBrowserFile")
        self.selectDestFile = QtWidgets.QPushButton(self.FilePage)
        self.selectDestFile.setGeometry(QtCore.QRect(700, 40, 271, 61))
        self.selectDestFile.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"padding: 16px;\n"
"color: rgb(255, 255, 255);\n"
"font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(85, 0, 255);")
        self.selectDestFile.setObjectName("selectDestFile")
        self.selectFileFile = QtWidgets.QPushButton(self.FilePage)
        self.selectFileFile.setGeometry(QtCore.QRect(350, 40, 271, 61))
        self.selectFileFile.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"padding: 16px;\n"
"color: rgb(255, 255, 255);\n"
"font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(85, 0, 255);")
        self.selectFileFile.setObjectName("selectFileFile")
        self.chooseFile = QtWidgets.QLabel(self.FilePage)
        self.chooseFile.setGeometry(QtCore.QRect(350, 0, 621, 31))
        self.chooseFile.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.chooseFile.setObjectName("chooseFile")
        self.encryptButton_4 = QtWidgets.QPushButton(self.FilePage)
        self.encryptButton_4.setGeometry(QtCore.QRect(350, 310, 211, 68))
        self.encryptButton_4.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"padding: 16px;\n"
"color: rgb(255, 255, 255);\n"
"font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(255, 0, 0);")
        self.encryptButton_4.setObjectName("encryptButton_4")
        self.decryptButton_3 = QtWidgets.QPushButton(self.FilePage)
        self.decryptButton_3.setGeometry(QtCore.QRect(770, 310, 211, 68))
        self.decryptButton_3.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"padding: 16px;\n"
"background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 87 14pt \"Arial Black\";")
        self.decryptButton_3.setObjectName("decryptButton_3")
        self.stackedWidget.addWidget(self.FilePage)
        self.textBrowserFile.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n")














        # folder page
        self.folderPage = QtWidgets.QWidget()
        self.folderPage.setObjectName("folderPage")
        self.textBrowserFolder = QtWidgets.QTextBrowser(self.folderPage)
        self.textBrowserFolder.setGeometry(QtCore.QRect(10, 10, 321, 371))
        self.textBrowserFolder.setObjectName("textBrowserFolder")
        self.decryptButton_4 = QtWidgets.QPushButton(self.folderPage)
        self.decryptButton_4.setGeometry(QtCore.QRect(770, 310, 211, 68))
        self.decryptButton_4.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"padding: 16px;\n"
"background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 87 14pt \"Arial Black\";")
        self.decryptButton_4.setObjectName("decryptButton_4")
        self.orEnterFile_2 = QtWidgets.QLabel(self.folderPage)
        self.orEnterFile_2.setGeometry(QtCore.QRect(350, 120, 621, 31))
        self.orEnterFile_2.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.orEnterFile_2.setObjectName("orEnterFile_2")
        self.chooseFile_2 = QtWidgets.QLabel(self.folderPage)
        self.chooseFile_2.setGeometry(QtCore.QRect(350, 0, 621, 31))
        self.chooseFile_2.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.chooseFile_2.setObjectName("chooseFile_2")
        self.selectDestFile_2 = QtWidgets.QPushButton(self.folderPage)
        self.selectDestFile_2.setGeometry(QtCore.QRect(700, 40, 271, 61))
        self.selectDestFile_2.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"padding: 16px;\n"
"color: rgb(255, 255, 255);\n"
"font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(85, 0, 255);")
        self.selectDestFile_2.setObjectName("selectDestFile_2")
        self.pathInputFile_2 = QtWidgets.QLineEdit(self.folderPage)
        self.pathInputFile_2.setGeometry(QtCore.QRect(350, 150, 301, 61))
        self.pathInputFile_2.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.pathInputFile_2.setObjectName("pathInputFile_2")
        self.destInputFile_2 = QtWidgets.QLineEdit(self.folderPage)
        self.destInputFile_2.setGeometry(QtCore.QRect(660, 150, 311, 61))
        self.destInputFile_2.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.destInputFile_2.setObjectName("destInputFile_2")
        self.encryptButton_5 = QtWidgets.QPushButton(self.folderPage)
        self.encryptButton_5.setGeometry(QtCore.QRect(350, 310, 211, 68))
        self.encryptButton_5.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"padding: 16px;\n"
"color: rgb(255, 255, 255);\n"
"font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(255, 0, 0);")
        self.encryptButton_5.setObjectName("encryptButton_5")
        self.selectFileFile_2 = QtWidgets.QPushButton(self.folderPage)
        self.selectFileFile_2.setGeometry(QtCore.QRect(350, 40, 271, 61))
        self.selectFileFile_2.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"padding: 16px;\n"
"color: rgb(255, 255, 255);\n"
"font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(85, 0, 255);")
        self.selectFileFile_2.setObjectName("selectFileFile_2")
        self.validateFile_2 = QtWidgets.QPushButton(self.folderPage)
        self.validateFile_2.setGeometry(QtCore.QRect(350, 220, 621, 41))
        self.validateFile_2.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"color: rgb(255, 255, 255);\n"
"font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(0, 170, 0);")
        self.validateFile_2.setObjectName("validateFile_2")
        self.stackedWidget.addWidget(self.folderPage)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)






        # making string as default screen
        self.stackedWidget.setCurrentWidget(self.stringPage)
        self.stringButton.setStyleSheet("background-color: rgb(200, 200, 200);\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"border-style: solid;\n"
"border-color: rgb(0, 0, 0);\n"
"border-width: 2px;\n"
"padding: 16px;")







        # bottom buttons
        self.stringButton.clicked.connect(self.stringButtonPress)
        self.fileButton.clicked.connect(self.fileButtonPress)
        self.folderButton.clicked.connect(self.dirButtonPress)






        # password view button
        self.encryptButton_2.clicked.connect(self.passViewButton)
        







        # string page button
        self.encryptButton.pressed.connect(self.encryptButtonPress)
        self.encryptButton.released.connect(self.encryptButtonPressR)

        self.decryptButton.pressed.connect(self.decryptButtonPress)
        self.decryptButton.released.connect(self.decryptButtonPressR)

        self.encryptButton_3.pressed.connect(self.copyToClipboard)
        self.encryptButton_3.released.connect(self.copyToClipboardR)





        # file page button
        self.selectFileFile.pressed.connect(self.fileSelect)
        self.selectFileFile.released.connect(self.fileSelectR)

        self.selectFileFile.pressed.connect(self.fileDestSelect)
        self.selectFileFile.released.connect(self.fileDestSelectR)

        self.validateFile.pressed.connect(self.validateFileFunc)
        self.validateFile.released.connect(self.validateFileFuncR)















    def validateFileFunc(self):
        self.validateFile.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"color: rgb(0, 0, 0);\n"
"font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(197, 197, 197);")

        filePathInputted = self.pathInputFile.text()
        destPathInputted = self.destInputFile.text()

        self.textBrowserFile.clear()

        if(not(os.path.isfile(filePathInputted))):
                self.textBrowserFile.setText("File path given is incorrect")
                self.textBrowserFile.append("\nRemember you don't have to press validate if you have already selected the path from buttons above")
                return

        
        if(not(os.path.isdir(destPathInputted))):
                self.textBrowserFile.setText("Dest path given is incorrect")
                self.textBrowserFile.append("\nRemember you don't have to press validate if you have already selected the path from buttons above")
                return

        GlobalData.file_filePath = (filePathInputted)
        GlobalData.file_destPath = (destPathInputted)
        self.textBrowserFile.append("Paths validated...\n\nReady for encryption or decryption")


    def validateFileFuncR(self):
        time.sleep(0.5)
        self.validateFile.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"color: rgb(255, 255, 255);\n"
"font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(0, 170, 0);")














    def fileSelect(self):
        self.selectFileFile.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"padding: 16px;\n"
"color: rgb(0, 0, 0);\n"
"font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(197, 197, 197);")

        self.textBrowserFile.clear()
        self.textBrowserFile.append("Select files from file explorer opened")
        root = Tk()
        filePath = filedialog.askopenfilenames()
        self.textBrowserFile.append("\nFiles added for encrption = " + str(len(filePath)))
        if(len(filePath) != 0):
                GlobalData.file_filePath = filePath
        root.destroy()
        if(GlobalData.file_destPath == None):
                self.textBrowserFile.append("\nNow select the path to destination by clicking on destination path button")
        else:
                self.textBrowserFile.append("\nReady for encryption or decryption")


        



    def fileSelectR(self):
            self.selectFileFile.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"padding: 16px;\n"
"color: rgb(255, 255, 255);\n"
"font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(85, 0, 255);")











    def fileDestSelect(self):
        self.selectDestFile.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"padding: 16px;\n"
"color: rgb(0, 0, 0);\n"
"font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(197, 197, 197);")

        self.textBrowserFile.clear()
        self.textBrowserFile.append("Select destination path from file explorer opened")
        root = Tk()
        filePath = filedialog.askdirectory()
        try:
                self.textBrowserFile.append("\nfiles will be exported to " + str(filePath[0]))
                GlobalData.file_destPath = filePath
        except Exception:
                self.textBrowserFile.append("\nCould not load the destination path try again..")
        root.destroy()
        if(GlobalData.file_filePath == None):
                self.textBrowserFile.append("\nNow select the path to file by clicking on file path button")
        else:
                self.textBrowserFile.append("\nReady for encryption or decryption")


        



    def fileDestSelectR(self):
            self.selectDestFile.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"padding: 16px;\n"
"color: rgb(255, 255, 255);\n"
"font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(85, 0, 255);")








    def passViewButton(self):
        if(self.encryptButton_2.text() == "View"):

                self.encryptButton_2.setStyleSheet("border-color: rgb(0, 0, 0);\n"
        "border-style: solid;\n"
        "border-width: 1px;\n"
        "padding: 8px;\n"
        "color: rgb(255, 255, 255);\n"
        "background-color: rgb(255, 0, 0);\n"
        "font: 12pt \"MS Shell Dlg 2\";\n"
        "width: 80px;")

                self.encryptButton_2.setText("Hide")

                self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Normal)
                self.PinInput.setEchoMode(QtWidgets.QLineEdit.Normal)

        else:
                self.encryptButton_2.setStyleSheet("border-color: rgb(0, 0, 0);\n"
        "border-style: solid;\n"
        "border-width: 1px;\n"
        "padding: 8px;\n"
        "color: rgb(255, 255, 255);\n"
        "background-color: rgb(0, 170, 0);\n"
        "font: 12pt \"MS Shell Dlg 2\";\n"
        "width: 80px;")

                self.encryptButton_2.setText("View")

                self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)
                self.PinInput.setEchoMode(QtWidgets.QLineEdit.Password)
        





    def copyToClipboard(self):
        self.encryptButton_3.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"padding: 16px;\n"
"color: rgb(255, 255, 255);\n"
"font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(185, 185, 185);")
        pyperclip.copy(self.textBrowser.toPlainText())
        pyperclip.paste()
        self.encryptButton_3.setText("Copied!")

    def copyToClipboardR(self):
        time.sleep(0.75)
        self.encryptButton_3.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"padding: 16px;\n"
"color: rgb(255, 255, 255);\n"
"font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(0, 170, 0);")
        self.encryptButton_3.setText("Copy")









    def encryptButtonPress(self):
        self.encryptButton.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"padding: 16px;\n"
"color: rgb(255, 255, 255);\n"
"font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(185, 185, 185);")

        if(len(self.PinInput.text()) == 0):
                try:
                        GlobalData.sedObj.setPassword_Pin(self.passwordInput.text() , "123456")
                except Exception as e:
                        self.textBrowser.clear()
                        self.textBrowser.setPlainText("password input error: " + str(e))
                        return
        else:
                try:
                        GlobalData.sedObj.setPassword_Pin(self.passwordInput.text() , self.PinInput.text())
                except Exception as e:
                        self.textBrowser.clear()
                        self.textBrowser.setPlainText("password input error: " + str(e))
                        return
                
        try:
                encText = GlobalData.sedObj.encrypter(self.textEdit.toPlainText())
                self.textBrowser.clear()
                self.textBrowser.setPlainText(encText)
        except Exception as e:
                self.textBrowser.clear()
                self.textBrowser.setPlainText("Could not encrypt. Error: " + str(e))
                


    def encryptButtonPressR(self):
        time.sleep(0.1)
        self.encryptButton.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"padding: 16px;\n"
"color: rgb(255, 255, 255);\n"
"font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(255, 0, 0);")










    def decryptButtonPress(self):
        self.decryptButton.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"padding: 16px;\n"
"color: rgb(255, 255, 255);\n"
"font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(185, 185, 185);")

        if(len(self.PinInput.text()) == 0):
                try:
                        GlobalData.sedObj.setPassword_Pin(self.passwordInput.text() , "123456")
                except Exception as e:
                        self.textBrowser.clear()
                        self.textBrowser.setPlainText("password input error: " + str(e))
                        return
        else:
                try:
                        GlobalData.sedObj.setPassword_Pin(self.passwordInput.text() , self.PinInput.text())
                except Exception as e:
                        self.textBrowser.clear()
                        self.textBrowser.setPlainText("password input error: " + str(e))
                        return 

        try:                
                decText = GlobalData.sedObj.decrypter(self.textEdit.toPlainText())
                self.textBrowser.clear()
                self.textBrowser.setPlainText(decText)
        except Exception as e:
                self.textBrowser.clear()
                self.textBrowser.setPlainText("Could not decrypt. Error: " + str(e))

    def decryptButtonPressR(self):
        time.sleep(0.1)
        self.decryptButton.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"padding: 16px;\n"
"color: rgb(255, 255, 255);\n"
"font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(0, 0, 255);")

















    # function to simulate the string button press
    def stringButtonPress(self):
        self.stackedWidget.setCurrentWidget(self.stringPage)
        self.stringButton.setStyleSheet("background-color: rgb(200, 200, 200);\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"border-style: solid;\n"
"border-color: rgb(0, 0, 0);\n"
"border-width: 2px;\n"
"padding: 16px;")

        self.fileButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"border-style: solid;\n"
"border-color: rgb(0, 0, 0);\n"
"border-width: 2px;\n"
"padding: 16px;")

        self.folderButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"border-style: solid;\n"
"border-color: rgb(0, 0, 0);\n"
"border-width: 2px;\n"
"padding: 16px;")

        GlobalData.file_filePath = None 
        GlobalData.file_destPath = None
















    # function to simulate the file button press
    def fileButtonPress(self):
        self.stackedWidget.setCurrentWidget(self.FilePage)
        self.fileButton.setStyleSheet("background-color: rgb(200, 200, 200);\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"border-style: solid;\n"
"border-color: rgb(0, 0, 0);\n"
"border-width: 2px;\n"
"padding: 16px;")

        self.stringButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"border-style: solid;\n"
"border-color: rgb(0, 0, 0);\n"
"border-width: 2px;\n"
"padding: 16px;")

        self.folderButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"border-style: solid;\n"
"border-color: rgb(0, 0, 0);\n"
"border-width: 2px;\n"
"padding: 16px;")

        self.textBrowserFile.clear()
        self.textBrowserFile.setPlainText("Choose the path to the file and destination")

        GlobalData.file_filePath = None 
        GlobalData.file_destPath = None

    











    # function to simulate the dir button press
    def dirButtonPress(self):
        self.stackedWidget.setCurrentWidget(self.folderPage)
        self.folderButton.setStyleSheet("background-color: rgb(200, 200, 200);\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"border-style: solid;\n"
"border-color: rgb(0, 0, 0);\n"
"border-width: 2px;\n"
"padding: 16px;")

        self.fileButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"border-style: solid;\n"
"border-color: rgb(0, 0, 0);\n"
"border-width: 2px;\n"
"padding: 16px;")

        self.stringButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"border-style: solid;\n"
"border-color: rgb(0, 0, 0);\n"
"border-width: 2px;\n"
"padding: 16px;")

        GlobalData.file_filePath = None 
        GlobalData.file_destPath = None












    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.stringButton.setText(_translate("MainWindow", "String"))
        self.fileButton.setText(_translate("MainWindow", "File"))
        self.folderButton.setText(_translate("MainWindow", "Folder"))
        self.passwordPin.setText(_translate("MainWindow", "Enter Password & Pin : "))
        self.passwordInput.setPlaceholderText(_translate("MainWindow", "Password"))
        self.PinInput.setPlaceholderText(_translate("MainWindow", "Pin"))
        self.encryptButton_2.setText(_translate("MainWindow", "View"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "Enter String Here ... "))
        self.decryptButton.setText(_translate("MainWindow", "Decrypt"))
        self.encryptButton.setText(_translate("MainWindow", "Encrypt"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.textBrowser.setPlaceholderText(_translate("MainWindow", "Output Here ..."))
        self.encryptButton_3.setText(_translate("MainWindow", "Copy"))
        self.pathInputFile.setPlaceholderText(_translate("MainWindow", "Path to File"))
        self.validateFile.setText(_translate("MainWindow", "Validate"))
        self.orEnterFile.setText(_translate("MainWindow", "Or Enter the path to the File !"))
        self.destInputFile.setPlaceholderText(_translate("MainWindow", "Path to Destination"))
        self.selectDestFile.setText(_translate("MainWindow", "Destination Path"))
        self.selectFileFile.setText(_translate("MainWindow", "File Path"))
        self.chooseFile.setText(_translate("MainWindow", "Choose the File Path and Destination Path by clicking Below :"))
        self.encryptButton_4.setText(_translate("MainWindow", "Encrypt"))
        self.decryptButton_3.setText(_translate("MainWindow", "Decrypt"))
        self.decryptButton_4.setText(_translate("MainWindow", "Decrypt"))
        self.orEnterFile_2.setText(_translate("MainWindow", "Or Enter the path to the Folder !"))
        self.chooseFile_2.setText(_translate("MainWindow", "Choose the Folder Path and Destination Path by clicking Below :"))
        self.selectDestFile_2.setText(_translate("MainWindow", "Destination Path"))
        self.pathInputFile_2.setPlaceholderText(_translate("MainWindow", "Path to Folder"))
        self.destInputFile_2.setPlaceholderText(_translate("MainWindow", "Path to Destination"))
        self.encryptButton_5.setText(_translate("MainWindow", "Encrypt"))
        self.selectFileFile_2.setText(_translate("MainWindow", "Folder Path"))
        self.validateFile_2.setText(_translate("MainWindow", "Validate"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

