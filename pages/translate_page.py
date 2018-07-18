# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TranslatePage:
    _change_direction_translate_button = [By.CSS_SELECTOR, 'div.button.button_icon.button_icon_swap']
    _name_service = [By.CSS_SELECTOR, '#header > div.service > a.name']
    _input_field = [By.CSS_SELECTOR, '#textarea']
    _translated_text_field = (By.CSS_SELECTOR, '#translation')

    def __init__(self, driver, delay):
        self._delay = int(delay)
        self._driver = driver

    def check_download_page(self):
        name_service = self._driver.find_element(*self._name_service)
        text_check_for_dowload_page = 'Переводчик'
        return name_service.text == text_check_for_dowload_page

    def click_change_direction_translate_button(self):
        self._driver.find_element(*self._change_direction_translate_button).click()

    def verification_of_translation(self, input_text, translated_text):
        self._driver.find_element(*self._input_field).send_keys(input_text)
        translated_text_field = self._driver.find_element(*self._translated_text_field)
        WebDriverWait(self._driver, self._delay).until(
            expected_conditions.text_to_be_present_in_element(self._translated_text_field, translated_text))
        return translated_text_field.text == translated_text
