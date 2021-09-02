#importing code source of Olympic2020(ui file coverted to py)
import sys
from Olympic2020 import *

class MyForm(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        # program code for the the button click and call of the slot
        QtCore.QObject.connect(self.ui.pushButtonCount, QtCore.SIGNAL('clicked()'),self.dispmessage)

    # Method to count and display characters of the program
    def dispmessage(self):
        # this is the if statement to check that the input are entered and execute the count
        if self.ui.plainTextEditProject.toPlainText() == "":
            self.ui.labelDisplayCount.setText("Error: Sports name can not be empty")
        elif self.ui.lineEditChar.text() == "":
            self.ui.labelDisplayCount.setText("Error: Character can not be empty")
        else:
            word = str(self.ui.plainTextEditProject.toPlainText()).lower()
            chara = str(self.ui.lineEditChar.text()).lower()
            charcount = word.count(chara)
            self.ui.labelDisplayCount.setText("The number of ("+chara+") is: "+str(charcount))
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())

