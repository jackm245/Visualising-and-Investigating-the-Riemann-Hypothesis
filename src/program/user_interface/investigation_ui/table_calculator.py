"""
table_calculator.py
===================
A GUI for the table calculator page of the investigation section
"""


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TableCalculatorScreen(object):

    def setupUi(self, TableCalculatorScreen):
        TableCalculatorScreen.setObjectName("TableCalculatorScreen")
        TableCalculatorScreen.resize(1340, 720)
        TableCalculatorScreen.setSizeGripEnabled(False)
        self.widget = QtWidgets.QWidget(TableCalculatorScreen)
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
"background-color: rgb(69, 69,69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.SingleTab.setObjectName("SingleTab")
        self.TableTab = QtWidgets.QPushButton(self.TabBar)
        self.TableTab.setGeometry(QtCore.QRect(220, 5, 200, 70))
        self.TableTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.TableTab.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239, 239);\n"
"font: 18pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
"")
        self.TableTab.setObjectName("TableTab")
        self.LeaderboardTab = QtWidgets.QPushButton(self.TabBar)
        self.LeaderboardTab.setGeometry(QtCore.QRect(430, 5, 200, 70))
        self.LeaderboardTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.LeaderboardTab.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69,69);\n"
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
        self.SubTitleText.setGeometry(QtCore.QRect(40, 20, 381, 41))
        self.SubTitleText.setStyleSheet("font: 25pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239, 239); padding: 5px;")
        self.SubTitleText.setObjectName("SubTitleText")
        self.StartInput = QtWidgets.QLineEdit(self.MainWidget)
        self.StartInput.setGeometry(QtCore.QRect(485, 110, 421, 81))
        self.StartInput.setStyleSheet("background-color: rgb(239, 239, 239);\n"
"color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\";\n"
"border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);")
        self.StartInput.setText("")
        self.StartInput.setObjectName("StartInput")
        self.StartValueText = QtWidgets.QLabel(self.MainWidget)
        self.StartValueText.setGeometry(QtCore.QRect(100, 120, 291, 61))
        self.StartValueText.setStyleSheet("font: 36pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239, 239); padding: 5px;\n"
"text-decoration: underline;")
        self.StartValueText.setObjectName("StartValueText")
        self.CalculateButton = QtWidgets.QPushButton(self.MainWidget)
        self.CalculateButton.setGeometry(QtCore.QRect(980, 215, 200, 70))
        self.CalculateButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CalculateButton.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.CalculateButton.setObjectName("CalculateButton")
        self.StepText = QtWidgets.QLabel(self.MainWidget)
        self.StepText.setGeometry(QtCore.QRect(100, 220, 291, 61))
        self.StepText.setStyleSheet("font: 36pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239, 239); padding: 5px;\n"
"text-decoration: underline;")
        self.StepText.setObjectName("StepText")
        self.StepInput = QtWidgets.QLineEdit(self.MainWidget)
        self.StepInput.setGeometry(QtCore.QRect(485, 210, 421, 81))
        self.StepInput.setStyleSheet("background-color: rgb(239, 239, 239);\n"
"color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\";\n"
"border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);")
        self.StepInput.setText("")
        self.StepInput.setObjectName("StepInput")
        self.ErrorLabel = QtWidgets.QLabel(self.MainWidget)
        self.ErrorLabel.setGeometry(QtCore.QRect(400, 410, 701, 61))
        self.ErrorLabel.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 18pt \"Sans Serif\";")
        self.ErrorLabel.setObjectName("ErrorLabel")
        self.NoOfValuesText = QtWidgets.QLabel(self.MainWidget)
        self.NoOfValuesText.setGeometry(QtCore.QRect(10, 320, 381, 61))
        self.NoOfValuesText.setStyleSheet("font: 36pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239, 239); padding: 5px;\n"
"text-decoration: underline;")
        self.NoOfValuesText.setObjectName("NoOfValuesText")
        self.NoOfValuesInput = QtWidgets.QLineEdit(self.MainWidget)
        self.NoOfValuesInput.setGeometry(QtCore.QRect(485, 310, 421, 81))
        self.NoOfValuesInput.setStyleSheet("background-color: rgb(239, 239, 239);\n"
"color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\";\n"
"border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);")
        self.NoOfValuesInput.setText("")
        self.NoOfValuesInput.setObjectName("NoOfValuesInput")
        self.PrevButton.raise_()
        self.NextButton.raise_()
        self.StartInput.raise_()
        self.SubTitleText.raise_()
        self.StartValueText.raise_()
        self.CalculateButton.raise_()
        self.StepText.raise_()
        self.StepInput.raise_()
        self.ErrorLabel.raise_()
        self.NoOfValuesText.raise_()
        self.NoOfValuesInput.raise_()

        self.retranslateUi(TableCalculatorScreen)
        QtCore.QMetaObject.connectSlotsByName(TableCalculatorScreen)

    def retranslateUi(self, TableCalculatorScreen):
        _translate = QtCore.QCoreApplication.translate
        TableCalculatorScreen.setWindowTitle(_translate("TableCalculatorScreen", "Visualising the Riemann Hypothesis - Calculator"))
        self.Title.setText(_translate("TableCalculatorScreen", "Calculator"))
        self.SingleTab.setText(_translate("TableCalculatorScreen", "Single"))
        self.TableTab.setText(_translate("TableCalculatorScreen", "Table"))
        self.LeaderboardTab.setText(_translate("TableCalculatorScreen", "Leaderboard"))
        self.PrevButton.setText(_translate("TableCalculatorScreen", "Prev"))
        self.NextButton.setText(_translate("TableCalculatorScreen", "Next"))
        self.SubTitleText.setText(_translate("TableCalculatorScreen", "<html><head/><body><p><span style=\" font-weight:600;\">Table Zeta Calculation</span></p></body></html>"))
        self.StartInput.setPlaceholderText(_translate("TableCalculatorScreen", "    Enter Start Value"))
        self.StartValueText.setText(_translate("TableCalculatorScreen", "<html><head/><body><p align=\"right\"><span style=\" font-weight:600;\">Start Value:</span></p></body></html>"))
        self.CalculateButton.setText(_translate("TableCalculatorScreen", "Calculate 🠖"))
        self.StepText.setText(_translate("TableCalculatorScreen", "<html><head/><body><p align=\"right\"><span style=\" font-weight:600;\">Step:</span></p></body></html>"))
        self.StepInput.setPlaceholderText(_translate("TableCalculatorScreen", "    Enter Step Value"))
        self.ErrorLabel.setText(_translate("TableCalculatorScreen", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.NoOfValuesText.setText(_translate("TableCalculatorScreen", "<html><head/><body><p align=\"right\"><span style=\" font-weight:600;\">No. of Values:</span></p></body></html>"))
        self.NoOfValuesInput.setPlaceholderText(_translate("TableCalculatorScreen", "    Enter No. of Values"))
