# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\CoursesDialog.ui'
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

class Ui_CoursesDialog(object):
    def setupUi(self, CoursesDialog, listValues):
        CoursesDialog.setObjectName("CoursesDialog")
        CoursesDialog.resize(400, 160)
        self.buttonBox = QtWidgets.QDialogButtonBox(CoursesDialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 120, 381, 31))
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
        self.formLayoutWidget_2 = QtWidgets.QWidget(CoursesDialog)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 381, 111))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_DialogExpenses = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_DialogExpenses.setContentsMargins(6, 6, 6, 6)
        self.formLayout_DialogExpenses.setObjectName("formLayout_DialogExpenses")
        self.lblCourseID = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lblCourseID.setFont(font)
        self.lblCourseID.setObjectName("lblCourseID")
        self.formLayout_DialogExpenses.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblCourseID)
        self.txtCourseID = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.txtCourseID.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.txtCourseID.setFont(font)
        self.txtCourseID.setObjectName("txtCourseID")
        self.formLayout_DialogExpenses.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtCourseID)
        self.lblTitle = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lblTitle.setFont(font)
        self.lblTitle.setObjectName("lblTitle")
        self.formLayout_DialogExpenses.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblTitle)
        self.txtTitle = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.txtTitle.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.txtTitle.setFont(font)
        self.txtTitle.setObjectName("txtTitle")
        self.formLayout_DialogExpenses.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtTitle)
        self.lblCredits = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lblCredits.setFont(font)
        self.lblCredits.setObjectName("lblCredits")
        self.formLayout_DialogExpenses.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lblCredits)
        self.txtCredits = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.txtCredits.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.txtCredits.setFont(font)
        self.txtCredits.setObjectName("txtCredits")
        self.formLayout_DialogExpenses.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txtCredits)
        self.lblDepartment = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lblDepartment.setFont(font)
        self.lblDepartment.setObjectName("lblDepartment")
        self.formLayout_DialogExpenses.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lblDepartment)
        self.txtDepartment = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.txtDepartment.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.txtDepartment.setFont(font)
        self.txtDepartment.setObjectName("txtDepartment")
        self.formLayout_DialogExpenses.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txtDepartment)
        self.frame = QtWidgets.QFrame(CoursesDialog)
        self.frame.setGeometry(QtCore.QRect(10, 10, 381, 111))
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setLineWidth(1)
        self.frame.setObjectName("frame")
        self.frame.raise_()
        self.buttonBox.raise_()
        self.formLayoutWidget_2.raise_()

        self.retranslateUi(CoursesDialog)
        self.buttonBox.accepted.connect(CoursesDialog.accept) # type: ignore
        self.buttonBox.rejected.connect(CoursesDialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(CoursesDialog)

        self.listValues = listValues
        self.initialSetup()

    def retranslateUi(self, CoursesDialog):
        _translate = QtCore.QCoreApplication.translate
        CoursesDialog.setWindowTitle(_translate("CoursesDialog", "Courses Dialog"))
        self.lblCourseID.setText(_translate("CoursesDialog", "Course ID: "))
        self.lblTitle.setText(_translate("CoursesDialog", "Title:"))
        self.lblCredits.setText(_translate("CoursesDialog", "Credits:"))
        self.lblDepartment.setText(_translate("CoursesDialog", "Department:"))

#####################     End UI Generation     #####################

    def initialSetup(self):
        self.setValues()

    #########################################################################
    #                                                                       #
    #                            Events                                     #
    #                                                                       #
    #########################################################################

    def setValues(self):
        if self.listValues == None:
            return

        self.txtCourseID.setText(self.listValues[0])
        self.txtTitle.setText(self.listValues[1])
        self.txtCredits.setText(self.listValues[2])
        self.txtDepartment.setText(self.listValues[3])

    def getValues(self):
        listResult = []
        listResult.append(self.txtCourseID.text())
        listResult.append(self.txtTitle.text())
        listResult.append(self.txtCredits.text())
        listResult.append(self.txtDepartment.text())

        return listResult


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CoursesDialog = QtWidgets.QDialog()
    ui = Ui_CoursesDialog()
    ui.setupUi(CoursesDialog, None)
    CoursesDialog.show()
    sys.exit(app.exec_())
