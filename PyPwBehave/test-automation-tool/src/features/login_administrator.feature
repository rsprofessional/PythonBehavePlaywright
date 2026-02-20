Feature: User login on Serverest website as administrator


    Background:
      Given Launch browser acess app

    @allure.label:TMS-456
    # @smoke
    Scenario Outline: Demo administrator
      Given User logs in to the application as administrator
      When Validate users list and contain <user_mail>
      Then Close browsers

      Examples: users
      | user_mail              | 
      | raul.santos@bee-eng.pt |