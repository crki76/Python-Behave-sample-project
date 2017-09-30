Feature: Acting in trivago home page. Demonstrating some assertion and scooping methods

  Scenario Outline: User navigates to home page and observes page content
    Given I am redirected on home page
    When On page I want to see <element>
    Examples:
    |element          |
    |searching_bar    |
    |searching_button |

  Scenario: User navigates to home page and observes Trivago's slogan
    Given I am redirected on home page
    When In home page I want to see slogan


  Scenario: User navigates to home page, clicks on search button and is redirected to searching page
    Given I am redirected on home page
    When I click on searching_button in search bar
    Then In searching page I want to see searching_filter

# I use a regex for assertion as text was mark in the middle with end of the line special char
  Scenario: User navigates to home page and wants to see a Trivago slogan
    Given I am redirected on home page
    When I want to see Find your ideal hotel|nfor the best price in slogan





