# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/ayieko/Projects And  Research/PycharmProjects/HttpServer/GUI/MainDesign.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(881, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.eventLogEdit = QtWidgets.QTextEdit(self.splitter)
        self.eventLogEdit.setReadOnly(True)
        self.eventLogEdit.setObjectName("eventLogEdit")
        self.ConnectionsTableWidget = QtWidgets.QTableWidget(self.splitter)
        self.ConnectionsTableWidget.setObjectName("ConnectionsTableWidget")
        self.ConnectionsTableWidget.setColumnCount(6)
        self.ConnectionsTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.ConnectionsTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ConnectionsTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ConnectionsTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.ConnectionsTableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.ConnectionsTableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.ConnectionsTableWidget.setHorizontalHeaderItem(5, item)
        self.verticalLayout.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 881, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuServer = QtWidgets.QMenu(self.menubar)
        self.menuServer.setObjectName("menuServer")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuServer.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.ConnectionsTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.ConnectionsTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Account"))
        item = self.ConnectionsTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "IP Address"))
        item = self.ConnectionsTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Transfer"))
        item = self.ConnectionsTableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Progress"))
        item = self.ConnectionsTableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Speed"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuServer.setTitle(_translate("MainWindow", "Server"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
