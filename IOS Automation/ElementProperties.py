from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {}
desired_caps['platformName'] = 'IOS'
desired_caps['platformVersion'] = '13.2'
desired_caps['deviceName'] = 'iPhone 11 Pro'
desired_caps['automationName'] = 'XCUITest'
desired_caps['app'] = ('/Users/sujithreddy/Documents/IOS_APPS/UICatalog.app')

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

element = driver.find_element(AppiumBy.ACCESSIBILITY_ID,("AAPLDatePickerController") )# Accessibility ID


print("Is Displayed : ",element.is_displayed())
print("Is Enabled : ",element.is_enabled())
print("Is selected : ",element.is_selected())
print("Size : ",element.size)
print("Location : ",element.location)
