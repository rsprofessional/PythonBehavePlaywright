from behave import *

from pages.api_testing_page import ApiTesting

ApiTesting = ApiTesting()

@Given('Create a user and validate it')
def step_impl(context):
#     ApiTesting.testing_api_create_user_validate()
#    ApiTesting.testing_api_post()
     ApiTesting.create_user_validate_it()

# @Given("Get Request User")
# def step_impl(context):
#      ApiTesting.testing_api_get()

# @Given('Get Request one User "{user}"')
# def step_impl(context,user):
#      ApiTesting.testing_api_get_one_user_del(user)


# @Then('Delete one user')
# def step_impl(context):
#     ApiTesting.testing_api_del()

@Then('Close api connection_udemy_course')
def step_impl(context):
    ApiTesting.close_api()

@Given("Post Request user")
def step_impl(context):
    ApiTesting.testing_api_post()


