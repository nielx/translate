# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/jhe/khmerOS/svn-wf/trunk/editor/ui/MainEditor.ui'
#
# Created: Tue Dec 12 19:08:25 2006
#      by: PyQt4 UI code generator 4.0.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(QtCore.QSize(QtCore.QRect(0,0,498,492).size()).expandedTo(MainWindow.minimumSizeHint()))

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(7),QtGui.QSizePolicy.Policy(7))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(400,300))
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainWindow.setWindowIcon(QtGui.QIcon("../images/icon.png"))

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0,0,498,31))
        self.menubar.setObjectName("menubar")

        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")

        self.menuOpen_Recent = QtGui.QMenu(self.menuFile)
        self.menuOpen_Recent.setIcon(QtGui.QIcon("../images/open.png"))
        self.menuOpen_Recent.setObjectName("menuOpen_Recent")

        self.menuSettings = QtGui.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")

        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setEnabled(True)
        self.menuView.setObjectName("menuView")

        self.menuGo = QtGui.QMenu(self.menubar)
        self.menuGo.setObjectName("menuGo")

        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")

        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")

        self.menuWindow = QtGui.QMenu(self.menubar)
        self.menuWindow.setObjectName("menuWindow")

        self.menuToolbars = QtGui.QMenu(self.menuWindow)
        self.menuToolbars.setObjectName("menuToolbars")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.toolStandard = QtGui.QToolBar(MainWindow)
        self.toolStandard.setEnabled(True)
        self.toolStandard.setOrientation(QtCore.Qt.Horizontal)
        self.toolStandard.setObjectName("toolStandard")
        MainWindow.addToolBar(self.toolStandard)

        self.toolNavigation = QtGui.QToolBar(MainWindow)
        self.toolNavigation.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.toolNavigation.setAcceptDrops(False)
        self.toolNavigation.setOrientation(QtCore.Qt.Horizontal)
        self.toolNavigation.setObjectName("toolNavigation")
        MainWindow.addToolBar(self.toolNavigation)

        self.actionNew = QtGui.QAction(MainWindow)
        self.actionNew.setIcon(QtGui.QIcon("../images/new.png"))
        self.actionNew.setObjectName("actionNew")

        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setIcon(QtGui.QIcon("../images/open.png"))
        self.actionOpen.setObjectName("actionOpen")

        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setEnabled(False)
        self.actionSave.setIcon(QtGui.QIcon("../images/save.png"))
        self.actionSave.setObjectName("actionSave")

        self.actionSaveas = QtGui.QAction(MainWindow)
        self.actionSaveas.setEnabled(False)
        self.actionSaveas.setIcon(QtGui.QIcon("../images/saveAs.png"))
        self.actionSaveas.setObjectName("actionSaveas")

        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setIcon(QtGui.QIcon("../images/stop.png"))
        self.actionExit.setObjectName("actionExit")

        self.actionUndo = QtGui.QAction(MainWindow)
        self.actionUndo.setEnabled(False)
        self.actionUndo.setIcon(QtGui.QIcon("../images/undo.png"))
        self.actionUndo.setObjectName("actionUndo")

        self.actionRedo = QtGui.QAction(MainWindow)
        self.actionRedo.setEnabled(False)
        self.actionRedo.setIcon(QtGui.QIcon("../images/redo.png"))
        self.actionRedo.setObjectName("actionRedo")

        self.actionCut = QtGui.QAction(MainWindow)
        self.actionCut.setEnabled(False)
        self.actionCut.setIcon(QtGui.QIcon("../images/cut.png"))
        self.actionCut.setObjectName("actionCut")

        self.actionCopy = QtGui.QAction(MainWindow)
        self.actionCopy.setCheckable(False)
        self.actionCopy.setEnabled(False)
        self.actionCopy.setIcon(QtGui.QIcon("../images/copy.png"))
        self.actionCopy.setObjectName("actionCopy")

        self.actionPaste = QtGui.QAction(MainWindow)
        self.actionPaste.setEnabled(False)
        self.actionPaste.setIcon(QtGui.QIcon("../images/paste.png"))
        self.actionPaste.setObjectName("actionPaste")

        self.actionFind = QtGui.QAction(MainWindow)
        self.actionFind.setEnabled(False)
        self.actionFind.setIcon(QtGui.QIcon("../images/find.png"))
        self.actionFind.setObjectName("actionFind")

        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")

        self.actionShowMenuBar = QtGui.QAction(MainWindow)
        self.actionShowMenuBar.setObjectName("actionShowMenuBar")

        self.actionShowTUview = QtGui.QAction(MainWindow)
        self.actionShowTUview.setObjectName("actionShowTUview")

        self.actionAboutQT = QtGui.QAction(MainWindow)
        self.actionAboutQT.setObjectName("actionAboutQT")

        self.actionShow_MenuBar = QtGui.QAction(MainWindow)
        self.actionShow_MenuBar.setObjectName("actionShow_MenuBar")

        self.actionShow_TUview = QtGui.QAction(MainWindow)
        self.actionShow_TUview.setObjectName("actionShow_TUview")

        self.actionFirst = QtGui.QAction(MainWindow)
        self.actionFirst.setEnabled(False)
        self.actionFirst.setIcon(QtGui.QIcon("../images/first.png"))
        self.actionFirst.setObjectName("actionFirst")

        self.actionPrevious = QtGui.QAction(MainWindow)
        self.actionPrevious.setEnabled(False)
        self.actionPrevious.setIcon(QtGui.QIcon("../images/previous.png"))
        self.actionPrevious.setObjectName("actionPrevious")

        self.actionNext = QtGui.QAction(MainWindow)
        self.actionNext.setEnabled(False)
        self.actionNext.setIcon(QtGui.QIcon("../images/next.png"))
        self.actionNext.setObjectName("actionNext")

        self.actionLast = QtGui.QAction(MainWindow)
        self.actionLast.setEnabled(False)
        self.actionLast.setIcon(QtGui.QIcon("../images/last.png"))
        self.actionLast.setObjectName("actionLast")

        self.actionShowDetail = QtGui.QAction(MainWindow)
        self.actionShowDetail.setObjectName("actionShowDetail")

        self.actionShowComment = QtGui.QAction(MainWindow)
        self.actionShowComment.setObjectName("actionShowComment")

        self.actionShowOverview = QtGui.QAction(MainWindow)
        self.actionShowOverview.setObjectName("actionShowOverview")

        self.actionCopySource2Target = QtGui.QAction(MainWindow)
        self.actionCopySource2Target.setEnabled(False)
        self.actionCopySource2Target.setObjectName("actionCopySource2Target")

        self.actionToggleFuzzy = QtGui.QAction(MainWindow)
        self.actionToggleFuzzy.setEnabled(False)
        self.actionToggleFuzzy.setObjectName("actionToggleFuzzy")

        self.actionFile = QtGui.QAction(MainWindow)
        self.actionFile.setObjectName("actionFile")

        self.actionFind_Previous = QtGui.QAction(MainWindow)
        self.actionFind_Previous.setEnabled(False)
        self.actionFind_Previous.setObjectName("actionFind_Previous")

        self.actionFind_Next = QtGui.QAction(MainWindow)
        self.actionFind_Next.setEnabled(False)
        self.actionFind_Next.setObjectName("actionFind_Next")

        self.actionReplace = QtGui.QAction(MainWindow)
        self.actionReplace.setEnabled(False)
        self.actionReplace.setObjectName("actionReplace")

        self.actionFindNext = QtGui.QAction(MainWindow)
        self.actionFindNext.setEnabled(False)
        self.actionFindNext.setObjectName("actionFindNext")

        self.actionOpenInNewWindow = QtGui.QAction(MainWindow)
        self.actionOpenInNewWindow.setIcon(QtGui.QIcon("../images/window_new.png"))
        self.actionOpenInNewWindow.setObjectName("actionOpenInNewWindow")

        self.actionFindPrevious = QtGui.QAction(MainWindow)
        self.actionFindPrevious.setEnabled(False)
        self.actionFindPrevious.setObjectName("actionFindPrevious")

        self.actionSelectAll = QtGui.QAction(MainWindow)
        self.actionSelectAll.setEnabled(False)
        self.actionSelectAll.setObjectName("actionSelectAll")

        self.actionEdit_Header = QtGui.QAction(MainWindow)
        self.actionEdit_Header.setEnabled(False)
        self.actionEdit_Header.setObjectName("actionEdit_Header")

        self.actionPreferences = QtGui.QAction(MainWindow)
        self.actionPreferences.setIcon(QtGui.QIcon("../images/configure.png"))
        self.actionPreferences.setObjectName("actionPreferences")

        self.actionComment = QtGui.QAction(MainWindow)
        self.actionComment.setCheckable(True)
        self.actionComment.setObjectName("actionComment")

        self.actionToolbars = QtGui.QAction(MainWindow)
        self.actionToolbars.setObjectName("actionToolbars")

        self.actionFilterFuzzy = QtGui.QAction(MainWindow)
        self.actionFilterFuzzy.setCheckable(True)
        self.actionFilterFuzzy.setChecked(True)
        self.actionFilterFuzzy.setEnabled(False)
        self.actionFilterFuzzy.setObjectName("actionFilterFuzzy")

        self.actionFilterTranslated = QtGui.QAction(MainWindow)
        self.actionFilterTranslated.setCheckable(True)
        self.actionFilterTranslated.setChecked(True)
        self.actionFilterTranslated.setEnabled(False)
        self.actionFilterTranslated.setObjectName("actionFilterTranslated")

        self.actionFilterUntranslated = QtGui.QAction(MainWindow)
        self.actionFilterUntranslated.setCheckable(True)
        self.actionFilterUntranslated.setChecked(True)
        self.actionFilterUntranslated.setEnabled(False)
        self.actionFilterUntranslated.setObjectName("actionFilterUntranslated")
        self.menuFile.addAction(self.actionOpenInNewWindow)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.menuOpen_Recent.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveas)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuSettings.addAction(self.actionPreferences)
        self.menuView.addAction(self.actionFilterFuzzy)
        self.menuView.addAction(self.actionFilterTranslated)
        self.menuView.addAction(self.actionFilterUntranslated)
        self.menuGo.addAction(self.actionFirst)
        self.menuGo.addAction(self.actionPrevious)
        self.menuGo.addAction(self.actionNext)
        self.menuGo.addAction(self.actionLast)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionSelectAll)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionFind)
        self.menuEdit.addAction(self.actionFindPrevious)
        self.menuEdit.addAction(self.actionFindNext)
        self.menuEdit.addAction(self.actionReplace)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCopySource2Target)
        self.menuEdit.addAction(self.actionToggleFuzzy)
        self.menuEdit.addAction(self.actionEdit_Header)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionAboutQT)
        self.menuWindow.addSeparator()
        self.menuWindow.addSeparator()
        self.menuWindow.addAction(self.menuToolbars.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuGo.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolStandard.addAction(self.actionOpen)
        self.toolStandard.addAction(self.actionSave)
        self.toolStandard.addSeparator()
        self.toolStandard.addAction(self.actionCut)
        self.toolStandard.addAction(self.actionCopy)
        self.toolStandard.addAction(self.actionPaste)
        self.toolStandard.addSeparator()
        self.toolStandard.addAction(self.actionUndo)
        self.toolStandard.addAction(self.actionRedo)
        self.toolNavigation.addAction(self.actionFirst)
        self.toolNavigation.addAction(self.actionPrevious)
        self.toolNavigation.addAction(self.actionNext)
        self.toolNavigation.addAction(self.actionLast)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuOpen_Recent.setTitle(QtGui.QApplication.translate("MainWindow", "Open &Recent", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSettings.setTitle(QtGui.QApplication.translate("MainWindow", "&Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.menuView.setTitle(QtGui.QApplication.translate("MainWindow", "&View", None, QtGui.QApplication.UnicodeUTF8))
        self.menuGo.setTitle(QtGui.QApplication.translate("MainWindow", "&Go", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdit.setTitle(QtGui.QApplication.translate("MainWindow", "&Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuWindow.setTitle(QtGui.QApplication.translate("MainWindow", "&Window", None, QtGui.QApplication.UnicodeUTF8))
        self.menuToolbars.setTitle(QtGui.QApplication.translate("MainWindow", "Toolbars", None, QtGui.QApplication.UnicodeUTF8))
        self.toolStandard.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Standard Toolbar", None, QtGui.QApplication.UnicodeUTF8))
        self.toolNavigation.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Navigation Toolbar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setText(QtGui.QApplication.translate("MainWindow", "&New", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "&Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "&Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveas.setText(QtGui.QApplication.translate("MainWindow", "Save &As", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "&Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUndo.setText(QtGui.QApplication.translate("MainWindow", "Undo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUndo.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Z", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRedo.setText(QtGui.QApplication.translate("MainWindow", "Redo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRedo.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+Z", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCut.setText(QtGui.QApplication.translate("MainWindow", "Cut", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCut.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+X", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopy.setText(QtGui.QApplication.translate("MainWindow", "Copy", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopy.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+C", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPaste.setText(QtGui.QApplication.translate("MainWindow", "Paste", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPaste.setIconText(QtGui.QApplication.translate("MainWindow", "Paste", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPaste.setToolTip(QtGui.QApplication.translate("MainWindow", "Paste", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPaste.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+V", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFind.setText(QtGui.QApplication.translate("MainWindow", "Find", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFind.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+F", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShowMenuBar.setText(QtGui.QApplication.translate("MainWindow", "Show MenuBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShowMenuBar.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+M", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShowTUview.setText(QtGui.QApplication.translate("MainWindow", "Show TUview", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShowTUview.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+T", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAboutQT.setText(QtGui.QApplication.translate("MainWindow", "About QT", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShow_MenuBar.setText(QtGui.QApplication.translate("MainWindow", "Show MenuBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShow_TUview.setText(QtGui.QApplication.translate("MainWindow", "Show TUview", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFirst.setText(QtGui.QApplication.translate("MainWindow", "&First", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFirst.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+PgUp", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPrevious.setText(QtGui.QApplication.translate("MainWindow", "&Previous", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPrevious.setShortcut(QtGui.QApplication.translate("MainWindow", "PgUp", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNext.setText(QtGui.QApplication.translate("MainWindow", "&Next", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNext.setShortcut(QtGui.QApplication.translate("MainWindow", "PgDown", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLast.setText(QtGui.QApplication.translate("MainWindow", "&Last", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLast.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+PgDown", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShowDetail.setText(QtGui.QApplication.translate("MainWindow", "Show Detail", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShowComment.setText(QtGui.QApplication.translate("MainWindow", "Show Comment", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShowOverview.setText(QtGui.QApplication.translate("MainWindow", "Show Overview", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopySource2Target.setText(QtGui.QApplication.translate("MainWindow", "Copy Source to Target", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopySource2Target.setShortcut(QtGui.QApplication.translate("MainWindow", "F2", None, QtGui.QApplication.UnicodeUTF8))
        self.actionToggleFuzzy.setText(QtGui.QApplication.translate("MainWindow", "Toggle fuzzy", None, QtGui.QApplication.UnicodeUTF8))
        self.actionToggleFuzzy.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+U", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFile.setText(QtGui.QApplication.translate("MainWindow", "file", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFind_Previous.setText(QtGui.QApplication.translate("MainWindow", "Find Previous", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFind_Next.setText(QtGui.QApplication.translate("MainWindow", "Find Next", None, QtGui.QApplication.UnicodeUTF8))
        self.actionReplace.setText(QtGui.QApplication.translate("MainWindow", "&Replace", None, QtGui.QApplication.UnicodeUTF8))
        self.actionReplace.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+R", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFindNext.setText(QtGui.QApplication.translate("MainWindow", "Find Next", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFindNext.setIconText(QtGui.QApplication.translate("MainWindow", "Find Next", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFindNext.setToolTip(QtGui.QApplication.translate("MainWindow", "Find Next", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFindNext.setShortcut(QtGui.QApplication.translate("MainWindow", "F3", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpenInNewWindow.setText(QtGui.QApplication.translate("MainWindow", "Open in New Window", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFindPrevious.setText(QtGui.QApplication.translate("MainWindow", "Find Previous", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFindPrevious.setShortcut(QtGui.QApplication.translate("MainWindow", "Shift+F3", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSelectAll.setText(QtGui.QApplication.translate("MainWindow", "Select &All", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSelectAll.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+A", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEdit_Header.setText(QtGui.QApplication.translate("MainWindow", "Header...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreferences.setText(QtGui.QApplication.translate("MainWindow", "Preferences...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionComment.setText(QtGui.QApplication.translate("MainWindow", "Comment", None, QtGui.QApplication.UnicodeUTF8))
        self.actionToolbars.setText(QtGui.QApplication.translate("MainWindow", "Toolbars", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFilterFuzzy.setText(QtGui.QApplication.translate("MainWindow", "Fuzzy", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFilterTranslated.setText(QtGui.QApplication.translate("MainWindow", "Translated", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFilterUntranslated.setText(QtGui.QApplication.translate("MainWindow", "Untranslated", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
