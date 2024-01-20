from time import sleep

from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait


class TestMobile:

    def setup(self):
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

        sleep(5)
        el1 = self.driver.find_element(by=AppiumBy.ID,
                                       value="com.android.permissioncontroller:id/permission_allow_button")
        el1.click()

        sleep(2)
        el2 = self.driver.find_element(by=AppiumBy.ID,
                                       value="com.android.permissioncontroller:id/permission_allow_foreground_only_button")
        el2.click()

        sleep(3)
        el3 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Fechar mensagem")
        el3.click()

        wait_time = 20
        el4 = WebDriverWait(self.driver, wait_time).until(lambda x: x.find_element(
                    by=AppiumBy.ID,
                    value="com.globo.globotv:id/native_lgpd_banner_button"))

        el4.click()

    def test_ct001_search_title_exist(self):
        el5 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Busca")
        el5.click()

        el6 = self.driver.find_element(by=AppiumBy.ID, value="com.globo.globotv:id/search_src_text")
        el6.click()
        el6.send_keys("magnum ")

        el7 = self.driver.find_element(by=AppiumBy.XPATH,
                                       value="(//android.widget.ImageView[@resource-id=\"com.globo.globotv:id/poster_image_view_poster\"])[1]")
        el7.click()

        sleep(2)
        title = self.driver.find_element(by=AppiumBy.ID, value="com.globo.globotv:id/title_header_text_view_title")
        year = self.driver.find_element(by=AppiumBy.XPATH,
                                       value="//android.widget.TextView[@resource-id=\"com.globo.globotv:id/tag_text_view_title\" and @text=\"2018\"]")

        assert title.text == "Magnum P.I."
        assert year.text == "2018"

    def test_ct005_search_title_not_exist(self):
        el5 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Busca")
        el5.click()

        title_not_exist = "$$##@@@%%"
        el6 = self.driver.find_element(by=AppiumBy.ID, value="com.globo.globotv:id/search_src_text")
        el6.click()
        el6.send_keys(title_not_exist)

        el7 = self.driver.find_element(by=AppiumBy.ID, value="com.globo.globotv:id/fragment_search_text_view_empty_sate")

        assert el7.text == "Não foram encontrados resultados para “"+title_not_exist+"”"

    def test_ct006_search_by_themes(self):
        el1 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Busca")
        el1.click()

        sleep(2)
        el2 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="ao redor do mundo. botão")
        el2.click()

        el3 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="busca pelo bem-estar. botão")
        el3.click()

        el4 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID,
                                  value="Ver resultados da busca para os temas [ao redor do mundo, busca pelo bem-estar]. botão")
        el4.click()

        el5 = self.driver.find_element(by=AppiumBy.XPATH,
                                  value="(//android.widget.ImageView[@resource-id=\"com.globo.globotv:id/poster_image_view_poster\"])[1]")
        el5.click()

        sleep(3)
        title1 = self.driver.find_element(by=AppiumBy.ID, value="com.globo.globotv:id/title_header_text_view_title")
        assert title1.text == "O Dia Em Que Me Tornei Mais Forte"

        el7 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Navigate up")
        el7.click()

        sleep(2)
        el8 = self.driver.find_element(by=AppiumBy.XPATH,
                                  value="(//android.widget.ImageView[@resource-id=\"com.globo.globotv:id/poster_image_view_poster\"])[2]")
        el8.click()

        sleep(3)
        title2 = self.driver.find_element(by=AppiumBy.ID, value="com.globo.globotv:id/title_header_text_view_title")
        assert title2.text == "O Funcionário Feliz"

    def test_search_and_play_podcast(self):
        el1 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Busca")
        el1.click()

        el2 = self.driver.find_element(by=AppiumBy.ID, value="com.globo.globotv:id/search_src_text")
        el2.click()
        el2.send_keys("projeto humanos ")

        el3 = self.driver.find_element(by=AppiumBy.XPATH,
                                  value="(//android.widget.ImageView[@resource-id=\"com.globo.globotv:id/podcast_poster_image_view_poster\"])[1]")
        el3.click()

        wait_time = 20
        el4 = WebDriverWait(self.driver, wait_time).until(lambda x: x.find_element(
            by=AppiumBy.ID,
            value="com.globo.globotv:id/podcast_header_button_action"))
        el4.click()

        sleep(5)
        duracao = self.driver.find_element(by=AppiumBy.ID, value="com.globo.globotv:id/txt_position")
        assert duracao.text != "00:00"

    def teardown(self):
        self.driver.quit()
