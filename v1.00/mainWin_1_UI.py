# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWin_1_UI.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(703, 353)
        MainWindow.setMinimumSize(QtCore.QSize(703, 353))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.lineEdit_num = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_num.setObjectName("lineEdit_num")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_num)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.LabelRole, spacerItem)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_stress_diff = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_stress_diff.setObjectName("lineEdit_stress_diff")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_stress_diff)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.LabelRole, spacerItem1)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lineEdit_reservoir_thick = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_reservoir_thick.setObjectName("lineEdit_reservoir_thick")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_reservoir_thick)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(5, QtWidgets.QFormLayout.LabelRole, spacerItem2)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.lineEdit_upper_thick = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_upper_thick.setObjectName("lineEdit_upper_thick")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEdit_upper_thick)
        self.horizontalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox_2)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_15 = QtWidgets.QLabel(self.groupBox_2)
        self.label_15.setObjectName("label_15")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.lineEdit_lower_thick = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_lower_thick.setObjectName("lineEdit_lower_thick")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_lower_thick)
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("?????????")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.lineEdit_Q = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_Q.setObjectName("lineEdit_Q")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_Q)
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.lineEdit_scale = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_scale.setObjectName("lineEdit_scale")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_scale)
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.lineEdit_viscosity = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_viscosity.setObjectName("lineEdit_viscosity")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEdit_viscosity)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_2.setItem(1, QtWidgets.QFormLayout.LabelRole, spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_2.setItem(3, QtWidgets.QFormLayout.LabelRole, spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_2.setItem(5, QtWidgets.QFormLayout.LabelRole, spacerItem5)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_1 = QtWidgets.QPushButton(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setObjectName("pushButton_1")
        self.horizontalLayout_2.addWidget(self.pushButton_1)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.verticalLayout.setStretch(1, 3)
        self.verticalLayout.setStretch(2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_3.clicked.connect(MainWindow.inputData)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "?????????????????????????????????????????????????????????"))
        self.label.setText(_translate("MainWindow", "???????????????:????????????????????????????????????"))
        self.label_10.setText(_translate("MainWindow", "????????????"))
        self.label_6.setText(_translate("MainWindow", "??????????????????(MPa)"))
        self.label_7.setText(_translate("MainWindow", "????????????(m)"))
        self.label_8.setText(_translate("MainWindow", "??????????????????(m)"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">??????????????????(m)</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "????????????(m??/min)"))
        self.label_12.setText(_translate("MainWindow", "??????????????????(m??)"))
        self.label_13.setText(_translate("MainWindow", "??????(cp)"))
        self.pushButton_1.setText(_translate("MainWindow", "??????????????????????????????"))
        self.pushButton_2.setText(_translate("MainWindow", "????????????????????????"))
        self.pushButton_3.setText(_translate("MainWindow", "????????????"))
