# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindowUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RLTD(object):
    def setupUi(self, RLTD):
        RLTD.setObjectName("RLTD")
        RLTD.setEnabled(True)
        RLTD.resize(490, 547)
        RLTD.setMinimumSize(QtCore.QSize(300, 400))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        RLTD.setFont(font)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(RLTD)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.ledt_KeyWord = QtWidgets.QLineEdit(RLTD)
        self.ledt_KeyWord.setMinimumSize(QtCore.QSize(0, 40))
        self.ledt_KeyWord.setText("")
        self.ledt_KeyWord.setObjectName("ledt_KeyWord")
        self.horizontalLayout.addWidget(self.ledt_KeyWord)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pbt_Search = QtWidgets.QPushButton(RLTD)
        self.pbt_Search.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pbt_Search.setFont(font)
        self.pbt_Search.setObjectName("pbt_Search")
        self.horizontalLayout.addWidget(self.pbt_Search)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.lbl_SearchResult = QtWidgets.QLabel(RLTD)
        self.lbl_SearchResult.setText("")
        self.lbl_SearchResult.setObjectName("lbl_SearchResult")
        self.verticalLayout.addWidget(self.lbl_SearchResult)
        self.tblw_SearchResult = QtWidgets.QTableWidget(RLTD)
        self.tblw_SearchResult.setObjectName("tblw_SearchResult")
        self.tblw_SearchResult.setColumnCount(0)
        self.tblw_SearchResult.setRowCount(0)
        self.verticalLayout.addWidget(self.tblw_SearchResult)
        self.lbl_Msg = QtWidgets.QLabel(RLTD)
        self.lbl_Msg.setText("")
        self.lbl_Msg.setObjectName("lbl_Msg")
        self.verticalLayout.addWidget(self.lbl_Msg)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(RLTD)
        self.pbt_Search.clicked.connect(RLTD.pbt_Search_clicked)
        self.ledt_KeyWord.returnPressed.connect(RLTD.ledt_KeyWord_returnPressed)
        QtCore.QMetaObject.connectSlotsByName(RLTD)

    def retranslateUi(self, RLTD):
        _translate = QtCore.QCoreApplication.translate
        RLTD.setWindowTitle(_translate("RLTD", "RLTD"))
        self.ledt_KeyWord.setPlaceholderText(_translate("RLTD", "请输入书本名称..."))
        self.pbt_Search.setText(_translate("RLTD", "搜索"))