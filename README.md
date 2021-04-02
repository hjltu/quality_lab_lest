# quality_lab_test

* Task:
<br>Написать тестовый проект с использованием Python, Selenium и Page object паттерна. Тест должен уметь следующее: залогиниться на mail.ru; написать письмо любого содержания c заполнением поля Body (текста самого письма); отправить письмо. Проверка доставки письма не нужна, только отправка. Тестовый проект вставить как ссылку на GitHub в поле ответа

* Setup:
<br>python3 -m venv venv
<br>source venv/bin/activate
<br>pip install selenium pytest
<br>download geckodriver
<br>Add USERNAME, PASSWORD, RECEIVER in the mailtest.py

* Run:
<br>pytest -s mailtest.py
