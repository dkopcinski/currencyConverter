from PyQt6.QtWidgets import *
from PyQt6 import uic
from controller import Controller


class View(QMainWindow):

    def __init__(self, c: Controller):
        super().__init__()
        uic.loadUi("umrechnen.ui", self)
        self.pB_calc.clicked.connect(c.execute)
        self.pb_reset.clicked.connect(c.reset)
        self.setStatusBar(QStatusBar(self))
        self.setStatusTip("Please input!")

    def reset(self):
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.doubleSpinBox.setValue(0.00)
        self.textBrowser.setHtml("")
        self.setStatusTip("Please input!")

    def getValues(self):
        if self.lineEdit_2.text() == "":
            raise Exception("Please enter a value as your base currency")
        else:
            res = []
            res.append(self.doubleSpinBox.value())
            res.append(self.lineEdit_2.text())
            res.append(self.lineEdit_3.text())
            return res

    def setOutput(self, currencies, rates, date):
        html = f"<b>{self.doubleSpinBox.value()} {self.lineEdit_2.text()}</b> entsprechen <br><ul>"
        for i in range(len(currencies)):
            html += f"<li><b>{currencies[i]}</b> (Kurs: {rates[i]})</li>"
        html += f"</li><br>Stand: {date}"
        self.textBrowser.setHtml(html)