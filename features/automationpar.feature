Feature:Automation homepage
  Scenario:Automation homepage enter credentials
    Given Launch the chrome browser
    When Open the homepage
    And Enter name "Sandhyarani" and Enter email "sandha@gmail.com" and phone "8897448076"
    Then Close the browser
