#import asyncio
from behave import  *
from pages.common_page import OpenApplication


@Given("User navigates to the application")
def step_user_navigates_to_application(context):
    context.app = OpenApplication()  # criar a app no context
    print(">>> context.app criado", context.app)
    context.app.launch_browser_and_open_page()




