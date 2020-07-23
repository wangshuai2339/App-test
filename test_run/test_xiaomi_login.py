import sys, os

current_directory = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
sys.path.append(root_path)

from test_case.test_xiaomi import TestXiaoMi
from businessView.xiaomi_login import XiaoMi
from common.desired_caps import appium_desired
from common.common_fun import CommonFuntions
import logging
import pytest
logging.basicConfig(level=logging.INFO,
                    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')



def test_xiaomi_login():
    driver = appium_desired()
    com = XiaoMi(driver)
    csv_file = "../data/login_datas.csv"
    xiaomi_name = CommonFuntions().get_csv_datas(csv_file, 2)[0]
    xiaomi_pwd = CommonFuntions().get_csv_datas(csv_file, 2)[1]
    com.xiaomi(xiaomi_name, xiaomi_pwd)
    com1 = TestXiaoMi(driver)
    com1.test_xiaomi()
if __name__ == '__main__':
    test_xiaomi_login()