"""DiyPython 108 - Display PyQt5

References:
* http://pyqt.sourceforge.net/Docs/PyQt5/class_reference.html

* A little dated but useful:
* Rapid GUI Programming with Python and Qt: The Definitive Guide to PyQt Programming > Main Window Responsibilities

* http://pyqt.sourceforge.net/Docs/PyQt5/introduction.html
"""


import sys
from PyQt5 import QtWidgets

class QtTableWidgetThing(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(QtTableWidgetThing, self).__init__(parent)
        self.table = QtWidgets.QTableWidget()
        self.setCentralWidget(self.table)
        self.setWindowTitle("QtTableWidgetThing")
        self.resize(350, 150)
        self.init_table()
        self.show()

    def init_table(self, row_count = 3):
        self.table.clear()
        self.table.setRowCount(row_count)
        self.table.setColumnCount(3)
        self.table.setAlternatingRowColors(True)
        self.table.setHorizontalHeaderLabels(["Description", "YoLo?", "YoLo_MAX"])
        self.table.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.table.setSelectionMode(QtWidgets.QTableWidget.SingleSelection)
    def add(self,index, description, yolo, yolo_max):
        desc_item = QtWidgets.QTableWidgetItem(description)
        yolo_item = QtWidgets.QTableWidgetItem(str(yolo))
        yolo_max = QtWidgets.QTableWidgetItem(str(yolo_max))
        self.table.setItem(index, 0, desc_item)
        self.table.setItem(index, 1, yolo_item)
        self.table.setItem(index, 2, yolo_max)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    thing = QtTableWidgetThing()
    thing.add(0, "This is what it is", True, "Definitely TRUE!!!")
    thing.add(1, "This is what it aint!", True, "Most Definitely TRUE!!!")
    thing.add(2, "It's time to go", False, "NO YOLO")

    exit_code = app.exec_()
    sys.exit(exit_code)
