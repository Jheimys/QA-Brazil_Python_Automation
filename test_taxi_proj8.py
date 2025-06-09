from selenium import webdriver
import time

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages import UrbanRoutesPage

class TestUrbanRoutes:
    # Inicialize o driver do Chrome uma vez para a classe
    @classmethod
    def setup_class(cls):
        service = Service(ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.maximize_window()

    def test_set_route(self):
        self.driver.get(' https://cnt-1ce26e8b-e991-43b0-a07a-00ded493fb3e.containerhub.tripleten-services.com?lng=pt')
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations('East 2nd Street, 601', '1300 1st St')



    @classmethod
    def teardown_class(cls):
        cls.driver.quit()