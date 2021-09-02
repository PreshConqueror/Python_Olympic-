import sys
from Olympic2020Add import *
from PyQt4 import QtGui

class MyForm(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        # button click signal
        #call slot
        QtCore.QObject.connect(self.ui.pushButtonAdd, QtCore.SIGNAL('clicked()'), self.addSportsToList)
        QtCore.QObject.connect(self.ui.pushButtonSort, QtCore.SIGNAL('clicked()'), self.sortSportsToList)

    
    def addSportsToList(self):
        val = self.ui.lineEditSportNames.text().capitalize()
        d = 0
        for index in range(self.ui.listWidgetListNames.count()):
            if val == self.ui.listWidgetListNames.item(index).text():
                d = 1
        if self.ui.listWidgetListNames.count() < 1:
                self.ui.listWidgetListNames.addItem(val)
                self.ui.lineEditSportNames.setText('')
        else:
            if d == 1:
               QtGui.QMessageBox.warning(self, "List Item", "Duplicate value cannot be added")
            else:
                self.ui.listWidgetListNames.addItem(val)
                self.ui.lineEditSportNames.setText('')
        self.ui.lineEditSportNames.setFocus()
                
                
                
    def sortSportsToList(self):
        self.ui.listWidgetListNames.sortItems()
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
