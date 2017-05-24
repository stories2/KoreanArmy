#-*- coding: utf-8 -*-
from Setting import DefineManager
from Core import Crawler, Uploader
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

reload(sys)
sys.setdefaultencoding('utf8')

InitParameters()
InitProgram()
crawledData = Crawler.CrawlArmyNoticeData()
Uploader.UploadDataManager(crawledData)