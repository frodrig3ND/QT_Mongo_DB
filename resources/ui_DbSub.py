# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/DbSub.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DbSub(object):
    def setupUi(self, DbSub):
        DbSub.setObjectName("DbSub")
        DbSub.resize(400, 112)
        self.FBtn = QtWidgets.QDialogButtonBox(DbSub)
        self.FBtn.setGeometry(QtCore.QRect(290, 20, 81, 241))
        self.FBtn.setOrientation(QtCore.Qt.Vertical)
        self.FBtn.setStandardButtons(QtWidgets.QDialogButtonBox.Discard|QtWidgets.QDialogButtonBox.Save)
        self.FBtn.setObjectName("FBtn")
        self.formLayoutWidget = QtWidgets.QWidget(DbSub)
        self.formLayoutWidget.setGeometry(QtCore.QRect(9, 9, 271, 71))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.CodeLbl = QtWidgets.QLabel(self.formLayoutWidget)
        self.CodeLbl.setObjectName("CodeLbl")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.CodeLbl)
        self.CodeIn = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.CodeIn.setObjectName("CodeIn")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.CodeIn)
        self.DescLbl = QtWidgets.QLabel(self.formLayoutWidget)
        self.DescLbl.setObjectName("DescLbl")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.DescLbl)
        self.DescIn = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.DescIn.setObjectName("DescIn")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.DescIn)
        self.ResCom = QtWidgets.QLabel(DbSub)
        self.ResCom.setGeometry(QtCore.QRect(60, 80, 221, 20))
        self.ResCom.setObjectName("ResCom")

        self.retranslateUi(DbSub)
        self.FBtn.accepted.connect(DbSub.accept)
        self.FBtn.rejected.connect(DbSub.reject)
        QtCore.QMetaObject.connectSlotsByName(DbSub)

    def retranslateUi(self, DbSub):
        _translate = QtCore.QCoreApplication.translate
        DbSub.setWindowTitle(_translate("DbSub", "Dialog"))
        self.CodeLbl.setText(_translate("DbSub", "Code"))
        self.DescLbl.setText(_translate("DbSub", "Description"))
        self.ResCom.setText(_translate("DbSub", "TextLabel"))
