import sys
from PyQt5 import QtGui, QtWidgets

import des
import subprocess
class ExampleApp(QtWidgets.QMainWindow, des.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

def main():

    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    File = open("Combinear.qss", 'r')
    with File:
        qss = File.read()
        app.setStyleSheet(qss)
    window.show()
    app.exec_()



with open('countd.txt', 'wb', 0) as file:
    subprocess.Popen(r'c:\windows\system32\cmd.exe /C wmic logicaldisk get description,name', stdout=file)

if __name__ == '__main__':
    main()