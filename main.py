#entry point for the application
from PyQt5.QtWidgets import QApplication, QtWidgets
import sys

#passing in the system argument into the application
app = QApplication(sys.argv)
window = QWidget()
window.show()

app.exec()
