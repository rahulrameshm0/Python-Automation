from playwright.sync_api import  sync_playwright

with sync_playwright() as play:
    browser = play.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

    username = page.wait_for_selector('input[name="username"]')
    password = page.wait_for_selector('input[name="password"]')
    button = page.wait_for_selector('button[type="submit"]')
    username.type('Admin')
    password.type('admin123')
    button.click()

    page.wait_for_timeout(15000)
