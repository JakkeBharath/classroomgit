from selenium.webdriver.common.by import By

from PageObjects.ShopItems import ShopItem


class ShopItems:
    Name=(By.NAME,"name")
    Email = (By.NAME,"email")
    Password = (By.ID,"exampleInputPassword1")
    CheckBox = (By.ID,"exampleCheck1")
    Gender = (By.XPATH,"//*[@id = 'exampleFormControlSelect1']")
    RadioButton = (By.ID,"inlineRadio2")
    Button = (By.CLASS_NAME,"btn-success")
    alert = (By.CSS_SELECTOR,"div.alert-success")
    shop_button = (By.XPATH, "//*[@class='navbar-nav'] /li[2]/a")

    def __init__(self,driver):
        self.driver=driver
    def Name_Page(self):
        return self.driver.find_element(*ShopItems.Name)

    def Email_Page(self):
        return self.driver.find_element(*ShopItems.Email)

    def Password_Page(self):
        return self.driver.find_element(*ShopItems.Password)

    def CheckBox_Page(self):
        return self.driver.find_element(*ShopItems.CheckBox)

    def Gender_Page(self):
        return self.driver.find_element(*ShopItems.Gender)

    def RadioButton_Page(self):
        return self.driver.find_element(*ShopItems.RadioButton)

    def Button_Page(self):
        return self.driver.find_element(*ShopItems.Button)

    def alert_Page(self):
        return self.driver.find_element(*ShopItems.alert)

    def ShopItem_Page(self):
        self.driver.find_element(*ShopItems.shop_button).click()
        shopitems = ShopItem(self.driver)
        return shopitems