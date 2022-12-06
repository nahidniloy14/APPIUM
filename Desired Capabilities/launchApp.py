from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
#----------desired capabilities-----------
desired_caps = {} #dictionary varibale
#now lets create all the required design capabilities to it
desired_caps['platformName'] = 'Android'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['platformVersion'] = '12'
desired_caps['deviceName'] = 'Redmi Note 9 Pro'
desired_caps['app']= ('C:/Users/lm/PycharmProjects/Appium/Setup Files/ApiDemos-debug.apk')

#----------------webdriver object---------------
#cmd: dumpsys window windows
desired_caps['appPackage'] = 'com.code2lead.kwad'
desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'
# create object for the webdriver class
#establish connection by using port id and local host
#from cmd by typing appium we can get server id
#wd is a webdriver
#http://127.0.0.1---localhost:4723---serverid/wd/hub
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)


#-----------Action on the app-----------------------
ele_id = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue")
ele_id.click()
