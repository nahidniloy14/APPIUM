from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
import time

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '11'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['deviceName'] = 'Pixel'
desired_caps['app'] = ('/Users/sujithreddy/Documents/Code2Lead/others/kwad.apk')
desired_caps['appPackage'] = 'com.code2lead.kwad'
desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

ele = driver.find_element(AppiumBy.ID,"com.code2lead.kwad:id/ScrollView")
ele.click()

ele =driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                          'new UiScrollable(new UiSelector()).scrollIntoView(text("BUTTON12"))')
ele.click()

time.sleep(4)
driver.quit()
