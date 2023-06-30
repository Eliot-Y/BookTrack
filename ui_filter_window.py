# Form implementation generated from reading ui file 'filter_window.ui'
#
# Created by: PyQt6 UI code generator 6.5.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import res_ad_ed


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 670)
        Dialog.setMinimumSize(QtCore.QSize(400, 670))
        Dialog.setMaximumSize(QtCore.QSize(400, 672))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        Dialog.setFont(font)
        Dialog.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(22, 108, 204, 255), stop:1 rgba(83, 190, 201, 255));\n"
"")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(parent=Dialog)
        self.frame.setStyleSheet("border: none;\n"
"border-radius: 8px;\n"
"background-color: rgba(255, 255, 255, 40);\n"
"")
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.new_data_label = QtWidgets.QLabel(parent=self.frame)
        self.new_data_label.setMaximumSize(QtCore.QSize(10000, 50))
        self.new_data_label.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(20)
        self.new_data_label.setFont(font)
        self.new_data_label.setAutoFillBackground(False)
        self.new_data_label.setStyleSheet("border: none;\n"
"/*font-weight: bold;*/\n"
"font-size: 20pt;\n"
"background-color:none;\n"
"\n"
"")
        self.new_data_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.new_data_label.setObjectName("new_data_label")
        self.verticalLayout.addWidget(self.new_data_label)
        self.le_id_description = QtWidgets.QLineEdit(parent=self.frame)
        self.le_id_description.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(14)
        self.le_id_description.setFont(font)
        self.le_id_description.setAutoFillBackground(False)
        self.le_id_description.setStyleSheet("font-size: 14pt;\n"
"height: 40px;")
        self.le_id_description.setObjectName("le_id_description")
        self.verticalLayout.addWidget(self.le_id_description)
        self.le_title_description = QtWidgets.QLineEdit(parent=self.frame)
        self.le_title_description.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(14)
        self.le_title_description.setFont(font)
        self.le_title_description.setAutoFillBackground(False)
        self.le_title_description.setStyleSheet("font-size: 14pt;\n"
"height: 40px;")
        self.le_title_description.setObjectName("le_title_description")
        self.verticalLayout.addWidget(self.le_title_description)
        self.le_author_description = QtWidgets.QLineEdit(parent=self.frame)
        self.le_author_description.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(14)
        self.le_author_description.setFont(font)
        self.le_author_description.setAutoFillBackground(False)
        self.le_author_description.setStyleSheet("font-size: 14pt;\n"
"height: 40px;")
        self.le_author_description.setObjectName("le_author_description")
        self.verticalLayout.addWidget(self.le_author_description)
        self.le_genre_description = QtWidgets.QLineEdit(parent=self.frame)
        self.le_genre_description.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(14)
        self.le_genre_description.setFont(font)
        self.le_genre_description.setStyleSheet("font-size: 14pt;\n"
"height: 40px;")
        self.le_genre_description.setObjectName("le_genre_description")
        self.verticalLayout.addWidget(self.le_genre_description)
        self.le_date_from = QtWidgets.QLineEdit(parent=self.frame)
        self.le_date_from.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(14)
        self.le_date_from.setFont(font)
        self.le_date_from.setStyleSheet("font-size: 14pt;\n"
"height: 40px;")
        self.le_date_from.setObjectName("le_date_from")
        self.verticalLayout.addWidget(self.le_date_from)
        self.le_date_last = QtWidgets.QLineEdit(parent=self.frame)
        self.le_date_last.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(14)
        self.le_date_last.setFont(font)
        self.le_date_last.setStyleSheet("font-size: 14pt;\n"
"height: 40px;")
        self.le_date_last.setObjectName("le_date_last")
        self.verticalLayout.addWidget(self.le_date_last)
        self.cb_status_description = QtWidgets.QComboBox(parent=self.frame)
        self.cb_status_description.setMinimumSize(QtCore.QSize(0, 50))
        self.cb_status_description.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.cb_status_description.setFont(font)
        self.cb_status_description.setStyleSheet("QComboBox{\n"
"font-size: 16pt;\n"
"height: 40px;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(22, 108, 204, 255), stop:1 rgba(83, 190, 201, 255));\n"
"}\n"
"")
        self.cb_status_description.setEditable(False)
        self.cb_status_description.setObjectName("cb_status_description")
        self.cb_status_description.addItem("")
        self.cb_status_description.setItemText(0, "")
        self.cb_status_description.addItem("")
        self.cb_status_description.addItem("")
        self.cb_status_description.addItem("")
        self.cb_status_description.addItem("")
        self.verticalLayout.addWidget(self.cb_status_description)
        self.le_from_price_description = QtWidgets.QLineEdit(parent=self.frame)
        self.le_from_price_description.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(14)
        self.le_from_price_description.setFont(font)
        self.le_from_price_description.setStyleSheet("font-size: 14pt;\n"
"height: 40px;")
        self.le_from_price_description.setText("")
        self.le_from_price_description.setObjectName("le_from_price_description")
        self.verticalLayout.addWidget(self.le_from_price_description)
        self.le_top_price_description = QtWidgets.QLineEdit(parent=self.frame)
        self.le_top_price_description.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(14)
        self.le_top_price_description.setFont(font)
        self.le_top_price_description.setStyleSheet("font-size: 14pt;\n"
"height: 40px;")
        self.le_top_price_description.setText("")
        self.le_top_price_description.setObjectName("le_top_price_description")
        self.verticalLayout.addWidget(self.le_top_price_description)
        self.find_pushButton = QtWidgets.QPushButton(parent=self.frame)
        self.find_pushButton.setMinimumSize(QtCore.QSize(0, 65))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(14)
        self.find_pushButton.setFont(font)
        self.find_pushButton.setStyleSheet("QPushButton{\n"
"font-size: 14pt;\n"
"background-color: rgba(255, 255, 255, 10);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 6px;\n"
"height: 60px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255, 80);\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/icons_black/search_FILL0_wght400_GRAD0_opsz48.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.find_pushButton.setIcon(icon)
        self.find_pushButton.setIconSize(QtCore.QSize(30, 30))
        self.find_pushButton.setObjectName("find_pushButton")
        self.verticalLayout.addWidget(self.find_pushButton)
        self.verticalLayout_2.addWidget(self.frame)

        self.retranslateUi(Dialog)
        self.cb_status_description.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "filter"))
        self.new_data_label.setText(_translate("Dialog", "Фильтр"))
        self.le_id_description.setPlaceholderText(_translate("Dialog", "id"))
        self.le_title_description.setPlaceholderText(_translate("Dialog", "Название"))
        self.le_author_description.setPlaceholderText(_translate("Dialog", "Автор"))
        self.le_genre_description.setPlaceholderText(_translate("Dialog", "Жанр"))
        self.le_date_from.setPlaceholderText(_translate("Dialog", "Дата от: 2007-12-31"))
        self.le_date_last.setPlaceholderText(_translate("Dialog", "Дата до: 2014.10.23"))
        self.cb_status_description.setItemText(1, _translate("Dialog", "В планах"))
        self.cb_status_description.setItemText(2, _translate("Dialog", "Брошено"))
        self.cb_status_description.setItemText(3, _translate("Dialog", "В процессе"))
        self.cb_status_description.setItemText(4, _translate("Dialog", "Прочитано"))
        self.le_from_price_description.setPlaceholderText(_translate("Dialog", "Цена от:"))
        self.le_top_price_description.setPlaceholderText(_translate("Dialog", "Цена до:"))
        self.find_pushButton.setText(_translate("Dialog", "Поиск"))