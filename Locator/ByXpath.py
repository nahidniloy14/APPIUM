from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['platformVersion'] = '11'
desired_caps['deviceName'] = 'Pixel3XL'
desired_caps['app'] = ('/Users/sujithreddy/Documents/Code2Lead/Others/kwad.apk')
desired_caps['appPackage'] = 'com.code2lead.kwad'
desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
#//tag[@atrbiute='value']
# By using xpath and Content Description
ele_xpath = driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@content-desc="Btn1"]')

#Xpath and text
# ele_xpath = driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@text="ENTER SOME VALUE"]')

# xpath and Index value
# ele_xpath = driver.find_element(AppiumBy.XPATH,'//android.widget.Button[3]')
# ele_xpath.click()

time.sleep(2)
# xpath and Class Name
ele_xpath2 = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText')#tag name not required as it is as same as class name
ele_xpath2.send_keys("Skill2lead.com")

time.sleep(2)

driver.quit()