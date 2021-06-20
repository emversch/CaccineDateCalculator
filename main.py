import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from calcVacc import calcVacc
import ChildUi as cu

# start app
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = cu.ChildUi()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())