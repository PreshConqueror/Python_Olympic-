# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Olympic2020Enhanced.ui'
#
# Created: Tue Apr 28 19:37:21 2020
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(456, 384)
        self.listWidgetSportNames = QtGui.QListWidget(Dialog)
        self.listWidgetSportNames.setGeometry(QtCore.QRect(40, 70, 201, 231))
        self.listWidgetSportNames.setObjectName(_fromUtf8("listWidgetSportNames"))
        self.pushButtonAdd = QtGui.QPushButton(Dialog)
        self.pushButtonAdd.setGeometry(QtCore.QRect(270, 120, 75, 23))
        self.pushButtonAdd.setObjectName(_fromUtf8("pushButtonAdd"))
        self.pushButtonSort = QtGui.QPushButton(Dialog)
        self.pushButtonSort.setGeometry(QtCore.QRect(280, 160, 75, 23))
        self.pushButtonSort.setObjectName(_fromUtf8("pushButtonSort"))
        self.pushButtonDelete = QtGui.QPushButton(Dialog)
        self.pushButtonDelete.setGeometry(QtCore.QRect(290, 200, 75, 23))
        self.pushButtonDelete.setObjectName(_fromUtf8("pushButtonDelete"))
        self.pushButtonEdit = QtGui.QPushButton(Dialog)
        self.pushButtonEdit.setGeometry(QtCore.QRect(300, 240, 75, 23))
        self.pushButtonEdit.setObjectName(_fromUtf8("pushButtonEdit"))
        self.lineEditSport = QtGui.QLineEdit(Dialog)
        self.lineEditSport.setGeometry(QtCore.QRect(40, 40, 291, 20))
        self.lineEditSport.setObjectName(_fromUtf8("lineEditSport"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 10, 271, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(260, 320, 151, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(260, 350, 141, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_Count = QtGui.QLabel(Dialog)
        self.label_Count.setGeometry(QtCore.QRect(50, 330, 161, 41))
        self.label_Count.setText(_fromUtf8(""))
        self.label_Count.setObjectName(_fromUtf8("label_Count"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.pushButtonAdd.setText(_translate("Dialog", "Add", None))
        self.pushButtonSort.setText(_translate("Dialog", "Sort", None))
        self.pushButtonDelete.setText(_translate("Dialog", "Delete ", None))
        self.pushButtonEdit.setText(_translate("Dialog", "Edit", None))
        self.label.setText(_translate("Dialog", "Enter the names of ten Olympics that should be followed:", None))
        self.label_2.setText(_translate("Dialog", "Student Name: Precious Okafor", None))
        self.label_3.setText(_translate("Dialog", "Student Number: 61910198", None))

