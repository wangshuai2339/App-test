import sys, os

current_directory = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
sys.path.append(root_path)

from test_case.test_wechat import TestWeChat
from businessView.wechat_login import  WeChat
from common.desired_caps import appium_desired
import logging
import pytest
logging.basicConfig(level=logging.INFO,
                    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')



def test_wechat_login():
    driver = appium_desired()
    com = WeChat(driver)
    com.wechat()
    com1 = TestWeChat(driver)
    com1.test_wechat()



if __name__ == '__main__':
    test_wechat_login()