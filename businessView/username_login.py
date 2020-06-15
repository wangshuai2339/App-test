from common.desired_caps import appium_desired
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from common.common_fun import Common
import logging
logging.basicConfig(level=logging.INFO, format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class UserName(Common):
    # 用户名登录
    meme_username=(By.XPATH,"//*[@text='请输入手机号/么么号']")
    meme_password=(By.XPATH,"//*[@text='请输入您的密码']")
    login_button=(By.XPATH,"//*[@text='登录/注册']")
    meme_number = (By.XPATH, "//*[@text='么么号']")
    protocol_CheckBox = (By.XPATH, "//*[@class='android.widget.CheckBox']")

    def username(self,username,password):
        self.check_allow()
        self.find_element(*self.protocol_CheckBox).click()
        self.find_element(*self.meme_number).click()
        # self.check_login()
        self.find_element(*self.meme_username).send_keys(username)
        self.find_element(*self.meme_password).send_keys(password)
        logging.info("uesrname ,passward")

        self.find_element(*self.login_button).click()
        logging.info("login success")
        self.check_allow()
        self.check_teenager()
if __name__ == '__main__':
    driver = appium_desired()
    com = UserName(driver)
    com.username('55418083','123456')


