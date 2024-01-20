from appium.webdriver.common.appiumby import AppiumBy

from tests.page.Page import Page


class SearchPage(Page):

    def __init__(self, driver):
        super().__init__(driver=driver)

    def click_button_search(self):
        button_search = self.get_element(AppiumBy.ACCESSIBILITY_ID, "Busca")
        button_search.click()

    def fill_input_search(self, title_name):
        input_text_search = self.get_element(AppiumBy.ID, "com.globo.globotv:id/search_src_text")
        input_text_search.send_keys(title_name)

    def select_title(self, value):
        poster_image_result = self.get_element(AppiumBy.XPATH, value)
        poster_image_result.click()

    def get_message_not_found(self):
        return self.get_element(AppiumBy.ID, "com.globo.globotv:id/fragment_search_text_view_empty_sate").text

    def select_category(self, category_name):
        category = self.get_element(AppiumBy.ACCESSIBILITY_ID, category_name)
        category.click()

    def click_button_see_result(self):
        button = self.get_element(AppiumBy.ACCESSIBILITY_ID, value="Ver resultados da busca para os temas [ao redor do mundo, busca pelo bem-estar]. botão")
        button.click()
