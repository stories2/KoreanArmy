#-*- coding: utf-8 -*-
from selenium import webdriver
from Setting import DefineManager
import sys

def InitParameters():
    DefineManager.PLATFORM_INFO = sys.argv[1]
    DefineManager.SEARCH_DEFAULT_COUNTRY = sys.argv[2]
    DefineManager.SEARCH_DEFAULT_KEYWORD = sys.argv[3]
    print "Input Parameters", DefineManager.PLATFORM_INFO, DefineManager.SEARCH_DEFAULT_COUNTRY, DefineManager.SEARCH_DEFAULT_KEYWORD

def InitProgram():
    if DefineManager.PLATFORM_INFO == "MAC":
        DefineManager.CHROME_DEFAULT_BINARY_PATH = DefineManager.CHROME_MAC_PATH
    elif DefineManager.PLATFORM_INFO == "WINDOWS":
        DefineManager.CHROME_DEFAULT_BINARY_PATH = DefineManager.CHROME_WINDOWS_PATH
    elif DefineManager.PLATFORM_INFO == "LINUX":
        DefineManager.CHROME_LINUX_PATH = DefineManager.CHROME_LINUX_PATH
    else:
        DefineManager.CHROME_DEFAULT_BINARY_PATH = DefineManager.CHROME_MAC_PATH

def GetNoticeParsedData(oneOfSelectedNoticeInfo):
    noticeId = oneOfSelectedNoticeInfo.find_element_by_tag_name("th").text

    noticeDetailData = oneOfSelectedNoticeInfo.find_elements_by_tag_name("td")
    noticeTitle = noticeDetailData[DefineManager.TITLE_SAVED_POINT].text
    noticeRedirectUrl = noticeDetailData[DefineManager.TITLE_SAVED_POINT].find_element_by_tag_name('a').get_attribute('href')
    uploaderName = noticeDetailData[DefineManager.UPLOADER_SAVED_POINT].text
    uploadDate = noticeDetailData[DefineManager.UPLOAD_DATE_SAVED_POINT].text
    noticeShowedNum = noticeDetailData[DefineManager.PAGE_SHOWED_SAVED_POINT].text

    return [noticeId,
            noticeTitle,
            noticeRedirectUrl,
            uploaderName,
            uploadDate,
            noticeShowedNum]

def CrawlArmyNoticeData():

    chromeWebBrowser = webdriver.Chrome(DefineManager.CHROME_DEFAULT_BINARY_PATH)
    chromeWebBrowser.get(DefineManager.CRAWL_TARGET_URL)
    noticeList = chromeWebBrowser.find_element_by_xpath('//table//tbody')
    noticeListDatas = noticeList.find_elements_by_xpath("tr")

    for eachNoticeData in noticeListDatas:
        eachNoticeString = eachNoticeData.text
        if eachNoticeString.find(DefineManager.SEARCH_DEFAULT_COUNTRY) != DefineManager.NOT_AVAILABLE \
                and eachNoticeString.find(DefineManager.SEARCH_DEFAULT_KEYWORD) != DefineManager.NOT_AVAILABLE:
            parsedEachNoticeData = GetNoticeParsedData(eachNoticeData)
            for indexOfNoticeData in parsedEachNoticeData:
                print indexOfNoticeData
    chromeWebBrowser.quit()

reload(sys)
sys.setdefaultencoding('utf8')

InitParameters()
InitProgram()
CrawlArmyNoticeData()

