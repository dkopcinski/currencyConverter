import sys

from PyQt6.QtWidgets import QApplication
import model
import view

class Controller:
    def __init__(self):
        self.view = view.View(self)
        self.model = model.Model()
        self.view.setCurrencies(self.model.getCurrencies())

    def reset(self):
        self.view.reset()

    def execute(self):
        try:
            amount, baseC, targetC = self.view.getValues()
            if self.view.getLive():
                self.model.setStrategy(model.Live())
            else:
                self.model.setStrategy(model.Offline())
            currencies = self.model.convertC(baseC, targetC, amount)
            html = f"<b>{amount} {baseC}</b> entsprechen <br><ul>"
            for c in currencies[:-1]:
                converted, targetC, rate = c
                html += f"<li><b>{round(converted,2)} {targetC}</b> (Kurs: {round(rate, 5)})</li>"
            html += f"</li><br>Stand: {currencies[-1]}"
            self.view.setOutput(html)
            self.view.setStatusTip("Berechnung erfolgreich")
        except Exception as e:
            self.view.setStatusTip(str(e))


if __name__ == "__main__":
    app = QApplication([])
    c = Controller()
    c.view.show()
    sys.exit(app.exec())