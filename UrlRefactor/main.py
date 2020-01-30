# coding:utf-8

import sys
import widget
from widget import mainwidget

if __name__ == '__main__':
    app = widget.QApplication(sys.argv)
    w = mainwidget.UrlWidget()
    w.show()
    sys.exit(app.exec_())
