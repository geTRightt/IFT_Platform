import  sys
sys.path.append('../db_fixture')
from mysql_db import DB

# 创建测试数据
datas = {
    # 发布会表数据
    'sign_event':[],
    # 嘉宾表数据
    'sign_guest':[],
}

# 将测试数据插入表
def init_data():
    db = DB()
    for table,data in datas.items():
        db.clear(table)
        for d in data:
            db.insert(table,d)
    db.close()

if __name__ == "__main__":
    init_data()
