from behave import *
from pages.auth_basic_page import OpenHerokuapp


@Given("User logs in to herokuapp")
def step_user_navigates_to_application_ui(context):
    print(">>> Antes de todos os testes")
    context.app = OpenHerokuapp()
    context.app.auth_basic_poup()

@Then("Close browsers_auth")
def close_browsers(context):
    print(">>> Depois de todos os testes")
    context.app.close_browser_auth()
    context.app.playwright.stop()