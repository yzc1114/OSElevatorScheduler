# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):

        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(1381, 926)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)

        self.e_slider_1 = QtWidgets.QSlider(Form)
        self.e_slider_1.setEnabled(False)
        self.e_slider_1.setGeometry(QtCore.QRect(190, 90, 131, 641))
        self.e_slider_1.setMinimum(1)
        self.e_slider_1.setMaximum(20)
        self.e_slider_1.setPageStep(1)
        self.e_slider_1.setProperty("value", 1)
        self.e_slider_1.setSliderPosition(1)
        self.e_slider_1.setOrientation(QtCore.Qt.Vertical)
        self.e_slider_1.setObjectName("e_slider_1")

        self.e_slider_5 = QtWidgets.QSlider(Form)
        self.e_slider_5.setEnabled(False)
        self.e_slider_5.setGeometry(QtCore.QRect(1170, 90, 131, 641))
        self.e_slider_5.setMinimum(1)
        self.e_slider_5.setMaximum(20)
        self.e_slider_5.setOrientation(QtCore.Qt.Vertical)
        self.e_slider_5.setObjectName("e_slider_5")

        self.e_slider_3 = QtWidgets.QSlider(Form)
        self.e_slider_3.setEnabled(False)
        self.e_slider_3.setGeometry(QtCore.QRect(690, 90, 131, 641))
        self.e_slider_3.setMinimum(1)
        self.e_slider_3.setMaximum(20)
        self.e_slider_3.setOrientation(QtCore.Qt.Vertical)
        self.e_slider_3.setObjectName("e_slider_3")

        self.e_slider_2 = QtWidgets.QSlider(Form)
        self.e_slider_2.setEnabled(False)
        self.e_slider_2.setGeometry(QtCore.QRect(440, 90, 131, 641))
        self.e_slider_2.setMinimum(1)
        self.e_slider_2.setMaximum(20)
        self.e_slider_2.setOrientation(QtCore.Qt.Vertical)
        self.e_slider_2.setObjectName("e_slider_2")

        self.e_slider_4 = QtWidgets.QSlider(Form)
        self.e_slider_4.setEnabled(False)
        self.e_slider_4.setGeometry(QtCore.QRect(930, 90, 131, 641))
        self.e_slider_4.setMinimum(1)
        self.e_slider_4.setMaximum(20)
        self.e_slider_4.setOrientation(QtCore.Qt.Vertical)
        self.e_slider_4.setObjectName("e_slider_4")

        self.label = QtWidgets.QLabel(Form)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(140, 730, 101, 31))

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())

        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(420, 720, 101, 51))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(640, 720, 121, 41))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(950, 720, 91, 41))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(1190, 730, 81, 31))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")

        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(80, 90, 91, 641))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.e1_buttons = [QtWidgets.QPushButton(self.verticalLayoutWidget) for i in range(20)]
        for i, b in enumerate(reversed(self.e1_buttons)):
            b.setObjectName("e1_" + str(i+1))
            b.setText(str(i+1))
            self.verticalLayout.addWidget(self.e1_buttons[i])


        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(340, 90, 91, 641))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.e2_buttons = [QtWidgets.QPushButton(self.verticalLayoutWidget_2) for i in range(20)]
        for i, b in enumerate(reversed(self.e2_buttons)):
            b.setObjectName("e2_" + str(i + 1))
            b.setText(str(i + 1))
            self.verticalLayout_2.addWidget(self.e2_buttons[i])


        self.verticalLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(590, 90, 91, 641))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.e3_buttons = [QtWidgets.QPushButton(self.verticalLayoutWidget_3) for i in range(20)]
        for i, b in enumerate(reversed(self.e3_buttons)):
            b.setObjectName("e3_" + str(i + 1))
            b.setText(str(i + 1))
            self.verticalLayout_3.addWidget(self.e3_buttons[i])

        self.verticalLayoutWidget_4 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(840, 90, 81, 641))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.e4_buttons = [QtWidgets.QPushButton(self.verticalLayoutWidget_4) for i in range(20)]
        for i, b in enumerate(reversed(self.e4_buttons)):
            b.setObjectName("e4_" + str(i + 1))
            b.setText(str(i + 1))
            self.verticalLayout_4.addWidget(self.e4_buttons[i])

        self.verticalLayoutWidget_5 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(1080, 90, 81, 641))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")

        self.e5_buttons = [QtWidgets.QPushButton(self.verticalLayoutWidget_5) for i in range(20)]
        for i, b in enumerate(reversed(self.e5_buttons)):
            b.setObjectName("e5_" + str(i + 1))
            b.setText(str(i + 1))
            self.verticalLayout_5.addWidget(self.e5_buttons[i])


        self.e1_up = QtWidgets.QPushButton(Form)
        self.e1_up.setGeometry(QtCore.QRect(190, 760, 51, 41))
        self.e1_up.setObjectName("e1_up")

        self.e1_down = QtWidgets.QPushButton(Form)
        self.e1_down.setGeometry(QtCore.QRect(270, 760, 51, 41))
        self.e1_down.setObjectName("e1_down")

        self.e2_up = QtWidgets.QPushButton(Form)
        self.e2_up.setGeometry(QtCore.QRect(440, 760, 51, 41))
        self.e2_up.setObjectName("e2_up")

        self.e2_down = QtWidgets.QPushButton(Form)
        self.e2_down.setGeometry(QtCore.QRect(520, 760, 51, 41))
        self.e2_down.setObjectName("e2_down")

        self.e3_up = QtWidgets.QPushButton(Form)
        self.e3_up.setGeometry(QtCore.QRect(690, 760, 51, 41))
        self.e3_up.setObjectName("e3_up")

        self.e3_down = QtWidgets.QPushButton(Form)
        self.e3_down.setGeometry(QtCore.QRect(770, 760, 51, 41))
        self.e3_down.setObjectName("e3_down")

        self.e4_up = QtWidgets.QPushButton(Form)
        self.e4_up.setGeometry(QtCore.QRect(930, 760, 51, 41))
        self.e4_up.setObjectName("e4_up")

        self.e4_down = QtWidgets.QPushButton(Form)
        self.e4_down.setGeometry(QtCore.QRect(1010, 760, 51, 41))
        self.e4_down.setObjectName("e4_down")

        self.e5_up = QtWidgets.QPushButton(Form)
        self.e5_up.setGeometry(QtCore.QRect(1170, 760, 51, 41))
        self.e5_up.setObjectName("e5_up")

        self.e5_down = QtWidgets.QPushButton(Form)
        self.e5_down.setGeometry(QtCore.QRect(1240, 760, 51, 41))
        self.e5_down.setObjectName("e5_down")

        self.e1_spin_box = QtWidgets.QSpinBox(Form)
        self.e1_spin_box.setGeometry(QtCore.QRect(80, 760, 91, 91))
        self.e1_spin_box.setMinimum(1)
        self.e1_spin_box.setMaximum(20)
        self.e1_spin_box.setObjectName("e1_spin_box")

        self.e2_spin_box = QtWidgets.QSpinBox(Form)
        self.e2_spin_box.setGeometry(QtCore.QRect(340, 760, 91, 91))
        self.e2_spin_box.setMinimum(1)
        self.e2_spin_box.setMaximum(20)
        self.e2_spin_box.setObjectName("e2_spin_box")

        self.e3_spin_box = QtWidgets.QSpinBox(Form)
        self.e3_spin_box.setGeometry(QtCore.QRect(590, 760, 91, 91))
        self.e3_spin_box.setMinimum(1)
        self.e3_spin_box.setMaximum(20)
        self.e3_spin_box.setObjectName("e3_spin_box")

        self.e4_spin_box = QtWidgets.QSpinBox(Form)
        self.e4_spin_box.setGeometry(QtCore.QRect(840, 760, 81, 91))
        self.e4_spin_box.setMinimum(1)
        self.e4_spin_box.setMaximum(20)
        self.e4_spin_box.setObjectName("e4_spin_box")

        self.e5_spin_box = QtWidgets.QSpinBox(Form)
        self.e5_spin_box.setGeometry(QtCore.QRect(1080, 760, 81, 91))
        self.e5_spin_box.setMinimum(1)
        self.e5_spin_box.setMaximum(20)
        self.e5_spin_box.setObjectName("e5_spin_box")

        self.e1_open = QtWidgets.QPushButton(Form)
        self.e1_open.setGeometry(QtCore.QRect(190, 812, 51, 41))
        self.e1_open.setObjectName("e1_open")
        self.e1_close = QtWidgets.QPushButton(Form)
        self.e1_close.setGeometry(QtCore.QRect(270, 812, 51, 41))
        self.e1_close.setObjectName("e1_close")

        self.e2_open = QtWidgets.QPushButton(Form)
        self.e2_open.setGeometry(QtCore.QRect(440, 810, 51, 41))
        self.e2_open.setObjectName("e2_open")
        self.e2_close = QtWidgets.QPushButton(Form)
        self.e2_close.setGeometry(QtCore.QRect(520, 810, 51, 41))
        self.e2_close.setObjectName("e2_close")

        self.e3_open = QtWidgets.QPushButton(Form)
        self.e3_open.setGeometry(QtCore.QRect(690, 810, 51, 41))
        self.e3_open.setObjectName("e3_open")
        self.e3_close = QtWidgets.QPushButton(Form)
        self.e3_close.setGeometry(QtCore.QRect(770, 810, 51, 41))
        self.e3_close.setObjectName("e3_close")

        self.e4_open = QtWidgets.QPushButton(Form)
        self.e4_open.setGeometry(QtCore.QRect(930, 810, 51, 41))
        self.e4_open.setObjectName("e4_open")
        self.e4_close = QtWidgets.QPushButton(Form)
        self.e4_close.setGeometry(QtCore.QRect(1010, 810, 51, 41))
        self.e4_close.setObjectName("e4_close")

        self.e5_open = QtWidgets.QPushButton(Form)
        self.e5_open.setGeometry(QtCore.QRect(1170, 810, 51, 41))
        self.e5_open.setObjectName("e5_open")
        self.e5_close = QtWidgets.QPushButton(Form)
        self.e5_close.setGeometry(QtCore.QRect(1240, 810, 51, 41))
        self.e5_close.setObjectName("e5_close")

        self.level_1 = QtWidgets.QLabel(Form)
        self.level_1.setGeometry(QtCore.QRect(140, 30, 91, 41))
        self.level_1.setAlignment(QtCore.Qt.AlignCenter)
        self.level_1.setObjectName("level_1")
        self.level_2 = QtWidgets.QLabel(Form)
        self.level_2.setGeometry(QtCore.QRect(390, 30, 111, 41))
        self.level_2.setAlignment(QtCore.Qt.AlignCenter)
        self.level_2.setObjectName("level_2")
        self.level_3 = QtWidgets.QLabel(Form)
        self.level_3.setGeometry(QtCore.QRect(630, 30, 91, 41))
        self.level_3.setAlignment(QtCore.Qt.AlignCenter)
        self.level_3.setObjectName("level_3")
        self.level_4 = QtWidgets.QLabel(Form)
        self.level_4.setGeometry(QtCore.QRect(860, 40, 141, 31))
        self.level_4.setAlignment(QtCore.Qt.AlignCenter)
        self.level_4.setObjectName("level_4")
        self.level_5 = QtWidgets.QLabel(Form)
        self.level_5.setGeometry(QtCore.QRect(1110, 40, 111, 20))
        self.level_5.setAlignment(QtCore.Qt.AlignCenter)
        self.level_5.setObjectName("level_5")

        self.e_door_1 = QtWidgets.QLabel(Form)
        self.e_door_1.setGeometry(QtCore.QRect(120, 870, 141, 41))
        self.e_door_1.setAlignment(QtCore.Qt.AlignCenter)
        self.e_door_1.setObjectName("e_door_1")
        self.e_door_2 = QtWidgets.QLabel(Form)
        self.e_door_2.setGeometry(QtCore.QRect(400, 870, 141, 41))
        self.e_door_2.setAlignment(QtCore.Qt.AlignCenter)
        self.e_door_2.setObjectName("e_door_2")
        self.e_door_3 = QtWidgets.QLabel(Form)
        self.e_door_3.setGeometry(QtCore.QRect(620, 870, 141, 41))
        self.e_door_3.setAlignment(QtCore.Qt.AlignCenter)
        self.e_door_3.setObjectName("e_door_3")
        self.e_door_4 = QtWidgets.QLabel(Form)
        self.e_door_4.setGeometry(QtCore.QRect(880, 870, 141, 41))
        self.e_door_4.setAlignment(QtCore.Qt.AlignCenter)
        self.e_door_4.setObjectName("e_door_4")
        self.e_door_5 = QtWidgets.QLabel(Form)
        self.e_door_5.setGeometry(QtCore.QRect(1100, 870, 141, 41))
        self.e_door_5.setAlignment(QtCore.Qt.AlignCenter)
        self.e_door_5.setObjectName("e_door_5")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "电梯1"))
        self.label_2.setText(_translate("Form", "电梯2"))
        self.label_3.setText(_translate("Form", "电梯3"))
        self.label_4.setText(_translate("Form", "电梯4"))
        self.label_5.setText(_translate("Form", "电梯5"))



        self.e1_up.setText(_translate("Form", "上"))
        self.e1_down.setText(_translate("Form", "下"))
        self.e2_up.setText(_translate("Form", "上"))
        self.e2_down.setText(_translate("Form", "下"))
        self.e3_up.setText(_translate("Form", "上"))
        self.e3_down.setText(_translate("Form", "下"))
        self.e4_up.setText(_translate("Form", "上"))
        self.e4_down.setText(_translate("Form", "下"))
        self.e5_up.setText(_translate("Form", "上"))
        self.e5_down.setText(_translate("Form", "下"))
        self.e1_open.setText(_translate("Form", "开"))
        self.e1_close.setText(_translate("Form", "关"))
        self.e2_open.setText(_translate("Form", "开"))
        self.e2_close.setText(_translate("Form", "关"))
        self.e3_open.setText(_translate("Form", "开"))
        self.e3_close.setText(_translate("Form", "关"))
        self.e4_open.setText(_translate("Form", "开"))
        self.e4_close.setText(_translate("Form", "关"))
        self.e5_open.setText(_translate("Form", "开"))
        self.e5_close.setText(_translate("Form", "关"))
        self.level_1.setText(_translate("Form", "1 层"))
        self.level_2.setText(_translate("Form", "1 层"))
        self.level_3.setText(_translate("Form", "1 层"))
        self.level_4.setText(_translate("Form", "1 层"))
        self.level_5.setText(_translate("Form", "1 层"))
        self.e_door_1.setText(_translate("Form", "门状态：关"))
        self.e_door_2.setText(_translate("Form", "门状态：关"))
        self.e_door_3.setText(_translate("Form", "门状态：关"))
        self.e_door_4.setText(_translate("Form", "门状态：关"))
        self.e_door_5.setText(_translate("Form", "门状态：关"))

