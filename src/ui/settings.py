# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/settings.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(350, 450)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(350, 430))
        MainWindow.setMaximumSize(QtCore.QSize(350, 450))
        MainWindow.setBaseSize(QtCore.QSize(260, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/opt/yin-yang/src/ui/assets/yin-yang.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 40, 301, 391))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.kdesection = QtWidgets.QVBoxLayout()
        self.kdesection.setSpacing(6)
        self.kdesection.setObjectName("kdesection")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.kdesection.addWidget(self.label_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.kde_checkbox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.kde_checkbox.setText("")
        self.kde_checkbox.setObjectName("kde_checkbox")
        self.horizontalLayout_2.addWidget(self.kde_checkbox)
        self.kde_combo_light = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.kde_combo_light.setObjectName("kde_combo_light")
        self.horizontalLayout_2.addWidget(self.kde_combo_light)
        self.kde_combo_dark = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.kde_combo_dark.setObjectName("kde_combo_dark")
        self.horizontalLayout_2.addWidget(self.kde_combo_dark)
        self.kdesection.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.kdesection)
        self.gtk = QtWidgets.QVBoxLayout()
        self.gtk.setSpacing(6)
        self.gtk.setObjectName("gtk")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gtk.addWidget(self.label_7)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.gtk_checkbox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.gtk_checkbox.setText("")
        self.gtk_checkbox.setObjectName("gtk_checkbox")
        self.horizontalLayout_7.addWidget(self.gtk_checkbox)
        self.gtk_line_light = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.gtk_line_light.setObjectName("gtk_line_light")
        self.horizontalLayout_7.addWidget(self.gtk_line_light)
        self.gtk_line_dark = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.gtk_line_dark.setObjectName("gtk_line_dark")
        self.horizontalLayout_7.addWidget(self.gtk_line_dark)
        self.gtk.addLayout(self.horizontalLayout_7)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gtk.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.gtk)
        self.vscode = QtWidgets.QVBoxLayout()
        self.vscode.setSpacing(6)
        self.vscode.setObjectName("vscode")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.vscode.addWidget(self.label_6)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.code_checkbox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.code_checkbox.setText("")
        self.code_checkbox.setObjectName("code_checkbox")
        self.horizontalLayout_6.addWidget(self.code_checkbox)
        self.code_line_light = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.code_line_light.setObjectName("code_line_light")
        self.horizontalLayout_6.addWidget(self.code_line_light)
        self.code_line_dark = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.code_line_dark.setObjectName("code_line_dark")
        self.horizontalLayout_6.addWidget(self.code_line_dark)
        self.vscode.addLayout(self.horizontalLayout_6)
        self.verticalLayout.addLayout(self.vscode)
        self.atom = QtWidgets.QVBoxLayout()
        self.atom.setSpacing(6)
        self.atom.setObjectName("atom")
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.atom.addWidget(self.label_9)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(6)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.atom_checkbox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.atom_checkbox.setText("")
        self.atom_checkbox.setObjectName("atom_checkbox")
        self.horizontalLayout_9.addWidget(self.atom_checkbox)
        self.atom_line_light = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.atom_line_light.setObjectName("atom_line_light")
        self.horizontalLayout_9.addWidget(self.atom_line_light)
        self.atom_line_dark = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.atom_line_dark.setObjectName("atom_line_dark")
        self.horizontalLayout_9.addWidget(self.atom_line_dark)
        self.atom.addLayout(self.horizontalLayout_9)
        self.verticalLayout.addLayout(self.atom)
        self.Wallpaper = QtWidgets.QVBoxLayout()
        self.Wallpaper.setSpacing(6)
        self.Wallpaper.setObjectName("Wallpaper")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.Wallpaper.addWidget(self.label_8)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.wallpaper_checkbox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.wallpaper_checkbox.setText("")
        self.wallpaper_checkbox.setObjectName("wallpaper_checkbox")
        self.horizontalLayout_8.addWidget(self.wallpaper_checkbox)
        self.wallpaper_button_light = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.wallpaper_button_light.setObjectName("wallpaper_button_light")
        self.horizontalLayout_8.addWidget(self.wallpaper_button_light)
        self.wallpaper_button_dark = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.wallpaper_button_dark.setObjectName("wallpaper_button_dark")
        self.horizontalLayout_8.addWidget(self.wallpaper_button_dark)
        self.Wallpaper.addLayout(self.horizontalLayout_8)
        self.version_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.version_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.version_label.setObjectName("version_label")
        self.Wallpaper.addWidget(self.version_label)
        self.verticalLayout.addLayout(self.Wallpaper)
        self.back_button = QtWidgets.QPushButton(self.centralWidget)
        self.back_button.setGeometry(QtCore.QRect(230, 10, 94, 25))
        self.back_button.setObjectName("back_button")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Yin & Yang"))
        self.label.setText(_translate("MainWindow", "Settings"))
        self.label_2.setText(_translate("MainWindow", "KDE"))
        self.label_7.setText(_translate("MainWindow", "GTK"))
        self.gtk_line_light.setText(_translate("MainWindow", "Breeze"))
        self.gtk_line_dark.setText(_translate("MainWindow", "sdjhdjh"))
        self.label_6.setText(_translate("MainWindow", "VSCode"))
        self.label_9.setText(_translate("MainWindow", "Atom"))
        self.label_8.setText(_translate("MainWindow", "Wallpaper"))
        self.wallpaper_button_light.setText(_translate("MainWindow", "light"))
        self.wallpaper_button_dark.setText(_translate("MainWindow", "dark"))
        self.version_label.setText(_translate("MainWindow", "version: 0.1"))
        self.back_button.setText(_translate("MainWindow", "Back"))


