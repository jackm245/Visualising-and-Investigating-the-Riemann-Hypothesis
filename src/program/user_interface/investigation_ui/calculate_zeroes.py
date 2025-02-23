"""
calculate_zeroes.py
===================
A GUI for the calculate zeroes page of the investigation section
"""


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CalculateZeroesScreen(object):

    def setupUi(self, CalculateZeroesScreen):
        CalculateZeroesScreen.setObjectName("CalculateZeroesScreen")
        CalculateZeroesScreen.resize(1340, 720)
        CalculateZeroesScreen.setSizeGripEnabled(False)
        self.widget = QtWidgets.QWidget(CalculateZeroesScreen)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1340, 720))
        self.widget.setStyleSheet("background-color: rgb(69, 69, 69);")
        self.widget.setObjectName("widget")
        self.Title = QtWidgets.QLabel(self.widget)
        self.Title.setGeometry(QtCore.QRect(540, 20, 261, 51))
        self.Title.setStyleSheet("font: 36pt \"Sans Serif\"; color:rgb(239, 239, 239)")
        self.Title.setObjectName("Title")
        self.TabBar = QtWidgets.QWidget(self.widget)
        self.TabBar.setGeometry(QtCore.QRect(0, 80, 1340, 80))
        self.TabBar.setStyleSheet("background-color: rgb(239, 239, 239);")
        self.TabBar.setObjectName("TabBar")
        self.ZeroesTab = QtWidgets.QPushButton(self.TabBar)
        self.ZeroesTab.setGeometry(QtCore.QRect(10, 5, 220, 70))
        self.ZeroesTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ZeroesTab.setStyleSheet("border: 2px solid;\n"
                "border-radius: 20px;\n"
                "border-color:rgb(69, 69, 69);\n"
                "background-color: rgb(239, 239,239);\n"
                "font: 18pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
                "")
        self.ZeroesTab.setObjectName("ZeroesTab")
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
        self.NoOfZeroesInput = QtWidgets.QLineEdit(self.MainWidget)
        self.NoOfZeroesInput.setGeometry(QtCore.QRect(405, 190, 531, 81))
        self.NoOfZeroesInput.setStyleSheet("background-color: rgb(239, 239, 239);\n"
                "color: rgb(69, 69, 69);\n"
                "font: 18pt \"Sans Serif\";\n"
                "border: 2px solid;\n"
                "border-radius: 20px;\n"
                "border-color:rgb(69, 69, 69);")
        self.NoOfZeroesInput.setText("")
        self.NoOfZeroesInput.setObjectName("NoOfZeroesInput")
        self.NoOfZeroesText = QtWidgets.QLabel(self.MainWidget)
        self.NoOfZeroesText.setGeometry(QtCore.QRect(120, 80, 1101, 61))
        self.NoOfZeroesText.setStyleSheet("font: 36pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
                "background-color: rgb(239, 239, 239); padding: 5px;\n"
                "text-decoration: underline;")
        self.NoOfZeroesText.setObjectName("NoOfZeroesText")
        self.CalculateButton = QtWidgets.QPushButton(self.MainWidget)
        self.CalculateButton.setGeometry(QtCore.QRect(590, 400, 141, 91))
        self.CalculateButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CalculateButton.setStyleSheet("border: 2px solid;\n"
                "border-radius: 20px;\n"
                "border-color:rgb(69, 69, 69);\n"
                "background-color: rgb(69, 69, 69);\n"
                "font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
                "")
        self.CalculateButton.setObjectName("CalculateButton")
        self.ErrorLabel = QtWidgets.QLabel(self.MainWidget)
        self.ErrorLabel.setGeometry(QtCore.QRect(390, 300, 701, 61))
        self.ErrorLabel.setStyleSheet("color: rgb(255, 0, 0);\n"
                "font: 18pt \"Sans Serif\";")
        self.ErrorLabel.setObjectName("ErrorLabel")

        self.retranslateUi(CalculateZeroesScreen)
        QtCore.QMetaObject.connectSlotsByName(CalculateZeroesScreen)

    def retranslateUi(self, CalculateZeroesScreen):
        _translate = QtCore.QCoreApplication.translate
        CalculateZeroesScreen.setWindowTitle(_translate("CalculateZeroesScreen", "Visualising the Riemann Hypothesis - Zeta Zeroes"))
        self.Title.setText(_translate("CalculateZeroesScreen", "Zeta Zeroes"))
        self.ZeroesTab.setText(_translate("CalculateZeroesScreen", "Zeroes Calculator"))
        self.PrevButton.setText(_translate("CalculateZeroesScreen", "Prev"))
        self.NextButton.setText(_translate("CalculateZeroesScreen", "Next"))
        self.NoOfZeroesInput.setPlaceholderText(_translate("CalculateZeroesScreen", "    Enter Number of Zeroes"))
        self.NoOfZeroesText.setText(_translate("CalculateZeroesScreen", "<html><head/><body><p align=\"right\"><span style=\" font-weight:600;\">How many zeroes would you like to calculate?</span></p></body></html>"))
        self.CalculateButton.setText(_translate("CalculateZeroesScreen", "Calculate\n"
"🠖"))
        self.ErrorLabel.setText(_translate("CalculateZeroesScreen", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
