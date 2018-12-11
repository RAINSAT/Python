import os

def finddir(path):
    list = []
    if os.path.isdir(path):
        fd = open('qt.txt','a+')
        list = os.listdir(path)
        for i in range(len(list)):
            pat = '\"' +str(path) + '/' + str(list[i]) + '\"'+ '\r\n' 
            fd.write(pat)
        fd.close()


def main():
    curDir = 'D:/Qt/5.9.2/mingw53_32/include'
    finddir(curDir)

if __name__ == '__main__':
    main()