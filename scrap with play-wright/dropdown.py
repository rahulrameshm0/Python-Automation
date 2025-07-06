from playwright.sync_api import sync_playwright
#SELECT DROPDOWN
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://demo.automationtesting.in/Register.html')

    # Find the dropdown location
    # select_dropdown = page.query_selector('//select[@id="Skills"]')
    
    #Select the dropdown
    # select_dropdown.select_option(label='Art Design')

    page.select_option('//select[@id="Skills"]' ,label='Adobe InDesign')

    page.wait_for_timeout(5000)