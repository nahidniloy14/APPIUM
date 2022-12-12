# go to settings of mobile phone >> developer options >> enable pointer location
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
import time

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '11'
desired_caps['deviceName'] = 'Pixel'
desired_caps['app'] = ('/Users/sujithreddy/Documents/Code2Lead/Others/kwad.apk')
desired_caps['appPackage'] = 'com.code2lead.kwad'
desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)



ele = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                          'new UiScrollable(new UiSelector()).scrollIntoView(text("LOGIN"))')

actions = TouchAction(driver)
#actions.tap(webelement,x co-ordinate,y co-ordinate,count)

#without web elements
# actions.tap(None,700,1990,1)

#with web elements
actions.tap(ele, 940, 2400, 1)

actions.perform()

time.sleep(2)
driver.quit()

