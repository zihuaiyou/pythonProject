# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'program_2_UI_new.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

# 这是生成主界面3子窗口UI界面所需代码
from PyQt5 import QtCore, QtGui, QtWidgets

# 生成Form类型的UI
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(499, 299)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setTitle("")
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_n = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_n.setDragEnabled(True)
        self.lineEdit_n.setReadOnly(True)
        self.lineEdit_n.setObjectName("lineEdit_n")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_n)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_N = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_N.setReadOnly(True)
        self.lineEdit_N.setObjectName("lineEdit_N")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_N)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.LabelRole, spacerItem)
        self.horizontalLayout_2.addWidget(self.groupBox)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_1 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_1.setObjectName("pushButton_1")
        self.verticalLayout_2.addWidget(self.pushButton_1)
        self.pushButton = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.horizontalLayout_2.addWidget(self.groupBox_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 1)

        self.retranslateUi(Form)
        self.pushButton_1.clicked.connect(Form.printdata)
        self.pushButton_2.clicked.connect(Form.openfile)
        self.pushButton.clicked.connect(Form.clear_all)
        QtCore.QMetaObject.connectSlotsByName(Form)

    # Form 文字属性修改
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "输出结果"))
        self.label_2.setText(_translate("Form", "总射孔数"))
        self.label_3.setText(_translate("Form", "最优各层射孔数"))
        self.pushButton_1.setText(_translate("Form", "确认输出"))
        self.pushButton.setText(_translate("Form", "清空"))
        self.label_4.setText(_translate("Form", "全部射孔数量方案"))
        self.pushButton_2.setText(_translate("Form", "另存为"))
