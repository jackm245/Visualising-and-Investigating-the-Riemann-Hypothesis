"""
single_calculator.py
====================
A GUI for the single calculator page of the investigation section
"""


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SingleCalculatorScreen(object):

    def setupUi(self, SingleCalculatorScreen):
        SingleCalculatorScreen.setObjectName("SingleCalculatorScreen")
        SingleCalculatorScreen.resize(1340, 720)
        SingleCalculatorScreen.setSizeGripEnabled(False)
        self.widget = QtWidgets.QWidget(SingleCalculatorScreen)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1340, 720))
        self.widget.setStyleSheet("background-color: rgb(69, 69, 69);")
        self.widget.setObjectName("widget")
        self.Title = QtWidgets.QLabel(self.widget)
        self.Title.setGeometry(QtCore.QRect(560, 20, 221, 51))
        self.Title.setStyleSheet("font: 36pt \"Sans Serif\"; color:rgb(239, 239, 239)")
        self.Title.setObjectName("Title")
        self.TabBar = QtWidgets.QWidget(self.widget)
        self.TabBar.setGeometry(QtCore.QRect(0, 80, 1340, 80))
        self.TabBar.setStyleSheet("background-color: rgb(239, 239, 239);")
        self.TabBar.setObjectName("TabBar")
        self.SingleTab = QtWidgets.QPushButton(self.TabBar)
        self.SingleTab.setGeometry(QtCore.QRect(10, 5, 200, 70))
        self.SingleTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SingleTab.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239,239);\n"
"font: 18pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
"")
        self.SingleTab.setObjectName("SingleTab")
        self.TableTab = QtWidgets.QPushButton(self.TabBar)
        self.TableTab.setGeometry(QtCore.QRect(220, 5, 200, 70))
        self.TableTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.TableTab.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.TableTab.setObjectName("TableTab")
        self.LeaderboardTab = QtWidgets.QPushButton(self.TabBar)
        self.LeaderboardTab.setGeometry(QtCore.QRect(430, 5, 200, 70))
        self.LeaderboardTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.LeaderboardTab.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.LeaderboardTab.setObjectName("LeaderboardTab")
        self.MainWidget = QtWidgets.QWidget(self.widget)
        self.MainWidget.setGeometry(QtCore.QRect(10, 170, 1320, 540))
        self.MainWidget.setStyleSheet("background-color: rgb(239, 239, 239);\n"
"border-radius: 20px;")
        self.MainWidget.setObjectName("MainWidget")
        self.PrevButton = QtWidgets.QPushButton(self.MainWidget)
        self.PrevButton.setGeometry(QtCore.QRect(10, 460, 200, 70))
        self.PrevButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PrevButton.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.PrevButton.setObjectName("PrevButton")
        self.NextButton = QtWidgets.QPushButton(self.MainWidget)
        self.NextButton.setGeometry(QtCore.QRect(1110, 460, 200, 70))
        self.NextButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.NextButton.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.NextButton.setObjectName("NextButton")
        self.SubTitleText = QtWidgets.QLabel(self.MainWidget)
        self.SubTitleText.setGeometry(QtCore.QRect(40, 20, 421, 51))
        self.SubTitleText.setStyleSheet("font: 25pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239, 239); padding: 5px;")
        self.SubTitleText.setObjectName("SubTitleText")
        self.EquationImage = QtWidgets.QLabel(self.MainWidget)
        self.EquationImage.setGeometry(QtCore.QRect(155, 70, 1031, 131))
        self.EquationImage.setText("")
        self.EquationImage.setPixmap(QtGui.QPixmap("ui/investigation_screens/../../media/riemanns_functional_equation.png"))
        self.EquationImage.setObjectName("EquationImage")
        self.ZetaInput = QtWidgets.QLineEdit(self.MainWidget)
        self.ZetaInput.setGeometry(QtCore.QRect(170, 340, 371, 81))
        self.ZetaInput.setStyleSheet("background-color: rgb(239, 239, 239);\n"
"color: rgb(69, 69, 69);\n"
"font: 36pt \"Sans Serif\";\n"
"border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);")
        self.ZetaInput.setText("")
        self.ZetaInput.setObjectName("ZetaInput")
        self.ZetaOutput = QtWidgets.QLabel(self.MainWidget)
        self.ZetaOutput.setGeometry(QtCore.QRect(800, 340, 511, 81))
        self.ZetaOutput.setStyleSheet("background-color: rgb(239, 239, 239);\n"
"color: rgb(69, 69, 69);\n"
"font: 36pt \"Sans Serif\";\n"
"border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);")
        self.ZetaOutput.setText("")
        self.ZetaOutput.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.ZetaOutput.setObjectName("ZetaOutput")
        self.InputText = QtWidgets.QLabel(self.MainWidget)
        self.InputText.setGeometry(QtCore.QRect(230, 270, 281, 51))
        self.InputText.setStyleSheet("font: 25pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239, 239); padding: 5px;\n"
"text-decoration: underline;")
        self.InputText.setObjectName("InputText")
        self.OutputText = QtWidgets.QLabel(self.MainWidget)
        self.OutputText.setGeometry(QtCore.QRect(860, 250, 321, 61))
        self.OutputText.setStyleSheet("font: 25pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239, 239); padding: 5px;\n"
"text-decoration: underline;")
        self.OutputText.setObjectName("OutputText")
        self.DatabaseButton = QtWidgets.QPushButton(self.MainWidget)
        self.DatabaseButton.setGeometry(QtCore.QRect(429, 460, 211, 70))
        self.DatabaseButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.DatabaseButton.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.DatabaseButton.setObjectName("DatabaseButton")
        self.FileButton = QtWidgets.QPushButton(self.MainWidget)
        self.FileButton.setGeometry(QtCore.QRect(700, 460, 200, 70))
        self.FileButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.FileButton.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.FileButton.setObjectName("FileButton")
        self.ErrorLabel = QtWidgets.QLabel(self.MainWidget)
        self.ErrorLabel.setGeometry(QtCore.QRect(370, 210, 631, 41))
        self.ErrorLabel.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 18pt \"Sans Serif\";")
        self.ErrorLabel.setObjectName("ErrorLabel")
        self.CalculateButton = QtWidgets.QPushButton(self.MainWidget)
        self.CalculateButton.setGeometry(QtCore.QRect(570, 350, 200, 70))
        self.CalculateButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CalculateButton.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.CalculateButton.setObjectName("CalculateButton")
        self.PrevButton.raise_()
        self.NextButton.raise_()
        self.EquationImage.raise_()
        self.ZetaInput.raise_()
        self.SubTitleText.raise_()
        self.ZetaOutput.raise_()
        self.InputText.raise_()
        self.OutputText.raise_()
        self.DatabaseButton.raise_()
        self.FileButton.raise_()
        self.CalculateButton.raise_()
        self.ErrorLabel.raise_()

        self.retranslateUi(SingleCalculatorScreen)
        QtCore.QMetaObject.connectSlotsByName(SingleCalculatorScreen)

    def retranslateUi(self, SingleCalculatorScreen):
        _translate = QtCore.QCoreApplication.translate
        SingleCalculatorScreen.setWindowTitle(_translate("SingleCalculatorScreen", "Visualising the Riemann Hypothesis - Calculator"))
        self.Title.setText(_translate("SingleCalculatorScreen", "Calculator"))
        self.SingleTab.setText(_translate("SingleCalculatorScreen", "Single"))
        self.TableTab.setText(_translate("SingleCalculatorScreen", "Table"))
        self.LeaderboardTab.setText(_translate("SingleCalculatorScreen", "Leaderboard"))
        self.PrevButton.setText(_translate("SingleCalculatorScreen", "Prev"))
        self.NextButton.setText(_translate("SingleCalculatorScreen", "Next"))
        self.SubTitleText.setText(_translate("SingleCalculatorScreen", "<html><head/><body><p><span style=\" font-weight:600;\">Single Zeta Calculator</span></p></body></html>"))
        self.InputText.setText(_translate("SingleCalculatorScreen", "<html><head/><body><p><span style=\" font-weight:600;\">Input Value (s):</span></p></body></html>"))
        self.OutputText.setText(_translate("SingleCalculatorScreen", "<html><head/><body><p><span style=\" font-weight:600;\">Output Value 𝜻(s):</span></p></body></html>"))
        self.DatabaseButton.setText(_translate("SingleCalculatorScreen", "Save to database"))
        self.FileButton.setText(_translate("SingleCalculatorScreen", "Save to file"))
        self.ErrorLabel.setText(_translate("SingleCalculatorScreen", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.CalculateButton.setText(_translate("SingleCalculatorScreen", "Calculate 🠖"))
