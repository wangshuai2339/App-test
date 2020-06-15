from appium import  webdriver
import logging
import yaml
import sys, os


logging.basicConfig(level=logging.INFO,
                    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def appium_desired():

    current_directory = os.path.dirname(os.path.abspath(__file__))
    root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")

    with open(root_path+"\config/app_driver.yaml","r",encoding="utf-8") as file:
        data = yaml.load(file)

    desired_caps={}
    desired_caps["platformName"]=data["platformName"]                                    #平台
    desired_caps["platfromVersion"]=data["platfromVersion"]                                       #平台版本
    desired_caps["deviceName"]=data["deviceName"]                              #设备名称
    desired_caps["appPackage"]=data["appPackage"]                         #APK包名
    desired_caps["appActivity"]=data["appActivity"] #appActivity
    desired_caps["noReset"]=data["noReset"]                                             #否清除session信息
    desired_caps["automationName"]=data["automationName"]
    driver=webdriver.Remote("http://"+str(data["ip"])+":"+ str(data["port"])+"/wd/hub" ,desired_caps)
    driver.implicitly_wait(10)

    return driver

if __name__ == '__main__':
    driver=appium_desired()
    # 选择“手机号”/默认登录的时候
    driver.find_element_by_xpath("//*[@text='手机号']").click()
    logging.info("oter uername")

    driver.implicitly_wait(12)
    # 输入账号与密码
    driver.find_element_by_xpath("//*[@text='请输入手机号/么么号']").send_keys('55418083') #输入用户名
    driver.find_element_by_xpath("//*[@text='请输入您的密码']").send_keys('123456')#输入密码
    logging.info("uesrname ,passward")
    #登陆
    driver.find_element_by_xpath("//*[@text='登录/注册']").click()        #点击登陆按钮
    logging.info("login success")

