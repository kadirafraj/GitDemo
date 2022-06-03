from pageobjects.Homepage import Homepage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self):
        print("Hello World")
        print("Saturday")
        print("Rockstar")
        log=self.getlogger()
        homepage= Homepage(self.driver)
        checkoutpage=homepage.shopitems()
        mobiles=checkoutpage.GetCardTitles()
        i= -1
        for mobile in mobiles:
            i=i+1
            log.info(mobile.text)
            if mobile.text=="Blackberry":
                checkoutpage.GetFooter()[i].click()
        checkoutpage.CheckOutItems().click()
        confirm=checkoutpage.ConfirmCheckOut()
        log.info("Enter Country name as ind")
        confirm.SendingKeys().send_keys("ind")
        self.verifyingpresence("India")
        confirm.India().click()
        confirm.CheckBox().click()
        confirm.Submit().click()
        success_text= confirm.Success().text
        log.info("Text receieved from application is"+success_text)
        assert "Success" in success_text
        self.driver.get_screenshot_as_file("screen.png")