import unittest
import os
import HTMLTestRunnerCN
import sys
from multiprocessing import Process
# sys.path.append("..")

if __name__ == '__main__':

    case_path = os.path.join(os.getcwd(), 'Samyang_moc_E')
    discover = unittest.defaultTestLoader.discover(case_path, pattern='testcase*', top_level_dir=None)
    path = os.getcwd()
    file_path = os.path.join(path, '测试报告.html')
    fp = open(file_path, 'wb')
    runner = HTMLTestRunnerCN.HTMLTestReportCN(stream=fp, title='E级产品主线测试报告', description='测试用例集合', tester='bing')
    runner.run(discover)
    fp.close()
