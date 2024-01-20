from page.SearchPage import SearchPage
from page.TitlePage import TitlePage


class Test1:

    def test_ct001_search_title_exist(self, home_page):
        title_name = "magnum "
        expected_title_name = "Magnum P.I."

        search_page = SearchPage(home_page.driver)
        search_page.click_button_search()

        search_page.fill_input_search(title_name)

        search_page.select_title("(//android.widget.ImageView[@resource-id=\"com.globo.globotv:id/poster_image_view_poster\"])[1]")

        title_page = TitlePage(search_page.driver)
        name = title_page.get_name()

        assert name == expected_title_name
