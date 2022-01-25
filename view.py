from PyQt6.QtCore import QAbstractItemModel
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
        self.baseC.setCurrentIndex(0)
        for i in range(self.targetC.count()):
            item = self.targetC.item(i)
            item.setSelected(False)
        self.doubleSpinBox.setValue(0.00)
        self.textBrowser.setHtml("")
        self.setStatusTip("Please input!")

    def setCurrencies(self, currencies):
        self.targetC.addItems(currencies)
        self.baseC.addItems(currencies)

    def getValues(self):
        target = []
        for t in self.targetC.selectedItems():
            target.append(t.text())
        return (self.doubleSpinBox.value(), self.baseC.currentText(), target)

    def getLive(self):
        return self.isLive.isChecked()

    def setOutput(self, html):
        self.textBrowser.setHtml(html)