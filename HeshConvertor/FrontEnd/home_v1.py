import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PIL import Image
from pathlib import Path
from pygost.gost34112012 import GOST34112012

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(382, 391)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(50, 80, 281, 61))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 2, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(50, 170, 281, 80))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 0, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_2.addWidget(self.pushButton_4, 0, 1, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(50, 280, 281, 41))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 382, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_2.setEnabled(False)
        self.pushButton_3.hide()
        self.pushButton_4.hide()


        self.pushButton.clicked.connect(self.open_inage)
        self.pushButton_2.clicked.connect(self.start_project)
        self.pushButton_3.clicked.connect(self.open_hesh)
        self.pushButton_4.clicked.connect(self.open_pnm)

    def open_inage(self):

        x = self.comboBox.currentText()
        global format_file

        if x == 'JPG':
            format_file = 'JPG'

        elif x == 'PNG':
            format_file = 'PNG'

        elif x == 'BMP':
            format_file = 'BMP'

        elif x == 'WEBP':
            format_file = 'WEBP'

        else:
            format_file = '-'
            self.pushButton_2.setEnabled(False)

        if format_file == '-':
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ошибка")
            msg.setInformativeText('Не выбран файл!')
            msg.setWindowTitle("Error")
            msg.exec_()
            self.pushButton_2.setEnabled(False)

        else:
            global file_pic
            file_pic, check = QFileDialog.getOpenFileName(None, f'Выберите изображения {format_file}',
                                                          'Data/Image', f'{format_file} Files (*.{format_file})')
            if check:
                self.pushButton_2.setEnabled(True)

            else:
                file_pic = '-'
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setInformativeText('Не выбран файл!')
                msg.setWindowTitle("Attention")
                msg.exec_()

    def start_project(self):

        if file_pic == '-':
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setInformativeText('Не выбран файл!')
            msg.setWindowTitle("Attention")
            msg.exec_()

        else:
            global path

            test_data = bytes(f'{file_pic}', encoding='utf-8')
            path = Path(f'{file_pic}').stem
            m = GOST34112012(digest_size=256)
            m.update(test_data)
            hesh = m.hexdigest()
            img = Image.open(test_data)
            img.save(f'Data/OutputData/PNM/{path}.pnm')
            with open(f'Data/OutputData/Hesh/hesh_{path}.txt', "w") as output:
                output.write(str(hesh))

            self.pushButton_3.show()
            self.pushButton_4.show()
    def open_hesh(self):

        f = (f'Data/OutputData/Hesh/hesh_{path}.txt')
        ff = open(f, "r")

        gg = (ff.read())

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("ХЭШ исходного файла")
        msg.setInformativeText(f'{gg}')
        msg.exec_()

    def open_pnm(self):

        img = f'Data/OutputData/PNM/{path}.pnm'
        path__ = os.path.realpath(img)
        os.startfile(path__)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SadCat Inc."))
        self.pushButton.setText(_translate("MainWindow", "Выбрать изображение"))
        self.comboBox.setItemText(0, _translate("MainWindow", "-"))
        self.comboBox.setItemText(1, _translate("MainWindow", "JPG"))
        self.comboBox.setItemText(2, _translate("MainWindow", "PNG"))
        self.comboBox.setItemText(3, _translate("MainWindow", "BMP"))
        self.comboBox.setItemText(4, _translate("MainWindow", "WEBP"))
        self.pushButton_2.setText(_translate("MainWindow", "Go!"))
        self.label_2.setText(_translate("MainWindow", "Нормализация графики"))
        self.pushButton_3.setText(_translate("MainWindow", "Открыть Хэш\n"
"исходного файла"))
        self.pushButton_4.setText(_translate("MainWindow", "Открыть файл\n"
" в формате PNM"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

