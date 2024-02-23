from behave import *
from hamcrest import assert_that, is_, equal_to_ignoring_case
from playwright.sync_api import expect

from tests.feature.page_object.home_page import HomePage
from tests.feature.page_object.profile_page import ProfilePage

use_step_matcher("re")


@given("I am on the Home page")
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.accept_cookie_banner()


@step("I enter to the Login data form")
def step_impl(context):
    context.home_page.hover_login_icon_in_topbar()

@when("I enter valid credentials")
def step_impl(context):
    context.home_page.write_email()
    context.home_page.write_password()



@step("I click on the login button")
def step_impl(context):
    context.home_page.click_login()


@then("I should be redirected to the profile page")
def step_impl(context):
    expect(context.home_page.see_my_data).to_be_visible()


@when("I enter invalid user name")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When I enter invalid user name')


@then("I should see an error message")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then I should see an error message')


@step("I should see a link to go back to the login page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And I should see a link to go back to the login page')


@when("I enter valid user name")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When I enter valid user name')


@step("I enter invalid password")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And I enter invalid password')


