Feature: Acting in Searching page as required

Scenario Outline: User inserts searching text to the searching engine and expects to be succeed
  Given I am redirected on home page
  When  I insert <insert_text> to search bar
  Then  I click on searching_button in search bar
  And   I ensure that <insert_text> is in <element>
  And   I click on <option>
  And   I check if my <option> is selected
  Then  I expect <result> in searching_area for my searching of <insert_text> and <option>
  Examples:
  |insert_text                    |element            |option           |result |
  |Cork International Hotel       |searching_bar      |option_wife      |True   |
  |Jurys Inn Cork                 |searching_bar      |option_wife      |False  |
  |The River Lee                  |searching_bar      |option_spa       |True   |
  |Jurys Inn Cork                 |searching_bar      |option_spa       |False  |

