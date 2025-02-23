"""
prime_counting_function.py
==========================
A GUI for the prime counting function page of the investigation section
"""


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PrimeCountingFunctionScreen(object):
    def setupUi(self, PrimeCountingFunctionScreen):
        PrimeCountingFunctionScreen.setObjectName("PrimeCountingFunctionScreen")
        PrimeCountingFunctionScreen.resize(1340, 720)
        PrimeCountingFunctionScreen.setSizeGripEnabled(False)
        self.widget = QtWidgets.QWidget(PrimeCountingFunctionScreen)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1340, 720))
        self.widget.setStyleSheet("background-color: rgb(69, 69, 69);")
        self.widget.setObjectName("widget")
        self.Title = QtWidgets.QLabel(self.widget)
        self.Title.setGeometry(QtCore.QRect(550, 20, 251, 51))
        self.Title.setStyleSheet("font: 36pt \"Sans Serif\"; color:rgb(239, 239, 239)")
        self.Title.setObjectName("Title")
        self.TabBar = QtWidgets.QWidget(self.widget)
        self.TabBar.setGeometry(QtCore.QRect(0, 80, 1340, 80))
        self.TabBar.setStyleSheet("background-color: rgb(239, 239, 239);")
        self.TabBar.setObjectName("TabBar")
        self.ZetaZeroesPlotTab = QtWidgets.QPushButton(self.TabBar)
        self.ZetaZeroesPlotTab.setGeometry(QtCore.QRect(220, 5, 200, 70))
        self.ZetaZeroesPlotTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ZetaZeroesPlotTab.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.ZetaZeroesPlotTab.setObjectName("ZetaZeroesPlotTab")
        self.PolarTab = QtWidgets.QPushButton(self.TabBar)
        self.PolarTab.setGeometry(QtCore.QRect(10, 5, 200, 70))
        self.PolarTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PolarTab.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.PolarTab.setObjectName("PolarTab")
        self.PrimeTab = QtWidgets.QPushButton(self.TabBar)
        self.PrimeTab.setGeometry(QtCore.QRect(430, 5, 200, 70))
        self.PrimeTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PrimeTab.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239, 239);\n"
"font: 18pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
"")
        self.PrimeTab.setObjectName("PrimeTab")
        self.ZetaApproximationTab = QtWidgets.QPushButton(self.TabBar)
        self.ZetaApproximationTab.setGeometry(QtCore.QRect(640, 5, 200, 70))
        self.ZetaApproximationTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ZetaApproximationTab.setStyleSheet("border-radius: 20px;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"font: 18pt \"Sans Serif\";\n"
"")
        self.ZetaApproximationTab.setText("")
        self.ZetaApproximationTab.setObjectName("ZetaApproximationTab")
        self.ZetaApproximationLabel = QtWidgets.QLabel(self.TabBar)
        self.ZetaApproximationLabel.setGeometry(QtCore.QRect(640, 5, 200, 70))
        self.ZetaApproximationLabel.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.ZetaApproximationLabel.setObjectName("ZetaApproximationLabel")
        self.ZetaZeroesPlotTab.raise_()
        self.PolarTab.raise_()
        self.PrimeTab.raise_()
        self.ZetaApproximationLabel.raise_()
        self.ZetaApproximationTab.raise_()
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
        self.GraphButton = QtWidgets.QPushButton(self.MainWidget)
        self.GraphButton.setGeometry(QtCore.QRect(570, 460, 200, 70))
        self.GraphButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.GraphButton.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.GraphButton.setObjectName("GraphButton")
        self.SubTitleText = QtWidgets.QLabel(self.MainWidget)
        self.SubTitleText.setGeometry(QtCore.QRect(40, 20, 681, 41))
        self.SubTitleText.setStyleSheet("font: 25pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239, 239); padding: 5px;")
        self.SubTitleText.setObjectName("SubTitleText")
        self.MainText = QtWidgets.QLabel(self.MainWidget)
        self.MainText.setGeometry(QtCore.QRect(40, 80, 1251, 361))
        self.MainText.setStyleSheet("font: 13pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239, 239); padding: 5px;")
        self.MainText.setWordWrap(True)
        self.MainText.setObjectName("MainText")

        self.retranslateUi(PrimeCountingFunctionScreen)
        QtCore.QMetaObject.connectSlotsByName(PrimeCountingFunctionScreen)

    def retranslateUi(self, PrimeCountingFunctionScreen):
        _translate = QtCore.QCoreApplication.translate
        PrimeCountingFunctionScreen.setWindowTitle(_translate("PrimeCountingFunctionScreen", "Visualising the Riemann Hypothesis - Investigation"))
        self.Title.setText(_translate("PrimeCountingFunctionScreen", "Graph Plots"))
        self.ZetaZeroesPlotTab.setText(_translate("PrimeCountingFunctionScreen", "Zeroes"))
        self.PolarTab.setText(_translate("PrimeCountingFunctionScreen", "Polar"))
        self.PrimeTab.setText(_translate("PrimeCountingFunctionScreen", "Prime"))
        self.ZetaApproximationLabel.setText(_translate("PrimeCountingFunctionScreen", "<html><head/><body><p align=\"center\">Zeta<br/>Approximation</p></body></html>"))
        self.PrevButton.setText(_translate("PrimeCountingFunctionScreen", "Prev"))
        self.NextButton.setText(_translate("PrimeCountingFunctionScreen", "Next"))
        self.GraphButton.setText(_translate("PrimeCountingFunctionScreen", "Graph"))
        self.SubTitleText.setText(_translate("PrimeCountingFunctionScreen", "<html><head/><body><p><span style=\" font-weight:600;\">The Prime Counting Function</span></p></body></html>"))
        self.MainText.setText(_translate("PrimeCountingFunctionScreen", "<html><head/><body><p>The prime number theorem was a theorem thought of by Carl Friedrich Gauss near the end of the 18th century. This theorem describes the distribution of the prime numbers. It formalises the intuitive idea that as numbers get larger, the prime numbers are less common, by precisely quantifying the rate at which this occurs. One way this theorem was modelled was through the prime counting function (denoted π(N)). Where π(N) gives the number of primes that are less than or equal to N . Given this we can say that as N → ∞ then π(N)/log(N) → 1, where log(N) is the natural logarithm of N This, therefore, means that: π(N) ∼ N/log(N).</p><p>This means we can approximate the numbers of primes less than or equal to N, by calculating N/log(N). However, Peter Dirichlet and Carl Friedrich Gauss came up this a much better approximation for π(N). They said that: π(N) ∼ Li(N), where Li(N) is the logarithmic integral of N. Using Li(N) is much more accurate than using N/log(N). As well as the prime counting function, we also have a similar function called the prime power function (denoted by Π(N)). In the prime counting function, you would get 1 point per prime number (less than or equal to N ). But in the prime power function, you get 1 point per prime + 1/2 point per prime squared +1/3 point per prime cubed and so on.</p><p>But how is this related to the Riemann Hypothesis? It turns out that the prime number theorem was proved by using the Riemann Zeta Function. If the Riemann Hypothesis were true, then the difference between the prime counting function, and prime power function was be as small as possible. This is significant as it would lead to many other conjectures involving prime numbers to also be proven true.</p><p>Press the graph button to see the distribution of prime numbers, and how this is approximated using other functions.</p></body></html>"))
