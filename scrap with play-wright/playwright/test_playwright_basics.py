
def test_playwright(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context() #To do some operation, login ->
    page = context.new_page()
    page.goto('https://rahulshettyacademy.com')