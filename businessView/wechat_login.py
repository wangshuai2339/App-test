from common.desired_caps import appium_desired
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from common.common_fun import Common
import logging
logging.basicConfig(level=logging.INFO, format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class WeChat(Common):
    # 微信登录
    wechat_button=(By.XPATH,"//*[@text='微信登录']")
    protocol_CheckBox = (By.XPATH, "//*[@class='android.widget.CheckBox']")

    def wechat(self):
        self.check_allow()
        self.find_element(*self.protocol_CheckBox).click()
        self.find_element(*self.wechat_button).click()
        logging.info("login success")
        self.check_allow()
        self.check_teenager()
if __name__ == '__main__':
    driver = appium_desired()
    com = WeChat(driver)
    com.wechat()