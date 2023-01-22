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