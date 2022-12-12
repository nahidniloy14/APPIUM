from appium import webdriver
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
import time

#http://appium.io/docs/en/writing-running-appium/web/hybrid/

desired_caps = {}
desired_caps['platformName'] = 'IOS'
desired_caps['platformVersion'] = '13.2'
desired_caps['deviceName'] = 'iPhone 11 Pro'
desired_caps['autoWebview'] = 'true'
desired_caps['browserName'] = 'safari'
desired_caps['automationName'] = 'XCUITest'
# desired_caps['app'] = ('/Users/sujithreddy/Documents/IOS_APPS/AppiumDemo/AppiumDemoIOS.app')

# 1.) Create driver object
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

# 2.) Explict Wait object
wait = WebDriverWait(driver,25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException,ElementNotSelectableException,NoSuchElementException])

# 3.) Launch URL

driver.get("http://www.dummypoint.com/seleniumtemplate.html")

# 4.) Perform the testing on the URL
time.sleep(2)
ele = wait.until(lambda  x: x.find_element_by_id("user_input"))
ele.click()
ele.send_keys("Code2Lead.com")

ele2 = wait.until(lambda  x: x.find_element_by_id("submitbutton"))
ele2.click()

# 5.) Quite the driver
time.sleep(10)
driver.quit()