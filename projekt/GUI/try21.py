from PyQt5 import QtCore, QtGui, QtWidgets
#from bones import sisselugemine, printimine, lisamine
import codecs
import random
import sys
import os
class Window(QtWidgets.QWidget):

    def __init__(self): #constructor
        super(Window, self).__init__()
        self.setWindowIcon(QtGui.QIcon("logo.png"))
        self.setWindowTitle("Flashcards TBD")
        self.setGeometry(500,200,900,600)
        self.init_ui()


    def init_ui(self): #initializer

        self.progressBar = QtWidgets.QProgressBar(self)
        self.progressBar.setGeometry(QtCore.QRect(360, 510, 521, 20))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")

        self.textEdit = QtWidgets.QTextEdit(self)

        self.LineEdit = QtWidgets.QLineEdit()

        self.gifbox = QtWidgets.QLabel("Siia tuleb pilt")
        self.gifbox.setGeometry(0, 0, 100, 100)
        #self.gifbox.move()

        self.button = QtWidgets.QPushButton("Juppi on v", parent=self)
        self.button.move(120,120)
        self.button.show()

        self.clearButton = QtWidgets.QPushButton("Clear")

        self.exitButton = QtWidgets.QPushButton("Exit")

        self.saveButton = QtWidgets.QPushButton("Save")




        self.button.clicked.connect(self.setImage)
        self.clearButton.clicked.connect(self.buttonclick)
        self.exitButton.clicked.connect(self.buttonclick)
        #self.saveButton.clicked.connect(self.save_file)

        self.show()

    def setImage(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "",
                                                            "Image Files (*.png *.jpg *jpeg *.bmp)")  # Ask for file
        if fileName:  # If the user gives a file
            pixmap = QtGui.QPixmap(fileName)  # Setup pixmap with the provided image
            pixmap = pixmap.scaled(self.gifbox.width(), self.gifbox.height(),
                                   QtCore.Qt.KeepAspectRatio)  # Scale pixmap
            self.gifbox.setPixmap(pixmap)  # Set the pixmap onto the label
            self.gifbox.setAlignment(QtCore.Qt.AlignCenter)  # Align the label to center


    def buttonclick(self): #button methods
        sender = self.sender()
        if sender.text() == "Exit":
            sys.exit()
        elif sender.text() == "Clear":
            self.LineEdit.clear()
            self.textEdit.clear()

    #def save_file(self):
    #    filename = QFileDialog.getSaveFileName(self, "Save File", os.getenv("C:"))
    #    with open(filename[0], "w") as f:
    #        my_text = self.textEdit.toPlainText()
    #        f.write(my_text)


app = QtWidgets.QApplication(sys.argv)
aken = Window()
sys.exit(app.exec())