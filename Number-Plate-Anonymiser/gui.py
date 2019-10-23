# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(756, 581)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(420, 20, 311, 20))
        self.label.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop
        )
        self.label.setObjectName("label")
        self.results_window = QtWidgets.QTextEdit(Dialog)
        self.results_window.setGeometry(QtCore.QRect(420, 40, 311, 471))
        self.results_window.setObjectName("results_window")
        self.plate_no_box = QtWidgets.QTextEdit(Dialog)
        self.plate_no_box.setGeometry(QtCore.QRect(20, 40, 381, 471))
        self.plate_no_box.setObjectName("plate_no_box")
        self.encrypt_button = QtWidgets.QPushButton(Dialog)
        self.encrypt_button.setGeometry(QtCore.QRect(140, 530, 141, 31))
        self.encrypt_button.setObjectName("encrypt_button")
        self.refresh_button = QtWidgets.QPushButton(Dialog)
        self.refresh_button.setGeometry(QtCore.QRect(280, 530, 121, 31))
        self.refresh_button.setObjectName("refresh_button")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 381, 20))
        self.label_2.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop
        )
        self.label_2.setObjectName("label_2")
        self.copy_button = QtWidgets.QPushButton(Dialog)
        self.copy_button.setGeometry(QtCore.QRect(520, 530, 111, 31))
        self.copy_button.setObjectName("copy_button")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(680, 20, 51, 20))
        self.label_3.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTop | QtCore.Qt.AlignTrailing
        )
        self.label_3.setOpenExternalLinks(True)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Number Plate Anonymiser"))
        self.label.setText(_translate("Dialog", "Encrypted Plate Numbers"))
        self.encrypt_button.setText(_translate("Dialog", "Encrypt"))
        self.refresh_button.setText(_translate("Dialog", "Refresh Cypher"))
        self.label_2.setText(_translate("Dialog", "Input"))
        self.copy_button.setText(_translate("Dialog", "Copy Results"))
        self.label_3.setText(
            _translate(
                "Dialog",
                '<a href="https://github.com/TransportScotland/Number-Plate-Anonymiser/blob/master/README.md">Help</a>',
            )
        )


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
