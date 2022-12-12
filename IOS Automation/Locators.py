from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'IOS'
desired_caps['platformVersion'] = '13.2'
desired_caps['deviceName'] = 'iPhone 11 Pro'
desired_caps['automationName'] = 'XCUITest'
desired_caps['app'] = ('/Users/sujithreddy/Documents/IOS_APPS/UICatalog.app')

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

# ele = driver.find_element_by_accessibility_id("AAPLDatePickerController") # Accessibility ID
# ele = driver.find_element_by_id("AAPLDatePickerController") # name
# ele = driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="AAPLDatePickerController"]') # Xapth - name
# ele = driver.find_element_by_xpath('//XCUIElementTypeStaticText[@value="AAPLDatePickerController"]') # Xapth - value
#ele = driver.find_element_by_xpath('//XCUIElementTypeStaticText[@label="AAPLDatePickerController"]') # Xapth - Label
#ele.click()