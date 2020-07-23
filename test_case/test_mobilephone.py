from businessView.mobilephone_login import MobilePhone
from common.desired_caps import appium_desired
from selenium.webdriver.common.by import By
from common.common_fun import Common
from common.common_fun import CommonFuntions
import logging
import pytest


logging.basicConfig(level=logging.INFO,
                    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class TestMobilePhone(Common):
    personal_button = (By.XPATH, "//android.widget.TextView[@text='我']")

    def test_mobilephone(slef):
        slef.find_element(*slef.personal_button).click()
        logging.info("personal center")
        slef.check_new_user()
        b = slef.find_element(By.XPATH,"//*[contains(@text, '么么号：')]").get_attribute("name")
        csv_file = "../data/login_assert_datas.csv"
        mobilephone_assert = CommonFuntions().get_csv_datas(csv_file, 2)[0]
        mobilephone_assert_id = "么么号：" + mobilephone_assert
        assert b == mobilephone_assert_id
        logging.info("mobilephone login success")




if __name__ == '__main__':
    driver = appium_desired()
    com = MobilePhone(driver)
    com.mobilephone()
    com1=TestMobilePhone(driver)
    com1.test_mobilephone()
