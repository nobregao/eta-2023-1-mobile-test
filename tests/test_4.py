from time import sleep

from page.PodcastPage import PodcastPage
from page.SearchPage import SearchPage


class Test4:

    def test_search_and_play_podcast(self, home_page):

        podcast_name_search = "projeto humanos "
        initial_time = "00:00"

        search_page = SearchPage(home_page.driver)
        search_page.click_button_search()

        search_page.fill_input_search(podcast_name_search)

        search_page.select_title("(//android.widget.ImageView[@resource-id=\"com.globo.globotv:id/podcast_poster_image_view_poster\"])[1]")

        podcast_page = PodcastPage(search_page.driver)
        podcast_page.click_button_play()

        sleep(5)
        duration = podcast_page.get_duration()
        assert duration != initial_time
