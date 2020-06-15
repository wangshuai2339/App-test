import sys, os

current_directory = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
sys.path.append(root_path)

from test_case.test_qq import TestQq
from businessView.qq_login import QqLogin
from common.desired_caps import appium_desired
import logging
import pytest
logging.basicConfig(level=logging.INFO,
                    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')



def test_qq_login():
    driver = appium_desired()
    com = QqLogin(driver)
    com.qqlogin()
    com1 = TestQq(driver)
    com1.test_qq()


if __name__ == '__main__':
    test_qq_login()