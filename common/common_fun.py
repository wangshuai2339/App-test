from baseView.baseView import BaseView
from common.desired_caps import appium_desired
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import logging
logging.basicConfig(level=logging.INFO, format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class Common(BaseView):
    # 判断用户是否首次登录
    other_user=(By.XPATH,"//*[@text='使用其他账号']")
    phone_number=(By.XPATH,"//*[@text='手机号']")
    meme_number=(By.XPATH,"//*[@text='么么号']")
    protocol_CheckBox = (By.XPATH, "//*[@class='android.widget.CheckBox']")
    # 判断青少年弹窗
    teenager_windows=(By.XPATH,"//*[@text='我是青少年']")
    teenager_button=(By.XPATH,"//*[@text='我知道了']")
    # 判断授权弹窗
    allow_button=(By.XPATH, "//*[contains(@text, '允许') ][@class='android.widget.Button']")
    # 判断新手加入QQ的弹窗
    add_group=(By.XPATH, "//*[@text='立即加群']")
    # pull_down=(By.XPATH, "//*[@class='android.widget.ImageView' and 'index=2']")

    # 判断用户是否首次登录
    def check_login(self):
        try:
            # 页面是非首次登陆，页面有“点击下方头像登陆”
            self.find_element(*self.other_user)
        except NoSuchElementException:
            # 首次登陆，需要勾选协议
            # 勾选协议
            self.find_element(*self.protocol_CheckBox).click()
            logging.info("protocol CheckBox")
            # 选择“么么号”
            self.find_element(*self.meme_number).click()
            logging.info("meme uername")

        else:
            # 选择“手机号”
            self.find_element(*self.phone_number).click()
            logging.info("phone uername")

    # 判断青少年弹窗
    def check_teenager(self):
        try:
            # 首次登录，出现青少年弹窗
            self.find_element(*self.teenager_windows)
        except NoSuchElementException:
            # 没有青少年弹窗
            logging.info("teenager pass")

        else:
            # 点击“我知道了”
            self.find_element(*self.teenager_button).click()
            logging.info("I KNOW")

    # 判断授权弹窗
    def check_allow(self):
        try:
            # 登录，出现授权弹窗
            self.find_element(*self.allow_button)
        except NoSuchElementException:
            # 没有授权弹窗
            logging.info("allow pass")
        else:
            # 点击“允许”
            self.find_element(*self.allow_button).click()
            logging.info("allow ")

    # 登录之后，在我的页面出现，新手弹窗
    def check_new_user(self):
        try:
            self.find_element(*self.add_group)
        except NoSuchElementException:
            logging.info("add group pass")
        else:
            self.find_element(*self.add_group).click()
            logging.info("add group")






if __name__ == '__main__':
    driver=appium_desired()
    com=Common(driver)
    com.check_allow()
    com.check_login()
    driver.implicitly_wait(12)
    # 输入账号与密码
    driver.find_element_by_xpath("//*[@text='请输入手机号/么么号']").send_keys('55418083')  # 输入用户名
    driver.find_element_by_xpath("//*[@text='请输入您的密码']").send_keys('123456')  # 输入密码
    logging.info("uesrname ,passward")
    # 登陆
    driver.find_element_by_xpath("//*[@text='登录/注册']").click()  # 点击登陆按钮
    logging.info("login success")
    com.check_allow()
    com.check_teenager()

