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
https://selenium-python.readthedocs.io/api.html
"""


from time import sleep
from pages.basepage import BasePage
from selenium.webdriver.common.by import By


LOCATOR_USERNAME_FIELD = (By.NAME, "login")
LOCATOR_PASSWORD_BUTTON = (By.CLASS_NAME, "button")
LOCATOR_PASSWORD_FIELD = (By.NAME, "password")
LOCATOR_ENTER_BUTTON = (By.CLASS_NAME, "second-button")

MAIL_PAGE_URL = 'https://e.mail.ru/inbox/'
LOCATOR_COMPOSE_BUTTON = (By.CLASS_NAME, 'compose-button__txt')
LOCATOR_RECEIVER_FIELD = (By.XPATH, '//div[@data-type="to"]/div/div/label/div/div/input')
LOCATOR_MESSAGE_FIELD = (By.CLASS_NAME, 'cke_editable_inline')
LOCATOR_SEND_BUTTON = (By.CLASS_NAME, 'button2_primary')


class MainPage(BasePage):

    def logging_in(self, username, password):
        print('Logging')
        username_field = self.find_element(LOCATOR_USERNAME_FIELD)
        username_field.send_keys(username)
        sleep(1)
        password_button = self.find_element(LOCATOR_PASSWORD_BUTTON)
        password_button.click()
        password_field = self.find_element(LOCATOR_PASSWORD_FIELD)
        password_field.send_keys(password)
        sleep(1)
        sign_in_button = self.find_element(LOCATOR_ENTER_BUTTON)
        sign_in_button.click()
        current_url = self.driver.current_url
        print('current url:', current_url)
        return True


class MailPage(BasePage):

    def send_mail(self, receiver, message):
        self.driver.get(MAIL_PAGE_URL)
        current_url = self.driver.current_url
        print('current url:', current_url)
        compose_button = self.find_element(LOCATOR_COMPOSE_BUTTON)
        compose_button.click()
        receiver_field = self.find_element(LOCATOR_RECEIVER_FIELD)
        receiver_field.send_keys(receiver)
        message_field = self.find_element(LOCATOR_MESSAGE_FIELD)
        message_field.send_keys(message)
        send_button = self.find_element(LOCATOR_SEND_BUTTON)
        send_button.click()
        return True

