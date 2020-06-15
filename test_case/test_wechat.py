from businessView.wechat_login import WeChat
from common.desired_caps import appium_desired
from selenium.webdriver.common.by import By
from common.common_fun import Common
import logging
import pytest


logging.basicConfig(level=logging.INFO,
                    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class TestWeChat(Common):
    personal_button = (By.XPATH, "//android.widget.TextView[@text='我']")

    def test_wechat(slef):
        slef.find_element(*slef.personal_button).click()
        logging.info("personal center")
        slef.check_new_user()
        b = slef.find_element(By.XPATH,"//*[contains(@text, '么么号：')]").get_attribute("name")
        print(b)
        assert b == "么么号：74052965"
        logging.info("wechat login success")




if __name__ == '__main__':
    driver = appium_desired()
    com = WeChat(driver)
    com.wechat()
    com1=TestWeChat(driver)
    com1.test_wechat()
