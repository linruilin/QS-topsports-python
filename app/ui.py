# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from app.module.pulldata import pullData
from app.config import USER_TXT, SUCCESS_TXT
from app.module.async_call import async_call


class MainWindow(pullData):
    def __init__(self):
        pullData.__init__(self)
        self.userType = 0
        self.user = []

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(358, 290)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 171, 32))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 50, 181, 16))
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(200, 46, 104, 21))
        self.textEdit.setObjectName("textEdit")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(85, 76, 251, 32))
        self.comboBox.setObjectName("comboBox")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 71, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 116, 71, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 148, 71, 16))
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 210, 114, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 180, 71, 16))
        self.label_5.setObjectName("label_5")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(84, 110, 251, 32))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(85, 142, 251, 32))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(84, 173, 251, 32))
        self.comboBox_4.setObjectName("comboBox_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 358, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.eventUI(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "一键抢号"))
        self.pushButton.setText(_translate("MainWindow", "自动数据抓取30分钟"))
        self.label.setText(_translate("MainWindow", "同时开启抢号数量（默认3个）"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "选择品牌："))
        self.label_3.setText(_translate("MainWindow", "选择主题："))
        self.label_4.setText(_translate("MainWindow", "选择店铺："))
        self.pushButton_2.setText(_translate("MainWindow", "开始抢号"))
        self.label_5.setText(_translate("MainWindow", "选择尺码："))

    def eventUI(self, window):  # 事件绑定
        try:
            self.pushButton.clicked.connect(self.updateData)
            # self.pushButton_2.clicked.connect(self.run)
            self.pushButton_2.clicked.connect(self.run2)
            self.comboBox.currentIndexChanged.connect(self.cb1)
            self.comboBox_2.currentIndexChanged.connect(self.cb2)
            self.comboBox_3.currentIndexChanged.connect(self.cb3)
        except Exception as e:
            print("事件绑定错误:", e)

    def cb1(self, window):
        print(111)
        zhuti = []
        dianpu = []
        chima = []

        pinpain = self.comboBox.currentIndex()
        zhutin = self.comboBox_2.currentIndex()
        dianpun = self.comboBox_3.currentIndex()
        chiman = self.comboBox_4.currentIndex()
        print(pinpain, "pinpain")

        # 主题
        for x in range(int(len(self.data[pinpain]["data"]))):
            zhuti.append(self.data[pinpain]["data"][x]["name"])

        # 店铺
        for y in range(int(len(self.data[pinpain]["data"][zhutin]["data"]))):
            dianpu.append(
                self.data[pinpain]["data"][zhutin]["data"][y]["name"])

        # 尺码
        for j in range(int(len(self.data[pinpain]["data"][zhutin]["data"][dianpun]["data"]))):
            chima.append(
                self.data[pinpain]["data"][zhutin]["data"][dianpun]["data"][j]["name"])

        self.comboBox_4.clear()
        self.comboBox_4.addItems(chima)
        self.comboBox_3.clear()
        self.comboBox_3.addItems(dianpu)
        self.comboBox_2.clear()
        self.comboBox_2.addItems(zhuti)

    def cb2(self, window):
        dianpu = []
        chima = []

        zhutin = self.comboBox_2.currentIndex()
        dianpun = self.comboBox_3.currentIndex()
        chiman = self.comboBox_4.currentIndex()

        # 店铺
        for y in range(int(len(self.data[0]["data"][zhutin]["data"]))):
            dianpu.append(
                self.data[0]["data"][zhutin]["data"][y]["name"])

        # 尺码

        for j in range(int(len(self.data[0]["data"][zhutin]["data"][dianpun]["data"]))):
            chima.append(
                self.data[0]["data"][zhutin]["data"][dianpun]["data"][j]["name"])

        self.comboBox_4.clear()
        self.comboBox_4.addItems(chima)
        self.comboBox_3.clear()
        self.comboBox_3.addItems(dianpu)

    def cb3(self, window):
        dianpu = []
        chima = []

        zhutin = self.comboBox_2.currentIndex()
        dianpun = self.comboBox_3.currentIndex()
        chiman = self.comboBox_4.currentIndex()

        # 尺码
        for j in range(int(len(self.data[0]["data"][zhutin]["data"][dianpun]["data"]))):
            chima.append(
                self.data[0]["data"][zhutin]["data"][dianpun]["data"][j]["name"])

        self.comboBox_4.clear()
        self.comboBox_4.addItems(chima)

    def run(self, window):
        try:
            self.userType = 0
            self.user = []

            file_txt = open(USER_TXT, 'r', encoding='utf8')
            for line in file_txt.readlines():  # 依次读取每行
                line = line.strip()  # 去掉每行头尾空白
                if line != "":
                    self.user.append(line)

            # 关闭文件
            file_txt.close()

            webnumber = int(self.textEdit.toPlainText())
            pinpai = self.comboBox.currentText()
            zhuti = self.comboBox_2.currentText()
            dianpu = self.comboBox_3.currentText()
            chima = self.comboBox_4.currentText()

            # webnumber = 1
            # pinpai = "--选择品牌--"
            # zhuti = "--选择主题--"
            # dianpu = "--选择店铺--"
            # chima = "--选择尺码--"
            self.vieRun(webnumber, pinpai, zhuti, dianpu, chima)
        except Exception as e:
            print("抢购错误:", e)

    @async_call
    def run2(self, window):
        try:
            print("抢购")
            self.userType = 0
            self.user = []

            file_txt = open(USER_TXT, 'r', encoding='utf8')
            for line in file_txt.readlines():  # 依次读取每行
                line = line.strip()  # 去掉每行头尾空白
                if line != "":
                    self.user.append(line)

            # 关闭文件
            file_txt.close()

            webnumber = int(self.textEdit.toPlainText())
            pinpai = self.comboBox.currentText()
            zhuti = self.comboBox_2.currentText()
            dianpu = self.comboBox_3.currentText()
            chima = self.comboBox_4.currentText()

            print(pinpai, zhuti, dianpu, chima)

            pinpaiID = "",
            zhutiID = "",
            dianpuID = "",

            for i in self.data:
                if i["name"] == pinpai:
                    pinpaiID = i["id"]
                    for j in i["data"]:
                        if j["name"] == zhuti:
                            zhutiID = j["id"]
                            for k in j["data"]:
                                if k["name"] == dianpu:
                                    dianpuID = k["id"]

            print(pinpaiID, zhutiID, dianpuID)

            for i in self.user:
                # qianggouUrl = "http://hn.topsports.com.cn/asdf123zxc/phone/DataSour.aspx?ID=8&zhuti=" + \
                #     zhutiID+"&shop_id="+dianpuID+"&man_id="+i+"&size="+chima+"&brandName=NK"
                qianggouUrl = "http://hn.topsports.com.cn/asdf123zxc/phone/data/DataSour.aspx?ID=8&zhuti=" + \
                    zhutiID+"&shop_id="+dianpuID+"&man_id="+i+"&size="+chima+"&brandName=dg"

                # "referer": "http://hn.topsports.com.cn/asdf123zxc/phone/qh_xin.html?area_code=HN"
                headers = {
                    "host": "hn.topsports.com.cn",
                    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
                    "origin": "http://hn.topsports.com.cn",
                    "referer": "http://hn.topsports.com.cn/asdf123zxc/phone/qh_xin.html?area_code=dg"
                }

                resQianghao = requests.post(
                    qianggouUrl, timeout=10, headers=headers)
                resQianghao.encoding = 'utf-8'

                print(resQianghao.text, "resQianghao", qianggouUrl)
                reqqianghao = resQianghao.text.split("‘")

                # 抢号成功
                if len(reqqianghao) > 3:
                    # if len(reqqianghao) == 1:
                    file_txt = open(SUCCESS_TXT, mode='a', encoding='utf8')
                    file_txt.write(i)
                    file_txt.write("\n")
                    # 关闭文件
                    file_txt.close()

        except Exception as e:
            print("抢购错误:", e)

    def updateData(self, window):  # 抓取数据
        try:
            self.data = []
            # self.UpdateData(QMessageBox)
            self.UpdateData2(QMessageBox)
            # [{'name': '--选择品牌--', 'data': [{'name': '--选择主题--', 'data': [{'name': '--选择店铺--', 'data': [{'name': '--选择尺码--', 'data': []}]}]}]}]
        except Exception as e:
            print("抓取数据错误:", e)

    def updateDataOk(self):
        try:

            # self.data = [{'id': 'NK', 'name': 'Jordan', 'data': [{'id': '102019080701', 'name': 'Air Jordan 3 Tinker “Black Cement”', 'data': [{'id': 'NKSZ49', 'name': '深圳东门新安店NK', 'data': [{'id': '7', 'name': '7', 'data': []}, {'id': '7.5', 'name': '7.5', 'data': []}, {'id': '8', 'name': '8', 'data': []}, {'id': '8.5', 'name': '8.5', 'data': []}, {'id': '9', 'name': '9', 'data': []}, {'id': '9.5', 'name': '9.5', 'data': []}, {'id': '10', 'name': '10', 'data': []}, {'id': '10.5', 'name': '10.5', 'data': []}, {'id': '11', 'name': '11', 'data': []}]}, {'id': 'NKSZ94', 'name': '深圳南山万象天地店JD', 'data': [{'id': '7', 'name': '7', 'data': []}, {'id': '7.5', 'name': '7.5', 'data': []}, {'id': '8', 'name': '8', 'data': []}, {'id': '8.5', 'name': '8.5', 'data': []}, {'id': '9', 'name': '9', 'data': []}, {'id': '9.5', 'name': '9.5', 'data': []}, {'id': '10', 'name': '10', 'data': []}, {'id': '10.5', 'name': '10.5', 'data': []}, {'id': '11', 'name': '11', 'data': []}, {'id': '12', 'name': '12', 'data': []}]}, {'id': 'NKSZBN', 'name': '深圳罗湖金光华广场乔丹JD', 'data': [{'id': '7', 'name': '7', 'data': []}, {'id': '7.5', 'name': '7.5', 'data': []}, {'id': '8', 'name': '8', 'data': []}, {'id': '8.5', 'name': '8.5', 'data': []}, {'id': '9', 'name': '9', 'data': []}, {'id': '9.5', 'name': '9.5', 'data': []}, {'id': '10', 'name': '10', 'data': []}, {'id': '10.5', 'name': '10.5', 'data': []}, {'id': '11', 'name': '11', 'data': []}]}, {'id': 'NKSZBP', 'name': '深圳南山海岸城BEC', 'data': [{'id': '7.5', 'name': '7.5', 'data': []}, {'id': '8', 'name': '8', 'data': []}, {'id': '8.5', 'name': '8.5', 'data': []}, {'id': '9', 'name': '9', 'data': []}, {'id': '9.5', 'name': '9.5', 'data': []}, {'id': '10', 'name': '10', 'data': []}, {'id': '10.5', 'name': '10.5', 'data': []}, {'id': '11', 'name': '11', 'data': []}]}, {'id': 'NKSZUO', 'name': '深圳罗湖宝安南路华润万象城BEC', 'data': [{'id': '7.5', 'name': '7.5', 'data': []}, {'id': '8', 'name': '8', 'data': []}, {'id': '8.5', 'name': '8.5', 'data': []}, {'id': '9', 'name': '9', 'data': []}, {'id': '9.5', 'name': '9.5', 'data': []}, {'id': '10', 'name': '10', 'data': []}, {'id': '10.5', 'name': '10.5', 'data': []}, {'id': '11', 'name': '11', 'data': []}]}, {'id': 'NKSZBT', 'name': '深圳福田华强茂业KL', 'data': [{'id': '7.5', 'name': '7.5', 'data': []}, {'id': '8', 'name': '8', 'data': []}, {'id': '8.5', 'name': '8.5', 'data': []}, {'id': '9', 'name': '9', 'data': []}, {'id': '9.5', 'name': '9.5', 'data': []}, {'id': '10', 'name': '10', 'data': []}, {'id': '10.5', 'name': '10.5', 'data': []}, {'id': '13', 'name': '13', 'data': []}]}]}]},
            #              {'id': 'NK', 'name': 'NK', 'data': [{'id': '102019080701', 'name': 'Air Jordan 4 Tinker “Black Cement”', 'data': [{'id': 'NKSZ49', 'name': '深圳东门新安店NK2', 'data': [{'id': '7', 'name': '7222', 'data': []}, {'id': '7.5', 'name': '7.5', 'data': []}, {'id': '8', 'name': '8', 'data': []}, {'id': '8.5', 'name': '8.5', 'data': []}, {'id': '9', 'name': '9', 'data': []}, {'id': '9.5', 'name': '9.5', 'data': []}, {'id': '10', 'name': '10', 'data': []}, {'id': '10.5', 'name': '10.5', 'data': []}, {'id': '11', 'name': '11', 'data': []}]}, {'id': 'NKSZ94', 'name': '深圳南山万象天地店JD', 'data': [{'id': '7', 'name': '7', 'data': []}, {'id': '7.5', 'name': '7.5', 'data': []}, {'id': '8', 'name': '8', 'data': []}, {'id': '8.5', 'name': '8.5', 'data': []}, {'id': '9', 'name': '9', 'data': []}, {'id': '9.5', 'name': '9.5', 'data': []}, {'id': '10', 'name': '10', 'data': []}, {'id': '10.5', 'name': '10.5', 'data': []}, {'id': '11', 'name': '11', 'data': []}, {'id': '12', 'name': '12', 'data': []}]}, {'id': 'NKSZBN', 'name': '深圳罗湖金光华广场乔丹JD', 'data': [{'id': '7', 'name': '7', 'data': []}, {'id': '7.5', 'name': '7.5', 'data': []}, {'id': '8', 'name': '8', 'data': []}, {'id': '8.5', 'name': '8.5', 'data': []}, {'id': '9', 'name': '9', 'data': []}, {'id': '9.5', 'name': '9.5', 'data': []}, {'id': '10', 'name': '10', 'data': []}, {'id': '10.5', 'name': '10.5', 'data': []}, {'id': '11', 'name': '11', 'data': []}]}, {'id': 'NKSZBP', 'name': '深圳南山海岸城BEC', 'data': [{'id': '7.5', 'name': '7.5', 'data': []}, {'id': '8', 'name': '8', 'data': []}, {'id': '8.5', 'name': '8.5', 'data': []}, {'id': '9', 'name': '9', 'data': []}, {'id': '9.5', 'name': '9.5', 'data': []}, {'id': '10', 'name': '10', 'data': []}, {'id': '10.5', 'name': '10.5', 'data': []}, {'id': '11', 'name': '11', 'data': []}]}, {'id': 'NKSZUO', 'name': '深圳罗湖宝安南路华润万象城BEC', 'data': [{'id': '7.5', 'name': '7.5', 'data': []}, {'id': '8', 'name': '8', 'data': []}, {'id': '8.5', 'name': '8.5', 'data': []}, {'id': '9', 'name': '9', 'data': []}, {'id': '9.5', 'name': '9.5', 'data': []}, {'id': '10', 'name': '10', 'data': []}, {'id': '10.5', 'name': '10.5', 'data': []}, {'id': '11', 'name': '11', 'data': []}]}, {'id': 'NKSZBT', 'name': '深圳福田华强茂业KL', 'data': [{'id': '7.5', 'name': '7.5', 'data': []}, {'id': '8', 'name': '8', 'data': []}, {'id': '8.5', 'name': '8.5', 'data': []}, {'id': '9', 'name': '9', 'data': []}, {'id': '9.5', 'name': '9.5', 'data': []}, {'id': '10', 'name': '10', 'data': []}, {'id': '10.5', 'name': '10.5', 'data': []}, {'id': '13', 'name': '13', 'data': []}]}]}]}]
            # QMessageBox.information(
            #     self.centralwidget, '抓取数据', '抓取数据成功', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            
            
            # DG数据
            # [{'id': 'NK', 'name': 'DGNK', 'data': [{'id': '102019090701', 'name': 'AIR JORDAN XIII "LAKERS"', 'data': [{'id': 'NKDG38', 'name': '东莞南城海德广场Total Hoops', 'data': [{'id': '7.5', 'name': '7.5', 'data': []}, {'id': '8', 'name': '8', 'data': []}, {'id': '8.5', 'name': '8.5', 'data': []}, {'id': '9', 'name': '9', 'data': []}, {'id': '9.5', 'name': '9.5', 'data': []}, {'id': '10', 'name': '10', 'data': []}, {'id': '10.5', 'name': '10.5', 'data': []}, {'id': '11', 'name': '11', 'data': []}]}]}]}]
            # [{'id': 'NK', 'name': 'DGNK', 'data': [{'id': '102019090701', 'name': 'AIR JORDAN XIII "LAKERS"', 'data': [{'id': 'NKDG38', 'name': '东莞南城海德广场Total Hoops', 'data': [{'id': '7.5', 'name': '7.5', 'data': []}, {'id': '8', 'name': '8', 'data': []}, {'id': '8.5', 'name': '8.5', 'data': []}, {'id': '9', 'name': '9', 'data': []}, {'id': '9.5', 'name': '9.5', 'data': []}, {'id': '10', 'name': '10', 'data': []}, {'id': '10.5', 'name': '10.5', 'data': []}, {'id': '11', 'name': '11', 'data': []}]}]}]}]
            pinpai = []
            zhiti = []
            dianpu = []
            chima = []
            print(self.data,"data")

            for i in range(int(len(self.data))):
                print(i, self.data[i]["name"])
                pinpai.append(self.data[i]["name"])

            # 主题
            for x in range(int(len(self.data[0]["data"]))):
                zhiti.append(self.data[0]["data"][x]["name"])

            # 店铺
            for y in range(int(len(self.data[0]["data"][0]["data"]))):
                dianpu.append(
                    self.data[0]["data"][0]["data"][y]["name"])

            # 尺码
            for j in range(int(len(self.data[0]["data"][0]["data"][0]["data"]))):
                chima.append(
                    self.data[0]["data"][0]["data"][0]["data"][j]["name"])

            self.comboBox_4.addItems(chima)
            self.comboBox_3.addItems(dianpu)
            self.comboBox_2.addItems(zhiti)
            self.comboBox.addItems(pinpai)

        except Exception as e:
            print("抓取数据成功错误:", e)
