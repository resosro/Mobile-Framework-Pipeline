import time
import unittest
import os
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy as app
from appium.options.android import UiAutomator2Options

os.environ["ANDROID_HOME"] = "/Users/wil13465/Library/Android/sdk"
os.environ["JAVA_HOME"] = "$(/usr/libexec/java_home)"

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='emulator-5554',
    # appPackage='com.esri.earth.phone',
    # appActivity='.MainActivity',
    language='en',
    locale='US'
)

appium_server_url = 'http://localhost:4723'
capabilities_options = UiAutomator2Options().load_capabilities(capabilities)

class ArcGISEarth(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(command_executor=appium_server_url,options=capabilities_options)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()



    def test_find_gis_earth(self):
        click_app = self.driver.find_element(by=app.XPATH, value="//android.widget.TextView["
                                                                 "@content-desc='ArcGIS Earth']")
        click_app.click()

    def allow_permissions(self):
        time.sleep(2)
        allow_gallery = self.driver.find_element(by=app.ID, value="com.android.permissioncontroller:id/permission_allow_button")
        allow_gallery.click()
        time.sleep(2)
        allow_photo = self.driver.find_element(by=app.ID, value="com.android.permissioncontroller:id/permission_allow_foreground_only_button")
        allow_photo.click()
        time.sleep(2)
        allow_loc = self.driver.find_element(by=app.ID, value="com.android.permissioncontroller:id/permission_allow_foreground_only_button")
        allow_loc.click()
        time.sleep(2)




    # def test_find_battery(self) -> None:


if __name__ == '__main__':
    unittest.main()