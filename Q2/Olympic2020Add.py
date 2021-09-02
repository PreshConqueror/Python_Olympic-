# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Olympic2020Add.ui'
#
# Created: Tue Apr 28 18:34:19 2020
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
        Dialog.resize(437, 342)
        self.labelTitle = QtGui.QLabel(Dialog)
        self.labelTitle.setGeometry(QtCore.QRect(40, 9, 371, 31))
        self.labelTitle.setTextFormat(QtCore.Qt.RichText)
        self.labelTitle.setScaledContents(False)
        self.labelTitle.setWordWrap(True)
        self.labelTitle.setObjectName(_fromUtf8("labelTitle"))
        self.lineEditSportNames = QtGui.QLineEdit(Dialog)
        self.lineEditSportNames.setGeometry(QtCore.QRect(30, 50, 261, 20))
        self.lineEditSportNames.setObjectName(_fromUtf8("lineEditSportNames"))
        self.pushButtonAdd = QtGui.QPushButton(Dialog)
        self.pushButtonAdd.setGeometry(QtCore.QRect(310, 50, 75, 23))
        self.pushButtonAdd.setObjectName(_fromUtf8("pushButtonAdd"))
        self.listWidgetListNames = QtGui.QListWidget(Dialog)
        self.listWidgetListNames.setGeometry(QtCore.QRect(20, 90, 256, 192))
        self.listWidgetListNames.setObjectName(_fromUtf8("listWidgetListNames"))
        self.pushButtonSort = QtGui.QPushButton(Dialog)
        self.pushButtonSort.setGeometry(QtCore.QRect(310, 140, 75, 41))
        self.pushButtonSort.setObjectName(_fromUtf8("pushButtonSort"))
        self.labelStudentName = QtGui.QLabel(Dialog)
        self.labelStudentName.setGeometry(QtCore.QRect(30, 300, 151, 16))
        self.labelStudentName.setObjectName(_fromUtf8("labelStudentName"))
        self.labelStudentNumber = QtGui.QLabel(Dialog)
        self.labelStudentNumber.setGeometry(QtCore.QRect(30, 320, 141, 16))
        self.labelStudentNumber.setObjectName(_fromUtf8("labelStudentNumber"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.labelTitle.setText(_translate("Dialog", "Enter the names of ten Olympic sports that should be followed", None))
        self.pushButtonAdd.setText(_translate("Dialog", "Add", None))
        self.pushButtonSort.setText(_translate("Dialog", "SORT", None))
        self.labelStudentName.setText(_translate("Dialog", "Student Name: Precious Okafor", None))
        self.labelStudentNumber.setText(_translate("Dialog", "Student Number: 61910198", None))

