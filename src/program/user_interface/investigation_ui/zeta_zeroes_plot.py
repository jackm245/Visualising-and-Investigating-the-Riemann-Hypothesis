# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/investigation_screens/zeta_zeroes_plot.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ZetaZeroesPlotScreen(object):
    def setupUi(self, ZetaZeroesPlotScreen):
        ZetaZeroesPlotScreen.setObjectName("ZetaZeroesPlotScreen")
        ZetaZeroesPlotScreen.resize(1340, 720)
        ZetaZeroesPlotScreen.setSizeGripEnabled(False)
        self.widget = QtWidgets.QWidget(ZetaZeroesPlotScreen)
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
        self.ZetaZeroesPlotTab = QtWidgets.QPushButton(self.TabBar)
        self.ZetaZeroesPlotTab.setGeometry(QtCore.QRect(220, 5, 200, 70))
        self.ZetaZeroesPlotTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ZetaZeroesPlotTab.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239, 239);\n"
"font: 18pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
"")
        self.ZetaZeroesPlotTab.setObjectName("ZetaZeroesPlotTab")
        self.PrimeTab = QtWidgets.QPushButton(self.TabBar)
        self.PrimeTab.setGeometry(QtCore.QRect(430, 5, 200, 70))
        self.PrimeTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PrimeTab.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color:rgb(69, 69, 69);\n"
"background-color: rgb(69, 69, 69);\n"
"font: 18pt \"Sans Serif\"; color:rgb(239, 239, 239);\n"
"")
        self.PrimeTab.setObjectName("PrimeTab")
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
        self.MainText.setGeometry(QtCore.QRect(40, 80, 1251, 341))
        self.MainText.setStyleSheet("font: 13pt \"Sans Serif\"; color:rgb(69, 69, 69);\n"
"background-color: rgb(239, 239, 239); padding: 5px;")
        self.MainText.setWordWrap(True)
        self.MainText.setObjectName("MainText")

        self.retranslateUi(ZetaZeroesPlotScreen)
        QtCore.QMetaObject.connectSlotsByName(ZetaZeroesPlotScreen)

    def retranslateUi(self, ZetaZeroesPlotScreen):
        _translate = QtCore.QCoreApplication.translate
        ZetaZeroesPlotScreen.setWindowTitle(_translate("ZetaZeroesPlotScreen", "Visualising the Riemann Hypothesis - Investigation"))
        self.Title.setText(_translate("ZetaZeroesPlotScreen", "Graph Plots"))
        self.PolarTab.setText(_translate("ZetaZeroesPlotScreen", "Polar"))
        self.ZetaZeroesPlotTab.setText(_translate("ZetaZeroesPlotScreen", "Zeroes"))
        self.PrimeTab.setText(_translate("ZetaZeroesPlotScreen", "Prime"))
        self.PrevButton.setText(_translate("ZetaZeroesPlotScreen", "Prev"))
        self.NextButton.setText(_translate("ZetaZeroesPlotScreen", "Next"))
        self.GraphButton.setText(_translate("ZetaZeroesPlotScreen", "Graph"))
        self.SubTitleText.setText(_translate("ZetaZeroesPlotScreen", "<html><head/><body><p><span style=\" font-weight:600;\">Zeroes of the Riemann Zeta Function</span></p></body></html>"))
        self.MainText.setText(_translate("ZetaZeroesPlotScreen", "<html><head/><body><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla facilisis magna ante, mollis mattis lectus imperdiet vitae. Aliquam luctus felis nec leo finibus, vitae varius lorem ullamcorper. Aenean congue orci ut mi viverra auctor. Aliquam erat volutpat. Etiam quis porta nunc. Phasellus efficitur feugiat lorem sit amet fermentum. Vestibulum justo lorem, porta et pellentesque vitae, malesuada aliquet orci. In eget ultricies massa. In placerat dui dui, id vulputate turpis rutrum sagittis. Vivamus ut dui ut mi interdum sollicitudin. Pellentesque ut felis felis. Donec id felis leo. Suspendisse quis quam a turpis elementum tempus eget consequat ipsum. Nullam laoreet accumsan justo sed egestas. Integer sed lectus ex. Praesent laoreet id lacus ut molestie. Aliquam at eros sapien. Mauris scelerisque nibh ex, id consequat turpis pellentesque sit amet. Phasellus in nulla eget lacus vestibulum iaculis vitae sed diam. Sed lacinia metus id molestie feugiat. Aenean vitae cursus nibh, a posuere magna. Nunc id orci non ipsum eleifend dignissim. Donec sodales, nulla ac egestas facilisis, urna eros vulputate nisl, ac tempus nibh leo quis magna. Fusce in massa felis. Phasellus sollicitudin mollis ante, quis imperdiet orci egestas id. In velit lacus, gravida eget mauris id, venenatis dictum augue. Proin at orci sed mauris rutrum aliquet in eu tortor. Integer sapien purus, varius nec cursus eget, laoreet eu massa. In varius magna ac eros congue pretium. Donec vehicula a urna vel auctor. Proin convallis magna congue ex commodo, sit amet sodales velit tincidunt. Sed finibus elementum felis vel posuere. Nam turpis justo, pulvinar et accumsan nec, eleifend non ligula. Etiam tempor in mi eget dapibus. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Cras sollicitudin arcu mollis, iaculis tellus eget, commodo justo. Mauris mattis eget mi nec molestie. Sed nec lectus tristique, tempus elit pretium, consectetur magna. Integer dignissim augue in condimentum maximus. Fusce volutpat, nisl ac congue congue, lorem ligula tempus est, quis facilisis lacus dui ultrices ipsum. Aenean quis velit in arcu luctus eleifend vel semper ex. Duis efficitur placerat malesuada. Curabitur nec lacinia magna, sit amet cursus arcu. Pellentesque tristique lacus tincidunt ultricies ultricies. Sed congue odio ac tempor suscipit. Mauris imperdiet magna dolor, eu bibendum metus aliquam in. Quisque felis ex, consectetur id mi et, iaculis scelerisque arcu. Donec tincidunt volutpat risus, et tincidunt augue viverra non. Nulla gravida arcu a ornare aliquam.</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ZetaZeroesPlotScreen = QtWidgets.QDialog()
    ui = Ui_ZetaZeroesPlotScreen()
    ui.setupUi(ZetaZeroesPlotScreen)
    ZetaZeroesPlotScreen.show()
    sys.exit(app.exec_())
