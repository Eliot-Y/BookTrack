# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt6 UI code generator 6.5.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import res_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1109, 724)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(22, 108, 204, 255), stop:1 rgba(83, 190, 201, 255));\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.info_books_frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.info_books_frame.setStyleSheet("border: 2px solid rgba(255, 255, 255, 40);\n"
"background-color: rgb(170, 170, 255, 80);\n"
"border-radius: 13px;")
        self.info_books_frame.setObjectName("info_books_frame")
        self.Layout_books_info = QtWidgets.QHBoxLayout(self.info_books_frame)
        self.Layout_books_info.setObjectName("Layout_books_info")
        self.icon_label_1 = QtWidgets.QLabel(parent=self.info_books_frame)
        self.icon_label_1.setMinimumSize(QtCore.QSize(0, 60))
        self.icon_label_1.setMaximumSize(QtCore.QSize(100, 16777215))
        self.icon_label_1.setStyleSheet("border: none;\n"
"background-color:none;\n"
"padding-left: 27 px;\n"
"")
        self.icon_label_1.setText("")
        self.icon_label_1.setPixmap(QtGui.QPixmap(":/icons/icons_black/library_books_FILL0_wght400_GRAD0_opsz48.svg"))
        self.icon_label_1.setObjectName("icon_label_1")
        self.Layout_books_info.addWidget(self.icon_label_1)
        self.text_label_1 = QtWidgets.QLabel(parent=self.info_books_frame)
        self.text_label_1.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(20)
        font.setItalic(False)
        self.text_label_1.setFont(font)
        self.text_label_1.setStyleSheet("border: none;\n"
"/*font-weight: bold;*/\n"
"font-size: 20pt;\n"
"background-color:none;\n"
"")
        self.text_label_1.setObjectName("text_label_1")
        self.Layout_books_info.addWidget(self.text_label_1)
        self.amount_label = QtWidgets.QLabel(parent=self.info_books_frame)
        self.amount_label.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(20)
        self.amount_label.setFont(font)
        self.amount_label.setStyleSheet("border: none;\n"
"/*font-weight: bold;*/\n"
"font-size: 20pt;\n"
"background-color:none;\n"
"padding-left: 10px;")
        self.amount_label.setObjectName("amount_label")
        self.Layout_books_info.addWidget(self.amount_label)
        self.gap_label = QtWidgets.QLabel(parent=self.info_books_frame)
        self.gap_label.setStyleSheet("border: none;\n"
"/*font-weight: bold;*/\n"
"font-size: 20pt;\n"
"background-color:none;\n"
"padding-left: 20px;")
        self.gap_label.setText("")
        self.gap_label.setObjectName("gap_label")
        self.Layout_books_info.addWidget(self.gap_label)
        self.icon_label_2 = QtWidgets.QLabel(parent=self.info_books_frame)
        self.icon_label_2.setMinimumSize(QtCore.QSize(0, 60))
        self.icon_label_2.setMaximumSize(QtCore.QSize(70, 16777215))
        self.icon_label_2.setStyleSheet("border: none;\n"
"background-color:none;\n"
"padding-left: 15 px;\n"
"")
        self.icon_label_2.setText("")
        self.icon_label_2.setPixmap(QtGui.QPixmap(":/icons/icons_black/attach_money_FILL0_wght400_GRAD0_opsz48.svg"))
        self.icon_label_2.setObjectName("icon_label_2")
        self.Layout_books_info.addWidget(self.icon_label_2)
        self.text_label_2 = QtWidgets.QLabel(parent=self.info_books_frame)
        self.text_label_2.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(20)
        self.text_label_2.setFont(font)
        self.text_label_2.setStyleSheet("border: none;\n"
"/*font-weight: bold;*/\n"
"font-size: 20pt;\n"
"background-color:none;\n"
"")
        self.text_label_2.setObjectName("text_label_2")
        self.Layout_books_info.addWidget(self.text_label_2)
        self.total_price_label = QtWidgets.QLabel(parent=self.info_books_frame)
        self.total_price_label.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(20)
        self.total_price_label.setFont(font)
        self.total_price_label.setStyleSheet("border: none;\n"
"/*font-weight: bold;*/\n"
"font-size: 20pt;\n"
"background-color:none;\n"
"padding-left: 10px;")
        self.total_price_label.setObjectName("total_price_label")
        self.Layout_books_info.addWidget(self.total_price_label)
        self.verticalLayout.addWidget(self.info_books_frame)
        self.buttons_frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.buttons_frame.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255, 0);\n"
"")
        self.buttons_frame.setObjectName("buttons_frame")
        self.Layout_buttons = QtWidgets.QHBoxLayout(self.buttons_frame)
        self.Layout_buttons.setContentsMargins(12, 12, 12, 12)
        self.Layout_buttons.setSpacing(8)
        self.Layout_buttons.setObjectName("Layout_buttons")
        self.add_pushButton = QtWidgets.QPushButton(parent=self.buttons_frame)
        self.add_pushButton.setMinimumSize(QtCore.QSize(180, 65))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(14)
        self.add_pushButton.setFont(font)
        self.add_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.add_pushButton.setMouseTracking(False)
        self.add_pushButton.setAutoFillBackground(False)
        self.add_pushButton.setStyleSheet("QPushButton{\n"
"font-size: 14pt;\n"
"background-color: rgba(255, 255, 255, 10);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255, 80);\n"
"}\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons_black/add_circle_FILL0_wght400_GRAD0_opsz48.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.add_pushButton.setIcon(icon)
        self.add_pushButton.setIconSize(QtCore.QSize(30, 30))
        self.add_pushButton.setAutoDefault(False)
        self.add_pushButton.setDefault(False)
        self.add_pushButton.setFlat(False)
        self.add_pushButton.setObjectName("add_pushButton")
        self.Layout_buttons.addWidget(self.add_pushButton)
        self.edit_pushButton = QtWidgets.QPushButton(parent=self.buttons_frame)
        self.edit_pushButton.setMinimumSize(QtCore.QSize(180, 65))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei Light")
        font.setPointSize(14)
        self.edit_pushButton.setFont(font)
        self.edit_pushButton.setStyleSheet("QPushButton{\n"
"font-size: 14pt;\n"
"background-color: rgba(255, 255, 255, 10);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255, 80);\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons_black/edit_note_FILL0_wght400_GRAD0_opsz48.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.edit_pushButton.setIcon(icon1)
        self.edit_pushButton.setIconSize(QtCore.QSize(30, 30))
        self.edit_pushButton.setObjectName("edit_pushButton")
        self.Layout_buttons.addWidget(self.edit_pushButton)
        self.del_pushButton = QtWidgets.QPushButton(parent=self.buttons_frame)
        self.del_pushButton.setMinimumSize(QtCore.QSize(180, 65))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(14)
        self.del_pushButton.setFont(font)
        self.del_pushButton.setStyleSheet("QPushButton{\n"
"font-size: 14pt;\n"
"background-color: rgba(255, 255, 255, 10);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255, 80);\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons_black/delete_FILL0_wght400_GRAD0_opsz48.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.del_pushButton.setIcon(icon2)
        self.del_pushButton.setIconSize(QtCore.QSize(30, 30))
        self.del_pushButton.setObjectName("del_pushButton")
        self.Layout_buttons.addWidget(self.del_pushButton)
        self.filter_pushButton = QtWidgets.QPushButton(parent=self.buttons_frame)
        self.filter_pushButton.setMinimumSize(QtCore.QSize(180, 65))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(14)
        self.filter_pushButton.setFont(font)
        self.filter_pushButton.setStyleSheet("QPushButton{\n"
"font-size: 14pt;\n"
"background-color: rgba(255, 255, 255, 10);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255, 80);\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons_black/filter_alt_FILL0_wght400_GRAD0_opsz48.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.filter_pushButton.setIcon(icon3)
        self.filter_pushButton.setIconSize(QtCore.QSize(30, 30))
        self.filter_pushButton.setObjectName("filter_pushButton")
        self.Layout_buttons.addWidget(self.filter_pushButton)
        self.analytics_pushButton = QtWidgets.QPushButton(parent=self.buttons_frame)
        self.analytics_pushButton.setMinimumSize(QtCore.QSize(180, 65))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(14)
        self.analytics_pushButton.setFont(font)
        self.analytics_pushButton.setStyleSheet("QPushButton{\n"
"font-size: 14pt;\n"
"background-color: rgba(255, 255, 255, 10);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255, 80);\n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons_black/analytics_FILL0_wght400_GRAD0_opsz48.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.analytics_pushButton.setIcon(icon4)
        self.analytics_pushButton.setIconSize(QtCore.QSize(30, 30))
        self.analytics_pushButton.setObjectName("analytics_pushButton")
        self.Layout_buttons.addWidget(self.analytics_pushButton)
        self.verticalLayout.addWidget(self.buttons_frame)
        self.tableView = QtWidgets.QTableView(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(16)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.tableView.setFont(font)
        self.tableView.setStyleSheet("QTableView{\n"
"border: 1px solid rgba(255, 255, 255, 90);\n"
"background-color: rgba(255, 255, 255, 70);\n"
"border-bottom-left-radius: 8px;\n"
"border-bottom-right-radius: 8px; \n"
"}\n"
"\n"
"QHeaderView::section {\n"
"background-color: rgb(0, 159, 203);\n"
"border: 1px solid rgba(255, 255, 255, 100);\n"
"height: 50px;\n"
"font-size: 18pt;\n"
"font: 25 18pt \"Microsoft YaHei UI Light\";\n"
"}\n"
"\n"
"QTableView::item {\n"
"    border-style: none;\n"
"    border-bottom: 1px solid rgba(255,255,255,50);\n"
"    border-right: 1px solid rgba(255,255,255,50);\n"
"\n"
"}\n"
"\n"
"QTableView::item:selected{\n"
"    border:  rgba(255, 255, 255, 90);\n"
"    background-color: rgba(255, 255, 255, 70);\n"
"}\n"
"\n"
"\n"
"")
        self.tableView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tableView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tableView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableView.setTextElideMode(QtCore.Qt.TextElideMode.ElideRight)
        self.tableView.setShowGrid(False)
        self.tableView.setSortingEnabled(True)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setDefaultSectionSize(155)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableView)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BookTrack"))
        self.text_label_1.setText(_translate("MainWindow", "Всего книг"))
        self.amount_label.setText(_translate("MainWindow", "30"))
        self.text_label_2.setText(_translate("MainWindow", "Общая цена"))
        self.total_price_label.setText(_translate("MainWindow", "10 000"))
        self.add_pushButton.setText(_translate("MainWindow", "Добавить"))
        self.edit_pushButton.setText(_translate("MainWindow", "Редактировать"))
        self.del_pushButton.setText(_translate("MainWindow", "Удалить"))
        self.filter_pushButton.setText(_translate("MainWindow", "Фильтр"))
        self.analytics_pushButton.setText(_translate("MainWindow", "Аналитика"))
