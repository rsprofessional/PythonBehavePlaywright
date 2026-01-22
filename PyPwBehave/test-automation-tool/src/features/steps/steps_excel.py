from behave import *
from pages.common_page import OpenApplication

data = OpenApplication()

@Given("read data from excel")
def step_impl(context):
    data.read_data_excel()