# -*- coding: utf-8 -*-
from pages.main_yandex_page import MainYandexPage
from pages.translate_page import TranslatePage
from common import BaseTest
from config.work_config import Config


class TestClass(BaseTest):
    def test_check_translate(self, driver_transfer, path_before_config):
        file_config = Config(path_before_config)
        url = file_config.get("url")

        driver_transfer.instance.get(url)
        main_yandex_page = MainYandexPage(driver_transfer.instance, path_before_config)
        assert main_yandex_page.check_download_page()
        main_yandex_page.click_tab_translate()

        text_for_translate = "текст для перевода"
        text_for_check_translate = "text for translation"
        delay = file_config.get("wait_in_second")
        translation_page = TranslatePage(driver_transfer.instance, delay)
        assert translation_page.check_download_page()
        translation_page.click_change_direction_translate_button()
        assert translation_page.verification_of_translation(text_for_translate, text_for_check_translate)
