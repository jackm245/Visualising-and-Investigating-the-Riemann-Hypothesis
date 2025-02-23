"""
prime_numbers.py
================
A GUI for the prime numbers page of the investigation section
"""


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PrimeNumbersScreen(object):

    def setupUi(self, PrimeNumbersScreen):
        PrimeNumbersScreen.setObjectName("PrimeNumbersScreen")
        PrimeNumbersScreen.resize(1340, 720)
        PrimeNumbersScreen.setSizeGripEnabled(False)
        self.widget = QtWidgets.QWidget(PrimeNumbersScreen)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1340, 720))
        self.widget.setStyleSheet("background-color: rgb(69, 69, 69);")
        self.widget.setObjectName("widget")
        self.Title = QtWidgets.QLabel(self.widget)
        self.Title.setGeometry(QtCore.QRect(540, 20, 291, 51))
        self.Title.setStyleSheet("font: 36pt \"Sans Serif\"; color:rgb(239, 239, 239)")
        self.Title.setObjectName("Title")
        self.TabBar = QtWidgets.QWidget(self.widget)
        self.TabBar.setGeometry(QtCore.QRect(0, 80, 1340, 80))
        self.TabBar.setStyleSheet("background-color: rgb(239, 239, 239);")
        self.TabBar.setObjectName("TabBar")
        self.GraphsTab = QtWidgets.QPushButton(self.TabBar)
        self.GraphsTab.setGeometry(QtCore.QRect(10, 5, 200, 70))
        self.GraphsTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.GraphsTab.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.GraphsTab.setObjectName("GraphsTab")
        self.PrimesTab = QtWidgets.QPushButton(self.TabBar)
        self.PrimesTab.setGeometry(QtCore.QRect(220, 5, 200, 70))
        self.PrimesTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PrimesTab.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239, 239);\n"
"font: 18pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
"")
        self.PrimesTab.setObjectName("PrimesTab")
        self.CalculatorTab = QtWidgets.QPushButton(self.TabBar)
        self.CalculatorTab.setGeometry(QtCore.QRect(430, 5, 200, 70))
        self.CalculatorTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CalculatorTab.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.CalculatorTab.setObjectName("CalculatorTab")
        self.ZeroesTab = QtWidgets.QPushButton(self.TabBar)
        self.ZeroesTab.setGeometry(QtCore.QRect(640, 5, 200, 70))
        self.ZeroesTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ZeroesTab.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
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
        self.SubTitleText = QtWidgets.QLabel(self.MainWidget)
        self.SubTitleText.setGeometry(QtCore.QRect(40, 20, 681, 41))
        self.SubTitleText.setStyleSheet("font: 25pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239, 239); padding: 5px;")
        self.SubTitleText.setObjectName("SubTitleText")
        self.MainText = QtWidgets.QLabel(self.MainWidget)
        self.MainText.setGeometry(QtCore.QRect(40, 80, 1251, 341))
        self.MainText.setStyleSheet("font: 13pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239, 239); padding: 5px;")
        self.MainText.setWordWrap(True)
        self.MainText.setObjectName("MainText")
        self.NotesButton = QtWidgets.QPushButton(self.MainWidget)
        self.NotesButton.setGeometry(QtCore.QRect(570, 460, 200, 70))
        self.NotesButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.NotesButton.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.NotesButton.setObjectName("NotesButton")

        self.retranslateUi(PrimeNumbersScreen)
        QtCore.QMetaObject.connectSlotsByName(PrimeNumbersScreen)

    def retranslateUi(self, PrimeNumbersScreen):
        _translate = QtCore.QCoreApplication.translate
        PrimeNumbersScreen.setWindowTitle(_translate("PrimeNumbersScreen", "Visualising the Riemann Hypothesis - Investigation"))
        self.Title.setText(_translate("PrimeNumbersScreen", "Investigation"))
        self.GraphsTab.setText(_translate("PrimeNumbersScreen", "Graphs"))
        self.PrimesTab.setText(_translate("PrimeNumbersScreen", "Primes"))
        self.CalculatorTab.setText(_translate("PrimeNumbersScreen", "Calculator"))
        self.ZeroesTab.setText(_translate("PrimeNumbersScreen", "Zeroes"))
        self.PrevButton.setText(_translate("PrimeNumbersScreen", "Prev"))
        self.NextButton.setText(_translate("PrimeNumbersScreen", "Next"))
        self.SubTitleText.setText(_translate("PrimeNumbersScreen", "<html><head/><body><p><span style=\" font-weight:600;\">Prime Numbers</span></p></body></html>"))
        self.MainText.setText(_translate("PrimeNumbersScreen", "<html><head/><body><p>The Riemann Hypothesis and Prime Numbers go hand in hand. A prime number is a number larger than 1, such that it is only divisible by 1 and the number itself. </p><p>Just like with the non-trivial zeroes, there is not real way to calculate prime numbers apart from trial and error. However, we are able to use the Riemann Hypothesis in order to understand the distribution of prime numbers, and if the Riemann Hypothesis was proven to be true, we would be able to calculate certain values of prime numbers using a formula. </p><p>Another connection between the Riemann Hypothesis and the prime numbers, is that Leonhard Euler proved that the zeta function could be written as an infite product over all of the primes such that ζ(s) = Π(1/(1-p^-s)), where p is a prime number.</p><p>Furthermore if the Riemann Hypothesis was proven to be true, it would mean that the Weak Goldbach Conjecture is also true, which states that \'All odd integers greater than 5 are the sum of three primes\'. Furthermore, it would also mean that between consecutive cube numbers, there would always be at least 1 prime number.</p><p>All of these theorems and conjectures highlight the importance of the Riemann hypothesis, and that if it was to be proven, it would lead to several major break- throughs, not only in mathematics but quantum physics and computer science - fields that heavily use the prime numbers.</p></body></html>"))
        self.NotesButton.setText(_translate("PrimeNumbersScreen", "Notes"))
