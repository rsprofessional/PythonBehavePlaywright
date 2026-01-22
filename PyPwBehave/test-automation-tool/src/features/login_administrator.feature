Feature: User login on Serverest website as administrator


    Background:
      Given Launch browser acess app

    @allure.label:TMS-456
    Scenario: Demo administrator
      Given User logs in to the application as administrator
      Then Close browsers