# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication , QMainWindow
from app.ui import MainWindow


def main():  # 应用入口
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
    pass
