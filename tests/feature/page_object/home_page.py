class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def accept_cookie_banner(self):
        try:
            self.driver.visibility_of_element_located("css",
                                                    'aria-label:has-text("Antes de continuar: echa un vistazo al tratamiento de tus datos")')

            accept_button = self.driver.find_element_by_role("button", name="Aceptar")
            accept_button.click()
        except TimeoutError:
                print("Cookie banner did not appear. Continue")



    def click_all_recipes_button(self):
        self.driver.find_element('heading', name="Todas las recetas").click()
