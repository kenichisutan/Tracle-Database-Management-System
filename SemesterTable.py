# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\SemesterTable.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 600)
        Dialog.setStyleSheet("")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 80, 681, 511))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.horizontalLayoutWidget)
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.horizontalLayout.addWidget(self.tableWidget)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(700, 80, 81, 491))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnNew = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.btnNew.setFont(font)
        self.btnNew.setObjectName("btnNew")
        self.verticalLayout.addWidget(self.btnNew)
        self.btnEdit = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.btnEdit.setFont(font)
        self.btnEdit.setObjectName("btnEdit")
        self.verticalLayout.addWidget(self.btnEdit)
        self.btnDelete = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.btnDelete.setFont(font)
        self.btnDelete.setObjectName("btnDelete")
        self.verticalLayout.addWidget(self.btnDelete)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.btnClose = QtWidgets.QDialogButtonBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnClose.sizePolicy().hasHeightForWidth())
        self.btnClose.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.btnClose.setFont(font)
        self.btnClose.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnClose.setOrientation(QtCore.Qt.Vertical)
        self.btnClose.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.btnClose.setCenterButtons(False)
        self.btnClose.setObjectName("btnClose")
        self.verticalLayout.addWidget(self.btnClose)
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(150, 10, 221, 61))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setRowWrapPolicy(QtWidgets.QFormLayout.DontWrapRows)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.lblSemesterID = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lblSemesterID.setFont(font)
        self.lblSemesterID.setObjectName("lblSemesterID")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblSemesterID)
        self.lblSemester = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lblSemester.setFont(font)
        self.lblSemester.setObjectName("lblSemester")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lblSemester)
        self.txtSemesterID = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.txtSemesterID.setFont(font)
        self.txtSemesterID.setText("")
        self.txtSemesterID.setObjectName("txtSemesterID")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtSemesterID)
        self.txtSemester = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.txtSemester.setFont(font)
        self.txtSemester.setText("")
        self.txtSemester.setObjectName("txtSemester")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txtSemester)
        self.formLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(380, 10, 311, 61))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.lblOfferedYear = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lblOfferedYear.setFont(font)
        self.lblOfferedYear.setObjectName("lblOfferedYear")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblOfferedYear)
        self.txtOfferedYear = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.txtOfferedYear.setFont(font)
        self.txtOfferedYear.setText("")
        self.txtOfferedYear.setObjectName("txtOfferedYear")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtOfferedYear)
        self.lblTitle = QtWidgets.QLabel(Dialog)
        self.lblTitle.setGeometry(QtCore.QRect(10, 10, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lblTitle.setFont(font)
        self.lblTitle.setAcceptDrops(False)
        self.lblTitle.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblTitle.setAutoFillBackground(False)
        self.lblTitle.setStyleSheet("background-color: rgb(22, 9, 88);\n"
"color: rgb(255, 255, 255);")
        self.lblTitle.setFrameShape(QtWidgets.QFrame.Box)
        self.lblTitle.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lblTitle.setLineWidth(3)
        self.lblTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitle.setWordWrap(True)
        self.lblTitle.setObjectName("lblTitle")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(700, 10, 81, 61))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(5, 0, 5, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btnSearch = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnSearch.setFont(font)
        self.btnSearch.setObjectName("btnSearch")
        self.verticalLayout_2.addWidget(self.btnSearch)
        self.btnClear = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnClear.setFont(font)
        self.btnClear.setObjectName("btnClear")
        self.verticalLayout_2.addWidget(self.btnClear)
        self.frameTop = QtWidgets.QFrame(Dialog)
        self.frameTop.setGeometry(QtCore.QRect(140, 10, 641, 61))
        self.frameTop.setStyleSheet("color: rgb(255, 255, 0);")
        self.frameTop.setFrameShape(QtWidgets.QFrame.Box)
        self.frameTop.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frameTop.setLineWidth(2)
        self.frameTop.setObjectName("frameTop")
        self.frameRight = QtWidgets.QFrame(Dialog)
        self.frameRight.setGeometry(QtCore.QRect(700, 80, 81, 491))
        self.frameRight.setFrameShape(QtWidgets.QFrame.Panel)
        self.frameRight.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frameRight.setLineWidth(2)
        self.frameRight.setObjectName("frameRight")
        self.frameRight.raise_()
        self.frameTop.raise_()
        self.horizontalLayoutWidget.raise_()
        self.verticalLayoutWidget.raise_()
        self.formLayoutWidget.raise_()
        self.formLayoutWidget_2.raise_()
        self.lblTitle.raise_()
        self.verticalLayoutWidget_2.raise_()

        self.retranslateUi(Dialog)
        self.btnClose.accepted.connect(Dialog.accept) # type: ignore
        self.btnClose.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Semester Table"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Semester ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Semester"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Offered Year"))
        self.btnNew.setText(_translate("Dialog", "New"))
        self.btnEdit.setText(_translate("Dialog", "Edit"))
        self.btnDelete.setText(_translate("Dialog", "Delete"))
        self.lblSemesterID.setText(_translate("Dialog", "Semester ID:"))
        self.lblSemester.setText(_translate("Dialog", "Semester:"))
        self.lblOfferedYear.setText(_translate("Dialog", "Offered Year:"))
        self.lblTitle.setText(_translate("Dialog", "Semester Table"))
        self.btnSearch.setText(_translate("Dialog", "Search"))
        self.btnClear.setText(_translate("Dialog", "Clear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
