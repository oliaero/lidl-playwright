# playwright.sync_api import  TimeoutError


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def accept_cookie_banner(self):
        try:

            self.driver.wait_until_visibility_of_element_located("css",'aria-label:has-text("Antes de continuar: echa un vistazo al tratamiento de tus datos")' )

                #.to_be_visible()

            self.page.get_by_role('button', name="Aceptar").click()
            self.driver.find_element("role", "Aceptar", role_type="button")

        except TimeoutError:
                print("Cookie banner did not appear. Continue")

    def click_all_recipes_button(self):
        self.page.get_by_role('heading', name="Todas las recetas").click()

