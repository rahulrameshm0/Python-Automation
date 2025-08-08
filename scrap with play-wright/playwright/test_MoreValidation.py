from playwright.sync_api import Page, expect
import time

# Learning get_by_placeholder
def test_UIChecks(page:Page):
    # hide/display hidden boxes
    page.goto('https://rahulshettyacademy.com/AutomationPractice/')
    expect(page.get_by_placeholder('Hide/Show Example')).to_be_visible()
    page.get_by_role('button', name='Hide').click()
    expect(page.get_by_placeholder('Hide/Show Example')).to_be_hidden()

    # AlertBoxes
    page.on('dialog', lambda dialog: dialog.accept())
    page.get_by_role('button', name='Confirm').click()

    # Frame handling
    page_frame = page.frame_locator('#courses-iframe')
    page_frame.get_by_role('link', name='All Access plan').click()
    expect(page_frame.locator('body')).to_contain_text('All Access Subscription')

    # Check the price of rise is the equal to 37
    # Identify the price column
    # Extract the price of the rice

    page.goto('https://rahulshettyacademy.com/seleniumPractise/#/offers')

    for index in range(page.locator('th').count()):
        if page.locator('th').nth(index).filter(has_text='Price').count()>0:
            price_value = index
            print(f'The price of the rise is {price_value}')
            break

    rice_row = page.locator('tr').filter(has_text='Rice')
    if rice_row == page.locator('td'):
        print(rice_row)
    time.sleep(5)
