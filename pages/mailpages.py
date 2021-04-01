#!/usr/bin/env python3
# 01apr21 hjltu@ya.ru
# Copyright (c) 2021 hjltu

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


"""
dir(By):
    'CLASS_NAME', 'CSS_SELECTOR', 'ID', 'LINK_TEXT', 'NAME', 'PARTIAL_LINK_TEXT', 'TAG_NAME', 'XPATH'
"""


from time import sleep
from pages.basepage import BasePage
from selenium.webdriver.common.by import By


LOCATOR_LOGIN_BUTTON = (By.CLASS_NAME, "ph-login")
LOCATOR_LOGIN_FRAME = (By.CLASS_NAME, "ag-popup__frame__layout__iframe")
LOCATOR_USERNAME_FIELD = (By.NAME, "username")
LOCATOR_PASSWORD_BUTTON = (By.CLASS_NAME, "base-1-1-86")
LOCATOR_PASSWORD_FIELD = (By.NAME, "password")
LOCATOR_MAIL_SEARCH_BUTTON = (By.CLASS_NAME, "search2__button")
LOCATOR_MAIL_NAVIGATION_BAR = (By.CSS_SELECTOR, ".service__name")


class MainPage(BasePage):

    def open_login_page(self):
        print('Open login page')
        login_button = self.find_element(LOCATOR_LOGIN_BUTTON)
        login_button.click()

    def switch_to_login_frame(self):
        self.driver.switch_to.frame(self.find_element(LOCATOR_LOGIN_FRAME))

    def logging_in(self, username, password):
        print('Logging')
        username_field = self.find_element(LOCATOR_USERNAME_FIELD)
        username_field.send_keys(username)
        sleep(3)
        password_button = self.find_element(LOCATOR_PASSWORD_BUTTON)
        password_button.click()
        password_field = self.find_element(LOCATOR_PASSWORD_FIELD)
        password_field.send_keys(password)
        sleep(3)
        sign_in_button = self.find_element(LOCATOR_PASSWORD_BUTTON)
        sign_in_button.click()
        #return search_field

    def click_on_the_search_button(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_MAIL_SEARCH_BUTTON,time=2).click()

    def check_navigation_bar(self):
        all_list = self.find_elements(YandexSeacrhLocators.LOCATOR_MAIL_NAVIGATION_BAR,time=2)
        nav_bar_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_menu
