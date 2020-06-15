from businessView.microblog_login import MicroBlog
from common.desired_caps import appium_desired
from selenium.webdriver.common.by import By
from common.common_fun import Common
import logging
import pytest


logging.basicConfig(level=logging.INFO,
                    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class TestMicroBlog(Common):
    personal_button = (By.XPATH, "//android.widget.TextView[@text='我']")

    def test_microblog(slef):
        slef.find_element(*slef.personal_button).click()
        logging.info("personal center")
        slef.check_new_user()
        b = slef.find_element(By.XPATH,"//*[contains(@text, '么么号：')]").get_attribute("name")
        print(b)
        assert b == "么么号：79956987"
        logging.info("MicroBlog login success")




if __name__ == '__main__':
    driver = appium_desired()
    com = MicroBlog(driver)
    com.microblog()
    com1=TestMicroBlog(driver)
    com1.test_microblog()
