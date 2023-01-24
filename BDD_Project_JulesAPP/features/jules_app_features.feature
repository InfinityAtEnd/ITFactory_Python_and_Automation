Feature: Testing the homepage on jules.app

  Background:
    Given Home page: I am on jules.app

#    Test 1
#- Open jules.app
#- Input correct email
#- Leave pass empty
#- Verify error ‘Please enter your password!’ is displayed
#- Verify Log in btn is disable
  @Test01
  Scenario:  Check the email and password requirements
    When Home page: I enter the email "correct_mail@gmail.com"
    Then Home page: I check if Enter the password message is displayed
    Then Home page: I check if Log in button is disabled

#    Test 2
#- Base page: implementeaza metoda de verificare url care primeste ca si
#param url-ul paginii
#- Open jules.app
#- Click sign up
#- Verify url folosind metoda din base page: https://jules.app/sign-up
#- Click login
#- Verify url folosind metoda din base page: https://jules.app/sign-in
  @Test02
  Scenario: Check if the user switch between Sign In and Log In
    When Home page: I click on sign up
    Then Signup page: I check if I am on sign up page
    When Signup page: I click on login
    Then Home page: I check if I am on login page

#  Test 3
#- Open jules.app
#- Click sign up
#- Click Persona
#- Click Continue
#- Input correct first name
#- Click Continue
#- Input correct last name
#- Click Continue
#- Input wrong email
#- Verify msg is displayed “Please enter a valid email address.”
#- Clear email input
#- Input correct email
#- Verify that error is not displayed anymore (“Please enter a valid email
#address.”
  @Test03
  Scenario Outline: Check the sign up and log in functionality
    When Home page: I click on sign up
    When Signup page: I click on Personal
    When Signup page: I click continue button
    When Signup page: I type "<name>"
    When Signup page: I click continue button
    When Signup page: I type "<surname>"
    When Signup page: I click continue button
    When Signup page: I type "<email01>"
    Then Signup page: I check for Please enter a valid email address message to be "Shown"
    When Signup page: I clear the email text box
    When Signup page: I type "<email02>"
    Then Signup page: I check for Please enter a valid email address message to be "Hidden"
    Examples:
      | name   | surname   | email01               | email02                        |
      | marian | laurentiu | wrong_email&gmail.com | this_is_a_good_email@gmail.com |