from behave import *
from pages.common_page import OpenApplication
from pages.excel_page import ReadExcelDinamicaly

data = OpenApplication()
read_products = ReadExcelDinamicaly()

@Given("read data from excel")
def step_impl(context):
    data.read_data_excel()

@Given("read data from excel dinamicaly")
def step_impl(context):
    read_products.read_dinamicaly_products()
   