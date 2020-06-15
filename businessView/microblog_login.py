from common.desired_caps import appium_desired
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from common.common_fun import Common
import logging
logging.basicConfig(level=logging.INFO, format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class MicroBlog(Common):
    # 微博登录
    microblog_button = (By.XPATH, "//*[@text='微博']")
    protocol_CheckBox = (By.XPATH, "//*[@class='android.widget.CheckBox']")

    def microblog(self):
        self.check_allow()
        self.find_element(*self.protocol_CheckBox).click()
        self.find_element(*self.microblog_button).click()
        self.check_allow()
        logging.info("login success")
        self.check_allow()
        self.check_teenager()
if __name__ == '__main__':
    driver = appium_desired()
    com = MicroBlog(driver)
    com.microblog()