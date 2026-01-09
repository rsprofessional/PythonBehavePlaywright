from behave import *
from pages.common_page import OpenApplication



@Given("read data from excel")
def step_impl(context):
    context.data = OpenApplication()
    context.data.read_data_excel()