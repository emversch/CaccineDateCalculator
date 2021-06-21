import sys
from PyQt5 import QtWidgets as qtw
import ChildUi as cu

# start app
app = qtw.QApplication(sys.argv)
MainWindow = qtw.QMainWindow()
ui = cu.ChildUi()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())