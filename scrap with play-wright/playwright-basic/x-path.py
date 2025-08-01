from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login') 

    #x-path = //tagname[@atrribute="value"]

    # username = page.wait_for_selector('//input[@name="username"]')
    # username.type('Admin')
    # password = page.wait_for_selector('//input[@name="password"]')
    # password.type('admin123')
    # button = page.wait_for_selector('//button[@type="submit"]')
    # button.click()


    #text - //tagname[text()="text"]
    # page.wait_for_selector('//p[text()="Forgot your password? "]').click()

    #contains - //input[contains(@placeholder, "User")]
    #attributes - //tagname[contains(@attribute, "value")]

    #START-WITH - //tagneme[start-with(@id, 'name')]
    #ENN-WITH - //tagneme[start-with(@id, 'name')]
    #DYNAMIC

    page.wait_for_selector('//label[contains(text(), "User")]').click()
    page.wait_for_timeout(10000)