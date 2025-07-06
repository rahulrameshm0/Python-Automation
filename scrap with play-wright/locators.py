from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('https://demo.automationtesting.in/Index.html')


    email_textbox = page.wait_for_selector('#email')
    email_textbox.type('test@gmail.com')
    button = page.wait_for_selector('#enterimg')
    button.click()
    page.wait_for_timeout(10000)