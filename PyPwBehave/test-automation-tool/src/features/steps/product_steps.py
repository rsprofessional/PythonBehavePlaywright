from behave import *
from pages.products_page import Products


@Then("Register a product")
def stp_impl(context):
    products = Products(context.page)
    products.register_product()