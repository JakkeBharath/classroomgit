import time

import pytest
from selenium.webdriver.support.select import Select
from PageObjects.HomePage import ShopItems
from PageObjects.PaymentPage import PaymentPage
from Tests.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_end2end(self,getdata):

        log= self.getlogger()
        home_page= ShopItems(self.driver)
        home_page.Name_Page().send_keys(getdata[0])
        log.info("gettingUsername")
        time.sleep(3)
        home_page.Email_Page().send_keys(getdata[1])
        log.info("getting Emailid")
        time.sleep(3)
        home_page.Password_Page().send_keys(getdata[2])
        log.info("gettingPassword")
        time.sleep(3)
        home_page.CheckBox_Page().click()
        time.sleep(3)
        c=Select(home_page.Gender_Page())
        c.select_by_visible_text(getdata[3])
        time.sleep(3)
        home_page.RadioButton_Page().click()
        time.sleep(3)
        home_page.Button_Page().click()
        d= home_page.alert_Page().text
        log.info("text received from appllication"+d)
        print(d)
        assert "submitted successfully!" in d
        shopitems=home_page.ShopItem_Page()
        c=shopitems.Title_Page()
        print(len(c))
        a=-1
        for i in c:
            a=a+1
            cart = i.text
            print(cart)
            log.info(cart)
            if cart == "Blackberry":
                shopitems.AddButton_Page()[a].click()
        checkoutpage = shopitems.AddCart_Page()
        checkoutpage.checkoutButton_Page().click()
        payment_page = PaymentPage(self.driver)
        log.info("getting Country")
        payment_page.country_Page().send_keys("ind")
        self.verification("India")
        payment_page.CountryOptions_Page().click()
        payment_page.Checkbox_Page().click()
        payment_page.button_Page().click()
        c=payment_page.alert_Page().text
        log.info("text received from appllication is "+c)
        print(c)
        assert "Success!" in c

    @pytest.fixture(params=[("Jakke Bharath Kumar","JakkeBharath@gmail.com","Bharath@@2022","Male")])
    def getdata(self,request):
        return request.param