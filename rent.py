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
    homePageLoaded = False
    paymentPageLoaded = False
    timeElapsed = 0

    # Directing to payment page
    while not homePageLoaded or timeElapsed > 10:
        try:
            driver.find_element_by_xpath(
                '//*[@id="paymentsaspx_MenuLink"]').click()
            homePageLoaded = True
            timeElapsed = 0

        except:
            time.sleep(1)
            timeElapsed += 1
            pass

    if (timeElapsed > 10):
        print("The home page took too long to render. Try again later")
        exit()

    # Grabbing the amount due
    while not paymentPageLoaded or timeElapsed > 10:
        try:
            payAmount = driver.find_element_by_xpath(
                '//*[@id="PP2MakePayments"]/div[1]/div/div/div[1]/div[1]/h2/b')
            paymentPageLoaded = True
            return payAmount.text

        except:
            time.sleep(1)
            print('Payment page rendering {}'.format(timeElapsed))
            timeElapsed += 1
            pass

    if (timeElapsed > 10):
        print("The payment page took too long to render. Try again later")
        exit()


# Logs into the website
def login():
    # Grabbing the username and password fields
    inputUsername = driver.find_element_by_xpath('//*[@id="Username"]')
    inputPassword = driver.find_element_by_xpath('//*[@id="Password"]')

    # Inputing the username and passwords
    inputUsername.send_keys(USERNAME_SECRET)
    inputPassword.send_keys(PASSWORD_SECRET)
    # Submitting the fields
    driver.find_element_by_xpath('//*[@id="SignIn"]').click()


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
