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


from baseapp import BasePage
from selenium.webdriver.common.by import By


class MailLocators:
    #LOCATOR_MAIL_LOGIN = (By.ID, "text")
    LOCATOR_MAIL_LOGIN_BUTTON = (By.CLASS_NAME, "ph-login")
    LOCATOR_MAIL_SEARCH_BUTTON = (By.CLASS_NAME, "search2__button")
    LOCATOR_MAIL_NAVIGATION_BAR = (By.CSS_SELECTOR, ".service__name")

class MainPage(BasePage):

    def login(self):
        login_button = self.find_element(MailLocators.LOCATOR_MAIL_LOGIN_BUTTON)
        login_button.click()
        #search_field.send_keys(word)
        #return search_field

    def click_on_the_search_button(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_MAIL_SEARCH_BUTTON,time=2).click()

    def check_navigation_bar(self):
        all_list = self.find_elements(YandexSeacrhLocators.LOCATOR_MAIL_NAVIGATION_BAR,time=2)
        nav_bar_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_menu
