import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_on_page(browser):
    browser.get(link)
    time.sleep(5)
    btn_is_enab = browser.find_element_by_css_selector(".btn-add-to-basket").is_enabled()
    assert btn_is_enab, "button not found"

