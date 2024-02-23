from playwright.sync_api import expect


class ProfilePage:
    def __init__(self, driver):
        self.driver = driver

    # def see_my_data(self):
    #     my_orders_heading = self.driver.find_element_by_role("heading", "Mis Pedidos | Mis Devoluciones")
    #     expect(my_orders_heading).to_be_visible()
    #
    # def wait_until_loaded(self):
    #     self.driver.wait_until_loaded()







