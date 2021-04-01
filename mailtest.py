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
Usage:
    pytest -s mailtest.py
"""


import time
from pages.mailpages import MainPage


USERNAME = 'ql_test'
PASSWORD = '01apr21'


def test_mail_login(browser):
    print('Start Mail login test')
    mail_main_page = MainPage(browser)
    mail_main_page.go_to_site()
    mail_main_page.open_login_page()
    mail_main_page.switch_to_login_frame()
    mail_main_page.logging_in(USERNAME, PASSWORD)
    time.sleep(99)
    #mail_main_page.enter_word("Hello")
    #mail_main_page.click_on_the_search_button()
    #elements = yandex_main_page.check_navigation_bar()
    #assert "Картинки" and "Видео" in elements
