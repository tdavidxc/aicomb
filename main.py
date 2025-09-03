#entry point for the application
import sys
from PyQt5.QtWidgets import QApplication, QWidget

#passing in the system argument into the application
def main():
    app = QApplication(sys.argv)

    #creating main window
    window = QWidget()
    window.setWindowTitle("aicomb")
    window.resize(800, 600)
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()

