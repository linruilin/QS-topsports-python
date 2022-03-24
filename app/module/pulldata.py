# -*- coding: utf-8 -*-
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from app.config import STSTEM_TYPE
from app.module.async_call import async_call

# url = "http://hn.topsports.com.cn/phone/DataSour.aspx"
# url = "http://hn.topsports.com.cn/asdf123zxc/phone/DataSour.aspx"
url = "http://hn.topsports.com.cn/asdf123zxc/phone/data/DataSour.aspx"
#    http://hn.topsports.com.cn/asdf123zxc/phone/DataSour.aspx?ID=2&addCode=HN&brandName=Jordan
code = "&addCode=dg"


class pullData:

    def __init__(self):
        self.data = []

    def getData(self, browser):
        self.data = []
        try:
            brandName = Select(browser.find_element_by_id('brandName'))

            x = 0
            for i in brandName.options:
                x += 1
                if i.text == "Jordan":
                    self.data.append({
                        "name": i.text,
                        "data": []
                    })

            print(self.data)
            if x > 1:  # 判断是否有数据
                brandName.select_by_index(x-1)  # 选择第一个选项
                time.sleep(1)
                gmhp = Select(browser.find_element_by_id('gmhp'))  # 主题
                gmhpn = 0
                tx = 0
                for gmhps in gmhp.options:
                    if gmhps.text != "--选择主题--":
                        gmhpn += 1
                        print(gmhps.text)
                        self.data[tx]["data"].append({
                            "name": gmhps.text,
                            "data": []
                        })
                        gmhp.select_by_index(gmhpn)

                        # 店铺
                        time.sleep(1)
                        gmdp = Select(browser.find_element_by_id('gmdp'))
                        gmdpn = 0
                        for gmdps in gmdp.options:
                            print(gmdps.text, "店铺")
                            if gmdps.text != "--选择店铺--":
                                gmdpn += 1
                                self.data[tx]["data"][gmhpn-1]["data"].append({
                                    "name": gmdps.text,
                                    "data": []
                                })
                                gmdp.select_by_index(gmdpn)

                                # 尺码
                                time.sleep(1)
                                xzcm = Select(
                                    browser.find_element_by_id('xzcm'))
                                # xzcmn = 0
                                for xzcms in xzcm.options:
                                    if xzcms.text != "--选择尺码--":
                                        self.data[tx]["data"][gmhpn-1]["data"][gmdpn-1]["data"].append({
                                            "name": xzcms.text,
                                            "data": []
                                        })
                                        # xzcmn += 1

            else:  # 没有数据5秒后刷新
                time.sleep(5)
                browser.refresh()
                self.getData(browser)
        except Exception as e:
            print("读取数据错误:", e)

    @async_call
    def UpdateData2(self, QMessageBox):
        try:
            self.data = []
            # 抓取品牌url
            pinpai = url + "?ID=10" + code
            zhiti = url + "?ID=2" + code + "&brandName="
            dianpu = url + "?ID=5" + code + "&zhuti_id="
            chima = url + "?ID=6" + code + "&zhuti_id="

            # 抓取品牌
            resPinpai = requests.post(
                pinpai, timeout=10)
            resPinpai.encoding = 'utf-8'

            pinpaidata = resPinpai.text.split("^")

            pinpailen = len(pinpaidata)

            x = 0
            for i in pinpaidata:
                x += 1
                # 出现2个品牌
                if pinpailen > 1:
                    pinpais = str(i).split(",")
                    self.data.append({
                        "id": str(pinpais[0]),
                        "name": str(pinpais[1]),
                        "data": []
                    })
                # 只有一个品牌
                else:
                    pinpais = str(i).split(",")
                    self.data.append({
                        "id": str(pinpais[0]),
                        "name": str(pinpais[1]),
                        "data": []
                    })

                # 抓取主题
                zhitii = zhiti + str(pinpais[0])
                resZhuti = requests.post(
                    zhitii, timeout=10)
                resZhuti.encoding = 'utf-8'

                zhutidata = resZhuti.text.split("^")

                y = 0
                for j in zhutidata:
                    y += 1
                    zhutis = str(j).split("‘")
                    print(zhutis, "zhutis")
                    print(zhutis[0], "name")
                    print(zhutis[1], "id")
                    print(self.data[x-1]["data"], "data")

                    self.data[x-1]["data"].append({
                        "id": str(zhutis[1]),
                        "name": str(zhutis[0]),
                        "data": []
                    })

                    # 抓取店铺
                    dianpuj = dianpu + str(zhutis[1])
                    print(dianpu)
                    print(dianpuj)
                    resDianpu = requests.post(
                        dianpuj, timeout=10)
                    resDianpu.encoding = 'utf-8'

                    dianpudata = resDianpu.text.split("^")
                    print(self.data)
                    print(dianpudata, "dianpudata")

                    z = 0
                    for k in dianpudata:
                        z += 1
                        dianpus = str(k).split("‘")
                        self.data[x-1]["data"][y-1]["data"].append({
                            "id": str(dianpus[1]),
                            "name": str(dianpus[0]),
                            "data": []
                        })
                        print(self.data)

                        # 抓取尺码
                        chimak = chima + \
                            str(zhutis[1]) + "&shop_id=" + dianpus[1]
                        print(chima)
                        print(chimak)
                        resChima = requests.post(
                            chimak, timeout=10)
                        resChima.encoding = 'utf-8'

                        chimadata = resChima.text.split("^")

                        for l in chimadata:
                            # chimas = str(l).split("‘")
                            print(l)
                            self.data[x-1]["data"][y-1]["data"][z-1]["data"].append({
                                "id": str(l),
                                "name": str(l),
                                "data": []
                            })

                # print(zhutidata, "zhutidata")
                print(self.data)

            # 抓取店铺

            # 抓取尺码

            # if x > 0:
            #     print(x)
            #     print("存在数据")
            # else:  # 没有数据5秒后刷新
            #     time.sleep(5)
            #     # browser.refresh()
            #     self.UpdateData2()

            # print(resPinpai.text)
            # print(resPinpai.text.split("^"))

            # print(resZhuti.text)
            # print(resZhuti.text.split("^"))

            if x > 0:
                self.updateDataOk()
            else:
                time.sleep(1)
                self.UpdateData2(QMessageBox)

            return self.data
        except Exception as e:
            # browser.quit()
            print("抓取数据错误:", e)

    @async_call
    def UpdateData(self, QMessageBox):  # 抓取数据
        url = "http://hn.topsports.com.cn/phone/qh_xin.html"
        chrome_options = webdriver.ChromeOptions()

        if STSTEM_TYPE == "Windows":
            browser = webdriver.Chrome(
                "./chromedriver.exe", options=chrome_options)
        else:
            browser = webdriver.Chrome(
                "./chromedriver", options=chrome_options)
        try:
            browser.get(url)
            browser.set_window_size(414, 736)
            self.getData(browser)
            browser.quit()
            self.updateDataOk()
            return self.data
        except Exception as e:
            browser.quit()
            print("抓取数据错误:", e)

    def vieRun(self, webnumber, pinpai, zhuti, dianpu, chima):  # 抢购
        try:
            for i in range(webnumber):
                self.openChrome(pinpai, zhuti, dianpu, chima)
                time.sleep(1)
        except Exception as e:
            print("抢购错误:", e)

    @async_call
    def openChrome(self, pinpai, zhuti, dianpu, chima):  # 打开抢购浏览器
        url = "http://hn.topsports.com.cn/phone/qh_xin.html"
        chrome_options = webdriver.ChromeOptions()

        if STSTEM_TYPE == "Windows":
            browser = webdriver.Chrome(
                "./chromedriver.exe", options=chrome_options)
        else:
            browser = webdriver.Chrome(
                "./chromedriver", options=chrome_options)

        try:
            browser.get(url)
            browser.set_window_size(414, 736)

            # 输入身份证
            browser.find_element_by_name("verification").clear()
            browser.find_element_by_name("verification").send_keys(
                self.user[self.userType])
            self.userType += 1
            time.sleep(0.8)

            # 点击验证
            browser.find_element_by_id("tou3").click()
            time.sleep(1)

            # 选择
            Select(browser.find_element_by_id('brandName')
                   ).select_by_visible_text(pinpai)
            time.sleep(1)
            Select(browser.find_element_by_id('gmhp')
                   ).select_by_visible_text(zhuti)
            time.sleep(1)
            Select(browser.find_element_by_id('gmdp')
                   ).select_by_visible_text(dianpu)
            time.sleep(1)
            Select(browser.find_element_by_id('xzcm')
                   ).select_by_visible_text(chima)
            time.sleep(1)

            yanzheng = browser.find_element_by_id("vericontent").text
            yanzhengma = eval(yanzheng.rstrip('='))

            browser.find_element_by_id("Verinum").clear()
            browser.find_element_by_id("Verinum").send_keys(yanzhengma)

            browser.find_element_by_id("quhao").click()
            time.sleep(3)
            browser.quit()
            if self.userType < len(self.user):
                self.openChrome(pinpai, zhuti, dianpu, chima)

        except Exception as e:
            browser.quit()
            print("抢购浏览器错误:", e)
