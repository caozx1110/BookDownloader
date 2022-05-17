# coding=utf-8
"""
author: Cao Zhanxiang
project: Crawler
file: Crawler_DataSheet.py
date: 2021/6/11
function: 从TI.com中爬取datasheet，带搜索功能
"""

import requests
import re
from io import BytesIO
from PIL import Image
from PyQt5.QtCore import pyqtSignal
import os

# FOLDERNAME = "C:/Users/q7423/Desktop/doing/"
FOLDERNAME = ""

Header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.63'
}


# Search 对输入关键词进行搜索
def Search(keyword) -> list:
    # 通过解析网页找到如下链接
    # 可能有多页
    IsEnd = False
    idx = 1
    SearchResult = []
    while (not IsEnd) and (keyword != ''):
        result = requests.get(
            "http://reserves.lib.tsinghua.edu.cn/Search/ResBooks?bookName=" + keyword + "&page=" + str(idx),
            headers=Header)
        idx = idx + 1
        result.encoding = result.apparent_encoding
        TempFoundBook = re.findall(
            'img border=".*?" height=".*?" src="(.*?)/html5/m/1.jpg" width=".*?" />\s*</a>\s*<p><strong>(.*?)</strong></p>',
            result.text)
        # print(TempFoundBook)
        if not TempFoundBook.__len__():
            IsEnd = True
        SearchResult.extend(TempFoundBook)

    return SearchResult


# 根据搜索+用户确定的书名全称下载pdf
def DownLoad(FolderName, bookidx, bookname, currentidx) -> bool:
    # print("loading...")
    # THU的网站真TM辣鸡
    # /files/mobile/1.jpg
    IsChapterEnd = False
    IsBookEnd = False
    ChangedBookIdx = bookidx
    ChapterIdx = 1
    PageIdx = 1
    PdfName = FolderName + bookname.split('=')[0] + ".pdf"
    # 删除不能存在于文件名中的符号
    for NotUsed in ['\\', '/', ':', '*', '?', '\"', '>', '<', '|']:
        PdfName = PdfName.replace(NotUsed, '')
    fp = open(PdfName, 'w')
    print("PdfName: ", PdfName)
    print("InitBookIdx: ", bookidx)
    BookIdxList = bookidx.split('/')
    BookIdxList.remove('')
    ChapterChange = BookIdxList[-1]     # 新一章节需要更新的部分
    print(BookIdxList)
    fp.close()
    while not IsBookEnd:
        IsChapterEnd = False
        while not IsChapterEnd:
            print("Chapter.Page: " + str(ChapterIdx) + '.' + str(PageIdx))
            currentidx.emit(str(ChapterIdx) + '.' + str(PageIdx))   # 发射信号，当前下载的页数
            Result = requests.get('http://reserves.lib.tsinghua.edu.cn/' + ChangedBookIdx + '/files/mobile/' + str(PageIdx) + '.jpg')
            print('http://reserves.lib.tsinghua.edu.cn/' + ChangedBookIdx + '/files/mobile/' + str(PageIdx) + '.jpg')
            # print("status_code: ", Result.status_code)
            flag = False
            if Result.status_code == 200:
                try:
                    TempImg = Image.open(BytesIO(Result.content))
                    TempImg.convert('RGB').save(PdfName, append=bool(PageIdx))
                    PageIdx = PageIdx + 1
                except:
                    flag = True
            else:
                flag = True

            if flag:
                # 如果是第一页就下载失败,则本书下载完成
                if PageIdx == 1:
                    IsChapterEnd = True
                    IsBookEnd = True
                # 否则进入下一章
                elif len(BookIdxList) >= 3:
                    # zfill给int的前方补零
                    ChangedBookIdx = bookidx.replace(BookIdxList[-1], str((int(BookIdxList[-1]) + ChapterIdx)).zfill(len(BookIdxList[-1])))
                    print("ChangedBookIdx: ", ChangedBookIdx)
                    # 更新Idx
                    ChapterIdx = ChapterIdx + 1
                    PageIdx = 1
                    IsChapterEnd = True

    return IsBookEnd


if __name__ == '__main__':
    KeyWord = input("请输入器件名（直接回车则退出）：")

    # 如果不为空则继续等待输入
    while KeyWord != "":
        # 搜索关键词
        FoundInstName = Search(KeyWord)

        # 确定想找的元件
        if FoundInstName.__len__():
            print("您要找的是以下哪个元件？")
            for i in range(FoundInstName.__len__()):
                print(str(i + 1) + ": " + FoundInstName[i])
            NeedIdx = int(input("请输入数字代号："))
        else:
            print("抱歉，未找到相关文件")

        # 下载所选文件
        IsD = DownLoad(FOLDERNAME, FoundInstName[NeedIdx - 1])
        if IsD:
            print("Download " + FoundInstName[NeedIdx - 1] + ".pdf successfully")
        else:
            print("Can not find the instrument!")

        KeyWord = input("请输入器件名（直接回车则退出）：")

    print("Please refer to " + FOLDERNAME)
