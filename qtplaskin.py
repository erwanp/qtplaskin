# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtplaskin.ui'
#
# Created: Wed Jun  8 17:01:26 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1180, 659)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("qtplaskin.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("qtplaskin.svg")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("qtplaskin.svg")), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tab_4)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setSpacing(40)
        self.verticalLayout_6.setContentsMargins(5, 20, 5, 20)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.condList = QtGui.QListWidget(self.tab_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.condList.sizePolicy().hasHeightForWidth())
        self.condList.setSizePolicy(sizePolicy)
        self.condList.setObjectName(_fromUtf8("condList"))
        self.verticalLayout_6.addWidget(self.condList)
        self.condButton = QtGui.QPushButton(self.tab_4)
        self.condButton.setObjectName(_fromUtf8("condButton"))
        self.verticalLayout_6.addWidget(self.condButton)
        self.horizontalLayout_5.addLayout(self.verticalLayout_6)
        self.condWidget = ConditionsPlotWidget(self.tab_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.condWidget.sizePolicy().hasHeightForWidth())
        self.condWidget.setSizePolicy(sizePolicy)
        self.condWidget.setObjectName(_fromUtf8("condWidget"))
        self.horizontalLayout_5.addWidget(self.condWidget)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.tab)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setSpacing(40)
        self.verticalLayout_3.setContentsMargins(5, 20, 5, 20)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.speciesList = QtGui.QListWidget(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.speciesList.sizePolicy().hasHeightForWidth())
        self.speciesList.setSizePolicy(sizePolicy)
        self.speciesList.setObjectName(_fromUtf8("speciesList"))
        self.verticalLayout_3.addWidget(self.speciesList)
        self.plotButton = QtGui.QPushButton(self.tab)
        self.plotButton.setObjectName(_fromUtf8("plotButton"))
        self.verticalLayout_3.addWidget(self.plotButton)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.densWidget = DensityPlotWidget(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.densWidget.sizePolicy().hasHeightForWidth())
        self.densWidget.setSizePolicy(sizePolicy)
        self.densWidget.setObjectName(_fromUtf8("densWidget"))
        self.horizontalLayout_2.addWidget(self.densWidget)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.tab_3)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setSpacing(40)
        self.verticalLayout_4.setContentsMargins(5, 20, 5, 20)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.reactList = QtGui.QListWidget(self.tab_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reactList.sizePolicy().hasHeightForWidth())
        self.reactList.setSizePolicy(sizePolicy)
        self.reactList.setObjectName(_fromUtf8("reactList"))
        self.verticalLayout_4.addWidget(self.reactList)
        self.reactButton = QtGui.QPushButton(self.tab_3)
        self.reactButton.setObjectName(_fromUtf8("reactButton"))
        self.verticalLayout_4.addWidget(self.reactButton)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.reactWidget = RatePlotWidget(self.tab_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reactWidget.sizePolicy().hasHeightForWidth())
        self.reactWidget.setSizePolicy(sizePolicy)
        self.reactWidget.setObjectName(_fromUtf8("reactWidget"))
        self.horizontalLayout_4.addWidget(self.reactWidget)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.tab_2)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSpacing(40)
        self.verticalLayout_2.setContentsMargins(5, 20, 5, 20)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.speciesSourceList = QtGui.QListWidget(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.speciesSourceList.sizePolicy().hasHeightForWidth())
        self.speciesSourceList.setSizePolicy(sizePolicy)
        self.speciesSourceList.setObjectName(_fromUtf8("speciesSourceList"))
        self.verticalLayout_2.addWidget(self.speciesSourceList)
        self.sourceButton = QtGui.QPushButton(self.tab_2)
        self.sourceButton.setObjectName(_fromUtf8("sourceButton"))
        self.verticalLayout_2.addWidget(self.sourceButton)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.sourceWidget = SourcePlotWidget(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sourceWidget.sizePolicy().hasHeightForWidth())
        self.sourceWidget.setSizePolicy(sizePolicy)
        self.sourceWidget.setObjectName(_fromUtf8("sourceWidget"))
        self.horizontalLayout_3.addWidget(self.sourceWidget)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.tabWidget)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1180, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuOptions = QtGui.QMenu(self.menubar)
        self.menuOptions.setObjectName(_fromUtf8("menuOptions"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionLog_scale_in_time = QtGui.QAction(MainWindow)
        self.actionLog_scale_in_time.setCheckable(True)
        self.actionLog_scale_in_time.setObjectName(_fromUtf8("actionLog_scale_in_time"))
        self.actionExport_data = QtGui.QAction(MainWindow)
        self.actionExport_data.setObjectName(_fromUtf8("actionExport_data"))
        self.actionStart_a_simulation = QtGui.QAction(MainWindow)
        self.actionStart_a_simulation.setObjectName(_fromUtf8("actionStart_a_simulation"))
        self.actionImport_from_directory = QtGui.QAction(MainWindow)
        self.actionImport_from_directory.setObjectName(_fromUtf8("actionImport_from_directory"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionUpdate = QtGui.QAction(MainWindow)
        self.actionUpdate.setObjectName(_fromUtf8("actionUpdate"))
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionImport_from_directory)
        self.menuFile.addAction(self.actionExport_data)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionUpdate)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuOptions.addAction(self.actionLog_scale_in_time)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "QtPlaskin", None, QtGui.QApplication.UnicodeUTF8))
        self.condButton.setText(QtGui.QApplication.translate("MainWindow", "Plot", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QtGui.QApplication.translate("MainWindow", "Overview", None, QtGui.QApplication.UnicodeUTF8))
        self.plotButton.setText(QtGui.QApplication.translate("MainWindow", "Plot", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Densities", None, QtGui.QApplication.UnicodeUTF8))
        self.reactButton.setText(QtGui.QApplication.translate("MainWindow", "Plot", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("MainWindow", "Reactions", None, QtGui.QApplication.UnicodeUTF8))
        self.sourceButton.setText(QtGui.QApplication.translate("MainWindow", "Plot", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "Sensitivity analysis", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuOptions.setTitle(QtGui.QApplication.translate("MainWindow", "&Options", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "&Open...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "&Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLog_scale_in_time.setText(QtGui.QApplication.translate("MainWindow", "Log scale in time", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExport_data.setText(QtGui.QApplication.translate("MainWindow", "Export data...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStart_a_simulation.setText(QtGui.QApplication.translate("MainWindow", "Start a simulation...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImport_from_directory.setText(QtGui.QApplication.translate("MainWindow", "Import from directory...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImport_from_directory.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+I", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "Save...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUpdate.setText(QtGui.QApplication.translate("MainWindow", "Update", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUpdate.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+R", None, QtGui.QApplication.UnicodeUTF8))

from mplwidget import RatePlotWidget, SourcePlotWidget, ConditionsPlotWidget, DensityPlotWidget
