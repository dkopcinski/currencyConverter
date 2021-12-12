import sys

from PyQt6.QtWidgets import QApplication
import model
import view

class Controller:
    def __init__(self):
        self.model = model.Model()
        self.view = view.View(self)

    def reset(self):
        self.model.reset()
        self.view.reset()

    def execute(self):
        try:
            self.model.setAmount(self.view.getValues()[0])
            self.model.setBaseCurrency(self.view.getValues()[1])
            self.model.setTargetCurrency(self.view.getValues()[2])
            self.view.setOutput(self.model.convertCurrency(), self.model.getRates(), self.model.getDate())
            self.view.setStatusTip("Berechnung erfolgreich")
        except Exception as e:
            self.view.setStatusTip(str(e))


if __name__ == "__main__":
    app = QApplication([])
    c = Controller()
    c.view.show()
    sys.exit(app.exec())
