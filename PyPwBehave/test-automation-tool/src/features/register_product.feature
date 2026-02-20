Feature: User login on Serverest website as administrator and regster a product

    Background:
      Given Launch browser acess app

    @allure.label:TC-01
    @smoke
    Scenario Outline: Register a product
      Given User logs in to the application as administrator
      When Validate users list and contain <user_mail>
      Then Register a product
      Then Close browsers

    Examples: users
    | user_mail              | 
    | raul.santos@bee-eng.pt |  