# Will complete once moved to new apartment
from selenium import webdriver  # pylint: disable=import-error
from variables import *
import time

# Global variable
driver = webdriver.Firefox()


# Calculates my share of rent
def calculateMyRent(rent):
    baseRent = 700
    # Just need to calculate utilities and add those values up. Then can either return that amount or pay it


# Returns the total rent to be paid
def determineRent():
    elemLoaded = False
    timeElapsed = 0
    while not elemLoaded or timeElapsed > 10:
        # Waiting for the page to finish rendering
        try:
            payAmount = driver.find_element_by_xpath(
                '/html/body/div/section/div/div/div[8]/div[1]/div[1]/div[1]/span[2]')
            elemLoaded = True
            return payAmount.text
        except:
            time.sleep(1)
            timeElapsed += 1
            pass

    if (timeElapsed > 10):
        print("The page took too long to render. Try again later")
        exit()


# Logs into the website
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
        calculateMyRent(rent)

    # Close the page
    driver.close()


if __name__ == "__main__":
    main()
