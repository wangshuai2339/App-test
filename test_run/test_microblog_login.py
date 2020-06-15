import sys, os

current_directory = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
sys.path.append(root_path)

from test_case.test_microblog import TestMicroBlog
from businessView.microblog_login import MicroBlog
from common.desired_caps import appium_desired
import logging
import pytest
logging.basicConfig(level=logging.INFO,
                    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')



def test_microblog_login():
    driver = appium_desired()
    com = MicroBlog(driver)
    com.microblog()
    com1 = TestMicroBlog(driver)
    com1.test_microblog()


if __name__ == '__main__':
    test_microblog_login()