Feature: Google Search with different queries

  Scenario Outline: Search for different terms
    Given I search for "<query>"
    Then I should see "<result>" in the search results

    Examples:
      | query        | result       |
      | Selenium     | Selenium     |
      | Sele    | Sele   |