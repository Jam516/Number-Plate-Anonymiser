# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(756, 583)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(420, 20, 151, 16))
        self.label.setObjectName("label")
        self.results_window = QtWidgets.QTextEdit(Dialog)
        self.results_window.setGeometry(QtCore.QRect(420, 50, 311, 461))
        self.results_window.setObjectName("results_window")
        self.plate_no_box = QtWidgets.QTextEdit(Dialog)
        self.plate_no_box.setGeometry(QtCore.QRect(20, 20, 381, 541))
        self.plate_no_box.setObjectName("plate_no_box")
        self.encrypt_button = QtWidgets.QPushButton(Dialog)
        self.encrypt_button.setGeometry(QtCore.QRect(480, 530, 93, 28))
        self.encrypt_button.setObjectName("encrypt_button")
        self.refresh_button = QtWidgets.QPushButton(Dialog)
        self.refresh_button.setGeometry(QtCore.QRect(602, 530, 121, 28))
        self.refresh_button.setObjectName("refresh_button")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Number Plate Anonymiser"))
        self.label.setText(_translate("Dialog", "Encrypted Plate Numbers"))
        self.encrypt_button.setText(_translate("Dialog", "Encrypt"))
        self.refresh_button.setText(_translate("Dialog", "Refresh Cypher"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
