import sys
import tkinter
import pickle
import pyperclip
from PyQt5 import QtWidgets, uic
from tkinter import messagebox

from cypher import NumberplateCypher
import exe_fix


qtCreatorFile = "gui.ui" # Enter xml file here.

parent = tkinter.Tk()
parent.overrideredirect(1) # Avoid it appearing and then disappearing quickly
parent.withdraw() # Hide the window

class Ui(QtWidgets.QDialog):
    def __init__(self):
        super(Ui, self).__init__()

        self.cypher = NumberplateCypher()

        uic.loadUi('gui.ui', self)

        self.encrypt_button = self.findChild(QtWidgets.QPushButton, 'encrypt_button')
        self.encrypt_button.clicked.connect(self.encrypt) # Remember to pass the definition/method, not the return value!
        self.refresh_button = self.findChild(QtWidgets.QPushButton, 'refresh_button')
        self.refresh_button.clicked.connect(self.refresh)

        self.input = self.findChild(QtWidgets.QTextEdit, 'plate_no_box')

        self.output = self.findChild(QtWidgets.QTextEdit, 'results_window')

        self.show() # Show the GUI

    def encrypt(self):
        plates = self.input.toPlainText().splitlines()
        anonymised = '\n'.join([self.cypher.anonymise(plate) for plate in plates])
        self.output.setText(anonymised)
        pyperclip.copy(anonymised)
        info = messagebox.showinfo('Encrypted', 'Copied to clipboard', parent=parent)

    def refresh(self):
        okcancel = messagebox.askokcancel('Refresh Cypher', 'Are you sure you want to refresh the cypher?', parent=parent) # OK / Cancel
        if okcancel:
            self.cypher.randomise_cyphers()
            self.output.setText('')
            self.input.setText('')

app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
window = Ui() # Create an instance of our class
app.exec_() # Start the application
