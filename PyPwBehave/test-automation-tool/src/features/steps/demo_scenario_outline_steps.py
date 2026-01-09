from behave import *
from pages.page_scenario_outline import Demo_scenario

@Given("I put {thing} in a blender")
def step_impl(context, thing):
    context.element = Demo_scenario()
    context.element.writing_elements1(thing)

@When("I switch the blender on")
def step_impl(context):
    pass

@Then("it should transform into {other_thing}")
def step_impl(context, other_thing):
    context.element = Demo_scenario()
    context.element.writing_elements2(other_thing)

