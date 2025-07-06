from playwright.sync_api import sync_playwright

text_alert = []

def hanadle_dialog(dialog):
    message = dialog.type
    text_alert.append(message)
    dialog.accept('Rahul Ramesh')


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('https://demo.automationtesting.in/Alerts.html')

    page.wait_for_selector('//a[@href="#Textbox"]').click()
    page.wait_for_timeout(2000)

    #alert info

    page.on("dialog", hanadle_dialog)

    page.wait_for_selector('//div[@id="Textbox"]/button').click()
    page.wait_for_timeout(2000)
    print(text_alert[0])
