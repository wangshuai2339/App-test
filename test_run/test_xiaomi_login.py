import sys, os

current_directory = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
sys.path.append(root_path)

from test_case.test_xiaomi import TestXiaoMi
from businessView.xiaomi_login import XiaoMi
from common.desired_caps import appium_desired
import logging
import pytest
logging.basicConfig(level=logging.INFO,
                    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')



def test_xiaomi_login():
    driver = appium_desired()
    com = XiaoMi(driver)
    com.xiaomi('1088844433', 'xm13608428757ws')
    com1 = TestXiaoMi(driver)
    com1.test_xiaomi()
if __name__ == '__main__':
    test_xiaomi_login()