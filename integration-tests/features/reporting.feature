Feature: Reporting
    As a Senseyne Health representative
    I want to be able to confirm the clinical performance and safety of the products
    So that I can ensure continued acceptability of risk


  Scenario: Reporting service is running
    Given System is running
    Then the running endpoint returns as expected

  Scenario: Active weekly patient report is generated
    Given a weekly patient report is uploaded
    Then the weekly patient report is available


  Scenario: Daily created patient report is generated
    Given a daily created report is uploaded
    Then the daily created report is available
