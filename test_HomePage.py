import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        homePage.getEmail().send_keys(getData["EmailID"])
        # driver.find_element(By.NAME, 'email').send_keys('hello@gmail.com')
        log.info("Enter email id: " + getData["EmailID"])
        homePage.getPassword().send_keys("12345")
        # driver.find_element(By.ID, "exampleInputPassword1").send_keys('12345')
        log.info("Enter password")
        homePage.select_checkbox().click()
        # driver.find_element(By.ID, 'exampleCheck1').click()
        log.info("Click on checkbox")
        # XPATH - //tagname[@attribute = 'value'] --> //input[@type = 'submit']
        # CSSLocator -  tagname[attribute = 'value'] --> input[type = 'submit'], #id, .classname

        homePage.getName().send_keys(getData["First Name"])
        # driver.find_element(By.CSS_SELECTOR, "input[name = 'name']").send_keys("Rahul Shetty")
        log.info("Enter First Name")
        homePage.select_radio().click()
        # driver.find_element(By.CSS_SELECTOR, '#inlineRadio1').click()

        # Static dropdown

        self.selectOptionByText(homePage.getDropdown(), getData["Gender"])
        # dropdown = (Select(homePage.getDropdown())
        #             # (driver.find_element(By.ID, "exampleFormControlSelect1"))
        #
        # dropdown.select_by_visible_text("Female")
        # dropdown.select_by_index(0)
        # # dropdown.select_by_value()

        homePage.getSubmit().click()
        log.info("Click on Submit button")
        # driver.find_element(By.XPATH, "//input[@type = 'submit']").click()
        message = homePage.getMessage().text
            #driver.find_element(By.CLASS_NAME, "alert-success").text)
        print(message)
        log.info("Get success message: ")
        assert "Success" in message
        print("My first line of modified code to in Git Trainer 1")
        print("My first line of modified code to in Git Trainer 2")
        print("My first line of modified code to in Git Trainer 3")
        print("My first line of modified code to in Git Trainer 4")

        self.driver.refresh()

    # @pytest.fixture(params= [{"First Name": "Rahul", "EmailID":"hello@gmail.com", "Gender":"Male"},
    #                          {"First Name":"Anshika", "EmailID":"hello1@gmail.com", "Gender":"Female"},
    #                          {"First Name": 'Arizona', "EmailID": "hello2@gmail.com", "Gender": "Male"}])
                    # passing dataset as tuple [("Rahul", "hello@gmail.com", "Male"),
                          #  ("Anshika", "hello1@gmail.com", "Female"), ('Arizona', "hello@gmail.com", "Male")])
    @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    def getData(self, request):
        return request.param
        
def test():        
    print("My first line of modified code to in Git demo")
    print("My first line of modified code to in Git demo2")
    print("My first line of modified code to in Git demo3")
    print("My first line of modified code to in Git demo4")
    

def test2():        
    print("My first line of modified code to in Git demo")
    print("My first line of modified code to in Git demo2")
    print("My first line of modified code to in Git demo3")
    print("My first line of modified code to in Git demo4")
    

def test3():        
    print("My first line of modified code to in Git demo")
    print("My first line of modified code to in Git demo2")
    print("My first line of modified code to in Git demo3")
    print("My first line of modified code to in Git demo4")
    
    
def test3Trainer():        
    print("My first line of modified code to in Git demo")
    print("My first line of modified code to in Git demo2")
    print("My first line of modified code to in Git demo3")
    print("My first line of modified code to in Git demo4")