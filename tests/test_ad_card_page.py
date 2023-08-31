from selenium.common.exceptions import InvalidElementStateException
from pages.ad_card_page import AdCardPage
from pages.favorites_page import FavoritesPage
from pages.routes_constants import RoutesConstants

advert_url = "https://www.avito.ru/nikel/knigi_i_zhurnaly/domain-driven_design_distilled_vaughn_vernon_2639542363"
advert_id = "2639542363"

def test_should_be_add_advert_to_favorite(browser):
    page = AdCardPage(browser, advert_url)
    page.open()
    page.add_to_favorites()
    if page.is_favorite():
        favoritePage = FavoritesPage(browser, RoutesConstants.FAVORITES_PAGE)
        favoritePage.open()
        assert favoritePage.is_advert_in_favorite(advert_id) == True, "Объявление в 'Избранное' отсутствует"
    else:
        raise InvalidElementStateException("Не удалось добавить объявление в избранное")
   
