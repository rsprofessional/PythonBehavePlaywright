from behave import *
from pages.common_page import OpenApplication
from typing import cast


@Then("User logs in to the application")
def step_impl(context):
    # context.app = OpenApplication()
    app = cast(OpenApplication, context.app)
    app.login_ui()