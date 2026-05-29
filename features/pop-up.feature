Feature:Autopra alerts pop-up
  Scenario:Check alerts in the pop-up page
    Given Launch the browser11
    When Open the autopra homepage
    And Click on the prompt Alert button
    And Enter name promt "Sandhya"
    And Click on ok button
    Then Verify entered text in pop-up page
    And Close the browser3