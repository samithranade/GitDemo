import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)

        # Regular expression, Xpath - '//a[contains(@href,'shop')]  Css - 'a[href*='shop']
        checkOutPage = homePage.shopItems()
        log.info("Getting all the card titles")

        #products = checkOutPage.getProductTitles()
        products = checkOutPage.getProductdetails()
        #self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")

        for phone in products:
            phoneName = checkOutPage.getPhoneNames(phone)
            log.info(phoneName)
                # phone.find_element(By.XPATH, 'div/h4/a').text)
            if phoneName == "Blackberry":
                checkOutPage.getSelectPhone(phone).click()
                #phone.find_element(By.XPATH, "div/button").click()
            else:
                log.error("No phone by name blackberry")
                assert "Blackberry" not in phoneName
        checkOutPage.getCheckout().click()
        # self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn']").click()
        confirmPage = checkOutPage.checkout()
        # self.driver.find_element(By.CSS_SELECTOR, "button[class*='btn-success']").click()
        log.info("Entering country name as ind")
        # confirmPage = ConfirmPage(self.driver)
        confirmPage.CountryName().send_keys("ind")
        # self.driver.find_element(By.ID, "country").send_keys("ind")

        self.verifyLinkPresence("India")

        confirmPage.Name().click()
        # self.driver.find_element(By.LINK_TEXT, "India").click()
        confirmPage.Checkbox().click()
        # self.driver.find_element(By.CSS_SELECTOR, "div[class*='checkbox']").click()
        confirmPage.Purchase().click()
        # self.driver.find_element(By.XPATH, "//input[@type='submit']").click()

        success = confirmPage.Message().text
           # self.driver.find_element(By.CLASS_NAME, "alert-dismissible").text)
        log.info("Text received from application is " + success)
        assert "Success! Thank you!" in success
