from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://www.linkedin.com/in/rahul-ramesh-86a564325/')
    print('Chrome succesffully opened')
    print(page.title)
    page.wait_for_timeout(5000)