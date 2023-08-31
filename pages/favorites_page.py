from selenium.common.exceptions import NoSuchElementException
from .base_page import BasePage
from selenium.webdriver.common.by import By

class FavoritesPage(BasePage):
    def is_advert_in_favorite(self, id:str):
        try:
            self.browser.find_element(By.XPATH, f"//div[@data-marker='item-{id}']")
        except NoSuchElementException:
            return False
        return True
        
