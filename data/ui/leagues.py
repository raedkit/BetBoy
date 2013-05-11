# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'leagues.ui'
#
# Created: Sat May 11 22:28:09 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Leagues(object):
    def setupUi(self, Leagues):
        Leagues.setObjectName("Leagues")
        Leagues.resize(585, 579)
        self.horizontalLayout_11 = QtGui.QHBoxLayout(Leagues)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.tabWidget = QtGui.QTabWidget(Leagues)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.tab)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tree_teams = QtGui.QTreeWidget(self.tab)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.tree_teams.setPalette(palette)
        self.tree_teams.setObjectName("tree_teams")
        self.tree_teams.headerItem().setText(0, "1")
        self.verticalLayout_5.addWidget(self.tree_teams)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.button_teams_remove = QtGui.QPushButton(self.tab)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/actions/actions/edit_remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_teams_remove.setIcon(icon)
        self.button_teams_remove.setObjectName("button_teams_remove")
        self.horizontalLayout_3.addWidget(self.button_teams_remove)
        self.button_teams_clear = QtGui.QPushButton(self.tab)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/actions/actions/editclear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_teams_clear.setIcon(icon1)
        self.button_teams_clear.setObjectName("button_teams_clear")
        self.horizontalLayout_3.addWidget(self.button_teams_clear)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.button_teams_add = QtGui.QPushButton(self.tab)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/actions/actions/edit_add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_teams_add.setIcon(icon2)
        self.button_teams_add.setObjectName("button_teams_add")
        self.horizontalLayout_4.addWidget(self.button_teams_add)
        self.line_team = QtGui.QLineEdit(self.tab)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.line_team.setPalette(palette)
        self.line_team.setObjectName("line_team")
        self.horizontalLayout_4.addWidget(self.line_team)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.button_profile_save = QtGui.QPushButton(self.tab)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/actions/actions/filesaveas.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_profile_save.setIcon(icon3)
        self.button_profile_save.setObjectName("button_profile_save")
        self.horizontalLayout_2.addWidget(self.button_profile_save)
        self.line_teams_save = QtGui.QLineEdit(self.tab)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.line_teams_save.setPalette(palette)
        self.line_teams_save.setObjectName("line_teams_save")
        self.horizontalLayout_2.addWidget(self.line_teams_save)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        self.horizontalLayout_5.addLayout(self.verticalLayout_5)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tree_leagues = QtGui.QTreeWidget(self.tab)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.tree_leagues.setPalette(palette)
        self.tree_leagues.setObjectName("tree_leagues")
        self.tree_leagues.headerItem().setText(0, "1")
        self.verticalLayout_3.addWidget(self.tree_leagues)
        self.button_from_league = QtGui.QPushButton(self.tab)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/actions/actions/fileopen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_from_league.setIcon(icon4)
        self.button_from_league.setObjectName("button_from_league")
        self.verticalLayout_3.addWidget(self.button_from_league)
        self.verticalLayout_7.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tree_team_profiles = QtGui.QTreeWidget(self.tab)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.tree_team_profiles.setPalette(palette)
        self.tree_team_profiles.setObjectName("tree_team_profiles")
        self.tree_team_profiles.headerItem().setText(0, "1")
        self.verticalLayout_4.addWidget(self.tree_team_profiles)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_profile_load = QtGui.QPushButton(self.tab)
        self.button_profile_load.setIcon(icon4)
        self.button_profile_load.setObjectName("button_profile_load")
        self.horizontalLayout.addWidget(self.button_profile_load)
        self.button_profile_delete = QtGui.QPushButton(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_profile_delete.sizePolicy().hasHeightForWidth())
        self.button_profile_delete.setSizePolicy(sizePolicy)
        self.button_profile_delete.setObjectName("button_profile_delete")
        self.horizontalLayout.addWidget(self.button_profile_delete)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout_7.addLayout(self.verticalLayout_4)
        self.horizontalLayout_5.addLayout(self.verticalLayout_7)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.tree_matches = QtGui.QTreeWidget(self.tab_2)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.tree_matches.setPalette(palette)
        self.tree_matches.setFrameShape(QtGui.QFrame.Box)
        self.tree_matches.setFrameShadow(QtGui.QFrame.Plain)
        self.tree_matches.setEditTriggers(QtGui.QAbstractItemView.DoubleClicked)
        self.tree_matches.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tree_matches.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tree_matches.setRootIsDecorated(False)
        self.tree_matches.setItemsExpandable(False)
        self.tree_matches.setObjectName("tree_matches")
        self.tree_matches.headerItem().setText(0, "1")
        self.verticalLayout_10.addWidget(self.tree_matches)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.button_league_save = QtGui.QPushButton(self.tab_2)
        self.button_league_save.setIcon(icon3)
        self.button_league_save.setObjectName("button_league_save")
        self.horizontalLayout_7.addWidget(self.button_league_save)
        self.line_league_save = QtGui.QLineEdit(self.tab_2)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.line_league_save.setPalette(palette)
        self.line_league_save.setObjectName("line_league_save")
        self.horizontalLayout_7.addWidget(self.line_league_save)
        self.verticalLayout_10.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.button_up = QtGui.QPushButton(self.tab_2)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/actions/actions/1uparrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_up.setIcon(icon5)
        self.button_up.setObjectName("button_up")
        self.horizontalLayout_6.addWidget(self.button_up)
        self.button_down = QtGui.QPushButton(self.tab_2)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/actions/actions/1downarrow1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_down.setIcon(icon6)
        self.button_down.setObjectName("button_down")
        self.horizontalLayout_6.addWidget(self.button_down)
        self.verticalLayout_10.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.button_match_remove = QtGui.QPushButton(self.tab_2)
        self.button_match_remove.setIcon(icon)
        self.button_match_remove.setObjectName("button_match_remove")
        self.horizontalLayout_9.addWidget(self.button_match_remove)
        self.button_match_add = QtGui.QPushButton(self.tab_2)
        self.button_match_add.setIcon(icon2)
        self.button_match_add.setObjectName("button_match_add")
        self.horizontalLayout_9.addWidget(self.button_match_add)
        self.line_match = QtGui.QLineEdit(self.tab_2)
        self.line_match.setEnabled(True)
        self.line_match.setObjectName("line_match")
        self.horizontalLayout_9.addWidget(self.line_match)
        self.verticalLayout_10.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_12.addLayout(self.verticalLayout_10)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.tree_leagues_own = QtGui.QTreeWidget(self.tab_2)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.tree_leagues_own.setPalette(palette)
        self.tree_leagues_own.setObjectName("tree_leagues_own")
        self.tree_leagues_own.headerItem().setText(0, "1")
        self.verticalLayout_6.addWidget(self.tree_leagues_own)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.button_league_load = QtGui.QPushButton(self.tab_2)
        self.button_league_load.setIcon(icon4)
        self.button_league_load.setObjectName("button_league_load")
        self.horizontalLayout_8.addWidget(self.button_league_load)
        self.button_league_delete = QtGui.QPushButton(self.tab_2)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/actions/actions/editdelete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_league_delete.setIcon(icon7)
        self.button_league_delete.setObjectName("button_league_delete")
        self.horizontalLayout_8.addWidget(self.button_league_delete)
        self.verticalLayout_6.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_12.addLayout(self.verticalLayout_6)
        self.verticalLayout_11.addLayout(self.horizontalLayout_12)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.tree_teams_home = QtGui.QTreeWidget(self.tab_2)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.tree_teams_home.setPalette(palette)
        self.tree_teams_home.setHeaderHidden(False)
        self.tree_teams_home.setObjectName("tree_teams_home")
        self.tree_teams_home.headerItem().setText(0, "1")
        self.verticalLayout_8.addWidget(self.tree_teams_home)
        self.spin_home = QtGui.QSpinBox(self.tab_2)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.spin_home.setPalette(palette)
        self.spin_home.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
        self.spin_home.setMinimum(-1)
        self.spin_home.setProperty("value", -1)
        self.spin_home.setObjectName("spin_home")
        self.verticalLayout_8.addWidget(self.spin_home)
        self.horizontalLayout_10.addLayout(self.verticalLayout_8)
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.tree_teams_away = QtGui.QTreeWidget(self.tab_2)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.tree_teams_away.setPalette(palette)
        self.tree_teams_away.setObjectName("tree_teams_away")
        self.tree_teams_away.headerItem().setText(0, "1")
        self.verticalLayout_9.addWidget(self.tree_teams_away)
        self.spin_away = QtGui.QSpinBox(self.tab_2)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.spin_away.setPalette(palette)
        self.spin_away.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
        self.spin_away.setMinimum(-1)
        self.spin_away.setProperty("value", -1)
        self.spin_away.setObjectName("spin_away")
        self.verticalLayout_9.addWidget(self.spin_away)
        self.horizontalLayout_10.addLayout(self.verticalLayout_9)
        self.calendarWidget = QtGui.QCalendarWidget(self.tab_2)
        self.calendarWidget.setMinimumSize(QtCore.QSize(300, 0))
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setHorizontalHeaderFormat(QtGui.QCalendarWidget.SingleLetterDayNames)
        self.calendarWidget.setVerticalHeaderFormat(QtGui.QCalendarWidget.NoVerticalHeader)
        self.calendarWidget.setNavigationBarVisible(True)
        self.calendarWidget.setDateEditEnabled(False)
        self.calendarWidget.setObjectName("calendarWidget")
        self.horizontalLayout_10.addWidget(self.calendarWidget)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.verticalLayout_11.addLayout(self.verticalLayout)
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout_11.addWidget(self.tabWidget)

        self.retranslateUi(Leagues)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Leagues)

    def retranslateUi(self, Leagues):
        Leagues.setWindowTitle(QtGui.QApplication.translate("Leagues", "Leagues creator", None, QtGui.QApplication.UnicodeUTF8))
        self.button_teams_remove.setText(QtGui.QApplication.translate("Leagues", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.button_teams_clear.setText(QtGui.QApplication.translate("Leagues", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.button_teams_add.setText(QtGui.QApplication.translate("Leagues", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.button_profile_save.setText(QtGui.QApplication.translate("Leagues", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.button_from_league.setText(QtGui.QApplication.translate("Leagues", "Load", None, QtGui.QApplication.UnicodeUTF8))
        self.button_profile_load.setText(QtGui.QApplication.translate("Leagues", "Load", None, QtGui.QApplication.UnicodeUTF8))
        self.button_profile_delete.setText(QtGui.QApplication.translate("Leagues", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("Leagues", "Teams", None, QtGui.QApplication.UnicodeUTF8))
        self.tree_matches.setSortingEnabled(False)
        self.button_league_save.setText(QtGui.QApplication.translate("Leagues", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.button_up.setText(QtGui.QApplication.translate("Leagues", "move up", None, QtGui.QApplication.UnicodeUTF8))
        self.button_down.setText(QtGui.QApplication.translate("Leagues", "move down", None, QtGui.QApplication.UnicodeUTF8))
        self.button_match_remove.setText(QtGui.QApplication.translate("Leagues", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.button_match_add.setText(QtGui.QApplication.translate("Leagues", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.button_league_load.setText(QtGui.QApplication.translate("Leagues", "Load", None, QtGui.QApplication.UnicodeUTF8))
        self.button_league_delete.setText(QtGui.QApplication.translate("Leagues", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.spin_home.setSpecialValueText(QtGui.QApplication.translate("Leagues", "NULL", None, QtGui.QApplication.UnicodeUTF8))
        self.spin_away.setSpecialValueText(QtGui.QApplication.translate("Leagues", "NULL", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("Leagues", "Leagues", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
