Feature: Use  database querys mysql
  
   #@smoke
  Scenario: Use mysql
    Given Acess database suceffuly
    When Use a select query
    Then Close connection