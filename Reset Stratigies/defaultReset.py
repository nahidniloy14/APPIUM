from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {}

desired_caps['platformName'] = 'Android'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['platformVersion'] = '12'
desired_caps['deviceName'] = 'Redmi Note 9 Pro'
desired_caps['app']= ('C:/Users/lm/PycharmProjects/Appium/Setup Files/ApiDemos-debug.apk')

desired_caps['appPackage'] = 'com.code2lead.kwad'
desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'
#default reset is initialized automaticaly
#Stop and clear app data after test. Do not uninstall apk

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

