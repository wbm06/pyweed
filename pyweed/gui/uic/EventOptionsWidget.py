# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/uic/EventOptionsWidget.ui'
#
# Created: Tue Feb 28 15:37:45 2017
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_EventOptionsWidget(object):
    def setupUi(self, EventOptionsWidget):
        EventOptionsWidget.setObjectName(_fromUtf8("EventOptionsWidget"))
        EventOptionsWidget.resize(309, 743)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(EventOptionsWidget.sizePolicy().hasHeightForWidth())
        EventOptionsWidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QtGui.QVBoxLayout(EventOptionsWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.timeGroupBox = QtGui.QGroupBox(EventOptionsWidget)
        self.timeGroupBox.setObjectName(_fromUtf8("timeGroupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.timeGroupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.timeBetweenRadioButton = QtGui.QRadioButton(self.timeGroupBox)
        self.timeBetweenRadioButton.setEnabled(True)
        self.timeBetweenRadioButton.setChecked(True)
        self.timeBetweenRadioButton.setObjectName(_fromUtf8("timeBetweenRadioButton"))
        self.verticalLayout_2.addWidget(self.timeBetweenRadioButton)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setContentsMargins(24, -1, -1, -1)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.formLayout_3 = QtGui.QFormLayout()
        self.formLayout_3.setFieldGrowthPolicy(QtGui.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout_3.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout_3.setHorizontalSpacing(4)
        self.formLayout_3.setVerticalSpacing(1)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.starttimeLabel = QtGui.QLabel(self.timeGroupBox)
        self.starttimeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.starttimeLabel.setObjectName(_fromUtf8("starttimeLabel"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.starttimeLabel)
        self.starttimeDateTimeEdit = QtGui.QDateTimeEdit(self.timeGroupBox)
        self.starttimeDateTimeEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.starttimeDateTimeEdit.setCalendarPopup(True)
        self.starttimeDateTimeEdit.setTimeSpec(QtCore.Qt.UTC)
        self.starttimeDateTimeEdit.setObjectName(_fromUtf8("starttimeDateTimeEdit"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.starttimeDateTimeEdit)
        self.endtimeLabel = QtGui.QLabel(self.timeGroupBox)
        self.endtimeLabel.setObjectName(_fromUtf8("endtimeLabel"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.endtimeLabel)
        self.endtimeDateTimeEdit = QtGui.QDateTimeEdit(self.timeGroupBox)
        self.endtimeDateTimeEdit.setCalendarPopup(True)
        self.endtimeDateTimeEdit.setTimeSpec(QtCore.Qt.UTC)
        self.endtimeDateTimeEdit.setObjectName(_fromUtf8("endtimeDateTimeEdit"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.endtimeDateTimeEdit)
        self.verticalLayout_7.addLayout(self.formLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.time30DaysPushButton = QtGui.QPushButton(self.timeGroupBox)
        self.time30DaysPushButton.setObjectName(_fromUtf8("time30DaysPushButton"))
        self.horizontalLayout_2.addWidget(self.time30DaysPushButton)
        self.time1YearPushButton = QtGui.QPushButton(self.timeGroupBox)
        self.time1YearPushButton.setObjectName(_fromUtf8("time1YearPushButton"))
        self.horizontalLayout_2.addWidget(self.time1YearPushButton)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_7)
        spacerItem = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.horizontalLayout_3.setStretch(1, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.line_3 = QtGui.QFrame(self.timeGroupBox)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout_2.addWidget(self.line_3)
        self.timeFromStationsRadioButton = QtGui.QRadioButton(self.timeGroupBox)
        self.timeFromStationsRadioButton.setEnabled(True)
        self.timeFromStationsRadioButton.setObjectName(_fromUtf8("timeFromStationsRadioButton"))
        self.verticalLayout_2.addWidget(self.timeFromStationsRadioButton)
        self.verticalLayout.addWidget(self.timeGroupBox)
        self.magnitudeGroupBox = QtGui.QGroupBox(EventOptionsWidget)
        self.magnitudeGroupBox.setObjectName(_fromUtf8("magnitudeGroupBox"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.magnitudeGroupBox)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.magnitudeLayout = QtGui.QHBoxLayout()
        self.magnitudeLayout.setSpacing(0)
        self.magnitudeLayout.setObjectName(_fromUtf8("magnitudeLayout"))
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setSpacing(1)
        self.verticalLayout_9.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout_9.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setSpacing(4)
        self.horizontalLayout_15.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.minMagDoubleSpinBox = QtGui.QDoubleSpinBox(self.magnitudeGroupBox)
        self.minMagDoubleSpinBox.setDecimals(1)
        self.minMagDoubleSpinBox.setMaximum(10.0)
        self.minMagDoubleSpinBox.setObjectName(_fromUtf8("minMagDoubleSpinBox"))
        self.horizontalLayout_15.addWidget(self.minMagDoubleSpinBox)
        self.label_11 = QtGui.QLabel(self.magnitudeGroupBox)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_15.addWidget(self.label_11)
        self.maxMagDoubleSpinBox = QtGui.QDoubleSpinBox(self.magnitudeGroupBox)
        self.maxMagDoubleSpinBox.setDecimals(1)
        self.maxMagDoubleSpinBox.setMaximum(10.0)
        self.maxMagDoubleSpinBox.setObjectName(_fromUtf8("maxMagDoubleSpinBox"))
        self.horizontalLayout_15.addWidget(self.maxMagDoubleSpinBox)
        spacerItem1 = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem1)
        self.verticalLayout_9.addLayout(self.horizontalLayout_15)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_7 = QtGui.QLabel(self.magnitudeGroupBox)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout.addWidget(self.label_7)
        self.magTypeComboBox = QtGui.QComboBox(self.magnitudeGroupBox)
        self.magTypeComboBox.setEnabled(True)
        self.magTypeComboBox.setObjectName(_fromUtf8("magTypeComboBox"))
        self.magTypeComboBox.addItem(_fromUtf8(""))
        self.magTypeComboBox.addItem(_fromUtf8(""))
        self.magTypeComboBox.addItem(_fromUtf8(""))
        self.magTypeComboBox.addItem(_fromUtf8(""))
        self.magTypeComboBox.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.magTypeComboBox)
        spacerItem2 = QtGui.QSpacerItem(1, 0, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_9.addLayout(self.horizontalLayout)
        self.magnitudeLayout.addLayout(self.verticalLayout_9)
        spacerItem3 = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.magnitudeLayout.addItem(spacerItem3)
        self.magnitudeLayout.setStretch(1, 1)
        self.verticalLayout_3.addLayout(self.magnitudeLayout)
        self.verticalLayout.addWidget(self.magnitudeGroupBox)
        self.depthGroupBox = QtGui.QGroupBox(EventOptionsWidget)
        self.depthGroupBox.setObjectName(_fromUtf8("depthGroupBox"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.depthGroupBox)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.depthLayout = QtGui.QHBoxLayout()
        self.depthLayout.setSpacing(0)
        self.depthLayout.setObjectName(_fromUtf8("depthLayout"))
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setSpacing(4)
        self.horizontalLayout_16.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.minDepthDoubleSpinBox = QtGui.QDoubleSpinBox(self.depthGroupBox)
        self.minDepthDoubleSpinBox.setDecimals(1)
        self.minDepthDoubleSpinBox.setMaximum(6800.0)
        self.minDepthDoubleSpinBox.setObjectName(_fromUtf8("minDepthDoubleSpinBox"))
        self.horizontalLayout_16.addWidget(self.minDepthDoubleSpinBox)
        self.label_13 = QtGui.QLabel(self.depthGroupBox)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_16.addWidget(self.label_13)
        self.maxDepthDoubleSpinBox = QtGui.QDoubleSpinBox(self.depthGroupBox)
        self.maxDepthDoubleSpinBox.setDecimals(1)
        self.maxDepthDoubleSpinBox.setMaximum(6800.0)
        self.maxDepthDoubleSpinBox.setObjectName(_fromUtf8("maxDepthDoubleSpinBox"))
        self.horizontalLayout_16.addWidget(self.maxDepthDoubleSpinBox)
        self.label_12 = QtGui.QLabel(self.depthGroupBox)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_16.addWidget(self.label_12)
        self.depthLayout.addLayout(self.horizontalLayout_16)
        spacerItem4 = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.depthLayout.addItem(spacerItem4)
        self.depthLayout.setStretch(1, 1)
        self.verticalLayout_5.addLayout(self.depthLayout)
        self.verticalLayout.addWidget(self.depthGroupBox)
        self.locationGroupBox = QtGui.QGroupBox(EventOptionsWidget)
        self.locationGroupBox.setObjectName(_fromUtf8("locationGroupBox"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.locationGroupBox)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.locationGlobalRadioButton = QtGui.QRadioButton(self.locationGroupBox)
        self.locationGlobalRadioButton.setChecked(True)
        self.locationGlobalRadioButton.setObjectName(_fromUtf8("locationGlobalRadioButton"))
        self.verticalLayout_6.addWidget(self.locationGlobalRadioButton)
        self.line_4 = QtGui.QFrame(self.locationGroupBox)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.verticalLayout_6.addWidget(self.line_4)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.locationRangeRadioButton = QtGui.QRadioButton(self.locationGroupBox)
        self.locationRangeRadioButton.setChecked(False)
        self.locationRangeRadioButton.setObjectName(_fromUtf8("locationRangeRadioButton"))
        self.horizontalLayout_4.addWidget(self.locationRangeRadioButton)
        spacerItem5 = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.drawLocationRangeToolButton = QtGui.QToolButton(self.locationGroupBox)
        self.drawLocationRangeToolButton.setCheckable(True)
        self.drawLocationRangeToolButton.setObjectName(_fromUtf8("drawLocationRangeToolButton"))
        self.horizontalLayout_4.addWidget(self.drawLocationRangeToolButton)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.locationRangeLayout = QtGui.QHBoxLayout()
        self.locationRangeLayout.setSpacing(0)
        self.locationRangeLayout.setContentsMargins(24, -1, -1, -1)
        self.locationRangeLayout.setObjectName(_fromUtf8("locationRangeLayout"))
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setSpacing(1)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.horizontalLayout_23 = QtGui.QHBoxLayout()
        self.horizontalLayout_23.setObjectName(_fromUtf8("horizontalLayout_23"))
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem6)
        self.locationRangeNorthDoubleSpinBox = QtGui.QDoubleSpinBox(self.locationGroupBox)
        self.locationRangeNorthDoubleSpinBox.setMinimum(-90.0)
        self.locationRangeNorthDoubleSpinBox.setMaximum(90.0)
        self.locationRangeNorthDoubleSpinBox.setObjectName(_fromUtf8("locationRangeNorthDoubleSpinBox"))
        self.horizontalLayout_23.addWidget(self.locationRangeNorthDoubleSpinBox)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem7)
        self.verticalLayout_8.addLayout(self.horizontalLayout_23)
        self.horizontalLayout_24 = QtGui.QHBoxLayout()
        self.horizontalLayout_24.setObjectName(_fromUtf8("horizontalLayout_24"))
        self.locationRangeWestDoubleSpinBox = QtGui.QDoubleSpinBox(self.locationGroupBox)
        self.locationRangeWestDoubleSpinBox.setMinimum(-180.0)
        self.locationRangeWestDoubleSpinBox.setMaximum(180.0)
        self.locationRangeWestDoubleSpinBox.setObjectName(_fromUtf8("locationRangeWestDoubleSpinBox"))
        self.horizontalLayout_24.addWidget(self.locationRangeWestDoubleSpinBox)
        self.locationRangeEastDoubleSpinBox = QtGui.QDoubleSpinBox(self.locationGroupBox)
        self.locationRangeEastDoubleSpinBox.setMinimum(-180.0)
        self.locationRangeEastDoubleSpinBox.setMaximum(180.0)
        self.locationRangeEastDoubleSpinBox.setObjectName(_fromUtf8("locationRangeEastDoubleSpinBox"))
        self.horizontalLayout_24.addWidget(self.locationRangeEastDoubleSpinBox)
        self.verticalLayout_8.addLayout(self.horizontalLayout_24)
        self.horizontalLayout_25 = QtGui.QHBoxLayout()
        self.horizontalLayout_25.setObjectName(_fromUtf8("horizontalLayout_25"))
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem8)
        self.locationRangeSouthDoubleSpinBox = QtGui.QDoubleSpinBox(self.locationGroupBox)
        self.locationRangeSouthDoubleSpinBox.setMinimum(-90.0)
        self.locationRangeSouthDoubleSpinBox.setMaximum(90.0)
        self.locationRangeSouthDoubleSpinBox.setObjectName(_fromUtf8("locationRangeSouthDoubleSpinBox"))
        self.horizontalLayout_25.addWidget(self.locationRangeSouthDoubleSpinBox)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem9)
        self.verticalLayout_8.addLayout(self.horizontalLayout_25)
        self.locationRangeLayout.addLayout(self.verticalLayout_8)
        spacerItem10 = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.locationRangeLayout.addItem(spacerItem10)
        self.locationRangeLayout.setStretch(1, 1)
        self.verticalLayout_6.addLayout(self.locationRangeLayout)
        self.line = QtGui.QFrame(self.locationGroupBox)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_6.addWidget(self.line)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.locationDistanceFromPointRadioButton = QtGui.QRadioButton(self.locationGroupBox)
        self.locationDistanceFromPointRadioButton.setEnabled(True)
        self.locationDistanceFromPointRadioButton.setObjectName(_fromUtf8("locationDistanceFromPointRadioButton"))
        self.horizontalLayout_5.addWidget(self.locationDistanceFromPointRadioButton)
        spacerItem11 = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem11)
        self.drawDistanceFromPointToolButton = QtGui.QToolButton(self.locationGroupBox)
        self.drawDistanceFromPointToolButton.setCheckable(True)
        self.drawDistanceFromPointToolButton.setObjectName(_fromUtf8("drawDistanceFromPointToolButton"))
        self.horizontalLayout_5.addWidget(self.drawDistanceFromPointToolButton)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.locationDistanceFromPointLayout = QtGui.QHBoxLayout()
        self.locationDistanceFromPointLayout.setSpacing(0)
        self.locationDistanceFromPointLayout.setContentsMargins(24, -1, -1, -1)
        self.locationDistanceFromPointLayout.setObjectName(_fromUtf8("locationDistanceFromPointLayout"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setSpacing(1)
        self.verticalLayout_4.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout_4.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setSpacing(4)
        self.horizontalLayout_14.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.distanceFromPointMinRadiusDoubleSpinBox = QtGui.QDoubleSpinBox(self.locationGroupBox)
        self.distanceFromPointMinRadiusDoubleSpinBox.setMinimum(0.0)
        self.distanceFromPointMinRadiusDoubleSpinBox.setMaximum(180.0)
        self.distanceFromPointMinRadiusDoubleSpinBox.setObjectName(_fromUtf8("distanceFromPointMinRadiusDoubleSpinBox"))
        self.horizontalLayout_14.addWidget(self.distanceFromPointMinRadiusDoubleSpinBox)
        self.label_3 = QtGui.QLabel(self.locationGroupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_14.addWidget(self.label_3)
        self.distanceFromPointMaxRadiusDoubleSpinBox = QtGui.QDoubleSpinBox(self.locationGroupBox)
        self.distanceFromPointMaxRadiusDoubleSpinBox.setMinimum(0.0)
        self.distanceFromPointMaxRadiusDoubleSpinBox.setMaximum(180.0)
        self.distanceFromPointMaxRadiusDoubleSpinBox.setObjectName(_fromUtf8("distanceFromPointMaxRadiusDoubleSpinBox"))
        self.horizontalLayout_14.addWidget(self.distanceFromPointMaxRadiusDoubleSpinBox)
        self.label_8 = QtGui.QLabel(self.locationGroupBox)
        self.label_8.setEnabled(True)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_14.addWidget(self.label_8)
        self.verticalLayout_4.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_18 = QtGui.QHBoxLayout()
        self.horizontalLayout_18.setSpacing(4)
        self.horizontalLayout_18.setObjectName(_fromUtf8("horizontalLayout_18"))
        self.label_6 = QtGui.QLabel(self.locationGroupBox)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_18.addWidget(self.label_6)
        self.distanceFromPointEastDoubleSpinBox = QtGui.QDoubleSpinBox(self.locationGroupBox)
        self.distanceFromPointEastDoubleSpinBox.setMinimum(-180.0)
        self.distanceFromPointEastDoubleSpinBox.setMaximum(180.0)
        self.distanceFromPointEastDoubleSpinBox.setObjectName(_fromUtf8("distanceFromPointEastDoubleSpinBox"))
        self.horizontalLayout_18.addWidget(self.distanceFromPointEastDoubleSpinBox)
        self.label_14 = QtGui.QLabel(self.locationGroupBox)
        self.label_14.setEnabled(True)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.horizontalLayout_18.addWidget(self.label_14)
        self.distanceFromPointNorthDoubleSpinBox = QtGui.QDoubleSpinBox(self.locationGroupBox)
        self.distanceFromPointNorthDoubleSpinBox.setMinimum(-90.0)
        self.distanceFromPointNorthDoubleSpinBox.setMaximum(90.0)
        self.distanceFromPointNorthDoubleSpinBox.setObjectName(_fromUtf8("distanceFromPointNorthDoubleSpinBox"))
        self.horizontalLayout_18.addWidget(self.distanceFromPointNorthDoubleSpinBox)
        self.label_9 = QtGui.QLabel(self.locationGroupBox)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_18.addWidget(self.label_9)
        self.verticalLayout_4.addLayout(self.horizontalLayout_18)
        self.locationDistanceFromPointLayout.addLayout(self.verticalLayout_4)
        spacerItem12 = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.locationDistanceFromPointLayout.addItem(spacerItem12)
        self.locationDistanceFromPointLayout.setStretch(1, 1)
        self.verticalLayout_6.addLayout(self.locationDistanceFromPointLayout)
        self.line_2 = QtGui.QFrame(self.locationGroupBox)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout_6.addWidget(self.line_2)
        self.locationFromStationsRadioButton = QtGui.QRadioButton(self.locationGroupBox)
        self.locationFromStationsRadioButton.setEnabled(True)
        self.locationFromStationsRadioButton.setObjectName(_fromUtf8("locationFromStationsRadioButton"))
        self.verticalLayout_6.addWidget(self.locationFromStationsRadioButton)
        self.verticalLayout.addWidget(self.locationGroupBox)
        spacerItem13 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem13)

        self.retranslateUi(EventOptionsWidget)
        QtCore.QMetaObject.connectSlotsByName(EventOptionsWidget)

    def retranslateUi(self, EventOptionsWidget):
        self.timeGroupBox.setTitle(_translate("EventOptionsWidget", "Time", None))
        self.timeBetweenRadioButton.setText(_translate("EventOptionsWidget", "Between start and end times", None))
        self.starttimeLabel.setText(_translate("EventOptionsWidget", "Start", None))
        self.starttimeDateTimeEdit.setDisplayFormat(_translate("EventOptionsWidget", "yyyy-MM-dd hh:mm:ss", None))
        self.endtimeLabel.setText(_translate("EventOptionsWidget", "End", None))
        self.endtimeDateTimeEdit.setDisplayFormat(_translate("EventOptionsWidget", "yyyy-MM-dd hh:mm:ss", None))
        self.time30DaysPushButton.setText(_translate("EventOptionsWidget", "Last 30 days", None))
        self.time1YearPushButton.setText(_translate("EventOptionsWidget", "Last year", None))
        self.timeFromStationsRadioButton.setText(_translate("EventOptionsWidget", "Use the station time selection", None))
        self.magnitudeGroupBox.setTitle(_translate("EventOptionsWidget", "Magnitude", None))
        self.label_11.setText(_translate("EventOptionsWidget", "-", None))
        self.label_7.setText(_translate("EventOptionsWidget", "Type", None))
        self.magTypeComboBox.setItemText(0, _translate("EventOptionsWidget", "All Types", None))
        self.magTypeComboBox.setItemText(1, _translate("EventOptionsWidget", "TB", None))
        self.magTypeComboBox.setItemText(2, _translate("EventOptionsWidget", "ML", None))
        self.magTypeComboBox.setItemText(3, _translate("EventOptionsWidget", "MS", None))
        self.magTypeComboBox.setItemText(4, _translate("EventOptionsWidget", "MW", None))
        self.depthGroupBox.setTitle(_translate("EventOptionsWidget", "Depth", None))
        self.label_13.setText(_translate("EventOptionsWidget", "-", None))
        self.label_12.setText(_translate("EventOptionsWidget", "km", None))
        self.locationGroupBox.setTitle(_translate("EventOptionsWidget", "Location", None))
        self.locationGlobalRadioButton.setText(_translate("EventOptionsWidget", "Global", None))
        self.locationRangeRadioButton.setText(_translate("EventOptionsWidget", "Within lat/lon box", None))
        self.drawLocationRangeToolButton.setText(_translate("EventOptionsWidget", "Draw on map", None))
        self.locationDistanceFromPointRadioButton.setText(_translate("EventOptionsWidget", "Distance from point", None))
        self.drawDistanceFromPointToolButton.setText(_translate("EventOptionsWidget", "Draw on map", None))
        self.label_3.setText(_translate("EventOptionsWidget", "-", None))
        self.label_8.setText(_translate("EventOptionsWidget", "degrees", None))
        self.label_6.setText(_translate("EventOptionsWidget", "from", None))
        self.label_14.setText(_translate("EventOptionsWidget", "E", None))
        self.label_9.setText(_translate("EventOptionsWidget", "N", None))
        self.locationFromStationsRadioButton.setText(_translate("EventOptionsWidget", "Use the station location bounds", None))

