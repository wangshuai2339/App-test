from businessView.qq_login import QqLogin
from common.desired_caps import appium_desired
from selenium.webdriver.common.by import By
from common.common_fun import Common
from common.common_fun import CommonFuntions
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
        csv_file = "../data/login_assert_datas.csv"
        qq_assert = CommonFuntions().get_csv_datas(csv_file, 4)[0]
        qq_assert_id = "么么号：" + qq_assert
        assert b == qq_assert_id
        logging.info("qq login success")




if __name__ == '__main__':
    driver = appium_desired()
    com = QqLogin(driver)
    com.qqlogin()
    com1=TestQq(driver)
    com1.test_qq()
