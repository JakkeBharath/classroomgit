from selenium.webdriver.common.by import By



class CheckoutPage:
    Item = (By.XPATH,"/html/body/app-root/app-shop/div/div/div/table/tbody/tr[1]/td[1]/div/div/h4/a")
    checkoutButton = (By.CLASS_NAME,"btn-success")

    def __init__(self,driver):
        self.driver=driver
    def Item_Page(self):
        return self.driver.find_element(*CheckoutPage.Item)

    def checkoutButton_Page(self):
        return self.driver.find_element(*CheckoutPage.checkoutButton)
