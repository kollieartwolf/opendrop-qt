#!/usr/bin/env python

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, \
    QGridLayout
from PyQt5.QtCore import QSettings, QTranslator
import subprocess as sb


class OpenDropQt(QMainWindow):
    company_str = "CCLC"
    project_str = "opendrop-qt"

    def __init__(self, parent=None):
        super().__init__()
        if parent:
            self.setParent(parent)
        self.resize(300, 500)
        self.main_layout = QGridLayout()
        self.setLayout(self.main_layout)
        self.settings = QSettings(self.company_str, self.project_str)
        if 'init_completed' not in self.settings.allKeys():
            self.setup_initial()
        self.sb_owl = None
        self.sb_opendrop = None

    def setup_initial(self):
        print('We are here!')
        setup_container = QWidget()
        setup_container.setLayout(QVBoxLayout())
        initial_setup_label = QLabel(self.tr('Welcome to the initial setup of OpenDropQt!'))
        setup_container.layout().addWidget(initial_setup_label)
        self.main_layout.addWidget(setup_container)
    
    def start_owl(self):
        self.sb_owl = sb.Popen(["pkexec"])


def main():
    translator = QTranslator()
    translator.load('ru.qm')
    app = QApplication([])
    app.installTranslator(translator)
    w = OpenDropQt()
    w.show()
    return app.exec()


if __name__ == "__main__":
    main()
