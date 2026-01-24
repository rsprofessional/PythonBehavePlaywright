from behave import *


@Given('we have behave installed')
def step_impl(context):
    pass

@When('we implement a test')
def step_impl(context):
    assert True is not False

@Then('behave will test it for us!')
def step_impl(context):
    assert context.failed is True