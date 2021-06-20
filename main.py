import sys
from calcVacc import calcVacc
import ChildUi as cu
import datetime
from PyQt5 import QtCore, QtGui, QtWidgets

# start app
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = cu.Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())