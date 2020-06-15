from common.desired_caps import appium_desired
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from common.common_fun import Common
import logging
logging.basicConfig(level=logging.INFO, format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class QqLogin(Common):
    # QQ登录
    qq_login=(By.XPATH,"//*[@text='QQ授权登录']")
    qq_button = (By.XPATH, "//*[@text='QQ']")
    protocol_CheckBox = (By.XPATH, "//*[@class='android.widget.CheckBox']")

    def qqlogin(self):
        self.check_allow()
        self.find_element(*self.protocol_CheckBox).click()
        self.find_element(*self.qq_button).click()
        logging.info("QQ")

        self.find_element(*self.qq_login).click()
        logging.info("login success")
        self.check_allow()
        self.check_teenager()
if __name__ == '__main__':
    driver = appium_desired()
    com = QqLogin(driver)
    com.qqlogin()


