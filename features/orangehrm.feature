Feature:Orangehrm logo
  Scenario:logo presence on orangehrm homepage
    Given launch chrome browser
    When open orangehrm homepage
    Then verify logo present in the orangehrm homepage
    And close the browser