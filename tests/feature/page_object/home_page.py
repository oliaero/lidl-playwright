from time import sleep

from tests.feature.page_object.profile_page import ProfilePage


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.open("https://www.lidl.es/")

    def accept_cookie_banner(self):
            try:
                # cookie_banner = self.driver.visibility_of_element_located("css",
                #                                         'aria-label:has-text("Antes de continuar: echa un vistazo al tratamiento de tus datos")')
                accept_button = self.driver.find_element_by_role("button", name="Aceptar")
                accept_button.click()
            except TimeoutError:
                print("Cookie banner did not appear. Continue")

    def hover_login_icon_in_topbar(self):
            self.driver.find_element("css", "[class='ua-account overlay-opener-do-link']").hover()

    def write_email(self):
        self.driver.fill_in_the_form("E-mail", "oliaero@gmail.com" )

    def write_password(self):
        self.driver.fill_in_the_form("Contraseña", "Magazin2024?" )

    def click_login(self):
        self.driver.find_element_by_role("button", "Iniciar sesión").click()
        return ProfilePage(self.driver)


    def see_my_data(self):
        sleep(3)
        return self.driver.find_element_by_role("heading", "Mis Pedidos | Mis Devoluciones")






