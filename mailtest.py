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
from pages.mailpages import MainPage, MailPage


USERNAME = ''
PASSWORD = ''
RECEIVER = ''
MESSAGE = '{} test message'.format(time.strftime("%d%b%y_%H:%M"))


def test_send_mail(browser):

    print('Start Test.Login')
    main_page = MainPage(browser)
    main_page.go_to_site()
    res = main_page.logging_in(USERNAME, PASSWORD)
    assert res is True, 'Can\'t login'

    print('Send Mail')
    mail_page = MailPage(browser)
    res = mail_page.send_mail(RECEIVER, MESSAGE)
    assert res is True, 'Can\'t send email'
    print('End test.Success')
