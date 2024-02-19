from behave import *
from hamcrest import assert_that, is_

from tests.feature.page_object.home_page import HomePage
from tests.feature.page_object.recipes_page import RecipesPage

use_step_matcher("re")


@given("I am on the Home page")
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.accept_cookie_banner()


@when('I click "Todas las recetas" on menu bar')
def step_impl(context):
    context.home_page.click_all_recipes_button()
    context.recipes_page = RecipesPage(context.driver)

@then("I can see recipes on the page")
def step_impl(context):
    assert_that(context.recipes_page.all_recipes_are_visible(), is_(True))

@given("I am on the recipes page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given I am on the recipes page')


@when('I click "Tipo de plato" in the recipes filter')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When I click "Tipo de plato" in the recipes filter')


@step('I click "Postres" in dropdown menu')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And I click "Postres" in dropdown menu')


@then("I can see desserts recipes")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then I can see desserts recipes')