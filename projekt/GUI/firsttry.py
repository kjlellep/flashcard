from PyQt5 import QtCore, QtGui, QtWidgets
#from bones import sisselugemine, printimine, lisamine
import codecs
import random
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        #MainWindow.setGeometry(50,50, 900, 600)
        MainWindow.resize(900,600)
        MainWindow.setWindowIcon(QtGui.QIcon('logo.png'))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(360, 510, 521, 20))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")

        self.questiontimeCounter = QtWidgets.QProgressBar(self.centralwidget)
        self.questiontimeCounter.setGeometry(QtCore.QRect(90, 330, 331, 16))
        self.questiontimeCounter.setProperty("value", 24)
        self.questiontimeCounter.setObjectName("questiontimeCounter")

        self.questionBox = QtWidgets.QTextBrowser(self.centralwidget)
        self.questionBox.setGeometry(QtCore.QRect(90, 160, 331, 171))
        self.questionBox.setObjectName("questionBox")

        self.answerBox = QtWidgets.QTextEdit(self.centralwidget)
        self.answerBox.setGeometry(QtCore.QRect(90, 370, 271, 81))
        self.answerBox.setObjectName("answerBox")

        self.StylesMenu = QtWidgets.QComboBox(self.centralwidget)
        self.StylesMenu.setGeometry(QtCore.QRect(740, 0, 141, 31))
        self.StylesMenu.setObjectName("StylesMenu")

        self.openGL = QtWidgets.QLabel(self.centralwidget)
        self.openGL.setGeometry(QtCore.QRect(430, 160, 311, 171))
        self.openGL.setObjectName("openGL")

        self.QnAReverser = QtWidgets.QRadioButton(self.centralwidget)
        self.QnAReverser.setGeometry(QtCore.QRect(90, 30, 161, 21))
        self.QnAReverser.setObjectName("QnAReverser")

        self.MaximizecheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.MaximizecheckBox.setGeometry(QtCore.QRect(660, 0, 81, 31))
        self.MaximizecheckBox.setObjectName("MaximizecheckBox")

        self.ReadButton = QtWidgets.QPushButton(self.centralwidget)
        self.ReadButton.setGeometry(QtCore.QRect(0, 160, 91, 41))
        self.ReadButton.setObjectName("ReadButton")

        self.StartButton = QtWidgets.QPushButton(self.centralwidget)
        self.StartButton.setGeometry(QtCore.QRect(0, 200, 91, 41))
        self.StartButton.setObjectName("StartButton")

        self.PauseButton = QtWidgets.QPushButton(self.centralwidget)
        self.PauseButton.setGeometry(QtCore.QRect(0, 240, 91, 41))
        self.PauseButton.setObjectName("PauseButton")

        self.stopButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopButton.setGeometry(QtCore.QRect(0, 280, 91, 41))
        self.stopButton.setObjectName("stopButton")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 884, 21))
        self.menubar.setObjectName("menubar")

        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")

        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")

        self.actionEdit_dictionary = QtWidgets.QAction(MainWindow)
        self.actionEdit_dictionary.setObjectName("actionEdit_dictionary")

        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")

        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionEdit_dictionary)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.PauseButton.clicked.connect(self.setImage)
        #self.ReadButton.clicked.connect(self.)
        #self.actionOpen.triggered(self, )

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Flash-korttiohjelma"))
        self.QnAReverser.setText(_translate("MainWindow", "Reverse questions/answers"))
        self.MaximizecheckBox.setText(_translate("MainWindow", "Maximize"))
        self.StartButton.setText(_translate("MainWindow", "Start"))
        self.PauseButton.setText(_translate("MainWindow", "Pause"))
        self.stopButton.setText(_translate("MainWindow", "Stop"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionEdit_dictionary.setText(_translate("MainWindow", "Edit dictionary"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

    def setImage(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "",
                                                            "Image Files (*.png *.jpg *jpeg *.bmp)")  # Ask for file
        if fileName:  # If the user gives a file
            pixmap = QtGui.QPixmap(fileName)  # Setup pixmap with the provided image
            pixmap = pixmap.scaled(self.openGL.width(), self.openGL.height(),
                                   QtCore.Qt.KeepAspectRatio)  # Scale pixmap
            self.openGL.setPixmap(pixmap)  # Set the pixmap onto the label
            self.openGL.setAlignment(QtCore.Qt.AlignCenter)  # Align the label to center

    #def open_file(self):
    #    fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select dictionary", "",
    #                                                        "Text/JSON Files (*.txt *.json)")
    #    if fileName:


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

