from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('https://demo.automationtesting.in/Register.html')

    radio_button = page.query_selector('//input[@value="Male"]')
    radio_button.check()
    if radio_button.is_checked():
        print('passed')
    else:
        print('radio button failed')

    checkbox_button = page.query_selector_all('//input[@value="Cricket"] | //input[@value="Movies"]')
    for checkbox in checkbox_button:
        checkbox.check()

    if checkbox.is_checked():
        print('passed')

    else:
        print('checkbox button failed')
    page.wait_for_timeout(2000)
