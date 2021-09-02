import sys
from Olympic2020Enhanced import *
from PyQt4.QtGui import *

class MyForm(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        # button click signal
        # call slot
        QtCore.QObject.connect(self.ui.pushButtonAdd, QtCore.SIGNAL('clicked()'), self.addSportsToList)
        QtCore.QObject.connect(self.ui.pushButtonSort, QtCore.SIGNAL('clicked()'), self.sortSportsToList)
        QtCore.QObject.connect(self.ui.pushButtonDelete, QtCore.SIGNAL('clicked()'), self.deleteSportsList)
        QtCore.QObject.connect(self.ui.pushButtonEdit, QtCore.SIGNAL('clicked()'), self.editSportsList)

    def addSportsToList(self):
        val = self.ui.lineEditSport.text().capitalize()
        d = 0
        for index in range(self.ui.listWidgetSportNames.count()):
            if val == self.ui.listWidgetSportNames.item(index).text():
                d = 1
        if self.ui.listWidgetSportNames.count() < 1:
                self.ui.listWidgetSportNames.addItem(val)
                self.ui.lineEditSport.setText('')
        else:
            if d == 1:
               QtGui.QMessageBox.warning(self, "List Item", "Duplicate value cannot be added")
            else:
                self.ui.listWidgetSportNames.addItem(val)
                self.ui.lineEditSport.setText('')
        self.ui.lineEditSport.setFocus()
        cnt = self.ui.listWidgetSportNames.count()
        self.ui.label_Count.setText("There are currently "+str(cnt)+" items in the list.")
                
    def sortSportsToList(self):
        self.ui.listWidgetSportNames.sortItems()
        cnt = self.ui.listWidgetSportNames.count()
        self.ui.label_Count.setText("There are currently "+str(cnt)+" items in the list.")
        
    def deleteSportsList(self):
        row = self.ui.listWidgetSportNames.currentRow()
        if row == -1:
            QtGui.QMessageBox.warning(self, "List Item", "Select item before deleting")
        else:
            self.ui.listWidgetSportNames.takeItem(self.ui.listWidgetSportNames.currentRow())
        cnt = self.ui.listWidgetSportNames.count()
        self.ui.label_Count.setText("There are currently "+str(cnt)+" items in the list.")

    def editSportsList(self):
        row = self.ui.listWidgetSportNames.currentRow()
        
        if row == -1:
            QtGui.QMessageBox.warning(self, "List Item", "Select item before editing")
        else:
            newtext, ok = QInputDialog.getText(self, "List Item", "Enter new text")
            if ok and (len(newtext) != 0):
                self.ui.listWidgetSportNames.takeItem(self.ui.listWidgetSportNames.currentRow())
                self.ui.listWidgetSportNames.insertItem(row, QListWidgetItem(newtext.capitalize()))
        cnt = self.ui.listWidgetSportNames.count()
        self.ui.label_Count.setText("There are currently "+str(cnt)+" items in the list.")
    
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
