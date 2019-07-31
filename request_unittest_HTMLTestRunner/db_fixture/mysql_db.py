from pymysql import connect,cursors
from pymysql.err import OperationalError
import pymysql
import os
import configparser as cparser

# ==== read db_config.ini =====
base_dir =str(os.path.dirname(os.path.dirname(__file__)))
# print(base_dir)
# test_dir=os.path.dirname(__file__)
# print(test_dir)
# print(type(base_dir))
# print(type(test_dir))
base_dir = base_dir.replace('\\','/')
file_path = base_dir + "/db_config.ini"
print("配置文件路径：",file_path)
cf = cparser.ConfigParser()
cf.read(file_path)
host_is = cf.get("mysqlconf","host")
print("host:",host_is)
port_is = cf.get("mysqlconf","port")
print("port:",port_is)
db_is = cf.get("mysqlconf","db_name")
print("db:",db_is)
user_is = cf.get("mysqlconf","user")
print("user:",user_is)
password_is = cf.get("mysqlconf","password")
print("password:",password_is)

# ==== 封装mysql基本操作 ====
class DB:
    def __init__(self):
        try:
            # conn = pymysql.connect(host='127.0.0.1', user='root', password='123456', port=3306, db='testdb')
            self.conn =pymysql.connect(host = host_is,
                                       user = user_is,
                                       password = password_is,
                                       port = 3306,
                                       db = db_is)
        except OperationalError as e:
            print("Mysql Error %d:%s"%(e.args[0],e.args[1]))

    def clear(self,table_name):
        # real_sql = "truncate table" + table_name + ";"
        real_sql = "delete from" + table_name + ";"
        with self.conn.cursor() as cursor:
            # 执行sql语句
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(real_sql)
        # 提交到数据库执行
        self.conn.commit()

    def insert(self,table_name,table_data):
        for key in table_name:
            table_data[key] = "'"+str(table_data[key])+"'"
        key = ','.join(table_data.keys())
        value = ','.join(table_data.values())
        real_sql = "INSERT INTO" + table_name + "("+ key + ") VALUES (" + value + ")"
        print(real_sql)
        with self.conn.cursor() as cursor:
            cursor.execute(real_sql)
        self.conn.commit()

    # 关闭数据库
    def close(self):
        self.conn.close()

if __name__ == "__main__":
    '''db = DB()
    table_name = "sign_event"
    data = {'id':3,'event_name':'redmi','limits':2000,'statu':1,'address':
        'beijing','start_time':'2016-08-20 00:25:42'}
#    db.clear(table_name)
    db.insert(table_name,data)
    db.close()'''

    # 测试连接插入
    conn = pymysql.connect(host='127.0.0.1', user='root', password='123456', port=3306, db='testdb')
    cursor = conn.cursor()
    sql_insert = "insert into sign_event(event_name,limits,statu,address) values('小米发布会',2000,1,'北京会展中心')"
    cursor.execute(sql_insert)
    conn.commit()
    conn.close()
    cursor.close()
    print("1")