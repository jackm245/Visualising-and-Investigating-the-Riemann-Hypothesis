# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ForgottenPassword2.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ForgottenPassword2Screen(object):
    def setupUi(self, ForgottenPassword2Screen):
        ForgottenPassword2Screen.setObjectName("ForgottenPassword2Screen")
        ForgottenPassword2Screen.resize(1340, 720)
        ForgottenPassword2Screen.setSizeGripEnabled(False)
        self.widget = QtWidgets.QWidget(ForgottenPassword2Screen)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1340, 720))
        self.widget.setStyleSheet("background-color: rgb(69, 69, 69);")
        self.widget.setObjectName("widget")
        self.Title = QtWidgets.QLabel(self.widget)
        self.Title.setGeometry(QtCore.QRect(612, 20, 116, 51))
        self.Title.setStyleSheet("font: 36pt \"Sans Serif\"; color:rgb(239, 239, 239)")
        self.Title.setObjectName("Title")
        self.TabBar = QtWidgets.QWidget(self.widget)
        self.TabBar.setGeometry(QtCore.QRect(0, 80, 1340, 80))
        self.TabBar.setStyleSheet("background-color: rgb(239, 239, 239);")
        self.TabBar.setObjectName("TabBar")
        self.LoginTab = QtWidgets.QPushButton(self.TabBar)
        self.LoginTab.setGeometry(QtCore.QRect(10, 5, 200, 70))
        self.LoginTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.LoginTab.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 36pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.LoginTab.setObjectName("LoginTab")
        self.SignUpTab = QtWidgets.QPushButton(self.TabBar)
        self.SignUpTab.setGeometry(QtCore.QRect(220, 5, 200, 70))
        self.SignUpTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SignUpTab.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 36pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.SignUpTab.setObjectName("SignUpTab")
        self.ForgottenPasswordTab = QtWidgets.QPushButton(self.TabBar)
        self.ForgottenPasswordTab.setGeometry(QtCore.QRect(430, 5, 200, 70))
        self.ForgottenPasswordTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ForgottenPasswordTab.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239, 239);\n"
"font: 12pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
"")
        self.ForgottenPasswordTab.setObjectName("ForgottenPasswordTab")
        self.ResetPasswordTab = QtWidgets.QPushButton(self.TabBar)
        self.ResetPasswordTab.setGeometry(QtCore.QRect(640, 5, 200, 70))
        self.ResetPasswordTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ResetPasswordTab.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 20pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.ResetPasswordTab.setObjectName("ResetPasswordTab")
        self.MainWidget = QtWidgets.QWidget(self.widget)
        self.MainWidget.setGeometry(QtCore.QRect(10, 170, 1320, 540))
        self.MainWidget.setStyleSheet("background-color: rgb(239, 239, 239);\n"
"border-radius: 20px;")
        self.MainWidget.setObjectName("MainWidget")
        self.VerificationCodeText = QtWidgets.QLabel(self.MainWidget)
        self.VerificationCodeText.setGeometry(QtCore.QRect(300, 200, 301, 61))
        self.VerificationCodeText.setStyleSheet("font: 25pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239, 239); padding: 5px;")
        self.VerificationCodeText.setObjectName("VerificationCodeText")
        self.VerificationCodeInput = QtWidgets.QLineEdit(self.MainWidget)
        self.VerificationCodeInput.setGeometry(QtCore.QRect(720, 200, 261, 60))
        self.VerificationCodeInput.setStyleSheet("background-color: rgb(239, 239, 239);\n"
"color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\";\n"
"border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);")
        self.VerificationCodeInput.setText("")
        self.VerificationCodeInput.setCursorPosition(0)
        self.VerificationCodeInput.setObjectName("VerificationCodeInput")
        self.SubmitButton = QtWidgets.QPushButton(self.MainWidget)
        self.SubmitButton.setGeometry(QtCore.QRect(570, 440, 200, 70))
        self.SubmitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SubmitButton.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 36pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.SubmitButton.setObjectName("SubmitButton")
        self.VerificationText = QtWidgets.QLabel(self.MainWidget)
        self.VerificationText.setGeometry(QtCore.QRect(305, 60, 730, 61))
        self.VerificationText.setStyleSheet("font: 25pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239, 239); padding: 5px;")
        self.VerificationText.setObjectName("VerificationText")

        self.retranslateUi(ForgottenPassword2Screen)
        QtCore.QMetaObject.connectSlotsByName(ForgottenPassword2Screen)

    def retranslateUi(self, ForgottenPassword2Screen):
        _translate = QtCore.QCoreApplication.translate
        ForgottenPassword2Screen.setWindowTitle(_translate("ForgottenPassword2Screen", "Visualising the Riemann Hypothesis - Forgotten Password"))
        self.Title.setText(_translate("ForgottenPassword2Screen", "Login"))
        self.LoginTab.setText(_translate("ForgottenPassword2Screen", "Login"))
        self.SignUpTab.setText(_translate("ForgottenPassword2Screen", "Sign Up"))
        self.ForgottenPasswordTab.setText(_translate("ForgottenPassword2Screen", "Forgotten Password"))
        self.ResetPasswordTab.setText(_translate("ForgottenPassword2Screen", "Reset Password"))
        self.VerificationCodeText.setText(_translate("ForgottenPassword2Screen", "<html><head/><body><p align=\"right\">Verification Code:</p></body></html>"))
        self.VerificationCodeInput.setPlaceholderText(_translate("ForgottenPassword2Screen", "Enter Verification Code"))
        self.SubmitButton.setText(_translate("ForgottenPassword2Screen", "Submit"))
        self.VerificationText.setText(_translate("ForgottenPassword2Screen", "<html><head/><body><p align=\"center\">A Verification Code has been sent to your email</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ForgottenPassword2Screen = QtWidgets.QDialog()
    ui = Ui_ForgottenPassword2Screen()
    ui.setupUi(ForgottenPassword2Screen)
    ForgottenPassword2Screen.show()
    sys.exit(app.exec_())
