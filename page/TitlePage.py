from appium.webdriver.common.appiumby import AppiumBy

from tests.page.Page import Page


class TitlePage(Page):

    def __init__(self, driver):
        super().__init__(driver=driver)

    def get_name(self):
        return self.get_element(AppiumBy.ID, "com.globo.globotv:id/title_header_text_view_title").text

    def click_button_back(self):
        button = self.get_element(AppiumBy.ACCESSIBILITY_ID, "Navigate up")
        button.click()
