from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto('https://www.redbus.in/')

    my_cookies = page.context.cookies()
    print(my_cookies)

    page.context.clear_cookies()

    #To add the new cookies
    new_cookies = {
        'name':'ravi',
        'id':56468498
    }
    #To pass the new cookies
    # page.context.add_cookies([new_cookies])


    #Take screnshot
    page.screenshot(path='redbus.png', full_page=True)
