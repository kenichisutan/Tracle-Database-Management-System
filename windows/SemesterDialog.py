# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\SemesterDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


#########################################################################
#                                                                       #
#                            UI Generation                              #
#                                                                       #
#########################################################################

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QCoreApplication

QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)  # Enable high DPI scaling
QCoreApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)  # Use high DPI icons

class Ui_SemesterDialog(object):
    def setupUi(self, SemesterDialog, listValues):
        SemesterDialog.setObjectName("SemesterDialog")
        SemesterDialog.resize(400, 140)
        self.buttonBox = QtWidgets.QDialogButtonBox(SemesterDialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 100, 381, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayoutWidget_2 = QtWidgets.QWidget(SemesterDialog)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 381, 91))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_DialogExpenses = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_DialogExpenses.setContentsMargins(6, 6, 6, 6)
        self.formLayout_DialogExpenses.setObjectName("formLayout_DialogExpenses")
        self.lblSemesterID = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lblSemesterID.setFont(font)
        self.lblSemesterID.setObjectName("lblSemesterID")
        self.formLayout_DialogExpenses.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblSemesterID)
        self.txtSemesterID = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.txtSemesterID.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.txtSemesterID.setFont(font)
        self.txtSemesterID.setObjectName("txtSemesterID")
        self.formLayout_DialogExpenses.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtSemesterID)
        self.lblSemester = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lblSemester.setFont(font)
        self.lblSemester.setObjectName("lblSemester")
        self.formLayout_DialogExpenses.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblSemester)
        self.txtSemester = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.txtSemester.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.txtSemester.setFont(font)
        self.txtSemester.setObjectName("txtSemester")
        self.formLayout_DialogExpenses.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtSemester)
        self.lblOfferedYear = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lblOfferedYear.setFont(font)
        self.lblOfferedYear.setObjectName("lblOfferedYear")
        self.formLayout_DialogExpenses.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lblOfferedYear)
        self.txtOfferedYear = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.txtOfferedYear.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.txtOfferedYear.setFont(font)
        self.txtOfferedYear.setObjectName("txtOfferedYear")
        self.formLayout_DialogExpenses.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txtOfferedYear)
        self.frame = QtWidgets.QFrame(SemesterDialog)
        self.frame.setGeometry(QtCore.QRect(10, 10, 381, 91))
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setLineWidth(1)
        self.frame.setObjectName("frame")
        self.frame.raise_()
        self.buttonBox.raise_()
        self.formLayoutWidget_2.raise_()

        self.retranslateUi(SemesterDialog)
        self.buttonBox.accepted.connect(SemesterDialog.accept) # type: ignore
        self.buttonBox.rejected.connect(SemesterDialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(SemesterDialog)

        self.listValues = listValues
        self.initialSetup()

    def retranslateUi(self, SemesterDialog):
        _translate = QtCore.QCoreApplication.translate
        SemesterDialog.setWindowTitle(_translate("SemesterDialog", "Semester Dialog"))
        self.lblSemesterID.setText(_translate("SemesterDialog", "Semester ID:"))
        self.lblSemester.setText(_translate("SemesterDialog", "Semester:"))
        self.lblOfferedYear.setText(_translate("SemesterDialog", "Offered Year:"))

#####################     End UI Generation     #####################

    def initialSetup(self):
        print()
        self.setValues()

    #########################################################################
    #                                                                       #
    #                            Events                                     #
    #                                                                       #
    #########################################################################

    def setValues(self):
        if self.listValues == None:
            return

        self.txtSemesterID.setText(self.listValues[0])
        self.txtSemester.setText(self.listValues[1])
        self.txtOfferedYear.setText(self.listValues[2])


    def getValues(self):
        listResult = []
        listResult.append(self.txtSemesterID.text())
        listResult.append(self.txtSemester.text())
        listResult.append(self.txtOfferedYear.text())

        return listResult


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SemesterDialog = QtWidgets.QDialog()
    ui = Ui_SemesterDialog()
    ui.setupUi(SemesterDialog, None)
    SemesterDialog.show()
    sys.exit(app.exec_())
