from appium.webdriver.common.appiumby import AppiumBy

from tests.page.Page import Page


class PodcastPage(Page):

    def __init__(self, driver):
        super().__init__(driver=driver)

    def click_button_play(self):
        button = self.get_element(AppiumBy.ID, "com.globo.globotv:id/podcast_header_button_action")
        button.click()

    def get_duration(self):
        return self.get_element(AppiumBy.ID, "com.globo.globotv:id/txt_position").text
