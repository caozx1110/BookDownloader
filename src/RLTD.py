# coding=utf-8
"""
author: Cao Zhanxiang
project: RLTD(ReservesLibTsinghuaDownload
file: RLTD.py
date: 2021/6/25
function: 主程序
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from MainWindowUI import *
from MainProgress import MainProgress
from PyQt5.QtWidgets import QStyleFactory
import RLTD_rc


class MainWindow(QtWidgets.QWidget, Ui_RLTD):
    Mp = MainProgress()
    SearchResult: list
    idx: int

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon(":/RLTD.ico"))
        QtWidgets.QApplication.setStyle(QStyleFactory.create('Fusion'))

    # 按下search
    def pbt_Search_clicked(self):
        self.lbl_Msg.setText("Searching...")
        KeyWord = self.ledt_KeyWord.text()
        if KeyWord == "生石灰":
            self.lbl_Msg.setText("This is the app author!")
        self.Mp.Search(KeyWord)
        # 连接槽函数，如接收到线程发来的搜索结束信息
        self.Mp.SThread.SearchFinished.connect(self.slot_SearchFinished)

    # 搜索结束
    def slot_SearchFinished(self, searchresult):
        self.SearchResult = searchresult
        KeyWord = self.ledt_KeyWord.text()
        if KeyWord == "生石灰":
            self.lbl_Msg.setText("This is the app author!")
        else:
            self.lbl_Msg.setText("Search Finished.")
        # 设置指示信息
        if self.SearchResult.__len__():
            self.lbl_SearchResult.setText("搜索结果如下:")
        else:
            self.lbl_SearchResult.setText("未搜索到相关信息.")

        # 显示搜索结果
        self.tblw_SearchResult.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tblw_SearchResult.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)  # 不可编辑
        self.tblw_SearchResult.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)    # 不可选择
        self.tblw_SearchResult.setRowCount(self.SearchResult.__len__())  # 行数
        self.tblw_SearchResult.setColumnCount(2)  # 列数
        self.tblw_SearchResult.setHorizontalHeaderLabels(["书名", "操作"])  # 表头
        # 显示名称，按钮
        for i in range(self.SearchResult.__len__()):
            NewItem = QtWidgets.QTableWidgetItem(self.SearchResult[i][1])
            NewButton = QtWidgets.QPushButton("下载")
            NewButton.setStyleSheet(''' font-family: 微软雅黑;
                                        font-size: 16px;
                                        text-align: center;
                                        height: 30px;
                                        width: 40px; ''')
            # NewButton.setMaximumWidth(80)   # 按钮最大宽度
            NewButton.clicked.connect(self.pbt_Download_clicked)
            # 居中
            NewItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.tblw_SearchResult.setItem(i, 0, NewItem)
            self.tblw_SearchResult.setCellWidget(i, 1, NewButton)

    # 按下回车
    def ledt_KeyWord_returnPressed(self):
        self.pbt_Search_clicked()

    # 点击下载
    def pbt_Download_clicked(self):
        self.lbl_Msg.setText("Downloading...")
        button = self.sender()
        idx = self.tblw_SearchResult.indexAt(button.pos()).row()
        # 设置不可点击
        self.tblw_SearchResult.cellWidget(idx, 1).setEnabled(False)
        self.Mp.Download(self.SearchResult[idx][0], self.SearchResult[idx][1])
        self.Mp.DThread.DownloadIdx.connect(self.slot_DownloadIdx)      # 当前下载页数
        self.Mp.DThread.DownloadFinished.connect(self.slot_DownloadFinished)

    def slot_DownloadIdx(self, currentidx):
        self.lbl_Msg.setText("Downloading Page " + str(currentidx) + "...")

    # 下载完成
    def slot_DownloadFinished(self, isdownload, bookidx, bookname):
        # bookidx指的是网站上书的编号
        # 找到对应下载好的idx
        idx = self.SearchResult.index((bookidx, bookname))
        # 重新激活按钮
        self.tblw_SearchResult.cellWidget(idx, 1).setEnabled(True)
        # QtWidgets.QApplication.processEvents()
        if isdownload:
            self.tblw_SearchResult.cellWidget(idx, 1).setText("下载成功")
            self.lbl_Msg.setText("Download successfully.")
        else:
            self.lbl_Msg.setText("Please retry.")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())





