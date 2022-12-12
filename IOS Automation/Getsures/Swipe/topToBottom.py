import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'IOS'
desired_caps['platformVersion'] = '13.2'
desired_caps['deviceName'] = 'iPhone 11 Pro'
desired_caps['automationName'] = 'XCUITest'
desired_caps['app'] = ('/Users/sujithreddy/Documents/IOS_APPS/UICatalog.app')

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

wait = WebDriverWait(driver, 25, poll_frequency=1,
                     ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                         NoSuchElementException])

ele = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'text("ScrollView")'))
ele.click()

print("Device Width and Height : ", driver.get_window_size())
# out of print statement is :Device Width and Height :  {'width': 1440, 'height': 2621}
deviceSize = driver.get_window_size()
screenWidth = deviceSize['width']
screenHeight = deviceSize['height']


###### Swipe from Top to Bottom #######
startx2 = screenWidth / 2
endx2 = screenWidth / 2
starty2 = screenHeight * 2 / 9 #20% to avoid notification panel and 90% as 10% is taken by the buttons and menu
endy2 = screenHeight * 8 / 9

actions = TouchAction(driver)
time.sleep(2)
actions.long_press(None, startx2, starty2).move_to(None, endx2, endy2).release().perform()