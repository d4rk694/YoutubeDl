# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, sip
import time
import _thread
import os.path

DEBUT = "Début"
FIN = "Fin"

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 96)
        MainWindow.setMinimumSize(QtCore.QSize(500, 96))
        MainWindow.setMaximumSize(QtCore.QSize(500, 96))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("YoutubeDl/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet("background-color:rgb(54, 57, 62);\n"
"color:white;")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_3.setContentsMargins(9, 0, 9, 0)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.le_playlist_link = QtWidgets.QLineEdit(self.page)
        self.le_playlist_link.setObjectName("le_playlist_link")
        self.horizontalLayout_3.addWidget(self.le_playlist_link)
        self.bt_next_step = QtWidgets.QPushButton(self.page)
        self.bt_next_step.setAutoFillBackground(False)
        self.bt_next_step.setStyleSheet("QPushButton {\n"
"    border: 2px;\n"
"    border-radius: 2px;\n"
"    background-color: rgb(91,91,91);\n"
"    color:white;\n"
"    padding:4px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(110,110,110);\n"
"}")
        self.bt_next_step.setObjectName("bt_next_step")
        self.horizontalLayout_3.addWidget(self.bt_next_step)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.rb_music = QtWidgets.QRadioButton(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rb_music.sizePolicy().hasHeightForWidth())
        self.rb_music.setSizePolicy(sizePolicy)
        self.rb_music.setChecked(True)
        self.rb_music.setObjectName("rb_music")
        self.horizontalLayout_2.addWidget(self.rb_music)
        self.rb_video = QtWidgets.QRadioButton(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rb_video.sizePolicy().hasHeightForWidth())
        self.rb_video.setSizePolicy(sizePolicy)
        self.rb_video.setObjectName("rb_video")
        self.horizontalLayout_2.addWidget(self.rb_video)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.label = QtWidgets.QLabel(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.cb_debut = QtWidgets.QComboBox(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_debut.sizePolicy().hasHeightForWidth())
        self.cb_debut.setSizePolicy(sizePolicy)
        self.cb_debut.setStyleSheet("QComboBox {\n"
"    border: 2px;\n"
"    border-radius: 2px;\n"
"    background-color: rgb(91,91,91);\n"
"    color:white;\n"
"    padding:4px;\n"
"}\n"
"")
        self.cb_debut.setObjectName("cb_debut")
        self.horizontalLayout_2.addWidget(self.cb_debut)
        self.label_2 = QtWidgets.QLabel(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.cb_fin = QtWidgets.QComboBox(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_fin.sizePolicy().hasHeightForWidth())
        self.cb_fin.setSizePolicy(sizePolicy)
        self.cb_fin.setStyleSheet("QComboBox {\n"
"    border: 2px;\n"
"    border-radius: 2px;\n"
"    background-color: rgb(91,91,91);\n"
"    color:white;\n"
"    padding:4px;\n"
"}\n"
"")
        self.cb_fin.setObjectName("cb_fin")
        self.horizontalLayout_2.addWidget(self.cb_fin)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.bt_cancel = QtWidgets.QPushButton(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt_cancel.sizePolicy().hasHeightForWidth())
        self.bt_cancel.setSizePolicy(sizePolicy)
        self.bt_cancel.setStyleSheet("QPushButton {\n"
"    border: 2px;\n"
"    border-radius: 2px;\n"
"    background-color: rgb(91,91,91);\n"
"    color:white;\n"
"    padding:4px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(110,110,110);\n"
"}")
        self.bt_cancel.setObjectName("bt_cancel")
        self.horizontalLayout_4.addWidget(self.bt_cancel)
        self.bt_telech = QtWidgets.QPushButton(self.page_2)
        self.bt_telech.setStyleSheet("QPushButton {\n"
"    border: 2px;\n"
"    border-radius: 2px;\n"
"    background-color: rgb(91,91,91);\n"
"    color:white;\n"
"    padding:4px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(110,110,110);\n"
"}")
        self.bt_telech.setObjectName("bt_telech")
        self.horizontalLayout_4.addWidget(self.bt_telech)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.la_current = QtWidgets.QLabel(self.page_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.la_current.sizePolicy().hasHeightForWidth())
        self.la_current.setSizePolicy(sizePolicy)
        self.la_current.setText("")
        self.la_current.setObjectName("la_current")
        self.horizontalLayout_5.addWidget(self.la_current)
        self.la_index = QtWidgets.QLabel(self.page_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.la_index.sizePolicy().hasHeightForWidth())
        self.la_index.setSizePolicy(sizePolicy)
        self.la_index.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.la_index.setText("")
        self.la_index.setObjectName("la_index")
        self.horizontalLayout_5.addWidget(self.la_index)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.pb_dl = QtWidgets.QProgressBar(self.page_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_dl.sizePolicy().hasHeightForWidth())
        self.pb_dl.setSizePolicy(sizePolicy)
        self.pb_dl.setProperty("value", 0)
        self.pb_dl.setObjectName("pb_dl")
        self.verticalLayout_4.addWidget(self.pb_dl)
        self.la_eta = QtWidgets.QLabel(self.page_3)
        self.la_eta.setText("")
        self.la_eta.setObjectName("la_eta")
        self.verticalLayout_4.addWidget(self.la_eta)
        self.stackedWidget.addWidget(self.page_3)
        self.horizontalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
# Personnal Add
        self.bt_next_step.clicked.connect(self.handleButtonFirstStep)
        self.bt_telech.clicked.connect(self.telech)
        self.bt_cancel.clicked.connect(self.cancelStepTwo)
        self.le_playlist_link.returnPressed.connect(self.handleButtonFirstStep)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Youtube Downloader"))
        self.le_playlist_link.setPlaceholderText(_translate("MainWindow", "Entrez ici le lien vers la playlist"))
        self.bt_next_step.setText(_translate("MainWindow", "Etape suivante"))
        self.label_3.setText(_translate("MainWindow", "Some text about the playlist"))
        self.rb_music.setText(_translate("MainWindow", "Musique"))
        self.rb_video.setText(_translate("MainWindow", "Vidéo"))
        self.label.setText(_translate("MainWindow", "De "))
        self.label_2.setText(_translate("MainWindow", " à"))
        self.bt_cancel.setText(_translate("MainWindow", "Annuler"))
        self.bt_telech.setText(_translate("MainWindow", "Télécharger"))



    def handleButtonFirstStep(self):
        link = self.le_playlist_link.displayText()
        # print("Link : " + link)
        import pafy
        try:
            self.playlist = pafy.get_playlist2(link, True, False, False, None)
        except ValueError:
            QtWidgets.QMessageBox.warning(self.main, 'Lien invalide', "Le lien est invalide :\n" + link,
                                          QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)
            return

        # print("The playlist %s contains %d vidéos.\nBy %s" % (playlist.title, len(playlist), playlist.author))
        self.label_3.setText(
            "La playlist %s de %s contient %d vidéos." % (self.playlist.title, self.playlist.author, len(self.playlist)))
        self.cb_debut.addItem(DEBUT)
        for x in range(1, len(self.playlist)):
            self.cb_debut.addItem(str(x + 1))

        self.cb_fin.addItem(FIN)
        for x in range(len(self.playlist), 1, -1):
            self.cb_fin.addItem(str(x - 1))
        self.stackedWidget.setCurrentIndex(1)

    def telech(self):
        # Test correct Combo box, that the user isn't a fucking troll
        debut = self.cb_debut.currentText()
        fin = self.cb_fin.currentText()
        if (debut == DEBUT):
            debut = 1
        if (fin == FIN):
            fin = len(self.playlist)

        if (int(debut) > int(fin)):
            QtWidgets.QMessageBox.critical(self.main, 'Arrête de faire le con',
                                           "Tu vas pas télécharger de " + debut + " à " + fin + "\nY'a pas quelque chose qui cloche la ?",
                                           QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)
            return
        import os
        fileName = QtWidgets.QFileDialog.getExistingDirectory(None, "Open a folder", os.getcwd(),
                                                              QtWidgets.QFileDialog.ShowDirsOnly)
        if fileName:
            self.proceedDl(int(debut),int(fin), fileName)

    def cancelStepTwo(self):
        self.stackedWidget.setCurrentIndex(0)

    def proceedDl(self,start,end, fileName):
        self.stackedWidget.setCurrentIndex(2)
        self.la_current.setText("Récupération des données (cela peut prendre du temps) ...")
        self.la_eta.setText(" ")
        _thread.start_new_thread(self.threaded_Dl, (fileName, start,end, self.rb_video.isChecked()))

    def threaded_Dl(self,fileName, start, end, bothFlux):
        endPrint = end-start+1
        for x in range(start-1,end):
            current = None
            try:

                if(bothFlux):
                    current = self.playlist[x].getbest()
                else:
                    current = self.playlist[x].getbestaudio()
                self.la_index.setText(str(x-start+2) + "/" + str(endPrint))
                title = self.playlist[x].title
                self.la_current.setText(title)
                #qRatio = queue.LifoQueue()
                self.qRatio = 0
                self.saveRatio = 0
                _thread.start_new_thread(self.affichage, ())
                ext = current.extension
                name =str(x + 1) + " - " + title.replace("/", "-").replace("\\", "-") + '.' + ext
                fullPath = os.path.join(fileName, name)
                current.download(filepath=fullPath , quiet=True, callback=self.updateData)
            except Exception as e:
                print("ERROR", e)
                self.la_eta.setText("Erreur lors du téléchargement n°: " + str(x-start+2) + "\nLa vidéo est temporairement bloquée par des droits d'auteur, veuillez réessayer plus tard.")


        self.stackedWidget.setCurrentIndex(0)
        self.le_playlist_link.setText("")

    def updateData(self, total, recvd, ratio, rate, eta):
        # print("Ratio : " + str(ratio))
        self.qRatio = ratio

    def affichage(self):
        val = self.qRatio*100
        #print(val)
        if val >=98:
            return
        if val > self.saveRatio+3:
            self.pb_dl.setValue(val)
            self.saveRatio = val
        time.sleep(3)
        self.affichage()
