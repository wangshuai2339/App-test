import sys, os

current_directory = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
sys.path.append(root_path)

from test_case.test_username import TestUserName
from businessView.username_login import UserName
from common.desired_caps import appium_desired
import logging
import pytest
logging.basicConfig(level=logging.INFO,
                    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')



def test_username_login():
    driver = appium_desired()
    com = UserName(driver)
    com.username('55418083', '123456')
    com1 = TestUserName(driver)
    com1.test_username()


if __name__ == '__main__':
    test_username_login()