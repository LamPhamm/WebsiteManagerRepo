# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WebManagerDesign.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import webbrowser as web
import datetime
import mysql.connector
from tkinter import *
from tkinter import messagebox


#Connect to the database
db=mysql.connector.connect(
host="localhost",
user="Lam",
passwd="waterBell$73",
database="appData"
)
#Cursor that executes statements
myCursor=db.cursor()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MainBackgroundLabel = QtWidgets.QLabel(self.centralwidget)
        self.MainBackgroundLabel.setGeometry(QtCore.QRect(0, 0, 640, 480))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.MainBackgroundLabel.setFont(font)
        self.MainBackgroundLabel.setText("")
        self.MainBackgroundLabel.setPixmap(QtGui.QPixmap("mainBackground.jpg"))
        self.MainBackgroundLabel.setScaledContents(True)
        self.MainBackgroundLabel.setObjectName("MainBackgroundLabel")
        self.PennStateFolderLabel = QtWidgets.QLabel(self.centralwidget)
        self.PennStateFolderLabel.setGeometry(QtCore.QRect(260, 70, 120, 190))
        self.PennStateFolderLabel.setText("")
        self.PennStateFolderLabel.setPixmap(QtGui.QPixmap("PennStateFolder2.jpg"))
        self.PennStateFolderLabel.setScaledContents(True)
        self.PennStateFolderLabel.setObjectName("PennStateFolderLabel")
        self.outlookLabel = QtWidgets.QLabel(self.centralwidget)
        self.outlookLabel.setGeometry(QtCore.QRect(40, 80, 60, 60))
        self.outlookLabel.setText("")
        self.outlookLabel.setPixmap(QtGui.QPixmap("outlook.png"))
        self.outlookLabel.setScaledContents(True)
        self.outlookLabel.setObjectName("outlookLabel")
        self.personalFolderLabel = QtWidgets.QLabel(self.centralwidget)
        self.personalFolderLabel.setGeometry(QtCore.QRect(40, 70, 120, 190))
        self.personalFolderLabel.setText("")
        self.personalFolderLabel.setPixmap(QtGui.QPixmap("wallpaperFolder.jpg"))
        self.personalFolderLabel.setScaledContents(True)
        self.personalFolderLabel.setObjectName("personalFolderLabel")
        self.OtherFolderLabel = QtWidgets.QLabel(self.centralwidget)
        self.OtherFolderLabel.setGeometry(QtCore.QRect(470, 70, 120, 190))
        self.OtherFolderLabel.setText("")
        self.OtherFolderLabel.setPixmap(QtGui.QPixmap("chelseaOtherFolder.jpg"))
        self.OtherFolderLabel.setScaledContents(True)
        self.OtherFolderLabel.setObjectName("OtherFolderLabel")
        self.personalTextLabel = QtWidgets.QLabel(self.centralwidget)
        self.personalTextLabel.setGeometry(QtCore.QRect(50, 280, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Harlow Solid Italic")
        font.setPointSize(18)
        font.setItalic(True)
        self.personalTextLabel.setFont(font)
        self.personalTextLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.personalTextLabel.setObjectName("personalTextLabel")
        self.pennStateTextLabel = QtWidgets.QLabel(self.centralwidget)
        self.pennStateTextLabel.setGeometry(QtCore.QRect(260, 280, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Harlow Solid Italic")
        font.setPointSize(18)
        font.setItalic(True)
        self.pennStateTextLabel.setFont(font)
        self.pennStateTextLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.pennStateTextLabel.setObjectName("pennStateTextLabel")
        self.otherTextLabel = QtWidgets.QLabel(self.centralwidget)
        self.otherTextLabel.setGeometry(QtCore.QRect(510, 280, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Harlow Solid Italic")
        font.setPointSize(18)
        font.setItalic(True)
        self.otherTextLabel.setFont(font)
        self.otherTextLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.otherTextLabel.setObjectName("otherTextLabel")
        self.homeTextLabel = QtWidgets.QLabel(self.centralwidget)
        self.homeTextLabel.setGeometry(QtCore.QRect(220, 10, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Harlow Solid Italic")
        font.setPointSize(24)
        font.setItalic(True)
        self.homeTextLabel.setFont(font)
        self.homeTextLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.homeTextLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.homeTextLabel.setObjectName("homeTextLabel")
        self.homeButtonLabel = QtWidgets.QLabel(self.centralwidget)
        self.homeButtonLabel.setGeometry(QtCore.QRect(570, 410, 60, 60))
        self.homeButtonLabel.setText("")
        self.homeButtonLabel.setPixmap(QtGui.QPixmap("homeButton2.png"))
        self.homeButtonLabel.setScaledContents(True)
        self.homeButtonLabel.setObjectName("homeButtonLabel")
        self.youtubeLabel = QtWidgets.QLabel(self.centralwidget)
        self.youtubeLabel.setGeometry(QtCore.QRect(160, 80, 60, 60))
        self.youtubeLabel.setText("")
        self.youtubeLabel.setPixmap(QtGui.QPixmap("youtubeButton.png"))
        self.youtubeLabel.setScaledContents(True)
        self.youtubeLabel.setOpenExternalLinks(False)
        self.youtubeLabel.setObjectName("youtubeLabel")
        self.dateLabel = QtWidgets.QLabel(self.centralwidget)
        self.dateLabel.setGeometry(QtCore.QRect(560, 0, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Harlow Solid Italic")
        font.setPointSize(12)
        font.setItalic(True)
        self.dateLabel.setFont(font)
        self.dateLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.dateLabel.setObjectName("dateLabel")
        self.timeLabel = QtWidgets.QLabel(self.centralwidget)
        self.timeLabel.setGeometry(QtCore.QRect(560, 30, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Harlow Solid Italic")
        font.setPointSize(12)
        font.setItalic(True)
        self.timeLabel.setFont(font)
        self.timeLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.timeLabel.setText("")
        self.timeLabel.setObjectName("timeLabel")
        self.googleCalLabel = QtWidgets.QLabel(self.centralwidget)
        self.googleCalLabel.setGeometry(QtCore.QRect(280, 80, 60, 60))
        self.googleCalLabel.setText("")
        self.googleCalLabel.setPixmap(QtGui.QPixmap("googleCalendar.png"))
        self.googleCalLabel.setScaledContents(True)
        self.googleCalLabel.setOpenExternalLinks(False)
        self.googleCalLabel.setObjectName("googleCalLabel")
        self.lionpathLabel = QtWidgets.QLabel(self.centralwidget)
        self.lionpathLabel.setGeometry(QtCore.QRect(160, 80, 60, 60))
        self.lionpathLabel.setText("")
        self.lionpathLabel.setPixmap(QtGui.QPixmap("lionPathButton.jpeg"))
        self.lionpathLabel.setScaledContents(True)
        self.lionpathLabel.setOpenExternalLinks(False)
        self.lionpathLabel.setObjectName("lionpathLabel")
        self.bulletinLabel = QtWidgets.QLabel(self.centralwidget)
        self.bulletinLabel.setGeometry(QtCore.QRect(280, 80, 60, 60))
        self.bulletinLabel.setText("")
        self.bulletinLabel.setPixmap(QtGui.QPixmap("computerScienceButton.jpg"))
        self.bulletinLabel.setScaledContents(True)
        self.bulletinLabel.setOpenExternalLinks(False)
        self.bulletinLabel.setObjectName("bulletinLabel")
        self.canvasLabel = QtWidgets.QLabel(self.centralwidget)
        self.canvasLabel.setGeometry(QtCore.QRect(40, 80, 60, 60))
        self.canvasLabel.setText("")
        self.canvasLabel.setPixmap(QtGui.QPixmap("canvasButton.png"))
        self.canvasLabel.setScaledContents(True)
        self.canvasLabel.setOpenExternalLinks(False)
        self.canvasLabel.setObjectName("canvasLabel")
        self.typingLabel = QtWidgets.QLabel(self.centralwidget)
        self.typingLabel.setGeometry(QtCore.QRect(160, 80, 60, 60))
        self.typingLabel.setText("")
        self.typingLabel.setPixmap(QtGui.QPixmap("typingButton.jpg"))
        self.typingLabel.setScaledContents(True)
        self.typingLabel.setOpenExternalLinks(False)
        self.typingLabel.setObjectName("typingLabel")
        self.chelseaLabel = QtWidgets.QLabel(self.centralwidget)
        self.chelseaLabel.setGeometry(QtCore.QRect(40, 80, 60, 60))
        self.chelseaLabel.setText("")
        self.chelseaLabel.setPixmap(QtGui.QPixmap("chelseaButton.jpg"))
        self.chelseaLabel.setScaledContents(True)
        self.chelseaLabel.setOpenExternalLinks(False)
        self.chelseaLabel.setObjectName("chelseaLabel")
        self.docsLabel = QtWidgets.QLabel(self.centralwidget)
        self.docsLabel.setGeometry(QtCore.QRect(40, 200, 60, 60))
        self.docsLabel.setText("")
        self.docsLabel.setPixmap(QtGui.QPixmap("googledocButton.png"))
        self.docsLabel.setScaledContents(True)
        self.docsLabel.setOpenExternalLinks(False)
        self.docsLabel.setObjectName("docsLabel")
        self.googleLabel = QtWidgets.QLabel(self.centralwidget)
        self.googleLabel.setGeometry(QtCore.QRect(520, 80, 60, 60))
        self.googleLabel.setText("")
        self.googleLabel.setPixmap(QtGui.QPixmap("googleButton.png"))
        self.googleLabel.setScaledContents(True)
        self.googleLabel.setOpenExternalLinks(False)
        self.googleLabel.setObjectName("googleLabel")
        self.sheetsLabel = QtWidgets.QLabel(self.centralwidget)
        self.sheetsLabel.setGeometry(QtCore.QRect(160, 200, 60, 60))
        self.sheetsLabel.setText("")
        self.sheetsLabel.setPixmap(QtGui.QPixmap("googlesheetsButton.png"))
        self.sheetsLabel.setScaledContents(True)
        self.sheetsLabel.setOpenExternalLinks(False)
        self.sheetsLabel.setObjectName("sheetsLabel")
        self.twitterLabel = QtWidgets.QLabel(self.centralwidget)
        self.twitterLabel.setGeometry(QtCore.QRect(400, 80, 60, 60))
        self.twitterLabel.setText("")
        self.twitterLabel.setPixmap(QtGui.QPixmap("twitterButton.png"))
        self.twitterLabel.setScaledContents(True)
        self.twitterLabel.setOpenExternalLinks(False)
        self.twitterLabel.setObjectName("twitterLabel")
        self.linkedinLabel = QtWidgets.QLabel(self.centralwidget)
        self.linkedinLabel.setGeometry(QtCore.QRect(280, 200, 60, 60))
        self.linkedinLabel.setText("")
        self.linkedinLabel.setPixmap(QtGui.QPixmap("linkedinButton.png"))
        self.linkedinLabel.setScaledContents(True)
        self.linkedinLabel.setOpenExternalLinks(False)
        self.linkedinLabel.setObjectName("linkedinLabel")
        self.reccomendedTextLabel = QtWidgets.QLabel(self.centralwidget)
        self.reccomendedTextLabel.setGeometry(QtCore.QRect(30, 350, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Harlow Solid Italic")
        font.setPointSize(18)
        font.setItalic(True)
        self.reccomendedTextLabel.setFont(font)
        self.reccomendedTextLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.reccomendedTextLabel.setObjectName("reccomendedTextLabel")
        self.viewLabel = QtWidgets.QLabel(self.centralwidget)
        self.viewLabel.setGeometry(QtCore.QRect(220, 360, 40, 40))
        self.viewLabel.setText("")
        self.viewLabel.setPixmap(QtGui.QPixmap("view.png"))
        self.viewLabel.setScaledContents(True)
        self.viewLabel.setOpenExternalLinks(False)
        self.viewLabel.setObjectName("viewLabel")
        self.refreshLabel = QtWidgets.QLabel(self.centralwidget)
        self.refreshLabel.setGeometry(QtCore.QRect(220, 420, 40, 40))
        self.refreshLabel.setText("")
        self.refreshLabel.setPixmap(QtGui.QPixmap("refresh.png"))
        self.refreshLabel.setScaledContents(True)
        self.refreshLabel.setOpenExternalLinks(False)
        self.refreshLabel.setObjectName("refreshLabel")
        self.MainBackgroundLabel.raise_()
        self.outlookLabel.raise_()
        self.personalTextLabel.raise_()
        self.pennStateTextLabel.raise_()
        self.otherTextLabel.raise_()
        self.homeTextLabel.raise_()
        self.homeButtonLabel.raise_()
        self.youtubeLabel.raise_()
        self.dateLabel.raise_()
        self.timeLabel.raise_()
        self.googleCalLabel.raise_()
        self.lionpathLabel.raise_()
        self.bulletinLabel.raise_()
        self.canvasLabel.raise_()
        self.typingLabel.raise_()
        self.chelseaLabel.raise_()
        self.docsLabel.raise_()
        self.googleLabel.raise_()
        self.sheetsLabel.raise_()
        self.twitterLabel.raise_()
        self.linkedinLabel.raise_()
        self.PennStateFolderLabel.raise_()
        self.OtherFolderLabel.raise_()
        self.personalFolderLabel.raise_()
        self.reccomendedTextLabel.raise_()
        self.viewLabel.raise_()
        self.refreshLabel.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #Action events declaration
        #Changing the backgrounds
        self.PennStateFolderLabel.mousePressEvent = self.changeBackgroundPennState
        self.personalFolderLabel.mousePressEvent = self.changeBackgroundPersonal
        self.OtherFolderLabel.mousePressEvent = self.changeBackgroundOther
        self.homeButtonLabel.mousePressEvent = self.changeBackgroundMain

        #Hover over actions when mouse is over folders and apps
        #Folders-enter events
        self.PennStateFolderLabel.enterEvent = self.makePennStateFolderLarger
        self.personalFolderLabel.enterEvent = self.makePersonalFolderLarger
        self.OtherFolderLabel.enterEvent = self.makeOtherFolderLarger

        #Folders-leave events
        self.PennStateFolderLabel.leaveEvent = self.makePennStateFolderSmaller
        self.personalFolderLabel.leaveEvent = self.makePersonalFolderSmaller
        self.OtherFolderLabel.leaveEvent = self.makeOtherFolderSmaller

        #Home button enter and leave events
        self.homeButtonLabel.enterEvent = self.makeHomeButtonLarger
        self.homeButtonLabel.leaveEvent = self.makeHomeButtonSmaller

        #View button enter and leave events
        self.viewLabel.enterEvent = self.makeViewLarger
        self.viewLabel.leaveEvent = self.makeViewSmaller

        #Refresh button enter and leave events
        self.refreshLabel.enterEvent = self.makeRefreshLarger
        self.refreshLabel.leaveEvent = self.makeRefreshSmaller

        #Apps-enter events
        self.outlookLabel.enterEvent = self.makeOutlookButtonLarger
        self.youtubeLabel.enterEvent = self.makeYoutubeButtonLarger
        self.googleCalLabel.enterEvent = self.makeGoogleCalButtonLarger
        self.canvasLabel.enterEvent = self.makeCanvasLarger
        self.lionpathLabel.enterEvent = self.makeLionpathLarger
        self.bulletinLabel.enterEvent = self.makeBulletinLarger
        self.chelseaLabel.enterEvent = self.makeChelseaLarger
        self.typingLabel.enterEvent = self.makeTypingLarger
        self.twitterLabel.enterEvent = self.makeTwitterButtonLarger
        self.googleLabel.enterEvent = self.makeGoogleButtonLarger
        self.docsLabel.enterEvent = self.makeDocsButtonLarger
        self.sheetsLabel.enterEvent = self.makeSheetsButtonLarger
        self.linkedinLabel.enterEvent = self.makeLinkedinButtonLarger

        #Apps-leave events
        self.outlookLabel.leaveEvent = self.makeOutlookButtonSmaller
        self.youtubeLabel.leaveEvent = self.makeYoutubeButtonSmaller
        self.googleCalLabel.leaveEvent = self.makeGoogleCalButtonSmaller
        self.canvasLabel.leaveEvent = self.makeCanvasSmaller
        self.lionpathLabel.leaveEvent = self.makeLionpathSmaller
        self.bulletinLabel.leaveEvent = self.makeBulletinSmaller
        self.chelseaLabel.leaveEvent = self.makeChelseaSmaller
        self.typingLabel.leaveEvent = self.makeTypingmaller
        self.twitterLabel.leaveEvent = self.makeTwitterButtonSmaller
        self.googleLabel.leaveEvent = self.makeGoogleButtonSmaller
        self.docsLabel.leaveEvent = self.makeDocsButtonSmaller
        self.sheetsLabel.leaveEvent = self.makeSheetsButtonSmaller
        self.linkedinLabel.leaveEvent = self.makeLinkedinButtonSmaller

        #Hide the home button initially along with ALL the apps-except for reccomended apps(see code below)
        self.homeButtonLabel.setHidden(True)
        self.outlookLabel.setHidden(True)
        self.youtubeLabel.setHidden(True)
        self.googleCalLabel.setHidden(True)
        self.canvasLabel.setHidden(True)
        self.lionpathLabel.setHidden(True)
        self.bulletinLabel.setHidden(True)
        self.chelseaLabel.setHidden(True)
        self.typingLabel.setHidden(True)
        self.googleLabel.setHidden(True)
        self.twitterLabel.setHidden(True)
        self.docsLabel.setHidden(True)
        self.sheetsLabel.setHidden(True)
        self.linkedinLabel.setHidden(True)

        #Opening links
        self.outlookLabel.mousePressEvent = self.openOutlook
        self.youtubeLabel.mousePressEvent = self.openYoutube
        self.googleCalLabel.mousePressEvent = self.openGoogleCal
        self.canvasLabel.mousePressEvent = self.openCanvas
        self.lionpathLabel.mousePressEvent = self.openLionpath
        self.bulletinLabel.mousePressEvent = self.openBulletin
        self.chelseaLabel.mousePressEvent = self.openChelsea
        self.typingLabel.mousePressEvent = self.openTyping
        self.twitterLabel.mousePressEvent = self.openTwitter
        self.googleLabel.mousePressEvent = self.openGoogle
        self.docsLabel.mousePressEvent = self.openDocs
        self.sheetsLabel.mousePressEvent = self.openSheets
        self.linkedinLabel.mousePressEvent = self.openLinkedin

        #Other buttons
        self.viewLabel.mousePressEvent=self.showAllAppClicks
        self.refreshLabel.mousePressEvent=self.refreshTable

        #Initially, display the reccomended apps
        #Get the highest clicked apps
        highestClickApps=self.getHighestClickApps()

        #Move the highest clicked apps 
        global highestClickedAppsLabelObjs #Make the list global so other functions can use the lists 
        highestClickedAppsLabelObjs=self.moveReccomendedApps(highestClickApps)

        global locationsDict
        #Stores the label objects and their initial locations(hard coded coordinates, since label.x() and label.y() continuously update)
        locationsDict={self.outlookLabel:(40,80), #Personal apps
        self.youtubeLabel:(160,80),
        self.googleLabel:(520,80),
        self.twitterLabel:(400,80),
        self.docsLabel:(40,200),
        self.sheetsLabel:(160,200),
        self.linkedinLabel:(280,200),
        self.googleCalLabel:(280,80),

        self.canvasLabel:(40,80),                   #Penn State apps
        self.lionpathLabel:(160,80),
        self.bulletinLabel:(280,80),

        self.chelseaLabel:(40,80),                  #Other apps
        self.typingLabel:(160,80)}

        #Display the current date and time
        currentDate = datetime.datetime.now()
        self.dateLabel.setText(currentDate.strftime("%x"))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Lam's WindowManager"))
        self.personalTextLabel.setText(_translate("MainWindow", "Personal"))
        self.pennStateTextLabel.setText(_translate("MainWindow", "Penn State"))
        self.otherTextLabel.setText(_translate("MainWindow", "Other"))
        self.homeTextLabel.setText(_translate("MainWindow", "Home"))
        self.dateLabel.setText(_translate("MainWindow", "Date"))
        self.reccomendedTextLabel.setText(_translate("MainWindow", "Reccomended"))

    def changeBackgroundPersonal(self,event):
        #Change the background of the window
        self.MainBackgroundLabel.setPixmap(QtGui.QPixmap("personalBackground.jpg"))
        #Change the heading of the page
        self.homeTextLabel.setText("Personal")
        #Show the personal apps
        mainBool=False
        self.hideOrUnhidePersonalApps(mainBool)
        #Hide the folders,text, and other things by calling this function defined down below
        mainBool=True
        self.hideOrUnhideFoldersAndText(mainBool)
        #Show the home button
        self.homeButtonLabel.setHidden(False)
        
        personalObjs=[self.outlookLabel,self.youtubeLabel,self.googleLabel,self.googleCalLabel,self.twitterLabel,self.docsLabel,
        self.sheetsLabel,self.linkedinLabel]

        #Move the personal apps to their original locations
        for obj in personalObjs:
            #Each value in the dictionary is a tuple consisting of (x,y)
            xCoord=locationsDict[obj][0]
            yCoord=locationsDict[obj][1]
            obj.setGeometry(QtCore.QRect(xCoord, yCoord, 60, 60))
        
        #Iterate through each app in the list of highest clicked apps
        for labelObj in highestClickedAppsLabelObjs:
            #Hide the app if it's not a personal app
            if labelObj not in personalObjs:
                labelObj.setHidden(True)
        
    def changeBackgroundPennState(self,event):
        #Change the background of the window
        self.MainBackgroundLabel.setPixmap(QtGui.QPixmap("PennStateBackground.jpg"))
        #Change the heading of the page
        self.homeTextLabel.setText("Penn State")
        #Show the penn state apps
        mainBool=False
        self.hideOrUnhidePennStateApps(mainBool)
        #Hide the folders and text by calling this function defined down below
        mainBool=True
        self.hideOrUnhideFoldersAndText(mainBool)
        #Show the home button
        self.homeButtonLabel.setHidden(False)

        pennStateObjs=[self.canvasLabel,self.lionpathLabel,self.bulletinLabel]
        #Move the penn state apps to their original locations
        for obj in pennStateObjs:
            #Each value in the dictionary is a tuple consisting of (x,y)
            xCoord=locationsDict[obj][0]
            yCoord=locationsDict[obj][1]
            obj.setGeometry(QtCore.QRect(xCoord, yCoord, 60, 60))

        #Iterate through each app in the list of highest clicked apps
        for labelObj in highestClickedAppsLabelObjs:
            #Hide the app if it's not a penn state app
            if labelObj not in pennStateObjs:
                labelObj.setHidden(True)
        

    def changeBackgroundOther(self,event):
        #Change the background of the window
        self.MainBackgroundLabel.setPixmap(QtGui.QPixmap("otherBackground.jpg"))
        #Change the heading of the page
        self.homeTextLabel.setText("Other")
        #Show the other apps
        mainBool=False
        self.hideOrUnhideOtherApps(mainBool)
        #Hide the folders and text by calling this function defined down below
        mainBool=True
        self.hideOrUnhideFoldersAndText(mainBool)
        #Show the home button
        self.homeButtonLabel.setHidden(False)

        otherObjs=[self.typingLabel,self.chelseaLabel]
        #Move the other apps to their original locations
        for obj in otherObjs:
            #Each value in the dictionary is a tuple consisting of (x,y)
            xCoord=locationsDict[obj][0]
            yCoord=locationsDict[obj][1]
            obj.setGeometry(QtCore.QRect(xCoord, yCoord, 60, 60))

        #Iterate through each app in the list of highest clicked apps
        for labelObj in highestClickedAppsLabelObjs:
            #Hide the app if it's not an other app
            if labelObj not in otherObjs:
                labelObj.setHidden(True)
        

    def changeBackgroundMain(self,event):
        #Change the background of the window
        self.MainBackgroundLabel.setPixmap(QtGui.QPixmap("mainBackground.jpg"))
        #Change the heading of the page
        self.homeTextLabel.setText("Home")
        #Unhide the folders and text by calling this function defined down below
        mainBool=False
        self.hideOrUnhideFoldersAndText(mainBool)
        #Hide the home button
        self.homeButtonLabel.setHidden(True)
        #Hide all the personal apps, pennstate apps, and other apps
        mainBool=True
        self.hideOrUnhidePersonalApps(mainBool)
        self.hideOrUnhidePennStateApps(mainBool)
        self.hideOrUnhideOtherApps(mainBool)

        #Get the highest clicked apps
        highestClickApps=self.getHighestClickApps()

        #Move the highest clicked apps 
        labelObjs=self.moveReccomendedApps(highestClickApps)

        #When modifying global variables, declare them as global too
        global highestClickedAppsLabelObjs
        highestClickedAppsLabelObjs=labelObjs


    #Opening links
    def openOutlook(self,event):
        web.open("https://outlook.office.com/mail/inbox/id/AAQkADViNTAzMTQxLThiMDctNDI5NS1hNGIzLTVlYjQ0YTEwYTA2YwAQANIHzZbt4fdDieYocxL5Oq8%3D", new=1)
        #Increment the clicks in the database by calling this function
        self.incrementClicks("Outlook")

    def openYoutube(self,event):
        web.open("https://www.youtube.com/",new=1)
        #Increment the clicks in the database by calling this function
        self.incrementClicks("Youtube")

    def openGoogleCal(self,event):
        web.open("https://calendar.google.com/calendar/u/0/r",new=1)
        #Increment the clicks in the database by calling this function
        self.incrementClicks("Google Calendar")

    def openCanvas(self,event):
        web.open("https://canvas.psu.edu/",new=1)
        #Increment the clicks in the database by calling this function
        self.incrementClicks("Canvas")

    def openLionpath(self,event):
        web.open("https://lionpathsupport.psu.edu/",new=1)
        #Increment the clicks in the database by calling this function
        self.incrementClicks("Lionpath")

    def openBulletin(self,event):
        web.open("https://bulletins.psu.edu/undergraduate/colleges/engineering/computer-science-bs/",new=1)
        #Increment the clicks in the database by calling this function
        self.incrementClicks("Bulletin")

    def openChelsea(self,event):
        web.open("https://www.chelseafc.com/en",new=1)
        #Increment the clicks in the database by calling this function
        self.incrementClicks("Chelsea")

    def openTyping(self,event):
        web.open("https://10fastfingers.com/typing-test/english",new=1)
        #Increment the clicks in the database by calling this function
        self.incrementClicks("Typing")

    def openTwitter(self,event):
        web.open("https://twitter.com/home",new=1)
        #Increment the clicks in the database by calling this function
        self.incrementClicks("Twitter")

    def openGoogle(self,event):
        web.open("https://www.google.com/",new=1)
        #Increment the clicks in the database by calling this function
        self.incrementClicks("Google")

    def openDocs(self,event):
        web.open("https://docs.google.com/document/u/0/",new=1)
        #Increment the clicks in the database by calling this function
        self.incrementClicks("Docs")

    def openSheets(self,event):
        web.open("https://docs.google.com/spreadsheets/u/0/",new=1)
        #Increment the clicks in the database by calling this function
        self.incrementClicks("Sheets")

    def openLinkedin(self,event):
        web.open("https://www.linkedin.com/in/lampham10/",new=1)
        #Increment the clicks in the database by calling this function
        self.incrementClicks("Linkedin")

    def incrementClicks(self,app):
        #Get the number of clicks currently in the database, store it in a variable
        selectStatement="SELECT appName,clicks FROM appHistory WHERE appName=%s"
        values=(app,)
        myCursor.execute(selectStatement,values)
        results=myCursor.fetchall() #Fetch all of the results

        clicks=None
        for row in results:
            clicks=row[1]

        #Increment the number of clicks by 1
        clicks+=1

        #Update the record
        updateStatement="UPDATE appHistory SET clicks=%s WHERE appName=%s"
        values=(clicks, app)
        myCursor.execute(updateStatement,values)
        db.commit() #Commit the change to the database

    
    def getHighestClickApps(self):
        #Get the 2 apps with the highest number of clicks
        selectStatement="SELECT appName,clicks FROM appHistory ORDER BY clicks DESC LIMIT 2"
        
        myCursor.execute(selectStatement)
        #Fetch the results from the query
        results=myCursor.fetchall()

        #Store the highest clicked apps in a list and return it
        highestClickApps=[]
        for row in results:
            highestClickApps.append(row[0])

        return highestClickApps

    #Also returns the locations of the previous apps
    def moveReccomendedApps(self,highestClickApps):
        #A dictionary that maps each column in the table to its corresponding label
        apps={"Outlook":self.outlookLabel,"Google":self.googleLabel,"Twitter":self.twitterLabel, "Youtube":self.youtubeLabel,
        "Docs":self.docsLabel,"Sheets":self.sheetsLabel,"Linkedin":self.linkedinLabel,"Google Calendar":self.googleCalLabel,
        "Canvas":self.canvasLabel,"Lionpath":self.lionpathLabel,"Bulletin":self.bulletinLabel,"Typing":self.typingLabel,
        "Chelsea":self.chelseaLabel}

        mainAppCoords=[] #Stores the coordinates of each app
        labelObjs=[] #Stores the object of each app
       
        #Iterate through the apps 
        for i,app in enumerate(highestClickApps):
            objLabel=apps[app] #Get the object label of the app
           
            #Get the coordinates of the app
            appXCoord,appYCoord,appWidth,appHeight,scaleCoord,scaleDimensions=self.getAppCoordinatesAndDimensions(objLabel)
            
            #Create the tuple of the coordinates and append to the list
            appCoords=(appXCoord,appYCoord)
            mainAppCoords.append(appCoords)
            labelObjs.append(objLabel)

            #Move the first app to the correct location(leftmost on the gui)
            if i==0:
                objLabel.setGeometry(QtCore.QRect(20, 400, 60, 60))
            #Move the second app to the correct location(towards the right of the first app)
            else:
                objLabel.setGeometry(QtCore.QRect(110, 400, 60, 60))

            #Unhide the apps from the main webpage to see reccomended apps(special case)
            objLabel.setHidden(False)

        return labelObjs

    def showAllAppClicks(self,event):
        #Select all of the columns from the table order by clicks from highest to lowest
        selectStatement="SELECT * FROM appHistory ORDER BY clicks DESC"
        myCursor.execute(selectStatement)
        results=myCursor.fetchall()
   
        giantString=''
        for result in results:
            giantString+=result[0] + '\t\t' + str(result[1]) + '\n'
            
        #Display the clicks in a message box
        Tk().wm_withdraw() #To hide the main window
        messagebox.showinfo('App Clicks',giantString)

    def refreshTable(self,event):
        #Update all of the clicks to be 0
        updateStatement="UPDATE appHistory SET clicks=%s"
        values=(0,)
        myCursor.execute(updateStatement,values)
        db.commit() #Commit the change to the database
        

    #Hiding folders and text when clicking folders
    def hideOrUnhideFoldersAndText(self,mainBool):
        self.PennStateFolderLabel.setHidden(mainBool)
        self.OtherFolderLabel.setHidden(mainBool)
        self.pennStateTextLabel.setHidden(mainBool)
        self.otherTextLabel.setHidden(mainBool)
        self.personalFolderLabel.setHidden(mainBool)
        self.personalTextLabel.setHidden(mainBool)
        self.dateLabel.setHidden(mainBool)
        self.reccomendedTextLabel.setHidden(mainBool)
        self.viewLabel.setHidden(mainBool) #view label button as well
        self.refreshLabel.setHidden(mainBool) #refresh label button as well

    #Hiding folders and text when clicking folders
    #Personal Apps
    def hideOrUnhidePersonalApps(self,mainBool):
        self.outlookLabel.setHidden(mainBool)
        self.youtubeLabel.setHidden(mainBool)
        self.googleCalLabel.setHidden(mainBool)
        self.twitterLabel.setHidden(mainBool)
        self.googleLabel.setHidden(mainBool)
        self.docsLabel.setHidden(mainBool)
        self.sheetsLabel.setHidden(mainBool)
        self.linkedinLabel.setHidden(mainBool)

    #Penn State Apps
    def hideOrUnhidePennStateApps(self,mainBool):
        self.canvasLabel.setHidden(mainBool)
        self.lionpathLabel.setHidden(mainBool)
        self.bulletinLabel.setHidden(mainBool)
    
    #Other Apps
    def hideOrUnhideOtherApps(self,mainBool):
        self.chelseaLabel.setHidden(mainBool)
        self.typingLabel.setHidden(mainBool)

    #Functions for making folders and apps larger when hovered
    #Folders
    def makeOtherFolderLarger(self,event):
        self.makeButtonLarger(self.OtherFolderLabel)

    def makeOtherFolderSmaller(self,event):
        self.makeButtonSmaller(self.OtherFolderLabel)

    def makePennStateFolderLarger(self,event):
        self.makeButtonLarger(self.PennStateFolderLabel)

    def makePennStateFolderSmaller(self,event):
        self.makeButtonSmaller(self.PennStateFolderLabel)

    def makePersonalFolderLarger(self,event):
        self.makeButtonLarger(self.personalFolderLabel)

    def makePersonalFolderSmaller(self,event):
        self.makeButtonSmaller(self.personalFolderLabel)

    #Home Button
    def makeHomeButtonLarger(self,event):
        self.makeButtonLarger(self.homeButtonLabel)

    def makeHomeButtonSmaller(self,event):
        self.makeButtonSmaller(self.homeButtonLabel)

    #Personal Apps
    #Outlook App
    def makeOutlookButtonLarger(self,event):
        self.makeButtonLarger(self.outlookLabel)

    def makeOutlookButtonSmaller(self,event):
        self.makeButtonSmaller(self.outlookLabel)

    #Youtube App
    def makeYoutubeButtonLarger(self,event):
        self.makeButtonLarger(self.youtubeLabel)

    def makeYoutubeButtonSmaller(self,event):
        self.makeButtonSmaller(self.youtubeLabel)

    #Google Calendar App
    def makeGoogleCalButtonLarger(self,event):
        self.makeButtonLarger(self.googleCalLabel)

    def makeGoogleCalButtonSmaller(self,event):
        self.makeButtonSmaller(self.googleCalLabel)

    #Twitter App
    def makeTwitterButtonLarger(self,event):
        self.makeButtonLarger(self.twitterLabel)

    def makeTwitterButtonSmaller(self,event):
        self.makeButtonSmaller(self.twitterLabel)

    #Google App
    def makeGoogleButtonLarger(self,event):
        self.makeButtonLarger(self.googleLabel)

    def makeGoogleButtonSmaller(self,event):
       self.makeButtonSmaller(self.googleLabel)

    #Docs App
    def makeDocsButtonLarger(self,event):
        self.makeButtonLarger(self.docsLabel)

    def makeDocsButtonSmaller(self,event):
       self.makeButtonSmaller(self.docsLabel)
    
    #Sheets App
    def makeSheetsButtonLarger(self,event):
        self.makeButtonLarger(self.sheetsLabel)

    def makeSheetsButtonSmaller(self,event):
        self.makeButtonSmaller(self.sheetsLabel)
    
    #Linkedin App
    def makeLinkedinButtonLarger(self,event):
        self.makeButtonLarger(self.linkedinLabel)

    def makeLinkedinButtonSmaller(self,event):
        self.makeButtonSmaller(self.linkedinLabel)
    
    #Penn State Apps
    #Canvas App
    def makeCanvasLarger(self,event):
        self.makeButtonLarger(self.canvasLabel)

    def makeCanvasSmaller(self,event):
        self.makeButtonSmaller(self.canvasLabel)

    #Lionpath App
    def makeLionpathLarger(self,event):
        self.makeButtonLarger(self.lionpathLabel)

    def makeLionpathSmaller(self,event):
        self.makeButtonSmaller(self.lionpathLabel)

    #Bulletin App
    def makeBulletinLarger(self,event):
        self.makeButtonLarger(self.bulletinLabel)

    def makeBulletinSmaller(self,event):
        self.makeButtonSmaller(self.bulletinLabel)

    #Other Apps
    #Chelsea App
    def makeChelseaLarger(self,event):
        self.makeButtonLarger(self.chelseaLabel)

    def makeChelseaSmaller(self,event):
        self.makeButtonSmaller(self.chelseaLabel)

    #Typing App
    def makeTypingLarger(self,event):
        self.makeButtonLarger(self.typingLabel)

    def makeTypingmaller(self,event):
        self.makeButtonSmaller(self.typingLabel)

    #Other Buttons
    #View Button
    def makeViewLarger(self,event):
        self.makeButtonLarger(self.viewLabel)

    def makeViewSmaller(self,event):
        self.makeButtonSmaller(self.viewLabel)
        
    #Refresh Button
    def makeRefreshLarger(self,event):
        self.makeButtonLarger(self.refreshLabel)

    def makeRefreshSmaller(self,event):
        self.makeButtonSmaller(self.refreshLabel)

    #Function for getting app coordinates and dimensions
    def getAppCoordinatesAndDimensions(self,labelObj):
        #Get the dimensions by using the labelObj parameter
        appXCoord=labelObj.x()
        appYCoord=labelObj.y()
        appWidth=labelObj.width()
        appHeight=labelObj.height()
        scaleCoord=10
        scaleDimensions=20

        return appXCoord,appYCoord,appWidth,appHeight,scaleCoord,scaleDimensions

    def makeButtonLarger(self,labelObj):
        #Call this function to get the coordinates, dimensions, and scales for the label passing in the label object
        appXCoord,appYCoord,appWidth,appHeight,scaleCoord,scaleDimensions=self.getAppCoordinatesAndDimensions(labelObj)

        #Shift location of app down and expand width and height
        labelObj.setGeometry(QtCore.QRect(appXCoord-scaleCoord, appYCoord-scaleCoord, appWidth+scaleDimensions, appHeight+scaleDimensions))
        labelObj.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

    def makeButtonSmaller(self,labelObj):
        #Call this function to get the coordinates, dimensions, and scales for the label
        appXCoord,appYCoord,appWidth,appHeight,scaleCoord,scaleDimensions=self.getAppCoordinatesAndDimensions(labelObj)

        #Shift app back to original location
        labelObj.setGeometry(QtCore.QRect(appXCoord+scaleCoord, appYCoord+scaleCoord, appWidth-scaleDimensions, appHeight-scaleDimensions))
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

