from selenium.webdriver.common.by import By

def test_check_add_to_cart_button(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    button = browser.find_element(By.CLASS_NAME, 'btn-add-to-basket')
    assert button, "no button found"
    