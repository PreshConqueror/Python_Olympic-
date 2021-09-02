# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Olympic2020.ui'
#
# Created: Tue Apr 28 17:50:18 2020
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
        Dialog.resize(507, 354)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 30, 181, 41))
        self.label.setObjectName(_fromUtf8("label"))
        self.plainTextEditProject = QtGui.QPlainTextEdit(Dialog)
        self.plainTextEditProject.setGeometry(QtCore.QRect(200, 30, 291, 51))
        self.plainTextEditProject.setObjectName(_fromUtf8("plainTextEditProject"))
        self.labelCharCount = QtGui.QLabel(Dialog)
        self.labelCharCount.setGeometry(QtCore.QRect(30, 110, 91, 16))
        self.labelCharCount.setObjectName(_fromUtf8("labelCharCount"))
        self.lineEditChar = QtGui.QLineEdit(Dialog)
        self.lineEditChar.setGeometry(QtCore.QRect(130, 110, 61, 21))
        self.lineEditChar.setObjectName(_fromUtf8("lineEditChar"))
        self.pushButtonCount = QtGui.QPushButton(Dialog)
        self.pushButtonCount.setGeometry(QtCore.QRect(170, 170, 141, 31))
        self.pushButtonCount.setObjectName(_fromUtf8("pushButtonCount"))
        self.labelStudentName = QtGui.QLabel(Dialog)
        self.labelStudentName.setGeometry(QtCore.QRect(30, 300, 81, 16))
        self.labelStudentName.setObjectName(_fromUtf8("labelStudentName"))
        self.labelStudentNumber = QtGui.QLabel(Dialog)
        self.labelStudentNumber.setGeometry(QtCore.QRect(30, 330, 91, 16))
        self.labelStudentNumber.setObjectName(_fromUtf8("labelStudentNumber"))
        self.labelDisplayCount = QtGui.QLabel(Dialog)
        self.labelDisplayCount.setGeometry(QtCore.QRect(40, 240, 361, 51))
        self.labelDisplayCount.setText(_fromUtf8(""))
        self.labelDisplayCount.setObjectName(_fromUtf8("labelDisplayCount"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Enter the name of an Olympic sport", None))
        self.labelCharCount.setText(_translate("Dialog", "Enter a character", None))
        self.pushButtonCount.setText(_translate("Dialog", "Count Character", None))
        self.labelStudentName.setText(_translate("Dialog", "Student Name:", None))
        self.labelStudentNumber.setText(_translate("Dialog", "Student Number:", None))

