# -*- coding: utf-8 -*-

#
# Created: Thu Oct 12 09:06:39 2017
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SimulationDialog(object):
    def setupUi(self, SimulationDialog):
        SimulationDialog.setObjectName("SimulationDialog")
        SimulationDialog.resize(707, 370)
        self.verticalLayout = QtWidgets.QVBoxLayout(SimulationDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(SimulationDialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_simulation = QtWidgets.QWidget()
        self.tab_simulation.setObjectName("tab_simulation")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_simulation)
        self.gridLayout.setObjectName("gridLayout")
        self.lblCurrentRepeatValue = QtWidgets.QLabel(self.tab_simulation)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblCurrentRepeatValue.setFont(font)
        self.lblCurrentRepeatValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCurrentRepeatValue.setObjectName("lblCurrentRepeatValue")
        self.gridLayout.addWidget(self.lblCurrentRepeatValue, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.tab_simulation)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab_simulation)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 2, 1, 1)
        self.lblCurrentItemValue = QtWidgets.QLabel(self.tab_simulation)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblCurrentItemValue.setFont(font)
        self.lblCurrentItemValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCurrentItemValue.setObjectName("lblCurrentItemValue")
        self.gridLayout.addWidget(self.lblCurrentItemValue, 1, 3, 1, 1)
        self.btnSaveLog = QtWidgets.QToolButton(self.tab_simulation)
        icon = QtGui.QIcon.fromTheme("document-save")
        self.btnSaveLog.setIcon(icon)
        self.btnSaveLog.setObjectName("btnSaveLog")
        self.gridLayout.addWidget(self.btnSaveLog, 1, 4, 1, 1)
        self.textEditSimulation = QtWidgets.QTextEdit(self.tab_simulation)
        self.textEditSimulation.setReadOnly(True)
        self.textEditSimulation.setObjectName("textEditSimulation")
        self.gridLayout.addWidget(self.textEditSimulation, 0, 0, 1, 5)
        self.tabWidget.addTab(self.tab_simulation, "")
        self.tab_device = QtWidgets.QWidget()
        self.tab_device.setObjectName("tab_device")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab_device)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textEditDevices = QtWidgets.QTextEdit(self.tab_device)
        self.textEditDevices.setReadOnly(True)
        self.textEditDevices.setObjectName("textEditDevices")
        self.horizontalLayout_2.addWidget(self.textEditDevices)
        self.tabWidget.addTab(self.tab_device, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.btnStartStop = QtWidgets.QPushButton(SimulationDialog)
        icon = QtGui.QIcon.fromTheme("media-playback-start")
        self.btnStartStop.setIcon(icon)
        self.btnStartStop.setObjectName("btnStartStop")
        self.verticalLayout.addWidget(self.btnStartStop)

        self.retranslateUi(SimulationDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SimulationDialog)

    def retranslateUi(self, SimulationDialog):
        _translate = QtCore.QCoreApplication.translate
        SimulationDialog.setWindowTitle(_translate("SimulationDialog", "Simulation"))
        self.lblCurrentRepeatValue.setText(_translate("SimulationDialog", "0"))
        self.label.setText(_translate("SimulationDialog", "Current iteration:"))
        self.label_2.setText(_translate("SimulationDialog", "Current item:"))
        self.lblCurrentItemValue.setText(_translate("SimulationDialog", "0"))
        self.btnSaveLog.setText(_translate("SimulationDialog", "..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_simulation), _translate("SimulationDialog", "Simulation"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_device), _translate("SimulationDialog", "Device Messages"))
        self.btnStartStop.setText(_translate("SimulationDialog", "Start"))

