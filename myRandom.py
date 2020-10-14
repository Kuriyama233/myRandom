import xlrd
import numpy as np
import random
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from interface import Ui_MainWindow
import sys

class myRandom(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super(myRandom, self).__init__(parent)
        self.setupUi(self)
        self.status()

    def status(self):
        self.allcheck.stateChanged.connect(self.allcheckfunc)
        self.randomButton.clicked.connect(self.randomButtonfunc)

    def allcheckfunc(self):
        if self.allcheck.isChecked():
            for i in range(1, 12):
                eval('self.check' + str(i) + '.setChecked(True)')
        else:
            for i in range(1, 12):
                eval('self.check' + str(i) + '.setChecked(False)')


    def randomButtonfunc(self):
        count = []
        for i in range(1, 12):
            ischeck = eval('self.check' + str(i) + '.isChecked()')
            if ischeck:
                count.append(i)
        result = self.getResult(self.getData(), len(count))

        for index, i in enumerate(count):
            if eval('self.check' + str(i) + '.isChecked()'):
                eval('self.name' + str(i) + '.setText(result[index][0])')
                eval('self.number' + str(i) + '.setText(result[index][1])')


    def getData(self):
        rb = xlrd.open_workbook('2020届金融管理B班全员.xls')
        table = rb.sheets()[0]

        row = table.nrows
        col = table.ncols

        people = []
        for i in range(row):
            name = table.cell_value(i, 0)
            number = int(table.cell_value(i, 1))
            assert type(name) == str
            assert type(number) == int
            people.append([name, number])

        return np.array(people)

    def getResult(self, people:np.ndarray, count):
        def getPeople(index):
            return people[index]
        Interval = range(0, people.shape[0])
        randomIndex = random.sample(Interval, count)
        result = list(map(getPeople, randomIndex))
        return np.array(result)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    a = myRandom()
    a.show()
    sys.exit(app.exec_())


# people = getData()
# a = getResult(people, 9)
# print(a)