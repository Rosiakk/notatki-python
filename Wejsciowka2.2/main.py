import sys
from MainWidget import MainWidget
from PySide6.QtWidgets import QApplication, QWidget



def main():

    app = QApplication(sys.argv)
    wideget = MainWidget()
    wideget.show()
    return app.exec_()


if __name__ == '__main__':
    main()