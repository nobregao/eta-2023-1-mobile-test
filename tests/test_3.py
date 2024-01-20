from page.SearchPage import SearchPage
from page.TitlePage import TitlePage


class Test3:

    def test_ct006_search_by_themes(self, home_page):

        category_one = "ao redor do mundo. botão"
        category_second = "busca pelo bem-estar. botão"

        expected_title_name_first = "O Dia Em Que Me Tornei Mais Forte"
        expected_title_name_second = "O Funcionário Feliz"

        search_page = SearchPage(home_page.driver)
        search_page.click_button_search()

        search_page.select_category(category_one)
        search_page.select_category(category_second)

        search_page.click_button_see_result()

        search_page.select_title("(//android.widget.ImageView[@resource-id=\"com.globo.globotv:id/poster_image_view_poster\"])[1]")

        title_page_first = TitlePage(search_page.driver)
        assert title_page_first.get_name() == expected_title_name_first

        title_page_first.click_button_back()

        search_page.select_title("(//android.widget.ImageView[@resource-id=\"com.globo.globotv:id/poster_image_view_poster\"])[2]")

        title_page_second = TitlePage(search_page.driver)
        assert title_page_second.get_name() == expected_title_name_second