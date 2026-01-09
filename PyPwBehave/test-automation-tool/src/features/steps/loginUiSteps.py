import asyncio
from behave import *

@Then("User logs in to the application")
def step_impl(context):
    context.app.login_ui()