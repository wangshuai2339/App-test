from businessView.qq_login import QqLogin
from common.desired_caps import appium_desired
from selenium.webdriver.common.by import By
from common.common_fun import Common
import logging
import pytest


logging.basicConfig(level=logging.INFO,
                    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class TestQq(Common):
    personal_button = (By.XPATH, "//android.widget.TextView[@text='我']")

    def test_qq(slef):
        slef.find_element(*slef.personal_button).click()
        logging.info("personal center")
        slef.check_new_user()
        b = slef.find_element(By.XPATH,"//*[contains(@text, '么么号：')]").get_attribute("name")
        print(b)
        assert b == "么么号：74170793"
        logging.info("qq login success")




if __name__ == '__main__':
    driver = appium_desired()
    com = QqLogin(driver)
    com.qqlogin()
    com1=TestQq(driver)
    com1.test_qq()
