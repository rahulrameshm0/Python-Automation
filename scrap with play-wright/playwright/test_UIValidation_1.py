from playwright.sync_api import Page, Playwright, expect
import time

def test_UIValidationDynamicScript(page:Page):

    page.goto('https://rahulshettyacademy.com/loginpagePractise/')
    page.get_by_label('Username:').fill('rahulshettyacademy')
    page.get_by_label('Password:').fill('learning')
    page.get_by_role('combobox').select_option('teach')
    page.locator('#terms').check()
    page.get_by_role('button', name='Sign In').click()

    # Iphone X
    iphone = page.locator('app-card').filter(has_text='iphone X')
    iphone.get_by_role('button').click()

    #Nokia Edge
    nokia_edge = page.locator('app-card').filter(has_text='Nokia Edge')
    nokia_edge.get_by_role('button').click()

    page.get_by_text('Checkout').click()
    expect(page.locator('.media-body')).to_have_count(2)
    time.sleep(6)


def test_childWindowHandle(page : Page):
    page.goto('https://rahulshettyacademy.com/loginpagePractise/')

    with (page.expect_popup() as newPage_info):
        page.locator('.blinkingText').click()
        childPage = newPage_info.value
        text = childPage.locator('.red').text_content()
        print(text)
        words = text.split('at')
        email = words[1].strip().split(" ")[0]

        assert email == 'mentor@rahulshettyacademy.com'
        time.sleep(6)