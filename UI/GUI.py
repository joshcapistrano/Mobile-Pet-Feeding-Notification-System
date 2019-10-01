# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sample.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import time
from time import sleep
import datetime
import text_test
from datetime import timedelta
import threading
import json
import sys
import os

# <+ Change this to the RPi project path +>
PROJECT_DIR ="/home/pi/Documents/capstone_33"
# PROJECT_DIR ="/Users/capis/Documents/Rutgers/Capstone/capstone_33"
BLUETOOTH_DIR = os.path.join(PROJECT_DIR, "bluetooth")
UI_DIR = os.path.join(PROJECT_DIR, "UI")
LIGHTSTRIP_DIR = os.path.join(PROJECT_DIR, "light_strip")

sys.path.append(LIGHTSTRIP_DIR)
from LightStrip import LightStrip

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.file_name = os.path.join(UI_DIR, 'settings.json')
        self.settings = self.load_file(self.file_name)

        self.meals_fed = {'breakfast':False, 'dinner':False}

        self.notification_sent = {'breakfast':False, 'dinner':False,}

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(649, 483)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(40, 40, 571, 331))
        self.groupBox.setObjectName("groupBox")
        
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(60, 40, 161, 51))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 180, 101, 31))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(360, 40, 161, 51))
        self.pushButton_3.setObjectName("pushButton_3")

        self.listWidget = QtWidgets.QListWidget(self.groupBox)
        self.listWidget.setGeometry(QtCore.QRect(10, 100, 261, 71))
        self.listWidget.setObjectName("listWidget")

        self.listWidget_2 = QtWidgets.QListWidget(self.groupBox)
        self.listWidget_2.setGeometry(QtCore.QRect(320, 100, 241, 71))
        self.listWidget_2.setObjectName("listWidget_2")

        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(10, 310, 141, 17))
        self.checkBox.setObjectName("checkBox")

        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(390, 180, 101, 31))
        self.pushButton_4.setObjectName("pushButton_4")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 649, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.blt_connect_button = QtWidgets.QPushButton(self.groupBox)
        self.blt_connect_button.setGeometry(QtCore.QRect(300, 260, 100, 30))
        self.blt_connect_button.setObjectName("blt_connect_button")

        self.blt_done_button = QtWidgets.QPushButton(self.groupBox)
        self.blt_done_button.setGeometry(QtCore.QRect(300, 295, 100, 30))
        self.blt_done_button.setObjectName("blt_done_button")

        self.blt_label = QtWidgets.QLabel(self.groupBox)
        self.blt_label.setGeometry(QtCore.QRect(450, 280, 120, 50))
        self.blt_label.setObjectName("blt_label")
        self.blt_label.setText("")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.breakfast)

        self.pushButton_3.clicked.connect(self.dinner)

        self.pushButton.clicked.connect(self.addItemB)
        self.pushButton_3.clicked.connect(self.addItemD)

        self.pushButton_2.clicked.connect(self.undoButtonBreakfast)
        self.pushButton_4.clicked.connect(self.undoButtonDinner)

        self.checkBox.clicked.connect(self.textNotif)

        self.blt_connect_button.clicked.connect(self.blue_tooth_connect)
        self.blt_done_button.clicked.connect(self.blue_tooth_done)

        self.stop_thread = False

        self.check_state()

    def breakfast(self):
        date = datetime.datetime.now()
        print("Fed breakfast at " , date)

    def dinner(self):
        date = datetime.datetime.now()
        print("Fed dinner at " , date)

    def addItemB(self):
        self.listWidget.clear()
        date = datetime.datetime.now()
        date_string = date.strftime('%I:%M:%S - %b/%d/%Y')
        i = 0
        if i==0:
            self.listWidget.addItem("Fed Breakfast at: ")
            self.listWidget.addItem(date_string)
            self.meals_fed['breakfast'] = True
            self.state = LightStrip.firstHalfGreen()
            i = 1
        else:
            self.listWidget.clear()
            self.listWidget.addItem("Pet has already been fed.")
        nextday = date.replace(hour = 23, minute = 59, second = 59)
        if date > nextday:
            i = 0

    def addItemD(self):
        self.listWidget_2.clear()
        date = datetime.datetime.now()
        date_string = date.strftime('%I:%M:%S - %b/%d/%Y')
        self.listWidget_2.addItem("Fed Dinner at:")
        self.listWidget_2.addItem(date_string)
        self.meals_fed['dinner'] = True
        self.state = LightStrip.secondHalfGreen()

    def errorFeed1(self):
        self.listWidget.clear()
        print("Pet has already been fed breakfast!")

    def errorFeed2(self):
        self.listWidget.clear()
        print("Pet has already been fed dinner!")

    def alarm(self):
        stop = False
        while stop == False:
            rn = datetime.datetime.now().time()
            if rn >= "09:00:00.000000":
                self.listWidget.clear()
                self.listWidget.addItem("PET NEEDS TO BE FED BREAKFAST.")
                stop = True
            if rn >= "21:19:00.000000":
                self.listWidget.clear()
                self.listWidget.addItem("PET NEEDS TO BE FED DINNER.")
                stop = True

    def undoButton(self):
        now = datetime.datetime.now()
        morning1 = now.replace(hour = 0 , minute = 0, second = 0)
        morning2 = now.replace(hour = 11, minute = 59, second = 0)
        afternoon1 = now.replace(hour = 12, minute = 0, second = 0)
        afternoon2 = now.replace(hour = 23, minute = 59, second = 0)
        print(now)
        print(morning1)
        print(morning2)
        print(now > afternoon1 and now < afternoon2 )
        if now > moring1 and now < moring2:
            self.listWidget.clear()
            self.listWidget.addItem("Action has been undone.")
        elif now > afternoon1 and now < afternoon2:
            print("1")
            self.listWidget_2.clear()
            self.listWidget_2.addItem("Action has been undone.")

    def undoButtonBreakfast(self):
        self.listWidget.clear()
        self.listWidget.addItem("Action has been undone.")
        self.meals_fed['breakfast'] = False
        self.state = LightStrip.clearFirstHalf()

    def undoButtonDinner(self):
        self.listWidget_2.clear()
        self.listWidget_2.addItem("Action has been undone.")
        self.meals_fed['dinner'] = False
        self.state = LightStrip.clearSecondHalf()
        

    def sendText(self):
        text_test.text(self.settings['emails'])

    def textNotif(self):
        i = True
        if self.checkBox.isChecked() == True:
            print("Checked")
            I1 = input('Set Alarm Time: ')  # Makes it easy to set the alarm.
            if len(I1) > 3:  # The time needs to be 4 numbers long with no semicolon e.g. 0730
                hour1 = I1[0:2]  # seperrates the hour from the minutes
                minute1 = I1[2:]  # seperrates the minutes from the hours
                print ('Alarm set for: %s:%s' % (hour1,minute1))  # confirms the set time
                

                now = datetime.datetime.now()
                hournow = now.hour
                minnow = now.minute
                if int(hournow) == int (hour1) and int(minnow) == int(minute1):
                    print ('ALARM!' ) # this is a substitute for a buzzer or a beeper
                    text_test.text()
                    i = False
                sleep (1)
        else:
            print("Not sending notifications.")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Pet Feeding Notification System"))
        self.pushButton.setText(_translate("MainWindow", "Fed Breakfast"))
        self.pushButton_2.setText(_translate("MainWindow", "Undo"))
        self.pushButton_3.setText(_translate("MainWindow", "Fed Dinner"))
        self.checkBox.setText(_translate("MainWindow", "Notifications"))
        self.pushButton_4.setText(_translate("MainWindow", "Undo"))
        self.blt_connect_button.setText(_translate("MainWindow", "Connect"))
        self.blt_done_button.setText(_translate("MainWindow", "Done"))


    def print_settings(self):
        print("notification time: ", self.settings['notification_time'])
        print("b hour: ", self.settings['breakfast_hour'])
        print("b min ", self.settings['breakfast_minute'])
        print("d hour ", self.settings['dinner_hour'])
        print("d min ", self.settings['dinner_minute'])
        print("emails: ", self.settings['emails'])

    def load_file(self,filename):
        with open(filename, 'r') as f:
            settings = json.load(f)
        return settings

    def blue_tooth_connect(self):
        LightStrip.allBlue()
        self.print_settings()
        self.blt_label.setText("Bluetooth enabled...")
        self.stop_thread = False
        self.thread = threading.Thread(target=self.thread_funct)
        self.thread.start()

    def blue_tooth_done(self):
        LightStrip.clear()
        LightStrip.setState(self.state)
        self.blt_label.setText("Done")
        self.stop_thread = True
        self.settings = self.load_file(self.file_name)
        self.print_settings()

    def thread_funct(self):
        # exec(open('./mock_bt.py').read())
        exec(open(os.path.join(BLUETOOTH_DIR, 'rfcomm-server.py'), 'r').read())

    def check_state(self):
        threading.Timer(2.0, self.check_state).start()
        self.current_time = datetime.datetime.now()
        self.breakfast_time = self.current_time.replace(hour=self.settings['breakfast_hour'], minute=self.settings['breakfast_minute'])
        self.breakfast_notification_time = self.breakfast_time + timedelta(minutes = self.settings['notification_time'])

        self.dinner_time = self.current_time.replace(hour=self.settings['dinner_hour'], minute=self.settings['dinner_minute'])
        self.dinner_notification_time = self.dinner_time + timedelta(minutes = self.settings['notification_time'])
        
        if self.meals_fed['breakfast'] == False and self.current_time>self.breakfast_time:
            ''' Turn on light '''
            LightStrip.firstHalfRed()
            print('time to eat breakfast lol')
            self.listWidget.clear()
            self.listWidget.addItem("PET NEEDS TO BE FED BREAKFAST.")
            if self.current_time>self.breakfast_notification_time and self.notification_sent['breakfast']==False:
                ''' send notification '''
                self.sendText()
                self.notification_sent['breakfast']=True
        elif self.meals_fed['dinner'] == False and self.current_time>self.dinner_time:
            '''Turn on light'''
            LightStrip.firstHalfRed()
            self.listWidget_2.clear()
            self.liseWidget_2.addItem("PET NEEDS TO BE FED DINNER")
            if self.current_time>self.dinner_notification_time and self.notification_sent['dinner']==False:
                '''send notification'''
                self.sendText()
                print("Sent text")
                self.notification_sent['dinner'] == True

            



if __name__ == "__main__":
    LightStrip.clear()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

