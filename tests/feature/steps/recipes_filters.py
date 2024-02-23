from behave import *
from hamcrest import assert_that, is_

from tests.feature.page_object.home_recipes_page import HomeRecipesPage
from tests.feature.page_object.recipes_page import RecipesPage

use_step_matcher("parse")


@given("I am on the Home Recipes page")
def step_impl(context):
    context.home_recipes_page = HomeRecipesPage(context.driver)
    context.home_recipes_page.accept_cookie_banner()


@when('I click "Todas las recetas" on menu bar')
def step_impl(context):
    context.home_recipes_page.click_all_recipes_button()
    context.recipes_page = RecipesPage(context.driver)

@then('I can see "{number_of_recipes}" recipes on the page')
def step_impl(context, number_of_recipes):
    context.driver.expect_number_of_elements_to_be(context.recipes_page.card_css, int(number_of_recipes))

    # assert_that(context.recipes_page.count_number_of_recipes_loaded(), is_(int(number_of_recipes)))


@given("I am on the recipes page")
def step_impl(context):
    context.home_page = HomeRecipesPage(context.driver)
    context.home_recipes_page.accept_cookie_banner()
    context.home_recipes_page.click_all_recipes_button()
    context.recipes_page = RecipesPage(context.driver)


@when('I click "Tipo de plato" in the recipes filter')
def step_impl(context):
    context.recipes_page.click_course_button()

@step('I click "Postres" in dropdown menu')
def step_impl(context):
    context.recipes_page.click_desserts_button()


@then("I can see desserts recipes")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then I can see desserts recipes')