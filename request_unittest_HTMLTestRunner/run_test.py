import os,sys
import time,unittest
from HTMLTestRunner import HTMLTestRunner
sys.path.append('./interface')
sys.path.append('./db_fixture')
from db_fixture import test_data

test_dir = './interface'
discover = unittest.defaultTestLoader.discover(test_dir,pattern='*_test.py')

if __name__ == '__main__':
    now =time.strftime("%Y-%m-%d %H-%M-%S")
    file_name = './report/'+now+'_result.html'
    fp = open(file_name,'wb')
    runner = HTMLTestRunner(stream=fp,title='GMS interface test report',description='Implementation Example with:')
    runner.run(discover)
    fp.close()