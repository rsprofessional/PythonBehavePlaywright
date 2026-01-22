from behave import *
from pages.database_page import Database

db = Database()

@Given('Acess database suceffuly')
def step_impl(context):
    db.connect_db()

@When('Use a select query')
def step_impl(context):
    db.read_values()

@Then('Close connection')
def step_impl(context):
    db.close_connection()