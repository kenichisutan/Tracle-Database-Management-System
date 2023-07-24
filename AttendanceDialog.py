# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\AttendanceDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AttendanceDialog(object):
    def setupUi(self, AttendanceDialog):
        AttendanceDialog.setObjectName("AttendanceDialog")
        AttendanceDialog.resize(400, 190)
        self.buttonBox = QtWidgets.QDialogButtonBox(AttendanceDialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 160, 381, 31))
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
        self.formLayoutWidget_2 = QtWidgets.QWidget(AttendanceDialog)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 381, 141))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_DialogExpenses = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_DialogExpenses.setContentsMargins(6, 6, 6, 6)
        self.formLayout_DialogExpenses.setObjectName("formLayout_DialogExpenses")
        self.lblAttendanceID = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lblAttendanceID.setFont(font)
        self.lblAttendanceID.setObjectName("lblAttendanceID")
        self.formLayout_DialogExpenses.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblAttendanceID)
        self.txtAttendanceID = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.txtAttendanceID.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.txtAttendanceID.setFont(font)
        self.txtAttendanceID.setObjectName("txtAttendanceID")
        self.formLayout_DialogExpenses.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtAttendanceID)
        self.lblStudentID = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lblStudentID.setFont(font)
        self.lblStudentID.setObjectName("lblStudentID")
        self.formLayout_DialogExpenses.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblStudentID)
        self.txtStudentID = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.txtStudentID.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.txtStudentID.setFont(font)
        self.txtStudentID.setObjectName("txtStudentID")
        self.formLayout_DialogExpenses.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtStudentID)
        self.lblClassID = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lblClassID.setFont(font)
        self.lblClassID.setObjectName("lblClassID")
        self.formLayout_DialogExpenses.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lblClassID)
        self.txtClassID = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.txtClassID.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.txtClassID.setFont(font)
        self.txtClassID.setObjectName("txtClassID")
        self.formLayout_DialogExpenses.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txtClassID)
        self.lblPresent = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lblPresent.setFont(font)
        self.lblPresent.setObjectName("lblPresent")
        self.formLayout_DialogExpenses.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lblPresent)
        self.cmbPresent = QtWidgets.QComboBox(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.cmbPresent.setFont(font)
        self.cmbPresent.setObjectName("cmbPresent")
        self.cmbPresent.addItem("")
        self.cmbPresent.addItem("")
        self.formLayout_DialogExpenses.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.cmbPresent)
        self.lblAttendanceDate = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lblAttendanceDate.setFont(font)
        self.lblAttendanceDate.setObjectName("lblAttendanceDate")
        self.formLayout_DialogExpenses.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lblAttendanceDate)
        self.dateAttendance = QtWidgets.QDateEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.dateAttendance.setFont(font)
        self.dateAttendance.setObjectName("dateAttendance")
        self.formLayout_DialogExpenses.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.dateAttendance)
        self.frame = QtWidgets.QFrame(AttendanceDialog)
        self.frame.setGeometry(QtCore.QRect(10, 10, 381, 141))
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setLineWidth(1)
        self.frame.setObjectName("frame")
        self.frame.raise_()
        self.buttonBox.raise_()
        self.formLayoutWidget_2.raise_()

        self.retranslateUi(AttendanceDialog)
        self.buttonBox.accepted.connect(AttendanceDialog.accept) # type: ignore
        self.buttonBox.rejected.connect(AttendanceDialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(AttendanceDialog)

    def retranslateUi(self, AttendanceDialog):
        _translate = QtCore.QCoreApplication.translate
        AttendanceDialog.setWindowTitle(_translate("AttendanceDialog", "Attendance Dialog"))
        self.lblAttendanceID.setText(_translate("AttendanceDialog", "Attendance ID: "))
        self.lblStudentID.setText(_translate("AttendanceDialog", "Student ID:"))
        self.lblClassID.setText(_translate("AttendanceDialog", "Class ID:"))
        self.lblPresent.setText(_translate("AttendanceDialog", "Present:"))
        self.cmbPresent.setItemText(0, _translate("AttendanceDialog", "Y"))
        self.cmbPresent.setItemText(1, _translate("AttendanceDialog", "N"))
        self.lblAttendanceDate.setText(_translate("AttendanceDialog", "Attendance Date:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AttendanceDialog = QtWidgets.QDialog()
    ui = Ui_AttendanceDialog()
    ui.setupUi(AttendanceDialog)
    AttendanceDialog.show()
    sys.exit(app.exec_())