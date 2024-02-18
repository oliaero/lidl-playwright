from behave import *

from tests.feature.page_object.home_page import HomePage

use_step_matcher("re")


@given("I am on the Home page")
def step_impl(context):
    context.home_page = HomePage(context.browser)
    context.home_page.accept_cookie_banner()


@when('I click "Todas las recetas" on menu bar')
def step_impl(context):
    context.home_page.click_all_recipes_button()
    context.recipes_page = RecipesPage(context.driver)

@then("I can see recipes on the page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then I can see recipes on the page')


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