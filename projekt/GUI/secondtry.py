# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firsttry.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(884, 576)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.MaximizecheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.MaximizecheckBox.setObjectName("MaximizecheckBox")

        self.gridLayout.addWidget(self.MaximizecheckBox, 0, 3, 1, 1)

        self.StylesMenu = QtWidgets.QComboBox(self.centralwidget)
        self.StylesMenu.setObjectName("StylesMenu")

        self.gridLayout.addWidget(self.StylesMenu, 0, 4, 1, 1)

        self.QnAReverser = QtWidgets.QRadioButton(self.centralwidget)
        self.QnAReverser.setObjectName("QnAReverser")

        self.gridLayout.addWidget(self.QnAReverser, 1, 1, 1, 1)

        self.StartButton = QtWidgets.QPushButton(self.centralwidget)
        self.StartButton.setObjectName("StartButton")

        self.gridLayout.addWidget(self.StartButton, 2, 0, 1, 1)

        self.questionBox = QtWidgets.QTextBrowser(self.centralwidget)
        self.questionBox.setObjectName("questionBox")

        self.gridLayout.addWidget(self.questionBox, 2, 1, 3, 2)

        self.openGL = QtWidgets.QOpenGLWidget(self.centralwidget)
        self.openGL.setObjectName("openGL")

        self.gridLayout.addWidget(self.openGL, 2, 3, 3, 1)

        self.PauseButton = QtWidgets.QPushButton(self.centralwidget)
        self.PauseButton.setObjectName("PauseButton")

        self.gridLayout.addWidget(self.PauseButton, 3, 0, 1, 1)

        self.stopButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopButton.setObjectName("stopButton")

        self.gridLayout.addWidget(self.stopButton, 4, 0, 1, 1)

        self.questiontimeCounter = QtWidgets.QProgressBar(self.centralwidget)
        self.questiontimeCounter.setProperty("value", 24)
        self.questiontimeCounter.setObjectName("questiontimeCounter")

        self.gridLayout.addWidget(self.questiontimeCounter, 5, 1, 1, 2)

        self.answerBox = QtWidgets.QTextEdit(self.centralwidget)
        self.answerBox.setObjectName("answerBox")

        self.gridLayout.addWidget(self.answerBox, 6, 1, 1, 1)

        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")

        self.gridLayout.addWidget(self.progressBar, 7, 2, 1, 3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)

        self.menubar.setGeometry(QtCore.QRect(0, 0, 884, 21))

        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionEdit_dictionary = QtWidgets.QAction(MainWindow)
        self.actionEdit_dictionary.setObjectName("actionEdit_dictionary")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionwindowsvista = QtWidgets.QAction(MainWindow)
        self.actionwindowsvista.setObjectName("actionwindowsvista")
        self.actionPlastique = QtWidgets.QAction(MainWindow)
        self.actionPlastique.setObjectName("actionPlastique")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionEdit_dictionary)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Flash-korttiohjelma"))
        self.MaximizecheckBox.setText(_translate("MainWindow", "Maximize"))
        self.QnAReverser.setText(_translate("MainWindow", "Reverse questions/answers"))
        self.StartButton.setText(_translate("MainWindow", "Start"))
        self.PauseButton.setText(_translate("MainWindow", "Pause"))
        self.stopButton.setText(_translate("MainWindow", "Stop"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionEdit_dictionary.setText(_translate("MainWindow", "Edit dictionary"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionwindowsvista.setText(_translate("MainWindow", "windowsvista"))
        self.actionPlastique.setText(_translate("MainWindow", "Plastique"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())