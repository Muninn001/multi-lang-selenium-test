# multi-lang-selenium-test

Автотест на Selenium, проверяющие корректность отображения элементов (например, кнопки "Добавить в корзину") для разных языковых версий сайта.

Запуск с параметром --language=xx (например, --language=es для испанского).

Как использовать:
1. Установите зависимости:
    ```bash
   pip install -r requirements.txt
2. Запустите тест: 
   ```bash
   pytest --language=es test_items.py