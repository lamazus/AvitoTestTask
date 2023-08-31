from pages.base_page import BasePage
from pages.locators_constants import AdCardPageLocators

class AdCardPage(BasePage):
    def add_to_favorites(self):
        button = self.browser.find_element(*AdCardPageLocators.FAVORITE_BUTTON)
        if button.get_attribute("data-is-favorite") == "true":
            raise Exception("Объявление уже в Избранном")
        else:
            button.click()
    
    def is_favorite(self):
        button = self.browser.find_element(*AdCardPageLocators.FAVORITE_BUTTON)
        if button.get_attribute("data-is-favorite") == "false":
            return False
        return True
        