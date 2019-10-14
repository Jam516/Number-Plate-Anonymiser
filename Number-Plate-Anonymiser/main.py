import tkinter
from tkinter import messagebox

import pyperclip
from PyQt5 import QtWidgets, uic

from _version import __version__
from cypher import NumberplateCypher
from gui import Ui_Dialog
import exe_fix


class Ui(QtWidgets.QDialog):
    def __init__(self):
        super(Ui, self).__init__()

        self.cypher = NumberplateCypher()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle(f'Number Plate Anonymiser v{__version__}')

        self.encrypt_button = self.findChild(QtWidgets.QPushButton, 'encrypt_button')
        self.encrypt_button.clicked.connect(self.encrypt) # Remember to pass the definition/method, not the return value!
        self.refresh_button = self.findChild(QtWidgets.QPushButton, 'refresh_button')
        self.refresh_button.clicked.connect(self.refresh)

        self.refresh_button = self.findChild(QtWidgets.QPushButton, 'copy_button')
        self.refresh_button.clicked.connect(self.copy_output)

        self.input = self.findChild(QtWidgets.QTextEdit, 'plate_no_box')

        self.output = self.findChild(QtWidgets.QTextEdit, 'results_window')
        self.output.setReadOnly(True)

        self.show() # Show the GUI

    def encrypt(self):
        plates = self.input.toPlainText().splitlines()
        anonymised = '\n'.join([self.cypher.anonymise(plate) for plate in plates])
        self.output.setText(anonymised)
        self.copy_output()

    def copy_output(self):
        pyperclip.copy(self.output.toPlainText())
        messagebox.showinfo(
            'Copy complete!', 'Output copied to clipboard', parent=parent
        )


    def refresh(self):
        okcancel = messagebox.askokcancel('Refresh Cypher', 'Are you sure you want to refresh the cypher?', parent=parent) # OK / Cancel
        if okcancel:
            self.cypher.randomise_cyphers()
            self.output.setText('')
            self.input.setText('')


if __name__ == '__main__':
    parent = tkinter.Tk()
    parent.overrideredirect(1) # Avoid it appearing and then disappearing quickly
    parent.withdraw() # Hide the window

    app = QtWidgets.QApplication([]) # Create an instance of QtWidgets.QApplication
    window = Ui() # Create an instance of our class
    app.exec_() # Start the application
