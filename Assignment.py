import os
import time
import uiautomator2 as d1
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
  
 

driver = d1.connect (addr='emulator-5554')
 

os.system('adb shell am start -n hko.MyObservatory_v1_0/hko.MyObservatory_v1_0.AgreementPage');
time.sleep(1)

#First time enter Agreement 
#driver.click(0.406, 0.544)
#driver.click(0.812, 0.872)
#driver (className='android.widget.ImageButton').click()
#driver.click(0.895, 0.119)
#driver (resourceId='com.android.permissioncontroller:id/permission_allow_foreground_only_button').click()


#open menu
driver (className='android.widget.ImageButton').click()
time.sleep(0.5)


driver.swipe(627,1792, 627, 940)
time.sleep(2)

#open 9-Days forecast page
driver.click(0.329, 0.801)

driver.implicitly_wait(3) 
driver(resourceId='com.geely.pma.climate:id/fragrance_title').exists()


#Screenshot


current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
pfilename = 'C:\\XXXxxx\\pic'
pic_path = pfilename + '\\' + 'screenshot_' + current_time + '.png'
driver.screenshot(pic_path)


#os.system('adb shell screencap -p /sdcard/screenshot.png')


driver.app_stop_all()

