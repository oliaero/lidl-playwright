from playwright.sync_api import sync_playwright

from tests.lib.custom_driver import CustomDriver


def before_all(context):
    with sync_playwright() as p:
        context.browser = p.chromium.launch(headless=False, slow_mo=500)
        page = context.browser.new_page()
        page.goto("https://recetas.lidl.es/")
        context.driver = CustomDriver(context.browser, page)


def after_all(context):
    context.browser.close()

