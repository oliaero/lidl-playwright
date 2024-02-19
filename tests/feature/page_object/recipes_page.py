class RecipesPage:
    def __init__(self, driver):
        self.driver = driver

    def all_recipes_are_visible(self):
        self.driver.visibility_of_element_located("heading", "Todas las resetas")