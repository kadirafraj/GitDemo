from selenium.webdriver.common.by import By

from pageobjects.Checkoutpage import Checkoutpage


class Homepage:
    def __init__(self, driver):
        self.driver=driver
    shop=(By.CSS_SELECTOR, "a[href='/angularpractice/shop']")
    name=(By.CSS_SELECTOR, "input[name='name']")
    email=(By.CSS_SELECTOR, "input[name='email']")
    password=(By.ID, "exampleInputPassword1")
    checkbox=(By.ID, "exampleCheck1")
    gender=(By.ID, "exampleFormControlSelect1")
    submit=(By.CSS_SELECTOR, "input[type='submit']")
    success=(By.CSS_SELECTOR, "div[class='alert alert-success alert-dismissible']")
    def shopitems(self):
        self.driver.find_element(*Homepage.shop).click()
        return Checkoutpage(self.driver)
    def getname(self):
        return self.driver.find_element(*Homepage.name)
    def getemail(self):
        return self.driver.find_element(*Homepage.email)
    def getpassword(self):
        return self.driver.find_element(*Homepage.password)
    def selectcheckbox(self):
        return self.driver.find_element(*Homepage.checkbox)
    def getgender(self):
        return self.driver.find_element(*Homepage.gender)
    def submitform(self):
        return self.driver.find_element(*Homepage.submit)
    def successmessage(self):
        return self.driver.find_element(*Homepage.success)