#coding:utf-8

import xlwt
import os

Format = ['mp4','mkv','rmvb','avi']

class Xlfile(object):

    def getAllDir(self,pathEntrance, filelis):
        if os.path.exists(pathEntrance):
            li = os.listdir(pathEntrance)
            if len(li) != 0:
                for subDir in li:
                    if os.path.isdir(pathEntrance + '\\' + subDir):
                        self.getAllDir(pathEntrance + "\\" + subDir, filelis)
                    else:
                        if subDir.lower().split('.')[1] in Format:
                            filelis.append(pathEntrance + "\\" + subDir)

    def writeXlsx(self,xlsName,sheetName,filelis):
        workbook = xlwt.Workbook(encoding="ascii")
        worksheet = workbook.add_sheet(sheetName)
        i = 0
        for fan in filelis:
            part = str(fan).rsplit("\\",1)
            worksheet.write(i, 0, label = part[0])
            worksheet.write(i,1,label = part[1])
            i = i + 1
        workbook.save(xlsName)

if __name__ == '__main__':
    xls = Xlfile()
    file_li = []
    xls.getAllDir(R"F:/TCP",file_li)
    xls.writeXlsx("li.xls","sheet1",file_li)
