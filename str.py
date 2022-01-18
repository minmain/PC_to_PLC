
from pyModbusTCP.client import ModbusClient
c = ModbusClient(host="192.168.1.30", port=502, auto_open=True)
regs = c.read_holding_registers(0,3)
if regs:
         print(regs[0],regs[1], regs[2] ,sep='\n')
else:
         print("ㅠㅠ")

c.close()


import sys
from plc import Ui_MainWindow  # 수정부분
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class plc(QMainWindow, Ui_MainWindow):

     def __init__(self, parent = None):
         super().__init__(parent)
         self.ui = uic.loadUi("plc.ui", self)
         self.ui.show()

         self.pb1.clicked.connect(self.sand)
         self.pb2.clicked.connect(self.end)

     def sand(self):
          self.textEdit.setText('전송중...')
          print(regs[0])

     def end(self):
          self.textEdit.setText('종료됨...')
          print(regs[0])


if __name__ == "__main__":
    print("Hello Word");


app = QApplication([])
sn = plc()
QApplication.processEvents()
sys.exit(app.exec_())



