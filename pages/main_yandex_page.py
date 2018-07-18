# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from config.work_config import Config


class MainYandexPage:
    _button_search = [By.CSS_SELECTOR, "div.search2__button > button"]
    _translate_tab = [By.CSS_SELECTOR, "div.home-arrow__tabs > div > a:nth-child(6)"]

    def __init__(self, driver, path_before_config):
        file_config = Config(path_before_config)
        self._text_for_check_download = file_config.get("text_for_check_download_start_page")
        self._delay = file_config.get("wait_in_second")
        self._driver = driver

    def check_download_page(self):
        button_search_element = self._driver.find_element(*self._button_search)
        return button_search_element.text == self._text_for_check_download

    def click_tab_translate(self):
        self._driver.find_element(*self._translate_tab).click()

