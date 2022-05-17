# coding=utf-8
"""
author: Cao Zhanxiang
project: Crawler_DataSheet.py
file: MainProgress.py
date: 2021/6/11
function: 爬虫实现，转移自Crawler_DataSheet.py，多线程
"""

import Crawler_Book as Cb
from PyQt5.QtCore import QThread, pyqtSignal


# 搜索线程
class SearchThread(QThread):
    # 结束信号
    SearchFinished = pyqtSignal(list)
    SearchResult: list
    KeyWord: str

    # 参数从构造函数传入
    def __init__(self, kw):
        super(SearchThread, self).__init__()
        self.KeyWord = kw

    def run(self):
        self.SearchResult = Cb.Search(self.KeyWord)
        # 参数传出，靠信号发出
        self.SearchFinished.emit(self.SearchResult)


# 下载线程
class DownloadThread(QThread):
    # 结束信号
    DownloadFinished = pyqtSignal(bool, str, str)
    DownloadIdx = pyqtSignal(str)    # 用于显示当前下载的页数
    FolderName: str
    BookIdx: str
    BookName: str
    IsDownload: bool

    def __init__(self, fn, bi, bn):
        super(DownloadThread, self).__init__()
        self.FolderName = fn
        self.BookIdx = bi
        self.BookName = bn

    def run(self):
        self.IsDownload = Cb.DownLoad(self.FolderName, self.BookIdx, self.BookName, self.DownloadIdx)
        # 参数传出，靠信号发出
        self.DownloadFinished.emit(self.IsDownload, self.BookIdx, self.BookName)


# 主流程
class MainProgress:
    SearchResult: list
    FolderName: str
    SThread: SearchThread
    DThread: DownloadThread

    def __init__(self, fn=""):
        self.FolderName = fn

    def ChangeFolderName(self, nfn):
        self.FolderName = nfn

    def Search(self, KeyWord):
        self.SThread = SearchThread(KeyWord)
        self.SThread.start()

    def Download(self, BookIdx, BookName):
        self.DThread = DownloadThread(self.FolderName, BookIdx, BookName)
        self.DThread.start()

