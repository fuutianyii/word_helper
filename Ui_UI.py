# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\words_helper\UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1118, 581)
        MainWindow.setMinimumSize(QtCore.QSize(900, 550))
        MainWindow.setMaximumSize(QtCore.QSize(65535, 65535))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leftframe = QtWidgets.QFrame(self.centralwidget)
        self.leftframe.setMinimumSize(QtCore.QSize(80, 0))
        self.leftframe.setMaximumSize(QtCore.QSize(80, 16777215))
        self.leftframe.setAutoFillBackground(False)
        self.leftframe.setObjectName("leftframe")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.leftframe)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.leftframe_top = QtWidgets.QFrame(self.leftframe)
        self.leftframe_top.setMinimumSize(QtCore.QSize(80, 400))
        self.leftframe_top.setMaximumSize(QtCore.QSize(80, 400))
        self.leftframe_top.setObjectName("leftframe_top")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.leftframe_top)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.left_first_button = QtWidgets.QPushButton(self.leftframe_top)
        self.left_first_button.setMinimumSize(QtCore.QSize(50, 50))
        self.left_first_button.setMaximumSize(QtCore.QSize(50, 50))
        self.left_first_button.setObjectName("left_first_button")
        self.verticalLayout_2.addWidget(self.left_first_button)
        self.left_second_button = QtWidgets.QPushButton(self.leftframe_top)
        self.left_second_button.setMinimumSize(QtCore.QSize(50, 50))
        self.left_second_button.setMaximumSize(QtCore.QSize(50, 50))
        self.left_second_button.setObjectName("left_second_button")
        self.verticalLayout_2.addWidget(self.left_second_button)
        self.left_third_button = QtWidgets.QPushButton(self.leftframe_top)
        self.left_third_button.setMinimumSize(QtCore.QSize(50, 50))
        self.left_third_button.setMaximumSize(QtCore.QSize(50, 50))
        self.left_third_button.setObjectName("left_third_button")
        self.verticalLayout_2.addWidget(self.left_third_button)
        self.left_forth_button = QtWidgets.QPushButton(self.leftframe_top)
        self.left_forth_button.setMinimumSize(QtCore.QSize(50, 50))
        self.left_forth_button.setMaximumSize(QtCore.QSize(50, 50))
        self.left_forth_button.setObjectName("left_forth_button")
        self.verticalLayout_2.addWidget(self.left_forth_button)
        self.verticalLayout_3.addWidget(self.leftframe_top)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.leftframe)
        self.Stacked = QtWidgets.QStackedWidget(self.centralwidget)
        self.Stacked.setObjectName("Stacked")
        self.hello_page = QtWidgets.QWidget()
        self.hello_page.setObjectName("hello_page")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.hello_page)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalFrame = QtWidgets.QFrame(self.hello_page)
        self.verticalFrame.setMinimumSize(QtCore.QSize(400, 0))
        self.verticalFrame.setMaximumSize(QtCore.QSize(400, 16777215))
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_4.addItem(spacerItem1)
        self.hello_text = QtWidgets.QLabel(self.verticalFrame)
        self.hello_text.setMinimumSize(QtCore.QSize(0, 150))
        self.hello_text.setMaximumSize(QtCore.QSize(16777215, 150))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(20)
        self.hello_text.setFont(font)
        self.hello_text.setObjectName("hello_text")
        self.verticalLayout_4.addWidget(self.hello_text)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.horizontalLayout_2.addWidget(self.verticalFrame)
        self.Stacked.addWidget(self.hello_page)
        self.add_page = QtWidgets.QWidget()
        self.add_page.setObjectName("add_page")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.add_page)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.add_english_input_frame = QtWidgets.QFrame(self.add_page)
        self.add_english_input_frame.setMinimumSize(QtCore.QSize(0, 50))
        self.add_english_input_frame.setObjectName("add_english_input_frame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.add_english_input_frame)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_12 = QtWidgets.QFrame(self.add_english_input_frame)
        self.frame_12.setMaximumSize(QtCore.QSize(16777215, 150))
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.english_input_edit = QtWidgets.QLineEdit(self.frame_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.english_input_edit.sizePolicy().hasHeightForWidth())
        self.english_input_edit.setSizePolicy(sizePolicy)
        self.english_input_edit.setMaximumSize(QtCore.QSize(65535, 80))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(15)
        self.english_input_edit.setFont(font)
        self.english_input_edit.setObjectName("english_input_edit")
        self.verticalLayout_8.addWidget(self.english_input_edit)
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.frame_14 = QtWidgets.QFrame(self.frame_12)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.online_play_voice_1 = QtWidgets.QPushButton(self.frame_14)
        self.online_play_voice_1.setMinimumSize(QtCore.QSize(10, 30))
        self.online_play_voice_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.online_play_voice_1.setText("")
        self.online_play_voice_1.setObjectName("online_play_voice_1")
        self.horizontalLayout_30.addWidget(self.online_play_voice_1)
        self.online_play_voice_2 = QtWidgets.QPushButton(self.frame_14)
        self.online_play_voice_2.setMinimumSize(QtCore.QSize(10, 30))
        self.online_play_voice_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.online_play_voice_2.setText("")
        self.online_play_voice_2.setObjectName("online_play_voice_2")
        self.horizontalLayout_30.addWidget(self.online_play_voice_2)
        self.horizontalLayout_29.addWidget(self.frame_14)
        self.star = QtWidgets.QPushButton(self.frame_12)
        self.star.setMinimumSize(QtCore.QSize(30, 30))
        self.star.setMaximumSize(QtCore.QSize(30, 30))
        self.star.setText("")
        self.star.setObjectName("star")
        self.horizontalLayout_29.addWidget(self.star)
        self.list_line = QtWidgets.QLineEdit(self.frame_12)
        self.list_line.setMinimumSize(QtCore.QSize(30, 30))
        self.list_line.setMaximumSize(QtCore.QSize(60, 30))
        self.list_line.setObjectName("list_line")
        self.horizontalLayout_29.addWidget(self.list_line)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_29.addItem(spacerItem3)
        self.verticalLayout_8.addLayout(self.horizontalLayout_29)
        self.verticalLayout_6.addWidget(self.frame_12)
        self.frame_13 = QtWidgets.QFrame(self.add_english_input_frame)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.online = QtWidgets.QTabWidget(self.frame_13)
        self.online.setObjectName("online")
        self.online_youdao_page = QtWidgets.QWidget()
        self.online_youdao_page.setObjectName("online_youdao_page")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.online_youdao_page)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.online_youdao_textBoswer = QtWidgets.QTextBrowser(self.online_youdao_page)
        self.online_youdao_textBoswer.setObjectName("online_youdao_textBoswer")
        self.verticalLayout_9.addWidget(self.online_youdao_textBoswer)
        self.online.addTab(self.online_youdao_page, "")
        self.niujin_page_2 = QtWidgets.QWidget()
        self.niujin_page_2.setObjectName("niujin_page_2")
        self.verticalLayout_27 = QtWidgets.QVBoxLayout(self.niujin_page_2)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.online_Oxford_info_box = QtWidgets.QTextBrowser(self.niujin_page_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.online_Oxford_info_box.setFont(font)
        self.online_Oxford_info_box.setObjectName("online_Oxford_info_box")
        self.verticalLayout_27.addWidget(self.online_Oxford_info_box)
        self.online.addTab(self.niujin_page_2, "")
        self.verticalLayout_7.addWidget(self.online)
        self.verticalLayout_6.addWidget(self.frame_13)
        self.verticalLayout_5.addWidget(self.add_english_input_frame)
        self.Stacked.addWidget(self.add_page)
        self.change_page = QtWidgets.QWidget()
        self.change_page.setObjectName("change_page")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.change_page)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.search_frame = QtWidgets.QFrame(self.change_page)
        self.search_frame.setMinimumSize(QtCore.QSize(0, 50))
        self.search_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.search_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.search_frame.setObjectName("search_frame")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.search_frame)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.frame_5 = QtWidgets.QFrame(self.search_frame)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.filter_list_comboBox = QtWidgets.QComboBox(self.frame_5)
        self.filter_list_comboBox.setMinimumSize(QtCore.QSize(80, 25))
        self.filter_list_comboBox.setMaximumSize(QtCore.QSize(80, 25))
        self.filter_list_comboBox.setObjectName("filter_list_comboBox")
        self.horizontalLayout_13.addWidget(self.filter_list_comboBox)
        self.filter_date_comboBox = QtWidgets.QComboBox(self.frame_5)
        self.filter_date_comboBox.setMinimumSize(QtCore.QSize(100, 25))
        self.filter_date_comboBox.setMaximumSize(QtCore.QSize(100, 25))
        self.filter_date_comboBox.setObjectName("filter_date_comboBox")
        self.horizontalLayout_13.addWidget(self.filter_date_comboBox)
        self.search_date_time_frame = QtWidgets.QFrame(self.frame_5)
        self.search_date_time_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.search_date_time_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.search_date_time_frame.setObjectName("search_date_time_frame")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout(self.search_date_time_frame)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.more_functions = QtWidgets.QPushButton(self.search_date_time_frame)
        self.more_functions.setMinimumSize(QtCore.QSize(35, 35))
        self.more_functions.setMaximumSize(QtCore.QSize(35, 35))
        self.more_functions.setText("")
        self.more_functions.setIconSize(QtCore.QSize(25, 25))
        self.more_functions.setObjectName("more_functions")
        self.horizontalLayout_26.addWidget(self.more_functions)
        self.Sync = QtWidgets.QPushButton(self.search_date_time_frame)
        self.Sync.setMinimumSize(QtCore.QSize(35, 35))
        self.Sync.setMaximumSize(QtCore.QSize(35, 35))
        self.Sync.setText("")
        self.Sync.setIconSize(QtCore.QSize(25, 25))
        self.Sync.setObjectName("Sync")
        self.horizontalLayout_26.addWidget(self.Sync)
        self.display_search_line_edit = QtWidgets.QPushButton(self.search_date_time_frame)
        self.display_search_line_edit.setMinimumSize(QtCore.QSize(35, 35))
        self.display_search_line_edit.setMaximumSize(QtCore.QSize(35, 35))
        self.display_search_line_edit.setText("")
        self.display_search_line_edit.setIconSize(QtCore.QSize(25, 25))
        self.display_search_line_edit.setObjectName("display_search_line_edit")
        self.horizontalLayout_26.addWidget(self.display_search_line_edit)
        self.search_edit = QtWidgets.QLineEdit(self.search_date_time_frame)
        self.search_edit.setMinimumSize(QtCore.QSize(150, 0))
        self.search_edit.setMaximumSize(QtCore.QSize(150, 16777215))
        self.search_edit.setStyleSheet("")
        self.search_edit.setObjectName("search_edit")
        self.horizontalLayout_26.addWidget(self.search_edit)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_26.addItem(spacerItem4)
        self.horizontalLayout_13.addWidget(self.search_date_time_frame)
        self.frame_8 = QtWidgets.QFrame(self.frame_5)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.start_exam = QtWidgets.QPushButton(self.frame_8)
        self.start_exam.setObjectName("start_exam")
        self.horizontalLayout_25.addWidget(self.start_exam)
        self.search_forget_words = QtWidgets.QPushButton(self.frame_8)
        self.search_forget_words.setObjectName("search_forget_words")
        self.horizontalLayout_25.addWidget(self.search_forget_words)
        self.horizontalLayout_13.addWidget(self.frame_8)
        self.verticalLayout_15.addWidget(self.frame_5)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.update_table = QtWidgets.QTableWidget(self.search_frame)
        self.update_table.setMinimumSize(QtCore.QSize(150, 0))
        self.update_table.setMaximumSize(QtCore.QSize(150, 16777215))
        self.update_table.setObjectName("update_table")
        self.update_table.setColumnCount(0)
        self.update_table.setRowCount(0)
        self.horizontalLayout_14.addWidget(self.update_table)
        self.frame_6 = QtWidgets.QFrame(self.search_frame)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.selection_word = QtWidgets.QLabel(self.frame_6)
        self.selection_word.setMinimumSize(QtCore.QSize(0, 70))
        self.selection_word.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(30)
        self.selection_word.setFont(font)
        self.selection_word.setText("")
        self.selection_word.setObjectName("selection_word")
        self.verticalLayout_16.addWidget(self.selection_word)
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.frame_11 = QtWidgets.QFrame(self.frame_6)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.play_voice_1 = QtWidgets.QPushButton(self.frame_11)
        self.play_voice_1.setMinimumSize(QtCore.QSize(0, 30))
        self.play_voice_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.play_voice_1.setText("")
        self.play_voice_1.setObjectName("play_voice_1")
        self.horizontalLayout_28.addWidget(self.play_voice_1)
        self.play_voice_2 = QtWidgets.QPushButton(self.frame_11)
        self.play_voice_2.setMaximumSize(QtCore.QSize(150, 30))
        self.play_voice_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.play_voice_2.setText("")
        self.play_voice_2.setObjectName("play_voice_2")
        self.horizontalLayout_28.addWidget(self.play_voice_2)
        self.horizontalLayout_27.addWidget(self.frame_11)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_27.addItem(spacerItem5)
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.insert_date = QtWidgets.QLabel(self.frame_6)
        self.insert_date.setMinimumSize(QtCore.QSize(80, 25))
        self.insert_date.setMaximumSize(QtCore.QSize(80, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.insert_date.setFont(font)
        self.insert_date.setText("")
        self.insert_date.setObjectName("insert_date")
        self.verticalLayout_18.addWidget(self.insert_date)
        self.words_list = QtWidgets.QLabel(self.frame_6)
        self.words_list.setMinimumSize(QtCore.QSize(80, 25))
        self.words_list.setMaximumSize(QtCore.QSize(80, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.words_list.setFont(font)
        self.words_list.setText("")
        self.words_list.setObjectName("words_list")
        self.verticalLayout_18.addWidget(self.words_list)
        self.horizontalLayout_27.addLayout(self.verticalLayout_18)
        self.verticalLayout_16.addLayout(self.horizontalLayout_27)
        self.tabWidget = QtWidgets.QTabWidget(self.frame_6)
        self.tabWidget.setObjectName("tabWidget")
        self.youdao_page = QtWidgets.QWidget()
        self.youdao_page.setObjectName("youdao_page")
        self.tabWidget.addTab(self.youdao_page, "")
        self.niujin_page = QtWidgets.QWidget()
        self.niujin_page.setObjectName("niujin_page")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.niujin_page)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.Oxford_info_box = QtWidgets.QTextBrowser(self.niujin_page)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.Oxford_info_box.setFont(font)
        self.Oxford_info_box.setObjectName("Oxford_info_box")
        self.verticalLayout_19.addWidget(self.Oxford_info_box)
        self.tabWidget.addTab(self.niujin_page, "")
        self.defined_page = QtWidgets.QWidget()
        self.defined_page.setObjectName("defined_page")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.defined_page)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.word_info_table = QtWidgets.QTableWidget(self.defined_page)
        self.word_info_table.setObjectName("word_info_table")
        self.word_info_table.setColumnCount(0)
        self.word_info_table.setRowCount(0)
        self.verticalLayout_17.addWidget(self.word_info_table)
        self.tabWidget.addTab(self.defined_page, "")
        self.verticalLayout_16.addWidget(self.tabWidget)
        self.horizontalLayout_14.addWidget(self.frame_6)
        self.verticalLayout_15.addLayout(self.horizontalLayout_14)
        self.verticalLayout_14.addWidget(self.search_frame)
        self.Stacked.addWidget(self.change_page)
        self.exam_page = QtWidgets.QWidget()
        self.exam_page.setObjectName("exam_page")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.exam_page)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.exam_stacked = QtWidgets.QStackedWidget(self.exam_page)
        self.exam_stacked.setObjectName("exam_stacked")
        self.exam_main = QtWidgets.QWidget()
        self.exam_main.setObjectName("exam_main")
        self.gridLayout = QtWidgets.QGridLayout(self.exam_main)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.exam_main)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.change_calendar = QtWidgets.QPushButton(self.frame)
        self.change_calendar.setMinimumSize(QtCore.QSize(75, 23))
        self.change_calendar.setMaximumSize(QtCore.QSize(75, 23))
        self.change_calendar.setObjectName("change_calendar")
        self.horizontalLayout_4.addWidget(self.change_calendar)
        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem7, 2, 0, 1, 1)
        self.frame_10 = QtWidgets.QFrame(self.exam_main)
        self.frame_10.setMinimumSize(QtCore.QSize(0, 400))
        self.frame_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.frame_15 = QtWidgets.QFrame(self.frame_10)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.frame_15)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.frame_exam_today = QtWidgets.QFrame(self.frame_15)
        self.frame_exam_today.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_exam_today.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_exam_today.setObjectName("frame_exam_today")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.frame_exam_today)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.exam_today_button = QtWidgets.QPushButton(self.frame_exam_today)
        self.exam_today_button.setMaximumSize(QtCore.QSize(80, 20))
        self.exam_today_button.setObjectName("exam_today_button")
        self.horizontalLayout_21.addWidget(self.exam_today_button)
        self.verticalLayout_24.addWidget(self.frame_exam_today)
        self.frame_review_words = QtWidgets.QFrame(self.frame_15)
        self.frame_review_words.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_review_words.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_review_words.setObjectName("frame_review_words")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.frame_review_words)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.review_words_button = QtWidgets.QPushButton(self.frame_review_words)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.review_words_button.sizePolicy().hasHeightForWidth())
        self.review_words_button.setSizePolicy(sizePolicy)
        self.review_words_button.setMaximumSize(QtCore.QSize(80, 20))
        self.review_words_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.review_words_button.setAutoDefault(False)
        self.review_words_button.setFlat(False)
        self.review_words_button.setObjectName("review_words_button")
        self.horizontalLayout_19.addWidget(self.review_words_button)
        self.verticalLayout_24.addWidget(self.frame_review_words)
        self.frame_radom_exam = QtWidgets.QFrame(self.frame_15)
        self.frame_radom_exam.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_radom_exam.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_radom_exam.setObjectName("frame_radom_exam")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.frame_radom_exam)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.radom_exam_button = QtWidgets.QPushButton(self.frame_radom_exam)
        self.radom_exam_button.setMaximumSize(QtCore.QSize(80, 20))
        self.radom_exam_button.setObjectName("radom_exam_button")
        self.horizontalLayout_20.addWidget(self.radom_exam_button)
        self.verticalLayout_24.addWidget(self.frame_radom_exam)
        self.frame_review_Forgotten = QtWidgets.QFrame(self.frame_15)
        self.frame_review_Forgotten.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_review_Forgotten.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_review_Forgotten.setObjectName("frame_review_Forgotten")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.frame_review_Forgotten)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.review_Forgotten_button = QtWidgets.QPushButton(self.frame_review_Forgotten)
        self.review_Forgotten_button.setMaximumSize(QtCore.QSize(80, 20))
        self.review_Forgotten_button.setObjectName("review_Forgotten_button")
        self.horizontalLayout_22.addWidget(self.review_Forgotten_button)
        self.verticalLayout_24.addWidget(self.frame_review_Forgotten)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_24.addItem(spacerItem8)
        self.option_frame = QtWidgets.QFrame(self.frame_15)
        self.option_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.option_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.option_frame.setObjectName("option_frame")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout(self.option_frame)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        spacerItem9 = QtWidgets.QSpacerItem(539, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_24.addItem(spacerItem9)
        self.checkBox_voice = QtWidgets.QCheckBox(self.option_frame)
        self.checkBox_voice.setObjectName("checkBox_voice")
        self.horizontalLayout_24.addWidget(self.checkBox_voice)
        self.checkBox_random = QtWidgets.QCheckBox(self.option_frame)
        self.checkBox_random.setObjectName("checkBox_random")
        self.horizontalLayout_24.addWidget(self.checkBox_random)
        self.verticalLayout_24.addWidget(self.option_frame)
        self.verticalLayout_23.addWidget(self.frame_15)
        self.gridLayout.addWidget(self.frame_10, 3, 0, 1, 1)
        self.exam_stacked.addWidget(self.exam_main)
        self.exam_select = QtWidgets.QWidget()
        self.exam_select.setObjectName("exam_select")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.exam_select)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.frame_9 = QtWidgets.QFrame(self.exam_select)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem10)
        self.back_exam_main = QtWidgets.QPushButton(self.frame_9)
        self.back_exam_main.setMinimumSize(QtCore.QSize(75, 23))
        self.back_exam_main.setMaximumSize(QtCore.QSize(75, 23))
        self.back_exam_main.setObjectName("back_exam_main")
        self.horizontalLayout_18.addWidget(self.back_exam_main)
        self.verticalLayout_11.addWidget(self.frame_9)
        self.exam_calendarWidget = QtWidgets.QCalendarWidget(self.exam_select)
        self.exam_calendarWidget.setAutoFillBackground(True)
        self.exam_calendarWidget.setNavigationBarVisible(True)
        self.exam_calendarWidget.setDateEditEnabled(True)
        self.exam_calendarWidget.setObjectName("exam_calendarWidget")
        self.verticalLayout_11.addWidget(self.exam_calendarWidget)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_11.addItem(spacerItem11)
        self.exam_stacked.addWidget(self.exam_select)
        self.exam = QtWidgets.QWidget()
        self.exam.setObjectName("exam")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.exam)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.frame_2 = QtWidgets.QFrame(self.exam)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 80))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem12 = QtWidgets.QSpacerItem(611, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem12)
        self.progress_label = QtWidgets.QLabel(self.frame_2)
        self.progress_label.setObjectName("progress_label")
        self.horizontalLayout_9.addWidget(self.progress_label)
        self.verticalLayout_13.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.exam)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 200))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.exam_chinese_label = QtWidgets.QLabel(self.frame_3)
        self.exam_chinese_label.setMaximumSize(QtCore.QSize(65535, 90))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(17)
        self.exam_chinese_label.setFont(font)
        self.exam_chinese_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.exam_chinese_label.setAlignment(QtCore.Qt.AlignCenter)
        self.exam_chinese_label.setWordWrap(True)
        self.exam_chinese_label.setObjectName("exam_chinese_label")
        self.horizontalLayout_23.addWidget(self.exam_chinese_label)
        self.verticalLayout_20.addLayout(self.horizontalLayout_23)
        spacerItem13 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_20.addItem(spacerItem13)
        self.part_of_speech_label = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(15)
        self.part_of_speech_label.setFont(font)
        self.part_of_speech_label.setAlignment(QtCore.Qt.AlignCenter)
        self.part_of_speech_label.setObjectName("part_of_speech_label")
        self.verticalLayout_20.addWidget(self.part_of_speech_label)
        self.verticalLayout_13.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.exam)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.exam_english_lable = QtWidgets.QLineEdit(self.frame_4)
        self.exam_english_lable.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.exam_english_lable.setFont(font)
        self.exam_english_lable.setAutoFillBackground(False)
        self.exam_english_lable.setText("")
        self.exam_english_lable.setObjectName("exam_english_lable")
        self.horizontalLayout_11.addWidget(self.exam_english_lable)
        self.verticalLayout_13.addWidget(self.frame_4)
        self.frame_7 = QtWidgets.QFrame(self.exam)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.forget_label = QtWidgets.QLabel(self.frame_7)
        self.forget_label.setText("")
        self.forget_label.setObjectName("forget_label")
        self.verticalLayout_21.addWidget(self.forget_label)
        self.foetget_frame = QtWidgets.QFrame(self.frame_7)
        self.foetget_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.foetget_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.foetget_frame.setObjectName("foetget_frame")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.foetget_frame)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.verticalFrame1 = QtWidgets.QFrame(self.foetget_frame)
        self.verticalFrame1.setMaximumSize(QtCore.QSize(80, 16777215))
        self.verticalFrame1.setObjectName("verticalFrame1")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout(self.verticalFrame1)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.remove_forget_pushButton = QtWidgets.QPushButton(self.verticalFrame1)
        self.remove_forget_pushButton.setMaximumSize(QtCore.QSize(80, 16777215))
        self.remove_forget_pushButton.setObjectName("remove_forget_pushButton")
        self.verticalLayout_26.addWidget(self.remove_forget_pushButton)
        self.forget_pushButton = QtWidgets.QPushButton(self.verticalFrame1)
        self.forget_pushButton.setMaximumSize(QtCore.QSize(80, 16777215))
        self.forget_pushButton.setObjectName("forget_pushButton")
        self.verticalLayout_26.addWidget(self.forget_pushButton)
        self.horizontalLayout_12.addWidget(self.verticalFrame1)
        self.verticalLayout_21.addWidget(self.foetget_frame)
        self.verticalLayout_13.addWidget(self.frame_7)
        self.exam_stacked.addWidget(self.exam)
        self.verticalLayout_12.addWidget(self.exam_stacked)
        self.Stacked.addWidget(self.exam_page)
        self.horizontalLayout.addWidget(self.Stacked)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.Stacked.setCurrentIndex(1)
        self.online.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)
        self.exam_stacked.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.left_first_button.setText(_translate("MainWindow", "主页"))
        self.left_second_button.setText(_translate("MainWindow", "查询"))
        self.left_third_button.setText(_translate("MainWindow", "单词"))
        self.left_forth_button.setText(_translate("MainWindow", "测试"))
        self.hello_text.setText(_translate("MainWindow", "日期"))
        self.online.setTabText(self.online.indexOf(self.online_youdao_page), _translate("MainWindow", "有道"))
        self.online.setTabText(self.online.indexOf(self.niujin_page_2), _translate("MainWindow", "牛津"))
        self.start_exam.setText(_translate("MainWindow", "测试"))
        self.search_forget_words.setText(_translate("MainWindow", "遗忘"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.youdao_page), _translate("MainWindow", "有道"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.niujin_page), _translate("MainWindow", "牛津"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.defined_page), _translate("MainWindow", "自定义"))
        self.change_calendar.setText(_translate("MainWindow", "日历"))
        self.exam_today_button.setText(_translate("MainWindow", "测试本日"))
        self.review_words_button.setText(_translate("MainWindow", "复习单词"))
        self.radom_exam_button.setText(_translate("MainWindow", "随机测试"))
        self.review_Forgotten_button.setText(_translate("MainWindow", "复习遗忘"))
        self.checkBox_voice.setText(_translate("MainWindow", "语音"))
        self.checkBox_random.setText(_translate("MainWindow", "乱序"))
        self.back_exam_main.setText(_translate("MainWindow", "返回"))
        self.progress_label.setText(_translate("MainWindow", "0/0"))
        self.exam_chinese_label.setText(_translate("MainWindow", "chinese"))
        self.part_of_speech_label.setText(_translate("MainWindow", "part_of_speech"))
        self.remove_forget_pushButton.setText(_translate("MainWindow", "移除遗忘"))
        self.forget_pushButton.setText(_translate("MainWindow", "遗忘"))
