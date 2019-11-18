# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AddEditCoffeeForm(object):
    def setupUi(self, AddEditCoffeeForm):
        AddEditCoffeeForm.setObjectName("AddEditCoffeeForm")
        AddEditCoffeeForm.resize(400, 202)
        self.formLayout = QtWidgets.QFormLayout(AddEditCoffeeForm)
        self.formLayout.setObjectName("formLayout")
        self.name_label = QtWidgets.QLabel(AddEditCoffeeForm)
        self.name_label.setObjectName("name_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.name_label)
        self.name_lineEdit = QtWidgets.QLineEdit(AddEditCoffeeForm)
        self.name_lineEdit.setObjectName("name_lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.name_lineEdit)
        self.roaster_label = QtWidgets.QLabel(AddEditCoffeeForm)
        self.roaster_label.setObjectName("roaster_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.roaster_label)
        self.roaster_comboBox = QtWidgets.QComboBox(AddEditCoffeeForm)
        self.roaster_comboBox.setObjectName("roaster_comboBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.roaster_comboBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.taste_radioButton = QtWidgets.QRadioButton(AddEditCoffeeForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.taste_radioButton.sizePolicy().hasHeightForWidth())
        self.taste_radioButton.setSizePolicy(sizePolicy)
        self.taste_radioButton.setObjectName("taste_radioButton")
        self.horizontalLayout.addWidget(self.taste_radioButton)
        self.grains_radioButton = QtWidgets.QRadioButton(AddEditCoffeeForm)
        self.grains_radioButton.setObjectName("grains_radioButton")
        self.horizontalLayout.addWidget(self.grains_radioButton)
        self.formLayout.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.price_label = QtWidgets.QLabel(AddEditCoffeeForm)
        self.price_label.setObjectName("price_label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.price_label)
        self.price_spinBox = QtWidgets.QSpinBox(AddEditCoffeeForm)
        self.price_spinBox.setMaximum(99999)
        self.price_spinBox.setObjectName("price_spinBox")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.price_spinBox)
        self.volume_label = QtWidgets.QLabel(AddEditCoffeeForm)
        self.volume_label.setObjectName("volume_label")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.volume_label)
        self.volume_spinBox = QtWidgets.QSpinBox(AddEditCoffeeForm)
        self.volume_spinBox.setMaximum(99999)
        self.volume_spinBox.setObjectName("volume_spinBox")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.volume_spinBox)
        self.label = QtWidgets.QLabel(AddEditCoffeeForm)
        self.label.setObjectName("label")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label)
        self.taste_edit_btn = QtWidgets.QToolButton(AddEditCoffeeForm)
        self.taste_edit_btn.setObjectName("taste_edit_btn")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.taste_edit_btn)
        self.buttonBox = QtWidgets.QDialogButtonBox(AddEditCoffeeForm)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.buttonBox)

        self.retranslateUi(AddEditCoffeeForm)
        QtCore.QMetaObject.connectSlotsByName(AddEditCoffeeForm)

    def retranslateUi(self, AddEditCoffeeForm):
        _translate = QtCore.QCoreApplication.translate
        AddEditCoffeeForm.setWindowTitle(_translate("AddEditCoffeeForm", "Form"))
        self.name_label.setText(_translate("AddEditCoffeeForm", "Название"))
        self.roaster_label.setText(_translate("AddEditCoffeeForm", "Степень обжарки"))
        self.taste_radioButton.setText(_translate("AddEditCoffeeForm", "Молотый"))
        self.grains_radioButton.setText(_translate("AddEditCoffeeForm", "В зёрнах"))
        self.price_label.setText(_translate("AddEditCoffeeForm", "Цена"))
        self.volume_label.setText(_translate("AddEditCoffeeForm", "Объём"))
        self.label.setText(_translate("AddEditCoffeeForm", "Вкус"))
        self.taste_edit_btn.setText(_translate("AddEditCoffeeForm", "..."))

