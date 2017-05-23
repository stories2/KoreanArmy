from selenium import webdriver

binaryPath = "./files/chromedriverMac"

chromeWebBrowser = webdriver.Chrome(binaryPath)

chromeWebBrowser.get("http://www.naver.com")
chromeWebBrowser.quit()