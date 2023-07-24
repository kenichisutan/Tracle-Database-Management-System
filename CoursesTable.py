# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\CoursesTable.ui'
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
from PyQt5.QtCore import Qt, QCoreApplication, QDate

import mysql.connector
from PyQt5.QtWidgets import QMessageBox

import AttendanceDialog

import datetime

import CoursesDialog

QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)  # Enable high DPI scaling
QCoreApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)  # Use high DPI icons


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
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
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
        self.lblCourseID = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lblCourseID.setFont(font)
        self.lblCourseID.setObjectName("lblCourseID")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblCourseID)
        self.lblTitle = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lblTitle.setFont(font)
        self.lblTitle.setObjectName("lblTitle")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lblTitle)
        self.txtCourseID = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.txtCourseID.setFont(font)
        self.txtCourseID.setText("")
        self.txtCourseID.setObjectName("txtCourseID")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtCourseID)
        self.txtTitle = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.txtTitle.setFont(font)
        self.txtTitle.setObjectName("txtTitle")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txtTitle)
        self.formLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(380, 10, 311, 61))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.lblCredits = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lblCredits.setFont(font)
        self.lblCredits.setObjectName("lblCredits")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblCredits)
        self.txtCredits = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.txtCredits.setFont(font)
        self.txtCredits.setObjectName("txtCredits")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtCredits)
        self.lblDepartment = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lblDepartment.setFont(font)
        self.lblDepartment.setObjectName("lblDepartment")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lblDepartment)
        self.txtDepartment = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.txtDepartment.setFont(font)
        self.txtDepartment.setObjectName("txtDepartment")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txtDepartment)
        self.lblMainTitle = QtWidgets.QLabel(Dialog)
        self.lblMainTitle.setGeometry(QtCore.QRect(10, 10, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lblMainTitle.setFont(font)
        self.lblMainTitle.setAcceptDrops(False)
        self.lblMainTitle.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblMainTitle.setAutoFillBackground(False)
        self.lblMainTitle.setStyleSheet("background-color: rgb(22, 9, 88);\n"
"color: rgb(255, 255, 255);")
        self.lblMainTitle.setFrameShape(QtWidgets.QFrame.Box)
        self.lblMainTitle.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lblMainTitle.setLineWidth(3)
        self.lblMainTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lblMainTitle.setWordWrap(True)
        self.lblMainTitle.setObjectName("lblMainTitle")
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
        self.lblMainTitle.raise_()
        self.verticalLayoutWidget_2.raise_()

        self.initialSetup()

        self.retranslateUi(Dialog)
        self.btnClose.accepted.connect(Dialog.accept) # type: ignore
        self.btnClose.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Courses Table"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Course ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Title"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Credits"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Department"))
        self.btnNew.setText(_translate("Dialog", "New"))
        self.btnEdit.setText(_translate("Dialog", "Edit"))
        self.btnDelete.setText(_translate("Dialog", "Delete"))
        self.lblCourseID.setText(_translate("Dialog", "Course ID:"))
        self.lblTitle.setText(_translate("Dialog", "Title:"))
        self.lblCredits.setText(_translate("Dialog", "Credits:"))
        self.lblDepartment.setText(_translate("Dialog", "Department:"))
        self.lblMainTitle.setText(_translate("Dialog", "Courses Table"))
        self.btnSearch.setText(_translate("Dialog", "Search"))
        self.btnClear.setText(_translate("Dialog", "Clear"))

#####################     End UI Generation     #####################

    def initialSetup(self):
        self.setupEvents()
        self.setupDatabase()
        self.refreshCourses()
        # self.setupDatabase()
        # self.setupCombobox()
        # self.setValues()

    #########################################################################
    #                                                                       #
    #                            Events                                     #
    #                                                                       #
    #########################################################################

    def setupEvents(self):
        self.btnNew.clicked.connect(self.btnNewCourses_clicked)
        self.btnEdit.clicked.connect(self.btnEditCourses_clicked)
        self.btnDelete.clicked.connect(self.btnDeleteCourses_clicked)
        self.btnSearch.clicked.connect(self.btnSearch_clicked)
        self.btnClear.clicked.connect(self.btnClear_clicked)

    def btnNewCourses_clicked(self):
        Dialog = QtWidgets.QDialog()
        form = CoursesDialog.Ui_CoursesDialog()
        form.setupUi(Dialog, None)  # None -> no list, no need to send data when creating a new record
        result = Dialog.exec_()

        if result == 1:  # This means the user clicked OK
            #   Get the list of results from dialog
            listValues = form.getValues()

            cursor = self.cnx.cursor()

            query = "Select * From courses"

            cursor.execute(query)

            largestID = 0
            # Retreive the largest ID
            for (ID, Title, Credits, Department) in cursor:
                if (ID > largestID):
                    largestID = ID

            largestID += 1
            listValues[ 0 ] = str(largestID)

            print(listValues)

            # Insert the values in the database
            self.insertCourses(listValues)

            # Refresh the table
            self.refreshCourses()

    def btnEditCourses_clicked(self):
        currentRow = self.tableWidget.currentRow()

        if currentRow == -1:
            QMessageBox.warning(None, "Select Row", "Please select row first")
            return

        listValues = [ ]
        listValues.append(self.tableWidget.item(currentRow, 0).text())
        listValues.append(self.tableWidget.item(currentRow, 1).text())
        listValues.append(self.tableWidget.item(currentRow, 2).text())
        listValues.append(self.tableWidget.item(currentRow, 3).text())

        print(listValues)

        Dialog = QtWidgets.QDialog()
        form = CoursesDialog.Ui_CoursesDialog()
        form.setupUi(Dialog, listValues)
        result = Dialog.exec_()

        if result == 1:  # This means the user clicked OK
            #   Get the list of results from dialog
            newValues = form.getValues()
            newValues[ 0 ] = listValues[ 0 ]  # Set the ID to the original value

            # Insert the values in the database
            self.updateCourses(newValues)

            # Refresh the table
            self.refreshCourses()

    def btnDeleteCourses_clicked(self):
        currentRow = self.tableWidget.currentRow()

        if currentRow == -1:
            QMessageBox.warning(None, "Select Row", "Please select row first")
            return

        answer = QMessageBox.question(
            None,
            "Delete row?",
            "Are you sure you want to delete this row?",
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No
        )

        if answer == QMessageBox.StandardButton.Yes:
            ID = self.tableWidget.item(currentRow, 0).text()

            # Delete the values in the database
            self.deleteCourses(ID)
            self.refreshCourses()

    def btnSearch_clicked(self):
        ID = self.txtCourseID.text()
        Title = self.txtTitle.text()
        Credits = self.txtCredits.text()
        Department = self.txtDepartment.text()

        self.filterCourses(ID, Title, Credits, Department)

    def btnClear_clicked(self):
        self.txtCourseID.setText("")
        self.txtTitle.setText("")
        self.txtCredits.setText("")
        self.txtDepartment.setText("")

        self.refreshCourses()


    #########################################################################
    #                                                                       #
    #                            Database                                   #
    #                                                                       #
    #########################################################################

    def setupDatabase(self):
        self.connect()

    def connect(self):
        self.cnx = mysql.connector.connect(user="root",
                                            password="12345678",
                                            host="127.0.0.1",
                                            database="tracle")

    def refreshCourses(self):
        self.tableWidget.setRowCount(0)
        cursor = self.cnx.cursor()

        query = "Select * From courses Order By ID Asc"

        cursor.execute(query)

        for(ID, Title, Credits, Department) in cursor:
            rowCount = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowCount)
            self.tableWidget.setItem(rowCount, 0, QtWidgets.QTableWidgetItem(str(ID)))
            self.tableWidget.setItem(rowCount, 1, QtWidgets.QTableWidgetItem(str(Title)))
            self.tableWidget.setItem(rowCount, 2, QtWidgets.QTableWidgetItem(str(Credits)))
            self.tableWidget.setItem(rowCount, 3, QtWidgets.QTableWidgetItem(str(Department)))

        cursor.close()

    def insertCourses(self, a_listValues):
        cursor = self.cnx.cursor()

        query = ("Insert Into courses "
                 "(ID, Title, Credits, Department) "
                 "Values (%s, %s, %s, %s)")

        listValues = a_listValues

        cursor.execute(query, listValues)

        self.cnx.commit()

        cursor.close()

    def updateCourses(self, a_listValues):
        cursor = self.cnx.cursor()

        query = "Update courses " \
                "Set Title = %s, Credits = %s, Department = %s " \
                "Where ID = %s"

        listValues = a_listValues

        listValues.append(listValues.pop(0))

        print(listValues)

        cursor.execute(query, listValues)

        self.cnx.commit()

        cursor.close()

    def deleteCourses(self, a_ID):
        cursor = self.cnx.cursor()

        print(a_ID)

        query = "Delete From courses " \
                "Where ID = %s"

        print(query)

        cursor.execute(query, (a_ID,))

        self.cnx.commit()

        cursor.close()

    def filterCourses(self, a_ID, a_Title, a_Credits, a_Department):
        self.tableWidget.setRowCount(0)

        cursor = self.cnx.cursor()

        query = "Select * " \
                "From courses " \
                "WHERE (ID = %s OR %s = '') " \
                "AND (Title = %s OR %s = '') " \
                "AND (Credits = %s OR %s = '') " \
                "AND (Department = %s OR %s = '')"

        values = [ ]

        values.append(a_ID)
        values.append(a_ID)
        values.append(a_Title)
        values.append(a_Title)
        values.append(a_Credits)
        values.append(a_Credits)
        values.append(a_Department)
        values.append(a_Department)

        print(values)

        cursor.execute(query, values)

        for (ID, Title, Credits, Department) in cursor:
            rowCount = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowCount)
            self.tableWidget.setItem(rowCount, 0, QtWidgets.QTableWidgetItem(str(ID)))
            self.tableWidget.setItem(rowCount, 1, QtWidgets.QTableWidgetItem(str(Title)))
            self.tableWidget.setItem(rowCount, 2, QtWidgets.QTableWidgetItem(str(Credits)))
            self.tableWidget.setItem(rowCount, 3, QtWidgets.QTableWidgetItem(str(Department)))

        cursor.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
