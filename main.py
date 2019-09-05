import sys
import pandas as pd
import numpy as np
from PyQt5 import QtWidgets, uic

qtCreatorFile = "gui.ui" # Enter xml file here.
characters  = {'Chr': ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q',
               'R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']}
key = pd.DataFrame(characters)
cyphers = [key]

def cypher():
    for i in range(1,8): # make a list of 7 cyphers (one for each licence plate character by randomly arranging characters A-9
        cyphers.append(key)
        cyphers[i]['Values'] = np.random.random_sample(len(cyphers[0]))
        cyphers[i] = cyphers[i].sort_values('Values')
        cyphers[i] = cyphers[i].reset_index(drop=True)

cypher()

class Ui(QtWidgets.QDialog):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('gui.ui', self) # Load the .ui file

        self.encrypt_button = self.findChild(QtWidgets.QPushButton, 'encrypt_button')
        self.encrypt_button.clicked.connect(self.encrypt) # Remember to pass the definition/method, not the return value!
        self.refresh_button = self.findChild(QtWidgets.QPushButton, 'refresh_button')
        self.refresh_button.clicked.connect(self.refresh)

        self.input = self.findChild(QtWidgets.QTextEdit, 'plate_no_box')

        self.output = self.findChild(QtWidgets.QTextEdit, 'results_window')

        self.show() # Show the GUI

    def encrypt(self):
        plate_no = self.input.toPlainText()
        no_list = plate_no.splitlines()
        result_list = []
        output = ''
        for no in no_list:
            chrlist = list(no)
            for i in range(0,7):
                index = cyphers[0].index[cyphers[0]['Chr'] == chrlist[i]] # get index of the plate no character in A-9 range
                index = index[0]
                chrlist[i] = cyphers[i+1].at[index, 'Chr'] # replace character in plate no with corresponding character in corresponding cypher
            result_list.append(chrlist)
        for r in result_list:
            output = output + ''.join(r) + '\n'
        self.output.setText(output)

    def refresh(self):
        cyphers = [key]
        cypher()
        self.output.setText('')
        self.input.setText('')

app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
window = Ui() # Create an instance of our class
app.exec_() # Start the application
