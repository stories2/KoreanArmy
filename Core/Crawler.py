from selenium import webdriver
from Setting import DefineManager

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

    crawledData =[]

    chromeWebBrowser = webdriver.Chrome(DefineManager.CHROME_DEFAULT_BINARY_PATH)
    chromeWebBrowser.get(DefineManager.CRAWL_TARGET_URL)
    noticeList = chromeWebBrowser.find_element_by_xpath('//table//tbody')
    noticeListDatas = noticeList.find_elements_by_xpath("tr")

    for eachNoticeData in noticeListDatas:
        eachNoticeString = eachNoticeData.text
        if eachNoticeString.find(DefineManager.SEARCH_DEFAULT_COUNTRY) != DefineManager.NOT_AVAILABLE \
                and eachNoticeString.find(DefineManager.SEARCH_DEFAULT_KEYWORD) != DefineManager.NOT_AVAILABLE:
            parsedEachNoticeData = GetNoticeParsedData(eachNoticeData)
            crawledData.append(parsedEachNoticeData)
            for indexOfNoticeData in parsedEachNoticeData:
                print indexOfNoticeData
    chromeWebBrowser.quit()
    return crawledData