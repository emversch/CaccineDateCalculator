import datetime as dt
from PyQt5 import QtCore as qtc
from calcVacc import calcVacc
import gui

texttodata = {
    "Pfizer/BioNTech": "pfizer",
    "J&J": "jj",
    "Moderna": "moderna",
    "AstraZeneca/Oxford": "az"
}

# inheritance to create callbacks and modify stuff from automatically generated gui.py
class ChildUi(gui.Ui_MainWindow):

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)

        # set default dates to today
        self.dateLetter.setDateTime(qtc.QDateTime(dt.date.today(), qtc.QTime(0, 0, 0)))
        self.dateDose1Known.setDateTime(qtc.QDateTime(dt.date.today(), qtc.QTime(0, 0, 0)))

        # hide dates before first calculation
        self.hide_dates()

        # create callbacks
        self.calcbutton.clicked.connect(self.on_click)
        self.dose1Known.toggled.connect(self.on_select)
        self.vaccinSelector.textActivated.connect(self.hide_dates)
        self.dateLetter.dateChanged.connect(self.hide_dates)
        self.dateDose1Known.dateChanged.connect(self.hide_dates)

    # "click calculate" callback
    def on_click(self):

        self.clicked_once=True
        qv = self.dose1Known.isChecked()

        # use correct date for calculations
        if qv:
            dl = self.dateDose1Known.dateTime().toPyDateTime()
        else:
            dl = self.dateLetter.dateTime().toPyDateTime()

        # get vaccine name
        keycheckup = self.vaccinSelector.currentText()
        vc = texttodata[keycheckup]

        # calculate dates
        dates=calcVacc(vc, dl, qv)

        # set results
        self.dateDose1.setDateTime(qtc.QDateTime(dates[0], qtc.QTime(0, 0, 0)))
        self.dateDose2.setDateTime(qtc.QDateTime(dates[1], qtc.QTime(0, 0, 0)))
        self.dateProtected.setDateTime(qtc.QDateTime(dates[2], qtc.QTime(0, 0, 0)))

        # make dates visible
        self.show_dates()

    # "click dose1Known" callback
    def on_select(self):
        checkmark = self.dose1Known.isChecked()
        self.dateDose1Known.setEnabled(checkmark)
        self.labelDose1Known.setEnabled(checkmark)
        self.dateLetter.setEnabled(not checkmark)
        self.labelLetter.setEnabled(not checkmark)
        self.hide_dates()

    # show dates            
    def show_dates(self):
        ch = self.dose1Known.isChecked()  
        self.dateDose1.setVisible(not ch)
        self.labelDose1.setVisible(not ch)

        is_jj = texttodata[self.vaccinSelector.currentText()] == 'jj'
        self.dateDose2.setVisible(not is_jj)
        self.labelDose2.setVisible(not is_jj)

        self.dateProtected.show()
        self.labelProtected.show()
   
    # hide dates
    def hide_dates(self):
        self.dateDose1.hide()
        self.labelDose1.hide()
        self.dateProtected.hide()
        self.labelProtected.hide()
        self.labelDose2.hide()
        self.dateDose2.hide()