#-*- coding: utf-8 -*-
from selenium import webdriver
import sys

reload(sys)
sys.setdefaultencoding('utf8')

binaryPath = "./files/chromedriverMac"

chromeWebBrowser = webdriver.Chrome(binaryPath)

chromeWebBrowser.get("http://mma.go.kr/board/boardList.do?mc=usr0000053&gesipan_id=16")
noticeList = chromeWebBrowser.find_element_by_xpath('//table//tbody')
noticeListDatas = noticeList.find_elements_by_xpath("tr")
# print noticeListDatas
count = 0
for eachNoticeData in noticeListDatas:
    count += 1
    eachNoticeString = eachNoticeData.text
    if eachNoticeString.find("서울") != -1 and eachNoticeString.find("사회복무요원") != -1:
        print "#", count, eachNoticeString
chromeWebBrowser.quit()