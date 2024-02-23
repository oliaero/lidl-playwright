from playwright.sync_api import sync_playwright

from tests.lib.custom_driver import CustomDriver


def before_all(context):
    context.playwright = sync_playwright().start()

    context.browser = context.playwright.chromium.launch(headless=False, slow_mo=500)
    page = context.browser.new_page()
    context.driver = CustomDriver(context.browser, page)


def after_all(context):
    context.browser.close()
    context.playwright.stop()


