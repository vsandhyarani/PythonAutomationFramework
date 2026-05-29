Feature: autopra dropdown
  Scenario: autopra slect countries from dropdown
    Given Launch the chrome browser1
    When Open autopra homepage
    And Click and select the dropdown icon
    Then Verify user selected the country from dropdown
    And Close the browser2
