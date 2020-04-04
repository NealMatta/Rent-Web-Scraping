from selenium import webdriver
from variables import *
import time

# Global variable
driver = webdriver.Firefox()


def determineRent():
    elemLoaded = False

    while not elemLoaded:
        # Waiting for the page to finish rendering
        try:
            payAmount = driver.find_element_by_xpath(
                '/html/body/div[2]/div/div/div[8]/div[1]/div[1]/div[1]/span[2]')
            elemLoaded = True
            return payAmount.text
        except:
            pass


def login():
    # Grabbing the username and password fields
    inputUsername = driver.find_element_by_xpath('//*[@id="email"]')
    inputPassword = driver.find_element_by_xpath('//*[@id="password"]')

    # Inputing the username and passwords
    inputUsername.send_keys(USERNAME_SECRET)
    inputPassword.send_keys(PASSWORD_SECRET)
    # Submitting the fields
    driver.find_element_by_xpath('//*[@id="submit-button"]').click()


def main():

    driver.get(WEBSITE_URL)
    login()
    rent = determineRent()

    if (rent == '$0.00'):
        print("No rent to pay!")
    else:
        print(rent)

    # Close the page
    driver.close()


if __name__ == "__main__":
    main()
