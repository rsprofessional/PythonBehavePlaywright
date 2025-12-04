import asyncio
from behave import *

@Given("User logs in to the application")
def step_login(context):
# Usa o mesmo objeto criado anteriormente (context.app)
    context.app.login_ui()