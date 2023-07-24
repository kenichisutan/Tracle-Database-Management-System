# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ClassDialog.ui'
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


class Ui_ClassDialog(object):
    def setupUi(self, ClassDialog, listValues):
        ClassDialog.setObjectName("ClassDialog")
        ClassDialog.resize(400, 250)
        self.buttonBox = QtWidgets.QDialogButtonBox(ClassDialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 210, 381, 31))
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
        self.formLayoutWidget_2 = QtWidgets.QWidget(ClassDialog)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 381, 191))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_DialogExpenses = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_DialogExpenses.setContentsMargins(6, 6, 6, 6)
        self.formLayout_DialogExpenses.setObjectName("formLayout_DialogExpenses")
        self.lblClassID = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lblClassID.setFont(font)
        self.lblClassID.setObjectName("lblClassID")
        self.formLayout_DialogExpenses.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblClassID)
        self.txtClassID = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.txtClassID.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.txtClassID.setFont(font)
        self.txtClassID.setObjectName("txtClassID")
        self.formLayout_DialogExpenses.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtClassID)
        self.lblSemesterID = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lblSemesterID.setFont(font)
        self.lblSemesterID.setObjectName("lblSemesterID")
        self.formLayout_DialogExpenses.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblSemesterID)
        self.txtSemesterID = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.txtSemesterID.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.txtSemesterID.setFont(font)
        self.txtSemesterID.setObjectName("txtSemesterID")
        self.formLayout_DialogExpenses.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtSemesterID)
        self.lblCourseID = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lblCourseID.setFont(font)
        self.lblCourseID.setObjectName("lblCourseID")
        self.formLayout_DialogExpenses.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lblCourseID)
        self.lblProfessorID = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lblProfessorID.setFont(font)
        self.lblProfessorID.setObjectName("lblProfessorID")
        self.formLayout_DialogExpenses.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lblProfessorID)
        self.txtCourseID = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.txtCourseID.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.txtCourseID.setFont(font)
        self.txtCourseID.setObjectName("txtCourseID")
        self.formLayout_DialogExpenses.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txtCourseID)
        self.txtProfessorID = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.txtProfessorID.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.txtProfessorID.setFont(font)
        self.txtProfessorID.setObjectName("txtProfessorID")
        self.formLayout_DialogExpenses.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txtProfessorID)
        self.lblDays = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lblDays.setFont(font)
        self.lblDays.setObjectName("lblDays")
        self.formLayout_DialogExpenses.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lblDays)
        self.lblStartTime = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lblStartTime.setFont(font)
        self.lblStartTime.setObjectName("lblStartTime")
        self.formLayout_DialogExpenses.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.lblStartTime)
        self.lblEndTime = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lblEndTime.setFont(font)
        self.lblEndTime.setObjectName("lblEndTime")
        self.formLayout_DialogExpenses.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.lblEndTime)
        self.txtDays = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.txtDays.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.txtDays.setFont(font)
        self.txtDays.setObjectName("txtDays")
        self.formLayout_DialogExpenses.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.txtDays)
        self.timeStartTime = QtWidgets.QTimeEdit(self.formLayoutWidget_2)
        self.timeStartTime.setObjectName("timeStartTime")
        self.formLayout_DialogExpenses.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.timeStartTime)
        self.timeEndTime = QtWidgets.QTimeEdit(self.formLayoutWidget_2)
        self.timeEndTime.setObjectName("timeEndTime")
        self.formLayout_DialogExpenses.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.timeEndTime)
        self.frame = QtWidgets.QFrame(ClassDialog)
        self.frame.setGeometry(QtCore.QRect(10, 10, 381, 191))
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setLineWidth(1)
        self.frame.setObjectName("frame")
        self.frame.raise_()
        self.buttonBox.raise_()
        self.formLayoutWidget_2.raise_()

        self.retranslateUi(ClassDialog)
        self.buttonBox.accepted.connect(ClassDialog.accept) # type: ignore
        self.buttonBox.rejected.connect(ClassDialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(ClassDialog)

        self.listValues = listValues
        self.initialSetup()

    def retranslateUi(self, ClassDialog):
        _translate = QtCore.QCoreApplication.translate
        ClassDialog.setWindowTitle(_translate("ClassDialog", "Class Dialog"))
        self.lblClassID.setText(_translate("ClassDialog", "Class ID: "))
        self.lblSemesterID.setText(_translate("ClassDialog", "Semester ID:"))
        self.lblCourseID.setText(_translate("ClassDialog", "Course ID:"))
        self.lblProfessorID.setText(_translate("ClassDialog", "Professor ID:"))
        self.lblDays.setText(_translate("ClassDialog", "Days:"))
        self.lblStartTime.setText(_translate("ClassDialog", "Start Time:"))
        self.lblEndTime.setText(_translate("ClassDialog", "End Time:"))


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

        self.txtClassID.setText(self.listValues[0])
        self.txtSemesterID.setText(self.listValues[1])
        self.txtCourseID.setText(self.listValues[2])
        self.txtProfessorID.setText(self.listValues[3])
        self.txtDays.setText(self.listValues[4])
        self.timeStartTime.setTime(self.listValues[5])
        self.timeEndTime.setTime(self.listValues[6])


    def getValues(self):
        listResult = []
        listResult.append(self.txtClassID.text())
        listResult.append(self.txtSemesterID.text())
        listResult.append(self.txtCourseID.text())
        listResult.append(self.txtProfessorID.text())
        listResult.append(self.txtDays.text())
        listResult.append(self.timeStartTime.time())
        listResult.append(self.timeEndTime.time())

        return listResult



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ClassDialog = QtWidgets.QDialog()
    ui = Ui_ClassDialog()
    ui.setupUi(ClassDialog, None)
    ClassDialog.show()
    sys.exit(app.exec_())