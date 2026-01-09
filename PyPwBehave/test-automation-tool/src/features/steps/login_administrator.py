from behave import *


@Given("User logs in to the application as administrator")
def stp_impl(context):
    context.app.login_ui_administrator()







