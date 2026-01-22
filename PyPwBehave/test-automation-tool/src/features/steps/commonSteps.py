from behave import *
from pages.common_page import OpenApplication
from  elementsPage.general_variables import *

@Given("Launch browser acess app")
def step_user_navigates_to_application_ui(context):
    print(">>> Antes de todos os testes")
    context.app = OpenApplication()
    context.app.launch_browser_and_open_page()


@When('Validate home page app')
def step_validate_home_app(context):
    context.app.validate_home_page_app()

@Then("Close browsers")
def close_browsers(context):
    print(">>> Depois de todos os testes")
    # Stop tracing and export it into a zip archive.
    context.app.close_browser()
    context.app.playwright.stop()

@Then("Close api connection")
def close_api_all(context):
    print(">>> Fechar api connection")
    context.api = OpenApplication()
    context.api.close_api_all()

@Then("User logs in to the application via API")
def step_login_api(context):
      context.api = OpenApplication()
      context.api_test_req()
     # context.api.test_api()