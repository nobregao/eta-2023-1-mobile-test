from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait


class Page:

    def __init__(self, driver=None):
        self.wait_time = 30

        if driver is not None:
            self.driver = driver
        else:
            options = AppiumOptions()
            options.load_capabilities({
                "platformName": "Android",
                "appium:automationName": "UiAutomator2",
                "appium:appPackage": "com.globo.globotv",
                "appium:appActivity": "com.globo.globotv.mainmobile.MainActivity",
                "appium:ensureWebviewsHavePages": True,
                "appium:nativeWebScreenshot": True,
                "appium:newCommandTimeout": 3600,
                "appium:connectHardwareKeyboard": True
            })

            self.driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

    def get_element(self, appium_by, value):
        return WebDriverWait(self.driver, self.wait_time).until(lambda x: x.find_element(by=appium_by, value=value))

    def set_up(self):
        el1 = self.get_element(AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_button")
        el1.click()

        el2 = self.get_element(AppiumBy.ID,
                               "com.android.permissioncontroller:id/permission_allow_foreground_only_button")
        el2.click()

        el3 = self.get_element(AppiumBy.ACCESSIBILITY_ID, "Fechar mensagem")
        el3.click()

        el4 = self.get_element(AppiumBy.ID, "com.globo.globotv:id/native_lgpd_banner_button")

        el4.click()

    def teardown(self):
        self.driver.quit()
