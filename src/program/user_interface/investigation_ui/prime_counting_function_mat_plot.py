# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/investigation_screens/prime_counting_function_mat_plot.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PrimeCountingFunctionMatPlotScreen(object):
    def setupUi(self, PrimeCountingFunctionMatPlotScreen):
        PrimeCountingFunctionMatPlotScreen.setObjectName("PrimeCountingFunctionMatPlotScreen")
        PrimeCountingFunctionMatPlotScreen.resize(1340, 720)
        PrimeCountingFunctionMatPlotScreen.setSizeGripEnabled(False)

        self.retranslateUi(PrimeCountingFunctionMatPlotScreen)
        QtCore.QMetaObject.connectSlotsByName(PrimeCountingFunctionMatPlotScreen)

    def retranslateUi(self, PrimeCountingFunctionMatPlotScreen):
        _translate = QtCore.QCoreApplication.translate
        PrimeCountingFunctionMatPlotScreen.setWindowTitle(_translate("PrimeCountingFunctionMatPlotScreen", "Visualising the Riemann Hypothesis - Prime Counting Function"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PrimeCountingFunctionMatPlotScreen = QtWidgets.QDialog()
    ui = Ui_PrimeCountingFunctionMatPlotScreen()
    ui.setupUi(PrimeCountingFunctionMatPlotScreen)
    PrimeCountingFunctionMatPlotScreen.show()
    sys.exit(app.exec_())
