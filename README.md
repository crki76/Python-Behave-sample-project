# Python Behave sample project
Simple BDD test automation in frameworks: Behave framework, Selenium webdriver, Gherkin, Python(3.4). I used POM 
(page object modelling). Project uses a chromium driver (personally preffered slightly older version)
DOM elements found by using chrome inspector


Navigation in Trivago - REQUIREMENTS
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Automation Code Challenge

Create a set of Selenium Tests in any programming language for the following requirements.

The website http://trivago.com/ have extended their search filters with some new options.

The new options are to filter on hotels with:
Free WiFi
Spa

Write tests to test these new filters.

Test data that can be used for this test includes:

Location: Cork
Dates: One night stay (3 months from today’s date)
Room: Double Room

Results expected:
Select Filter
Hotel Name
Is Listed
Free Wifi
Cork International Hotel
True
Free Wifi
Jurys Inn Cork
False
Spa
The River Lee
True
Spa
Jurys Inn Cork
False

Assume that hotels would be expected in the top results (paging does not need to be considered)

NOTE:
In your solution we are looking for good coding standards/practices for writing automated tests.

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



Dependencies on my .env
selenium
behave
webdriver
selenium
gherkin
parse
nose

Test OUTPUT

/home/crki/git/kneat/miso3/bin/python /home/crki/git/kneat/miso3/bin/behave -D BROWSER=chrome features/test_scenarios/
Feature: Acting in trivago home page. Demonstrating some assertion and scooping methods # features/test_scenarios/home_page.feature:1

  Scenario Outline: User navigates to home page and observes page content -- @1.1   # features/test_scenarios/home_page.feature:8
    Given I am redirected on home page                                              # features/steps/home_page_steps.py:6
    When On page I want to see searching_bar                                        # features/steps/home_page_steps.py:26

  Scenario Outline: User navigates to home page and observes page content -- @1.2   # features/test_scenarios/home_page.feature:9
    Given I am redirected on home page                                              # features/steps/home_page_steps.py:6
    When On page I want to see searching_button                                     # features/steps/home_page_steps.py:26

  Scenario: User navigates to home page and observes Trivago's slogan  # features/test_scenarios/home_page.feature:11
    Given I am redirected on home page                                 # features/steps/home_page_steps.py:6
    When In home page I want to see slogan                             # features/steps/home_page_steps.py:12

  Scenario: User navigates to home page, clicks on search button and is redirected to searching page  # features/test_scenarios/home_page.feature:16
    Given I am redirected on home page                                                                # features/steps/home_page_steps.py:6
    When I click on searching_button in search bar                                                    # features/steps/home_page_steps.py:33
    Then In searching page I want to see searching_filter                                             # features/steps/home_page_steps.py:19

  Scenario: User navigates to home page and wants to see a Trivago slogan  # features/test_scenarios/home_page.feature:22
    Given I am redirected on home page                                     # features/steps/home_page_steps.py:6
    When I want to see Find your ideal hotel|nfor the best price in slogan # features/steps/home_page_steps.py:38

Feature: Acting in Searching page as required # features/test_scenarios/searching_page.feature:1

  Scenario Outline: User inserts searching text to the searching engine and expects to be succeed -- @1.1   # features/test_scenarios/searching_page.feature:13
    Given I am redirected on home page                                                                      # features/steps/home_page_steps.py:6
    When I insert Cork International Hotel to search bar                                                    # features/steps/searching_page_steps.py:6
    Then I click on searching_button in search bar                                                          # features/steps/searching_page_steps.py:19
    And I ensure that Cork International Hotel is in searching_bar                                          # features/steps/searching_page_steps.py:13
    And I click on option_wife                                                                              # features/steps/searching_page_steps.py:24
    And I check if my option_wife is selected                                                               # features/steps/searching_page_steps.py:32
    Then I expect True in searching_area for my searching of Cork International Hotel and option_wife       # features/steps/searching_page_steps.py:40

  Scenario Outline: User inserts searching text to the searching engine and expects to be succeed -- @1.2   # features/test_scenarios/searching_page.feature:14
    Given I am redirected on home page                                                                      # features/steps/home_page_steps.py:6
    When I insert Jurys Inn Cork to search bar                                                              # features/steps/searching_page_steps.py:6
    Then I click on searching_button in search bar                                                          # features/steps/searching_page_steps.py:19
    And I ensure that Jurys Inn Cork is in searching_bar                                                    # features/steps/searching_page_steps.py:13
    And I click on option_wife                                                                              # features/steps/searching_page_steps.py:24
    And I check if my option_wife is selected                                                               # features/steps/searching_page_steps.py:32
    Then I expect False in searching_area for my searching of Jurys Inn Cork and option_wife                # features/steps/searching_page_steps.py:40

  Scenario Outline: User inserts searching text to the searching engine and expects to be succeed -- @1.3   # features/test_scenarios/searching_page.feature:15
    Given I am redirected on home page                                                                      # features/steps/home_page_steps.py:6
    When I insert The River Lee to search bar                                                               # features/steps/searching_page_steps.py:6
    Then I click on searching_button in search bar                                                          # features/steps/searching_page_steps.py:19
    And I ensure that The River Lee is in searching_bar                                                     # features/steps/searching_page_steps.py:13
    And I click on option_spa                                                                               # features/steps/searching_page_steps.py:24
    And I check if my option_spa is selected                                                                # features/steps/searching_page_steps.py:32
    Then I expect True in searching_area for my searching of The River Lee and option_spa                   # features/steps/searching_page_steps.py:40

  Scenario Outline: User inserts searching text to the searching engine and expects to be succeed -- @1.4   # features/test_scenarios/searching_page.feature:16
    Given I am redirected on home page                                                                      # features/steps/home_page_steps.py:6
    When I insert Jurys Inn Cork to search bar                                                              # features/steps/searching_page_steps.py:6
    Then I click on searching_button in search bar                                                          # features/steps/searching_page_steps.py:19
    And I ensure that Jurys Inn Cork is in searching_bar                                                    # features/steps/searching_page_steps.py:13
    And I click on option_spa                                                                               # features/steps/searching_page_steps.py:24
    And I check if my option_spa is selected                                                                # features/steps/searching_page_steps.py:32
    Then I expect False in searching_area for my searching of Jurys Inn Cork and option_spa                 # features/steps/searching_page_steps.py:40

2 features passed, 0 failed, 0 skipped
9 scenarios passed, 0 failed, 0 skipped
39 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m52.643s

Process finished with exit code 0



