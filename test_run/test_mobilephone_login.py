import sys, os

current_directory = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
sys.path.append(root_path)

from test_case.test_mobilephone import TestMobilePhone
from businessView.mobilephone_login import MobilePhone
from common.desired_caps import appium_desired
import logging
import pytest
logging.basicConfig(level=logging.INFO,
                    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')



def test_mobilephone_login():
    driver = appium_desired()
    com = MobilePhone(driver)
    com.mobilephone()
    com1 = TestMobilePhone(driver)
    com1.test_mobilephone()


if __name__ == '__main__':
    test_mobilephone_login()