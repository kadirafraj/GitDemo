import pytest

from Testdata.HomePageData import HomePageData
from pageobjects.Homepage import Homepage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):
    def test_formsubmission(self, getData):
        print("Hello World")
        print("Hello India")
        print("Kadir")
        print("Hello World1")
        print("Hello India1")
        print("Kadir1")
        self.driver.implicitly_wait(3)
        log=self.getlogger()
        homepage=Homepage(self.driver)
        log.info("First name is"+getData["firstname"])
        homepage.getname().send_keys(getData["firstname"])
        homepage.getemail().send_keys(getData["email"])
        homepage.getpassword().send_keys(getData["password"])
        homepage.getpassword().click()
        self.selectgenderbytext(homepage.getgender(), getData["gender"])
        homepage.submitform().click()
        message=homepage.successmessage().text
        assert "success" in message
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData())
    def getData(self, request):
        return request.param