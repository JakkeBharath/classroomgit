from selenium.webdriver.common.by import By


class PaymentPage:
    country = (By.ID,"country")
    CountryOptions = (By.LINK_TEXT,"India")
    Checkbox = (By.XPATH,"//*[@class='checkbox checkbox-primary']")
    button = (By.CSS_SELECTOR,"input.btn-success")
    alert = (By.CSS_SELECTOR,"div.alert-success")


    def __init__(self,driver):
        self.driver=driver

    def country_Page(self):
        return self.driver.find_element(*PaymentPage.country)
    def CountryOptions_Page(self):
        return self.driver.find_element(*PaymentPage.CountryOptions)
    def Checkbox_Page(self):
        return self.driver.find_element(*PaymentPage.Checkbox)
    def button_Page(self):
        return self.driver.find_element(*PaymentPage.button)
    def alert_Page(self):
        return self.driver.find_element(*PaymentPage.alert)