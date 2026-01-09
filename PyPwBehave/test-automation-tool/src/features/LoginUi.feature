Feature: User login on Serverest website

    Background:
      Given Launch browser acess app

    @smoke
    Scenario:
      Then User logs in to the application
      When Validate the client area page
      Then Close browsers
