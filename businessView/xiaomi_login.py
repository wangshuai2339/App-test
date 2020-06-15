from common.desired_caps import appium_desired
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from common.common_fun import Common
import logging
logging.basicConfig(level=logging.INFO, format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class XiaoMi(Common):
    # 小米登录
    mi_username=(By.XPATH,"//*[@resource-id='username']")
    mi_password=(By.XPATH,"//*[@resource-id='pwd']")
    login_button=(By.XPATH,"//*[@text='登录']")
    mi_button = (By.XPATH, "//*[@text='小米']")
    protocol_CheckBox = (By.XPATH, "//*[@class='android.widget.CheckBox']")

    def xiaomi(self,username,password):
        self.check_allow()
        self.find_element(*self.protocol_CheckBox).click()
        self.find_element(*self.mi_button).click()
        self.find_element(*self.mi_username).send_keys(username)
        self.find_element(*self.mi_password).send_keys(password)
        logging.info("uesrname ,passward")

        self.find_element(*self.login_button).click()
        logging.info("login success")
        self.check_allow()
        self.check_teenager()
if __name__ == '__main__':
    driver = appium_desired()
    com = XiaoMi(driver)
    com.xiaomi('1088844433','xm13608428757ws')