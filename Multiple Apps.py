import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '11'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['deviceName'] = 'Pixel'
desired_caps['app'] = ('/Users/sujithreddy/Documents/Code2Lead/Others/kwad.apk')
desired_caps['appPackage'] = 'com.code2lead.kwad'
desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

# Secondary APP
#cmd: dumpsys window windows
driver.start_activity("com.Android.Vending","com.Android.Vending.AssestBrowserActivity")
time.sleep(5)


# Primary APP
driver.start_activity("com.code2lead.kwad","com.code2lead.kwad.MainActivity")
time.sleep(5)

driver.quit()

