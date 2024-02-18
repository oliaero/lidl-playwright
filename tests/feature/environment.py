from playwright.sync_api import sync_playwright


def before_all(context):
    with sync_playwright() as p:
        context.browser = p.chromium.launch(headless=False, slow_mo=500)
        context.page = context.browser.new_page()
        context.page.goto("https://recetas.lidl.es/")

def after_all(context):
    context.browser.close()