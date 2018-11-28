from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QStyleFactory, QFileDialog
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt
import codecs, random, sys, time, os
class Window(QtWidgets.QWidget):

    def __init__(self): #constructor
        super(Window, self).__init__()
        self.setWindowIcon(QtGui.QIcon("logo.png"))
        self.setWindowTitle("Flashcards TBD")
        self.setGeometry(500,200,900,600)
        self.init_ui()


    def init_ui(self): #initializer

        ### widgets ###
        self.progressBar = QtWidgets.QProgressBar(self)
        self.progressBar.setGeometry(QtCore.QRect(360, 510, 521, 20))
        self.progressBar.setProperty("value", 0)

        self.questiontimeCounter = QtWidgets.QProgressBar(self)
        self.questiontimeCounter.setGeometry(QtCore.QRect(90, 330, 331, 16))
        self.questiontimeCounter.setProperty("value", 100)

        self.questionBox = QtWidgets.QTextBrowser(self)
        self.questionBox.setGeometry(QtCore.QRect(90, 160, 331, 171))

        self.answerBox = QtWidgets.QTextEdit(self)
        self.answerBox.setGeometry(QtCore.QRect(90, 370, 271, 81))

        self.StylesMenu = QtWidgets.QComboBox(self)
        self.StylesMenu.setGeometry(QtCore.QRect(740, 40, 141, 31))

        self.gifbox = QtWidgets.QLabel("Picture frame", parent=self)
        self.gifbox.setGeometry(QtCore.QRect(430, 160, 450, 240)) #orig 311, 171

        self.QnAReverser = QtWidgets.QRadioButton("Reverse questions/answers", parent=self)
        self.QnAReverser.setGeometry(QtCore.QRect(90, 30, 161, 21))

        self.MaximizecheckBox = QtWidgets.QCheckBox("Maximize", parent=self)
        self.MaximizecheckBox.setGeometry(QtCore.QRect(660, 40, 81, 31))

        self.OpenButton = QtWidgets.QPushButton("Open", parent=self)
        self.OpenButton.setGeometry(QtCore.QRect(0, 160, 91, 41))

        self.StartButton = QtWidgets.QPushButton("Start", parent=self)
        self.StartButton.setGeometry(QtCore.QRect(0, 200, 91, 41))

        self.PauseButton = QtWidgets.QPushButton("Pause", parent=self)
        self.PauseButton.setGeometry(QtCore.QRect(0, 240, 91, 41))

        self.ClearButton = QtWidgets.QPushButton("Clear", parent=self)
        self.ClearButton.setGeometry(QtCore.QRect(0, 280, 91, 41))

        self.SaveButton = QtWidgets.QPushButton("Save", parent=self)
        self.SaveButton.setGeometry(QtCore.QRect(0,320,91,41))

        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))

        ### layout ###

        self.layout = QtWidgets.QGridLayout(self)
        
        self.layout.addWidget(self.MaximizecheckBox, 0, 3, 1, 1)
        self.layout.addWidget(self.StylesMenu, 0, 4, 1, 1)
        self.layout.addWidget(self.QnAReverser, 1, 1, 1, 1)
        self.layout.addWidget(self.questionBox, 2, 1, 3, 2)
        self.layout.addWidget(self.gifbox, 2, 3, 3, 1)
        self.layout.addWidget(self.OpenButton, 1, 0, 1, 1)
        self.layout.addWidget(self.StartButton, 2, 0, 1, 1)
        self.layout.addWidget(self.PauseButton, 3, 0, 1, 1)
        self.layout.addWidget(self.ClearButton, 4, 0, 1, 1)
        self.layout.addWidget(self.SaveButton, 5, 0, 1, 1)
        self.layout.addWidget(self.questiontimeCounter, 5, 1, 1, 2)
        self.layout.addWidget(self.answerBox, 6, 1, 1, 1)
        self.layout.addWidget(self.progressBar, 7, 2, 1, 3)

        ### methods connected to widgets ###

        self.MaximizecheckBox.stateChanged.connect(self.maximize)
        self.PauseButton.clicked.connect(self.buttonclick)
        self.StartButton.clicked.connect(self.buttonclick)
        self.ClearButton.clicked.connect(self.buttonclick)
        self.OpenButton.clicked.connect(self.buttonclick)
        self.SaveButton.clicked.connect(self.buttonclick)

        self.show()



    ### BUTTON METHODS ###

    def buttonclick(self):
        sender = self.sender()
        if sender.text() == "Pause":
            self.setImage()
        elif sender.text() == "Start":
            self.start_countdown()
        elif sender.text() == "Clear":
            self.answerBox.clear()
        elif sender.text() == "Open":
            self.open_file()
        elif sender.text() == "Save":
            self.save_file()

    def maximize(self, state):
        if state == QtCore.Qt.Checked:
            self.showMaximized()
            # self.menubar.setGeometry(QtCore.QRect(0, 0, 1720, 20))
        else:
            self.showNormal()
            # self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))

    def start_countdown(self):
        time_left = 100
        while time_left > 9:
            time_left -= 10
            time.sleep(1)
            self.questiontimeCounter.setValue(time_left)
        if time_left == 0:
            self.questionBox.setText("Aeg sai otsa!")

    ### MISC & FILE METHODS ###

    def save_file(self):
        path = QtCore.QDir.currentPath()
        filename = QFileDialog.getSaveFileName(self, "Save File", path)
        with open(filename[0], "w") as f:
            my_text = self.answerBox.toPlainText()
            f.write(my_text)

    def setImage(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "",
                                                            "Image Files (*.png *.jpg *jpeg *.bmp)")  # Ask for file
        if fileName:  # If the user gives a file
            try:
                pixmap = QtGui.QPixmap(fileName)  # Setup pixmap with the provided image
                pixmap = pixmap.scaled(self.gifbox.width(), self.gifbox.height(),
                                   QtCore.Qt.KeepAspectRatio)  # Scale pixmap
                self.gifbox.setPixmap(pixmap)  # Set the pixmap onto the label
                self.gifbox.setAlignment(QtCore.Qt.AlignCenter)  # Align the label to center
            except Exception as e:
                print(e)
                self.questionBox.setText("Can't construct image from file", e)

    ### MAIN CODE FUNCTIONS ###

    def open_file(self):
        path = QtCore.QDir.currentPath()
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        failinimi, _ = QFileDialog.getOpenFileName(self, "Open File",
                                                  "All Files (*)", options=options)
        if failinimi[1] == ".txt":
            self.questionBox.setText(f.read())
        else:
            with codecs.open(failinimi[0], encoding='utf-8') as f:
                for line in f:
                    rida = line.split("\\")
                    kysimustik[rida[0]] = rida[1].strip()
            self.questionBox.setText(kysimustik)

### dark theme conf ###

dark_palette = QPalette()
dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
dark_palette.setColor(QPalette.WindowText, Qt.white)
dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
dark_palette.setColor(QPalette.ToolTipText, Qt.white)
dark_palette.setColor(QPalette.Text, Qt.white)
dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
dark_palette.setColor(QPalette.ButtonText, Qt.white)
dark_palette.setColor(QPalette.BrightText, Qt.red)
dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
dark_palette.setColor(QPalette.HighlightedText, Qt.black)

### start app ###

app = QtWidgets.QApplication(sys.argv)
app.setPalette(dark_palette)
app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")
app.setStyle(QStyleFactory.create("fusion"))
aken = Window()
sys.exit(app.exec())