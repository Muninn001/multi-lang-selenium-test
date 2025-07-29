from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_item_page_have_add_button(browser):
    browser.get(link)
    button = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    assert button.is_displayed(), "Не отображена кнопка добавления товара"