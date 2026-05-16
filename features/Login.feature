# Created by thoma at 5/11/2026
Feature: Login

  #Scenario: User logs in
  #Given the user is on the Google login page
  #When the user clicks gmail label to go mail page
  #Then the user verifies gmail page
  
  Scenario Outline: Login Jenkins successfully
    Given the user is on the Jenkins login page
    When the user enters <username> and <password>
    And the user clicks login button
    Then the user logins Jenkins successfully

    Examples:
      | username | password |
      | Admin    | 123      |

  Scenario Outline: Login Jenkins failed
    Given the user is on the Jenkins login page
    When the user enters <username> and <password>
    And the user clicks login button
    Then the user logins Jenkins failed

    Examples:
      | username | password |
      | user1    | 123      |
      | user2    | 231      |
      | *_+      | 123      |