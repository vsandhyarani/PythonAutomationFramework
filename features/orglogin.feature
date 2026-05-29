Feature:Orangehrm login

  Scenario: Login to orangehrm dashboard page with valid credentials
    Given Launch chrome browser11
    When Open orangehrm homepage
    And Enter valid "Admin" and valid "admin123"
    And Click on login button
    Then Verify user login to the dashboard page

  Scenario: Login to orangehrm dashboard page with invalid credentials
    Given Launch chrome browser12
    When Open orangehrm homepage
    And Enter invalid "Adminxy" and invalid "admin123"
    And Click on login button
    Then Verify user not login to the dashboard page