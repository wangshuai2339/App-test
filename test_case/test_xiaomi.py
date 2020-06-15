from businessView.xiaomi_login import XiaoMi
from common.desired_caps import appium_desired
from selenium.webdriver.common.by import By
from common.common_fun import Common
import logging
import pytest


logging.basicConfig(level=logging.INFO,
                    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class TestXiaoMi(Common):
    personal_button = (By.XPATH, "//android.widget.TextView[@text='我']")

    def test_xiaomi(slef):
        slef.find_element(*slef.personal_button).click()
        logging.info("personal center")
        slef.check_new_user()
        b = slef.find_element(By.XPATH,"//*[contains(@text, '么么号：')]").get_attribute("name")
        print(b)
        assert b == "么么号：78766179"
        logging.info("xiaomi login success")




if __name__ == '__main__':
    driver = appium_desired()
    com = XiaoMi(driver)
    com.xiaomi('1088844433', 'xm13608428757ws')
    com1=TestXiaoMi(driver)
    com1.test_xiaomi()

