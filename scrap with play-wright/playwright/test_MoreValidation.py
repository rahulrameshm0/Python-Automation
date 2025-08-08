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

    time.sleep(5)

    # Frame handling
