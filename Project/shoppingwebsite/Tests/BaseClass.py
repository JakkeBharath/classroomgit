

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import logging
@pytest.mark.usefixtures("setup")
class BaseClass:
    def getlogger(self):

        logger = logging.getLogger(__name__)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s: %(name)s:%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger

    def verification(self,text):
        element = WebDriverWait(self.driver, 15)
        element.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))
