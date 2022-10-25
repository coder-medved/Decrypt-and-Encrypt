from PyQt6.QtWidgets import QApplication, QMainWindow, QMenu, QMenuBar, QFrame, QLabel, QStatusBar, QWidget, QTabWidget, QPushButton, QLineEdit
from PyQt6.QtGui import QIcon, QPixmap, QFont
from PyQt6.QtCore import QSize, Qt, QRect, QMetaObject, QCoreApplication


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(580, 200)
        MainWindow.setMinimumSize(QSize(580, 200))
        MainWindow.setMaximumSize(QSize(580, 200))
        icon = QIcon(QPixmap("../Files/icons8_lock_file.ico"))
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget_2 = QTabWidget(self.centralwidget)
        self.tabWidget_2.setGeometry(QRect(10, 20, 401, 131))
        self.tabWidget_2.setElideMode(Qt.TextElideMode.ElideLeft)
        self.tabWidget_2.setDocumentMode(False)
        self.tabWidget_2.setTabsClosable(False)
        self.tabWidget_2.setMovable(True)
        self.tabWidget_2.setTabBarAutoHide(False)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.encoder_2 = QWidget()
        self.encoder_2.setObjectName("encoder_2")
        self.pushButton_7 = QPushButton(self.encoder_2)
        self.pushButton_7.setGeometry(QRect(290, 20, 81, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QPushButton(self.encoder_2)
        self.pushButton_8.setGeometry(QRect(290, 60, 81, 31))
        self.pushButton_8.setObjectName("pushButton_8")
        self.lineEdit_3 = QLineEdit(self.encoder_2)
        self.lineEdit_3.setGeometry(QRect(10, 20, 261, 31))
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lineEdit_3.setText("")
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setClearButtonEnabled(False)
        self.lineEdit_3.setObjectName("lineEdit_3")
        icon1 = QIcon()
        icon1.addPixmap(QPixmap("../Files/Icons/Encode.ico"))
        self.tabWidget_2.addTab(self.encoder_2, icon1, "")
        self.decoder_2 = QWidget()
        self.decoder_2.setObjectName("decoder_2")
        self.pushButton_9 = QPushButton(self.decoder_2)
        self.pushButton_9.setGeometry(QRect(290, 20, 81, 31))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QPushButton(self.decoder_2)
        self.pushButton_10.setGeometry(QRect(290, 60, 81, 31))
        self.pushButton_10.setObjectName("pushButton_10")
        self.lineEdit_4 = QLineEdit(self.decoder_2)
        self.lineEdit_4.setGeometry(QRect(10, 20, 261, 31))
        font = QFont(pointSize=10, weight=50)
        font.setBold(False)
        font.setKerning(True)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lineEdit_4.setText("")
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setClearButtonEnabled(False)
        self.lineEdit_4.setObjectName("lineEdit_4")
        icon2 = QIcon(QPixmap("../Files/Icons/Decode.ico"))
        self.tabWidget_2.addTab(self.decoder_2, icon2, "")
        self.frame = QFrame(self.centralwidget)
        self.frame.setGeometry(QRect(440, 30, 121, 120))
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setGeometry(QRect(25, 40, 80, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setGeometry(QRect(25, 80, 80, 30))
        self.pushButton.setObjectName("pushButton")
        self.label = QLabel(self.frame)
        self.label.setGeometry(QRect(25, 10, 100, 20))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 580, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout_us = QMenu(self.menubar)
        self.menuAbout_us.setObjectName("menuAbout_us")
        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout_us.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget_2.setCurrentIndex(1)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Кодировщик файлов"))
        self.pushButton_7.setText(_translate("MainWindow", "Открыть файл"))
        self.pushButton_8.setText(_translate("MainWindow", "Зашифровать"))
        self.lineEdit_3.setPlaceholderText(
            _translate("MainWindow", "Путь файла"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(
            self.encoder_2), _translate("MainWindow", "Кодировщик"))
        self.tabWidget_2.setTabToolTip(self.tabWidget_2.indexOf(self.encoder_2), _translate(
            "MainWindow", "<html><head/><body><p>You can encode your file here</p></body></html>"))
        self.pushButton_9.setText(_translate("MainWindow", "Открыть файл"))
        self.pushButton_10.setText(_translate("MainWindow", "Расшифровать"))
        self.lineEdit_4.setPlaceholderText(
            _translate("MainWindow", "Путь файла"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(
            self.decoder_2), _translate("MainWindow", "Зашифровать"))
        self.tabWidget_2.setTabToolTip(self.tabWidget_2.indexOf(self.decoder_2), _translate(
            "MainWindow", "<html><head/><body><p>You can decode your file here</p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Загрузить КЛЮЧ"))
        self.pushButton.setText(_translate("MainWindow", "Генерировать КЛЮЧ"))
        self.label.setText(_translate("MainWindow", "Ключ: "))
        self.menuFile.setTitle(_translate("MainWindow", "Помощь"))
        self.menuAbout_us.setTitle(_translate("MainWindow", "Обо мне"))


if __name__ == "__main__":
    import sys
    app = QApplication([])
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())