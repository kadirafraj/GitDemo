from selenium.webdriver.common.by import By

from pageobjects.ConfirmPage import Confirm


class Checkoutpage:
    def __init__(self, driver):
        self.driver=driver
    mobiles=(By.CSS_SELECTOR, "card-title a")
    cardfooter= (By.CSS_SELECTOR, ".card-footer button")
    checkout=(By.XPATH, "//a[@class='nav-link btn btn-primary']")
    confirmcheckout=(By.XPATH, "//button[@class='btn btn-success']")
    def GetCardTitles(self):
        return self.driver.find_elements(*Checkoutpage.mobiles)
    def GetFooter(self):
        return self.driver.find_element(*Checkoutpage.cardfooter)
    def CheckOutItems(self):
        return self.driver.find_element(*Checkoutpage.checkout)
    def ConfirmCheckOut(self):
        self.driver.find_element(*Checkoutpage.confirmcheckout).click()
        return Confirm(self.driver)