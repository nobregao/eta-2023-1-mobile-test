from page.SearchPage import SearchPage


class Teste2:

    def test_ct005_search_title_not_exist(self, home_page):
        title_not_exist = "$$##@@@%%"
        expected_message = "Não foram encontrados resultados para “" + title_not_exist + "”"

        search_page = SearchPage(home_page.driver)
        search_page.click_button_search()

        search_page.fill_input_search(title_not_exist)

        message = search_page.get_message_not_found()

        assert expected_message == message
