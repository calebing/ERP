import os.path
import unittest
from Method_requests import reBasePage
import pymysql
import yaml
class TestCase(unittest.TestCase,reBasePage):
    url = os.path.join(os.path.dirname(__file__) + '/Data/url.yml')
    data = os.path.join(os.path.dirname(__file__) + '/Data/data.yml')
    requestsbody = os.path.join(os.path.dirname(__file__) + '/Data/requestsbody.yml')
    headers = os.path.join(os.path.dirname(__file__) + '/Data/headers.yml')
    @classmethod
    def setUpClass(cls) -> None:
        db = pymysql.connect(host='192.168.15.17', user='dev', password='dev', database='sy_mom_test_sit_005')
        a = db.cursor()
        mysql_table = os.path.join(os.path.dirname(__file__) + '/Data/mysql_table.yml')
        with open(mysql_table, 'r',
                  encoding='UTF-8', ) as d:
            sql = yaml.load(d, Loader=yaml.FullLoader)
        for i in sql:
            a.execute(str(sql[i]))
            db.commit()
        db.close()
        pass
    @classmethod
    def tearDownClass(cls) -> None:
        pass


    def test001(self):
        '''
        新增仓库性值
        :return:
        '''
        self.get_request('unit-list-sim','headers_json')



if __name__ == '__main__':
    unittest.main()
















