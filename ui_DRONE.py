# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DRONE.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import ICONS_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(896, 809)
        MainWindow.setStyleSheet(u"*{\n"
"border:none;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.header_frame = QFrame(self.centralwidget)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setStyleSheet(u"background-color: rgb(163, 82, 0);")
        self.header_frame.setFrameShape(QFrame.NoFrame)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.header_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(3, 0, 0, 0)
        self.header_left = QFrame(self.header_frame)
        self.header_left.setObjectName(u"header_left")
        self.header_left.setFrameShape(QFrame.StyledPanel)
        self.header_left.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.header_left)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.header_left)
        self.pushButton.setObjectName(u"pushButton")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/icon/align-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.pushButton)


        self.horizontalLayout.addWidget(self.header_left, 0, Qt.AlignLeft)

        self.central_frame = QFrame(self.header_frame)
        self.central_frame.setObjectName(u"central_frame")
        self.central_frame.setFrameShape(QFrame.StyledPanel)
        self.central_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.central_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.central_frame)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/icons/icon/cpu.svg"))

        self.horizontalLayout_3.addWidget(self.label, 0, Qt.AlignRight)

        self.label_2 = QLabel(self.central_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_2)


        self.horizontalLayout.addWidget(self.central_frame)

        self.header_right = QFrame(self.header_frame)
        self.header_right.setObjectName(u"header_right")
        self.header_right.setFrameShape(QFrame.StyledPanel)
        self.header_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header_right)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 3, 0)
        self.minimize = QPushButton(self.header_right)
        self.minimize.setObjectName(u"minimize")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icon/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize.setIcon(icon1)
        self.minimize.setIconSize(QSize(16, 16))

        self.horizontalLayout_2.addWidget(self.minimize)

        self.restore = QPushButton(self.header_right)
        self.restore.setObjectName(u"restore")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icon/copy.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restore.setIcon(icon2)
        self.restore.setIconSize(QSize(16, 16))

        self.horizontalLayout_2.addWidget(self.restore)

        self.close = QPushButton(self.header_right)
        self.close.setObjectName(u"close")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icon/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close.setIcon(icon3)
        self.close.setIconSize(QSize(16, 16))

        self.horizontalLayout_2.addWidget(self.close)


        self.horizontalLayout.addWidget(self.header_right, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.header_frame, 0, Qt.AlignTop)

        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy)
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_8 = QHBoxLayout(self.main_frame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.left_menu_frame_content = QFrame(self.main_frame)
        self.left_menu_frame_content.setObjectName(u"left_menu_frame_content")
        self.left_menu_frame_content.setMinimumSize(QSize(20, 0))
        self.left_menu_frame_content.setMaximumSize(QSize(60, 16777215))
        self.left_menu_frame_content.setStyleSheet(u"background-color: rgb(163, 82, 0);")
        self.left_menu_frame_content.setFrameShape(QFrame.StyledPanel)
        self.left_menu_frame_content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.left_menu_frame_content)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.menu_frame = QFrame(self.left_menu_frame_content)
        self.menu_frame.setObjectName(u"menu_frame")
        self.menu_frame.setMinimumSize(QSize(200, 0))
        self.menu_frame.setFrameShape(QFrame.StyledPanel)
        self.menu_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.menu_frame)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(4, 0, 0, 0)
        self.pushButton_5 = QPushButton(self.menu_frame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icon/code-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setIconSize(QSize(40, 40))

        self.gridLayout.addWidget(self.pushButton_5, 2, 0, 1, 1, Qt.AlignLeft)

        self.pushButton_3 = QPushButton(self.menu_frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icon/keyboard1-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon5)
        self.pushButton_3.setIconSize(QSize(40, 40))

        self.gridLayout.addWidget(self.pushButton_3, 0, 0, 1, 1, Qt.AlignLeft)

        self.pushButton_6 = QPushButton(self.menu_frame)
        self.pushButton_6.setObjectName(u"pushButton_6")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icon/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon6)
        self.pushButton_6.setIconSize(QSize(40, 40))

        self.gridLayout.addWidget(self.pushButton_6, 3, 0, 1, 1, Qt.AlignLeft)

        self.pushButton_4 = QPushButton(self.menu_frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icon/game-controller-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon7)
        self.pushButton_4.setIconSize(QSize(40, 40))

        self.gridLayout.addWidget(self.pushButton_4, 1, 0, 1, 1, Qt.AlignLeft)

        self.label_6 = QLabel(self.menu_frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMargin(5)

        self.gridLayout.addWidget(self.label_6, 2, 1, 1, 1, Qt.AlignLeft)

        self.label_7 = QLabel(self.menu_frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMargin(5)

        self.gridLayout.addWidget(self.label_7, 3, 1, 1, 1, Qt.AlignLeft)

        self.label_5 = QLabel(self.menu_frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMargin(5)

        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 1, Qt.AlignLeft)

        self.label_4 = QLabel(self.menu_frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMargin(5)

        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1, Qt.AlignLeft)


        self.horizontalLayout_9.addWidget(self.menu_frame, 0, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout_8.addWidget(self.left_menu_frame_content)

        self.main_menu_frame_contents = QFrame(self.main_frame)
        self.main_menu_frame_contents.setObjectName(u"main_menu_frame_contents")
        self.main_menu_frame_contents.setFrameShape(QFrame.StyledPanel)
        self.main_menu_frame_contents.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.main_menu_frame_contents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.stackedWidget = QStackedWidget(self.main_menu_frame_contents)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_3 = QVBoxLayout(self.page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.joystick_frame = QFrame(self.page)
        self.joystick_frame.setObjectName(u"joystick_frame")
        self.joystick_frame.setFrameShape(QFrame.StyledPanel)
        self.joystick_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.joystick_frame)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.left_joystick_frame = QFrame(self.joystick_frame)
        self.left_joystick_frame.setObjectName(u"left_joystick_frame")
        self.left_joystick_frame.setFrameShape(QFrame.StyledPanel)
        self.left_joystick_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.left_joystick_frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton_7 = QPushButton(self.left_joystick_frame)
        self.pushButton_7.setObjectName(u"pushButton_7")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icon/triangle-up-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon8)
        self.pushButton_7.setIconSize(QSize(40, 40))

        self.gridLayout_2.addWidget(self.pushButton_7, 0, 0, 1, 2)

        self.pushButton_10 = QPushButton(self.left_joystick_frame)
        self.pushButton_10.setObjectName(u"pushButton_10")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icon/triangle-left-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_10.setIcon(icon9)
        self.pushButton_10.setIconSize(QSize(40, 40))

        self.gridLayout_2.addWidget(self.pushButton_10, 1, 0, 1, 1)

        self.pushButton_9 = QPushButton(self.left_joystick_frame)
        self.pushButton_9.setObjectName(u"pushButton_9")
        icon10 = QIcon()
        icon10.addFile(u":/icons/icon/triangle-right-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon10)
        self.pushButton_9.setIconSize(QSize(40, 40))

        self.gridLayout_2.addWidget(self.pushButton_9, 1, 1, 1, 1)

        self.pushButton_8 = QPushButton(self.left_joystick_frame)
        self.pushButton_8.setObjectName(u"pushButton_8")
        icon11 = QIcon()
        icon11.addFile(u":/icons/icon/triangle-down-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon11)
        self.pushButton_8.setIconSize(QSize(40, 40))

        self.gridLayout_2.addWidget(self.pushButton_8, 2, 0, 1, 2)


        self.horizontalLayout_10.addWidget(self.left_joystick_frame)

        self.right_joystick_frame = QFrame(self.joystick_frame)
        self.right_joystick_frame.setObjectName(u"right_joystick_frame")
        self.right_joystick_frame.setFrameShape(QFrame.StyledPanel)
        self.right_joystick_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.right_joystick_frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pushButton_13 = QPushButton(self.right_joystick_frame)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setIcon(icon8)
        self.pushButton_13.setIconSize(QSize(40, 40))

        self.gridLayout_3.addWidget(self.pushButton_13, 0, 0, 1, 2)

        self.pushButton_11 = QPushButton(self.right_joystick_frame)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setIcon(icon9)
        self.pushButton_11.setIconSize(QSize(40, 40))

        self.gridLayout_3.addWidget(self.pushButton_11, 1, 0, 1, 1)

        self.pushButton_12 = QPushButton(self.right_joystick_frame)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setIcon(icon10)
        self.pushButton_12.setIconSize(QSize(40, 40))

        self.gridLayout_3.addWidget(self.pushButton_12, 1, 1, 1, 1)

        self.pushButton_14 = QPushButton(self.right_joystick_frame)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setIcon(icon11)
        self.pushButton_14.setIconSize(QSize(40, 40))

        self.gridLayout_3.addWidget(self.pushButton_14, 2, 0, 1, 2)


        self.horizontalLayout_10.addWidget(self.right_joystick_frame)

        self.armed = QFrame(self.joystick_frame)
        self.armed.setObjectName(u"armed")
        self.armed.setFrameShape(QFrame.StyledPanel)
        self.armed.setFrameShadow(QFrame.Raised)
        self.pushButton_15 = QPushButton(self.armed)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setGeometry(QRect(60, 20, 93, 28))
        self.pushButton_15.setFont(font)
        self.pushButton_16 = QPushButton(self.armed)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setGeometry(QRect(140, 20, 93, 28))
        self.pushButton_16.setFont(font)

        self.horizontalLayout_10.addWidget(self.armed)


        self.verticalLayout_3.addWidget(self.joystick_frame)

        self.frame = QFrame(self.page)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_13 = QLabel(self.frame)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_4.addWidget(self.label_13, 5, 3, 1, 1)

        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_4.addWidget(self.label_11, 5, 0, 1, 1)

        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_4.addWidget(self.label_9, 0, 1, 1, 2)

        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_4.addWidget(self.label_10, 5, 1, 1, 1)

        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_4.addWidget(self.label_8, 0, 0, 1, 1)

        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_4.addWidget(self.label_12, 0, 3, 1, 1)

        self.label_14 = QLabel(self.frame)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_4.addWidget(self.label_14, 0, 4, 1, 1)

        self.label_15 = QLabel(self.frame)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_4.addWidget(self.label_15, 5, 4, 1, 1)

        self.label_16 = QLabel(self.frame)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_4.addWidget(self.label_16, 6, 2, 1, 1)


        self.verticalLayout_3.addWidget(self.frame)

        self.shortcut = QFrame(self.page)
        self.shortcut.setObjectName(u"shortcut")
        self.shortcut.setFrameShape(QFrame.StyledPanel)
        self.shortcut.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.shortcut)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_36 = QLabel(self.shortcut)
        self.label_36.setObjectName(u"label_36")

        self.gridLayout_7.addWidget(self.label_36, 6, 1, 1, 1)

        self.label_34 = QLabel(self.shortcut)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout_7.addWidget(self.label_34, 0, 4, 1, 1)

        self.label_39 = QLabel(self.shortcut)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout_7.addWidget(self.label_39, 6, 4, 1, 1)

        self.label_41 = QLabel(self.shortcut)
        self.label_41.setObjectName(u"label_41")

        self.gridLayout_7.addWidget(self.label_41, 4, 5, 1, 1)

        self.label_17 = QLabel(self.shortcut)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_7.addWidget(self.label_17, 0, 0, 1, 1)

        self.label_18 = QLabel(self.shortcut)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_7.addWidget(self.label_18, 4, 0, 1, 1)

        self.label_20 = QLabel(self.shortcut)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_7.addWidget(self.label_20, 0, 1, 1, 1)

        self.label_24 = QLabel(self.shortcut)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_7.addWidget(self.label_24, 4, 4, 1, 1)

        self.label_22 = QLabel(self.shortcut)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_7.addWidget(self.label_22, 0, 3, 1, 1)

        self.label_37 = QLabel(self.shortcut)
        self.label_37.setObjectName(u"label_37")

        self.gridLayout_7.addWidget(self.label_37, 6, 3, 1, 1)

        self.label_38 = QLabel(self.shortcut)
        self.label_38.setObjectName(u"label_38")

        self.gridLayout_7.addWidget(self.label_38, 0, 5, 1, 1)

        self.label_21 = QLabel(self.shortcut)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_7.addWidget(self.label_21, 4, 3, 1, 1)

        self.label_19 = QLabel(self.shortcut)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_7.addWidget(self.label_19, 6, 0, 1, 1)

        self.label_23 = QLabel(self.shortcut)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_7.addWidget(self.label_23, 4, 1, 1, 1)

        self.label_35 = QLabel(self.shortcut)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_7.addWidget(self.label_35, 0, 6, 1, 1)

        self.label_40 = QLabel(self.shortcut)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_7.addWidget(self.label_40, 4, 6, 1, 1)


        self.verticalLayout_3.addWidget(self.shortcut)

        self.stackedWidget.addWidget(self.page)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.horizontalLayout_11 = QHBoxLayout(self.page_3)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.frame_3 = QFrame(self.page_3)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_29 = QLabel(self.frame_5)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_5.addWidget(self.label_29, 2, 0, 1, 1)

        self.label_26 = QLabel(self.frame_5)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_5.addWidget(self.label_26, 0, 1, 1, 1)

        self.label_25 = QLabel(self.frame_5)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_5.addWidget(self.label_25, 0, 0, 1, 1)

        self.label_28 = QLabel(self.frame_5)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_5.addWidget(self.label_28, 1, 1, 1, 1)

        self.label_27 = QLabel(self.frame_5)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_5.addWidget(self.label_27, 1, 0, 1, 1)

        self.label_30 = QLabel(self.frame_5)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_5.addWidget(self.label_30, 2, 1, 1, 1)

        self.label_31 = QLabel(self.frame_5)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_5.addWidget(self.label_31, 3, 0, 1, 1)

        self.label_32 = QLabel(self.frame_5)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_5.addWidget(self.label_32, 3, 1, 1, 1)

        self.pushButton_17 = QPushButton(self.frame_5)
        self.pushButton_17.setObjectName(u"pushButton_17")

        self.gridLayout_5.addWidget(self.pushButton_17, 5, 1, 1, 1)


        self.verticalLayout_4.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.label_33 = QLabel(self.frame_6)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(130, 170, 55, 16))

        self.verticalLayout_4.addWidget(self.frame_6)


        self.horizontalLayout_11.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.page_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.pushButton_19 = QPushButton(self.frame_4)
        self.pushButton_19.setObjectName(u"pushButton_19")
        icon12 = QIcon()
        icon12.addFile(u":/icons/icon/monitor.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_19.setIcon(icon12)
        self.pushButton_19.setIconSize(QSize(35, 35))

        self.gridLayout_6.addWidget(self.pushButton_19, 1, 0, 1, 1)

        self.pushButton_18 = QPushButton(self.frame_4)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setIcon(icon4)
        self.pushButton_18.setIconSize(QSize(35, 35))

        self.gridLayout_6.addWidget(self.pushButton_18, 0, 0, 1, 1)


        self.horizontalLayout_11.addWidget(self.frame_4)

        self.stackedWidget.addWidget(self.page_3)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout_8.addWidget(self.main_menu_frame_contents)


        self.verticalLayout.addWidget(self.main_frame)

        self.footer_frame = QFrame(self.centralwidget)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setFrameShape(QFrame.NoFrame)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.footer_left = QFrame(self.footer_frame)
        self.footer_left.setObjectName(u"footer_left")
        self.footer_left.setFrameShape(QFrame.StyledPanel)
        self.footer_left.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.footer_left)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(self.footer_left)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_6.addWidget(self.label_3, 0, Qt.AlignLeft)


        self.horizontalLayout_5.addWidget(self.footer_left)

        self.frame_2 = QFrame(self.footer_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_7.addWidget(self.pushButton_2, 0, Qt.AlignRight)


        self.horizontalLayout_5.addWidget(self.frame_2, 0, Qt.AlignRight)

        self.size_grid = QFrame(self.footer_frame)
        self.size_grid.setObjectName(u"size_grid")
        self.size_grid.setMinimumSize(QSize(10, 10))
        self.size_grid.setMaximumSize(QSize(10, 10))
        self.size_grid.setLayoutDirection(Qt.LeftToRight)
        self.size_grid.setFrameShape(QFrame.StyledPanel)
        self.size_grid.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.size_grid, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout.addWidget(self.footer_frame, 0, Qt.AlignBottom)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"ngDroneNet", None))
        self.minimize.setText("")
        self.restore.setText("")
        self.close.setText("")
        self.pushButton_5.setText("")
        self.pushButton_3.setText("")
        self.pushButton_6.setText("")
        self.pushButton_4.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Pre_written script", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Information", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Game_control", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Keybord control", None))
        self.pushButton_7.setText("")
        self.pushButton_10.setText("")
        self.pushButton_9.setText("")
        self.pushButton_8.setText("")
        self.pushButton_13.setText("")
        self.pushButton_11.setText("")
        self.pushButton_12.setText("")
        self.pushButton_14.setText("")
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"Unarmed", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"Armed", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Roll", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Yaw", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Throttle", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Pitch", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"drone information", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"a", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"d", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"k", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"ROLL_INCR", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"THROTTLE_INCR", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"THROTTLE_DECR", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"w", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"i", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"YAW_INCR", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"PITCH_DECR", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"ROLL_DECR", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"PITCH_INCR", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"YAW_DECR", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"j", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"i", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"ROLL", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"value", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"THROTTLE", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"value", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"YAW", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"value", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"PITCH", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"value", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"Execute", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"POST_SCRIPT", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"PRE_SCRIPT", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Version 1.0 | copyright 307", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"?", None))
    # retranslateUi

