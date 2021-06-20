
from calcVacc import calcVacc
import VaccineDateCalculator as vdc
import datetime
from PyQt5 import QtCore, QtGui, QtWidgets

texttodata = {
    "Pfizer/BioNTech": "pfizer",
    "J&J": "jj",
    "Moderna": "moderna",
    "AstraZeneca/Oxford": "az"
}

class ChildUi(vdc.Ui_MainWindow):

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)

        # set default dates to today
        self.dateLetter.setDateTime(QtCore.QDateTime(datetime.date.today(), QtCore.QTime(0, 0, 0)))
        self.dateDose2.setDateTime(QtCore.QDateTime(datetime.date.today(), QtCore.QTime(0, 0, 0)))
        self.dateQvax.setDateTime(QtCore.QDateTime(datetime.date.today(), QtCore.QTime(0, 0, 0)))

        # create callbacks
        self.calcbutton.clicked.connect(self.on_click)
        self.Qvax.toggled.connect(self.on_select)
        self.vaccinSelector.textActivated.connect(self.on_JJ)

    # "click calculate" callback
    def on_click(self):
        qv = self.Qvax.isChecked()
        if qv:
            dl = self.dateQvax.dateTime().toPyDateTime()
        else:
            dl = self.dateLetter.dateTime().toPyDateTime()
        keycheckup = self.vaccinSelector.currentText()
        vc = texttodata[keycheckup]
        dates=calcVacc(vc, dl, qv)
        self.dateDose1.setDateTime(QtCore.QDateTime(dates[0], QtCore.QTime(0, 0, 0)))
        self.dateDose2.setDateTime(QtCore.QDateTime(dates[1], QtCore.QTime(0, 0, 0)))
        self.dateProtected.setDateTime(QtCore.QDateTime(dates[2], QtCore.QTime(0, 0, 0)))

    # "click QVax" callback
    def on_select(self):
        vinkje = self.Qvax.isChecked()
        self.dateQvax.setEnabled(vinkje)
        self.labelQvax.setEnabled(vinkje)
        self.dateLetter.setEnabled(not vinkje)
        self.labelLetter.setEnabled(not vinkje)
        if vinkje:
            self.dateDose1.hide()
            self.labelDose1.hide()
        else:
            self.dateDose1.show()
            self.labelDose1.show()

    # "select J&J" callback
    def on_JJ(self):
        if self.vaccinSelector.currentText() == 'J&J':
            self.dateDose2.hide()
            self.labelDose2.hide()
        else:
            self.dateDose2.show()
            self.labelDose2.show()