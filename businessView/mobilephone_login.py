from common.desired_caps import appium_desired
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from common.common_fun import Common
import logging
logging.basicConfig(level=logging.INFO, format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class MobilePhone(Common):
    # 手机一键登录登录
    login_button=(By.XPATH,"//*[@text='立即登录']")
    mobilephone_button = (By.XPATH, "//*[@text='本机号码一键安全登录']")
    protocol_CheckBox = (By.XPATH, "//*[@class='android.widget.CheckBox']")

    def mobilephone(self):
        self.check_allow()
        self.find_element(*self.protocol_CheckBox).click()
        self.find_element(*self.mobilephone_button).click()
        self.find_element(*self.login_button).click()
        logging.info("login success")
        self.check_allow()
        self.check_teenager()
if __name__ == '__main__':
    driver = appium_desired()
    com = MobilePhone(driver)
    com.mobilephone()