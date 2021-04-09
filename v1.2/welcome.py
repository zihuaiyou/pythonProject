#
# -*- coding: utf-8 -*-
# # Created by: PyQt5 version 5.15.1 Author:zihuaiyou
#
import sys
from PyQt5.QtWidgets import *
import mainWin_1
import mainWin_2
import mainWin_3
import Ui_welcome
import os


# 欢迎界面
class myMainWindow(QMainWindow, Ui_welcome.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 软件所有的窗口
    w0 = myMainWindow()
    w1 = mainWin_1.myMainWindow()
    w2 = mainWin_2.myMainWindow()
    w3 = mainWin_3.myMainWindow()
    w1_1 = mainWin_1.myChildWindow1()
    w1_2 = mainWin_1.myChildWindow2()
    w2_1 = mainWin_2.myChildWindow()
    w3_1 = mainWin_3.MychildWindow()

    # 显示欢迎界面
    w0.show()


    # 显示主界面1
    def showWin1():
        w1.show()

        # 显示子界面1
        def show_w1_1():
            w1_1.show()

        # 显示子界面2
        def show_w1_2():
            w1_2.show()

        # 绑定pushbutton
        w1.pushButton_1.clicked.connect(show_w1_1)
        w1.pushButton_2.clicked.connect(show_w1_2)


    # 显示主界面2
    def showWin2():
        w2.show()

        def show_w2():
            w2_1.show()

        # 绑定pushbutton
        w2.pushButton_1.clicked.connect(show_w2)


    # 显示主界面3
    def showWin3():
        w3.show()

        def show_w3():
            w3_1.show()

        # 绑定pushbutton
        w3.pushButton.clicked.connect(show_w3)


    # 显示帮助文档
    def showHelpDoc():
        os.popen('软件用户手册.pdf')


    # 绑定pushbutton
    w0.pushButton_1.clicked.connect(showWin1)
    w0.pushButton_2.clicked.connect(showWin2)
    w0.pushButton_3.clicked.connect(showWin3)

    # 帮助文档
    w0.pushButton_4.clicked.connect(showHelpDoc)

    sys.exit(app.exec_())
