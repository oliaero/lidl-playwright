class RecipesPage:
    def __init__(self, driver):
        self.driver = driver
        self.card_css = ".nuc-o-card"

    # def count_number_of_recipes_loaded(self):
    #     # self.driver.visibility_of_element_located("css", self.card_css)
    #
    #     return len(self.driver.find_elements_by_css("css", self.card_css))



    def click_course_button(self):
        dropdown_selector = self.driver.find_element_by_role("button", name="Tipo de plato")
        dropdown_selector.click()

    def click_desserts_button(self):
        self.driver.click("xpath", '//*[@name="f63ec0ec-82e8-4205-a0d1-cd24c5176197"]/../..')

