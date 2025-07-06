from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto('https://demo.automationtesting.in/Selectable.html')
    
    #MOUSE ACTION

    #Hover
    page.wait_for_selector('//a[text()="SwitchTo"]').hover()
    
    #click
    page.wait_for_selector('//a[text()="SwitchTo"]').click()
    
    #double click
    page.wait_for_selector('//a[text()="SwitchTo"]').dblclick()
    
    #right click
    page.wait_for_selector('//a[text()="SwitchTo"]').click(button='right')

    #shift
    page.wait_for_selector('//a[text()="SwitchTo"]').click(modifiers=['shift'])

    page.wait_for_timeout(2000)

    #KEYBOARD OPTION
    page.wait_for_selector('//a[text()="SwitchTo"]').press('$')
