from behave import *
from pages.common_page import OpenApplication
from typing import cast



@when("Validate the client area page")
def step_validate_the_client_area_page(context):
# Usa o mesmo objeto criado anteriormente (context.app)
    # context.app = OpenApplication()
    app = cast(OpenApplication, context.app)
    app.validate_client_area_page()