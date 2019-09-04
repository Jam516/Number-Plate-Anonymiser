import sys
import pandas as pd
import numpy as np
from PyQt5 import QtWidgets, uic

qtCreatorFile = "gui.ui" # Enter file here.
characters  = {'Chr': ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q',
               'R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']}
key = pd.DataFrame(characters)
cyphers = [key]

def cypher():
    # cyphers = [key] may need to do this to clean the cypher list before making new cyphers. could aslo just clean in the method for that btn
    for i in range(1,8): # make a list of 7 cyphers (one for each licence plate character by randomly arranging characters A-9
        cyphers.append(key)
        cyphers[i]['Values'] = np.random.random_sample(len(cyphers[0]))
        cyphers[i] = cyphers[i].sort_values('Values')
        cyphers[i] = cyphers[i].reset_index(drop=True) #this will be a method in the app that'll be called whenever we need to refresh ecryption

cypher()

class Ui(QtWidgets.QDialog):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('gui.ui', self) # Load the .ui file

        self.button = self.findChild(QtWidgets.QPushButton, 'encrypt_button')
        self.button.clicked.connect(self.encrypt) # Remember to pass the definition/method, not the return value!

        self.input = self.findChild(QtWidgets.QTextEdit, 'plate_no_box')

        self.output = self.findChild(QtWidgets.QTextEdit, 'results_window')

        self.show() # Show the GUI

    def encrypt(self):
        # cypher()
        plate_no = self.input.toPlainText()
        chrlist = list(plate_no)
        for i in range(0,7):
            index = cyphers[0].index[cyphers[0]['Chr'] == chrlist[i]] # get index of the plate no character in A-9 range
            index = index[0]
            chrlist[i] = cyphers[i+1].at[index, 'Chr'] # replace character in plate no with corresponding character in corresponding cypher
        new_no = ''.join(chrlist)
        self.output.setText(new_no)

app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
window = Ui() # Create an instance of our class
app.exec_() # Start the application
