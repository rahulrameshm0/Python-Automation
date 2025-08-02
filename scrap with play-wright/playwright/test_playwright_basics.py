import time

from playwright.sync_api import Page, expect
def test_playwright(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context() #To do some operation, login ->
    page = context.new_page()
    page.goto('https://rahulshettyacademy.com')

def test_playwrightShortcut(page:Page):
    page.goto('https://rahulshettyacademy.com')

def test_coreLocators(page:Page):
    page.goto('https://rahulshettyacademy.com/loginpagePractise/')
    page.get_by_label('Username:').fill('rahulshettyacademy')
    page.get_by_label('Password:').fill('learning')
    page.get_by_role('combobox').select_option('teach')
    page.get_by_role('link',name='terms and conditions').click()
    page.locator('#terms').check()
    page.get_by_role('button', name='Sign In').click()
    expect(page.get_by_text('Incorrect username/password.')).to_be_visible()
    time.sleep(6)
