from behave import *
from pages.common_page import OpenApplication
from typing import cast

@Given("User logs in to the application as administrator")
def stp_impl(context):
    app = cast(OpenApplication, context.app)
    app.login_ui_administrator()
    
    #podia estar como em baixo  o codigo comentado mapenas nao funciona o crtl+click para saltar para o metodo
    # context.app.login_ui_administrator()

@When("Validate users list and contain {user_mail}")
def stp_impl(context, user_mail):    
    app = cast(OpenApplication, context.app)
    app.validate_lista_usuarios(user_mail)
     






