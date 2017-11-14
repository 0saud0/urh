# -*- coding: utf-8 -*-

#
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SimulatorTab(object):
    def setupUi(self, SimulatorTab):
        SimulatorTab.setObjectName("SimulatorTab")
        SimulatorTab.resize(827, 485)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(SimulatorTab)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.scrollArea = QtWidgets.QScrollArea(SimulatorTab)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 827, 485))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.splitter_2 = QtWidgets.QSplitter(self.scrollAreaWidgetContents)
        self.splitter_2.setStyleSheet("QSplitter::handle:vertical {\n"
"margin: 4px 0px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, \n"
"stop:0 rgba(255, 255, 255, 0), \n"
"stop:0.5 rgba(100, 100, 100, 100), \n"
"stop:1 rgba(255, 255, 255, 0));\n"
"image: url(:/icons/data/icons/splitter_handle_horizontal.svg);\n"
"}")
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setHandleWidth(6)
        self.splitter_2.setObjectName("splitter_2")
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setStyleSheet("QSplitter::handle:horizontal {\n"
"margin: 4px 0px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"stop:0 rgba(255, 255, 255, 0), \n"
"stop:0.5 rgba(100, 100, 100, 100), \n"
"stop:1 rgba(255, 255, 255, 0));\n"
"image: url(:/icons/data/icons/splitter_handle_vertical.svg);\n"
"}")
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(6)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.treeProtocols = GeneratorTreeView(self.layoutWidget)
        self.treeProtocols.setObjectName("treeProtocols")
        self.verticalLayout_3.addWidget(self.treeProtocols)
        self.layoutWidget_2 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setStyleSheet("QTabWidget::pane { border: 0; }")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gvSimulator = SimulatorGraphicsView(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gvSimulator.sizePolicy().hasHeightForWidth())
        self.gvSimulator.setSizePolicy(sizePolicy)
        self.gvSimulator.setObjectName("gvSimulator")
        self.verticalLayout.addWidget(self.gvSimulator)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.toolButton = QtWidgets.QToolButton(self.tab)
        icon = QtGui.QIcon.fromTheme("document-save")
        self.toolButton.setIcon(icon)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout_2.addWidget(self.toolButton)
        spacerItem = QtWidgets.QSpacerItem(37, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.btnPrevNav = QtWidgets.QToolButton(self.tab)
        self.btnPrevNav.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnPrevNav.sizePolicy().hasHeightForWidth())
        self.btnPrevNav.setSizePolicy(sizePolicy)
        self.btnPrevNav.setMaximumSize(QtCore.QSize(20, 16777215))
        icon = QtGui.QIcon.fromTheme("go-previous")
        self.btnPrevNav.setIcon(icon)
        self.btnPrevNav.setObjectName("btnPrevNav")
        self.horizontalLayout_2.addWidget(self.btnPrevNav)
        self.navLineEdit = QtWidgets.QLineEdit(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.navLineEdit.sizePolicy().hasHeightForWidth())
        self.navLineEdit.setSizePolicy(sizePolicy)
        self.navLineEdit.setObjectName("navLineEdit")
        self.horizontalLayout_2.addWidget(self.navLineEdit)
        self.btnNextNav = QtWidgets.QToolButton(self.tab)
        self.btnNextNav.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnNextNav.sizePolicy().hasHeightForWidth())
        self.btnNextNav.setSizePolicy(sizePolicy)
        self.btnNextNav.setMaximumSize(QtCore.QSize(20, 16777215))
        icon = QtGui.QIcon.fromTheme("go-next")
        self.btnNextNav.setIcon(icon)
        self.btnNextNav.setObjectName("btnNextNav")
        self.horizontalLayout_2.addWidget(self.btnNextNav)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.tblViewMessage = SimulatorMessageTableView(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tblViewMessage.sizePolicy().hasHeightForWidth())
        self.tblViewMessage.setSizePolicy(sizePolicy)
        self.tblViewMessage.setAlternatingRowColors(True)
        self.tblViewMessage.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tblViewMessage.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tblViewMessage.setShowGrid(False)
        self.tblViewMessage.setObjectName("tblViewMessage")
        self.tblViewMessage.horizontalHeader().setHighlightSections(False)
        self.tblViewMessage.verticalHeader().setHighlightSections(False)
        self.verticalLayout_6.addWidget(self.tblViewMessage)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lNumSelectedColumns = QtWidgets.QLabel(self.tab_2)
        self.lNumSelectedColumns.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lNumSelectedColumns.setObjectName("lNumSelectedColumns")
        self.horizontalLayout_3.addWidget(self.lNumSelectedColumns)
        self.lColumnsSelectedText = QtWidgets.QLabel(self.tab_2)
        self.lColumnsSelectedText.setObjectName("lColumnsSelectedText")
        self.horizontalLayout_3.addWidget(self.lColumnsSelectedText)
        spacerItem1 = QtWidgets.QSpacerItem(138, 33, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.cbViewType = QtWidgets.QComboBox(self.tab_2)
        self.cbViewType.setObjectName("cbViewType")
        self.cbViewType.addItem("")
        self.cbViewType.addItem("")
        self.cbViewType.addItem("")
        self.horizontalLayout_3.addWidget(self.cbViewType)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.line = QtWidgets.QFrame(self.layoutWidget_2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.btnStartSim = QtWidgets.QPushButton(self.layoutWidget_2)
        self.btnStartSim.setObjectName("btnStartSim")
        self.verticalLayout_2.addWidget(self.btnStartSim)
        self.layoutWidget_3 = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lblMsgFieldsValues = QtWidgets.QLabel(self.layoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblMsgFieldsValues.sizePolicy().hasHeightForWidth())
        self.lblMsgFieldsValues.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblMsgFieldsValues.setFont(font)
        self.lblMsgFieldsValues.setAlignment(QtCore.Qt.AlignCenter)
        self.lblMsgFieldsValues.setObjectName("lblMsgFieldsValues")
        self.verticalLayout_4.addWidget(self.lblMsgFieldsValues)
        self.detail_view_widget = QtWidgets.QStackedWidget(self.layoutWidget_3)
        self.detail_view_widget.setObjectName("detail_view_widget")
        self.page_empty = QtWidgets.QWidget()
        self.page_empty.setObjectName("page_empty")
        self.detail_view_widget.addWidget(self.page_empty)
        self.page_goto_action = QtWidgets.QWidget()
        self.page_goto_action.setObjectName("page_goto_action")
        self.verticalLayout_7 = QtWidgets.QGridLayout(self.page_goto_action)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_9 = QtWidgets.QLabel(self.page_goto_action)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_7.addWidget(self.label_9, 0, 0, 1, 1)
        self.goto_combobox = QtWidgets.QComboBox(self.page_goto_action)
        self.goto_combobox.setObjectName("goto_combobox")
        self.verticalLayout_7.addWidget(self.goto_combobox, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_7.addItem(spacerItem2, 0, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem3, 1, 0, 1, 3)
        self.detail_view_widget.addWidget(self.page_goto_action)
        self.page_message = QtWidgets.QWidget()
        self.page_message.setObjectName("page_message")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.page_message)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_10 = QtWidgets.QLabel(self.page_message)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setObjectName("label_10")
        self.gridLayout_6.addWidget(self.label_10, 1, 0, 1, 1)
        self.tblViewFieldValues = QtWidgets.QTableView(self.page_message)
        self.tblViewFieldValues.setAlternatingRowColors(True)
        self.tblViewFieldValues.setShowGrid(False)
        self.tblViewFieldValues.setObjectName("tblViewFieldValues")
        self.tblViewFieldValues.horizontalHeader().setDefaultSectionSize(150)
        self.tblViewFieldValues.horizontalHeader().setStretchLastSection(True)
        self.tblViewFieldValues.verticalHeader().setVisible(False)
        self.gridLayout_6.addWidget(self.tblViewFieldValues, 2, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.page_message)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setObjectName("label_11")
        self.gridLayout_6.addWidget(self.label_11, 2, 0, 1, 1)
        self.spinBoxRepeat = QtWidgets.QSpinBox(self.page_message)
        self.spinBoxRepeat.setMinimum(1)
        self.spinBoxRepeat.setObjectName("spinBoxRepeat")
        self.gridLayout_6.addWidget(self.spinBoxRepeat, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.page_message)
        self.label_2.setObjectName("label_2")
        self.gridLayout_6.addWidget(self.label_2, 0, 0, 1, 1)
        self.lblEncodingDecoding = QtWidgets.QLabel(self.page_message)
        self.lblEncodingDecoding.setObjectName("lblEncodingDecoding")
        self.gridLayout_6.addWidget(self.lblEncodingDecoding, 0, 2, 1, 1)
        self.detail_view_widget.addWidget(self.page_message)
        self.page_rule = QtWidgets.QWidget()
        self.page_rule.setObjectName("page_rule")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_rule)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_12 = QtWidgets.QLabel(self.page_rule)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 0, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem4, 1, 0, 1, 2)
        self.ruleCondLineEdit = ExpressionLineEdit(self.page_rule)
        self.ruleCondLineEdit.setObjectName("ruleCondLineEdit")
        self.gridLayout_3.addWidget(self.ruleCondLineEdit, 0, 1, 1, 1)
        self.detail_view_widget.addWidget(self.page_rule)
        self.page_ext_prog_action = QtWidgets.QWidget()
        self.page_ext_prog_action.setObjectName("page_ext_prog_action")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.page_ext_prog_action)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_13 = QtWidgets.QLabel(self.page_ext_prog_action)
        self.label_13.setObjectName("label_13")
        self.gridLayout_9.addWidget(self.label_13, 3, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.page_ext_prog_action)
        self.label_14.setObjectName("label_14")
        self.gridLayout_9.addWidget(self.label_14, 1, 0, 1, 1)
        self.extProgramLineEdit = QtWidgets.QLineEdit(self.page_ext_prog_action)
        self.extProgramLineEdit.setReadOnly(True)
        self.extProgramLineEdit.setObjectName("extProgramLineEdit")
        self.gridLayout_9.addWidget(self.extProgramLineEdit, 1, 1, 1, 1)
        self.cmdLineArgsLineEdit = QtWidgets.QLineEdit(self.page_ext_prog_action)
        self.cmdLineArgsLineEdit.setObjectName("cmdLineArgsLineEdit")
        self.gridLayout_9.addWidget(self.cmdLineArgsLineEdit, 3, 1, 1, 4)
        self.btnChooseExtProg = QtWidgets.QToolButton(self.page_ext_prog_action)
        self.btnChooseExtProg.setObjectName("btnChooseExtProg")
        self.gridLayout_9.addWidget(self.btnChooseExtProg, 1, 3, 1, 2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_9.addItem(spacerItem5, 4, 0, 1, 5)
        self.detail_view_widget.addWidget(self.page_ext_prog_action)
        self.verticalLayout_4.addWidget(self.detail_view_widget)
        self.verticalLayout_5.addWidget(self.splitter_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_8.addWidget(self.scrollArea)

        self.retranslateUi(SimulatorTab)
        self.tabWidget.setCurrentIndex(0)
        self.detail_view_widget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(SimulatorTab)

    def retranslateUi(self, SimulatorTab):
        _translate = QtCore.QCoreApplication.translate
        SimulatorTab.setWindowTitle(_translate("SimulatorTab", "Form"))
        self.label.setText(_translate("SimulatorTab", "Protocols:"))
        self.toolButton.setText(_translate("SimulatorTab", "..."))
        self.btnPrevNav.setText(_translate("SimulatorTab", "<"))
        self.btnNextNav.setText(_translate("SimulatorTab", ">"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("SimulatorTab", "Flow Graph"))
        self.lNumSelectedColumns.setText(_translate("SimulatorTab", "0"))
        self.lColumnsSelectedText.setText(_translate("SimulatorTab", "column(s) selected"))
        self.label_5.setText(_translate("SimulatorTab", "Viewtype:"))
        self.cbViewType.setItemText(0, _translate("SimulatorTab", "Bit"))
        self.cbViewType.setItemText(1, _translate("SimulatorTab", "Hex"))
        self.cbViewType.setItemText(2, _translate("SimulatorTab", "ASCII"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("SimulatorTab", "Messages"))
        self.btnStartSim.setText(_translate("SimulatorTab", "Start simulation ..."))
        self.lblMsgFieldsValues.setText(_translate("SimulatorTab", "Detail view for item"))
        self.label_9.setText(_translate("SimulatorTab", "Goto:"))
        self.label_10.setText(_translate("SimulatorTab", "Repeat:"))
        self.label_11.setText(_translate("SimulatorTab", "Labels:"))
        self.label_2.setText(_translate("SimulatorTab", "Coding:"))
        self.lblEncodingDecoding.setText(_translate("SimulatorTab", "-"))
        self.label_12.setText(_translate("SimulatorTab", "Condition:"))
        self.ruleCondLineEdit.setPlaceholderText(_translate("SimulatorTab", "not (item1.crc == 0b1010 and item2.length >=3)"))
        self.label_13.setText(_translate("SimulatorTab", "Command line arguments:"))
        self.label_14.setText(_translate("SimulatorTab", "External program:"))
        self.btnChooseExtProg.setText(_translate("SimulatorTab", "..."))

from urh.ui.ExpressionLineEdit import ExpressionLineEdit
from urh.ui.views.GeneratorTreeView import GeneratorTreeView
from urh.ui.views.SimulatorGraphicsView import SimulatorGraphicsView
from urh.ui.views.SimulatorMessageTableView import SimulatorMessageTableView
from . import urh_rc
