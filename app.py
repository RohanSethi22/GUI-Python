import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def window():
   app = QApplication(sys.argv)

   w = QWidget()
   w.setWindowTitle("PyQt5")
   # Sets window position (x,y) relative to monitor & size(width,height)
   w.setGeometry(100,100,200,50)

   b = QLabel(w)
   b.setText("Hello World!")
   # Displaces the text within the window by given (x,y) coordinates
   b.move(50,20)
   w.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   window()
