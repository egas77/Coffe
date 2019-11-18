# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\editTasteForm.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EditTasteForm(object):
    def setupUi(self, EditTasteForm):
        EditTasteForm.setObjectName("EditTasteForm")
        EditTasteForm.resize(632, 538)
        self.gridLayout = QtWidgets.QGridLayout(EditTasteForm)
        self.gridLayout.setObjectName("gridLayout")
        self.name_label = QtWidgets.QLabel(EditTasteForm)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.name_label.setFont(font)
        self.name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.name_label.setObjectName("name_label")
        self.gridLayout.addWidget(self.name_label, 0, 0, 1, 1)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(EditTasteForm)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 1, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(EditTasteForm)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)

        self.retranslateUi(EditTasteForm)
        QtCore.QMetaObject.connectSlotsByName(EditTasteForm)

    def retranslateUi(self, EditTasteForm):
        _translate = QtCore.QCoreApplication.translate
        EditTasteForm.setWindowTitle(_translate("EditTasteForm", "Form"))
        self.name_label.setText(_translate("EditTasteForm", "{name}"))

