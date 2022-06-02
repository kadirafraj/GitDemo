from selenium.webdriver.common.by import By


class Confirm:
    def __init__(self, driver):
        self.driver=driver
    confirm= (By.XPATH, "//input[@id='country']")
    india= (By.LINK_TEXT, "India")
    check=(By.XPATH, "//div[@class='checkbox checkbox-primary']")
    submitbutton= (By.CSS_SELECTOR, "input[type='submit']")
    successtext= (By.CSS_SELECTOR, "div[class='alert alert-success alert-dismissible']")
    def SendingKeys(self):
        return self.driver.find_element(*Confirm.confirm)
    def India(self):
        return self.driver.find_element(*Confirm.india)
    def CheckBox(self):
        return self.driver.find_element(*Confirm.check)
    def Submit(self):
        return self.driver.find_element(*Confirm.submitbutton)
    def Success(self):
        return self.driver.find_element(*Confirm.successtext)