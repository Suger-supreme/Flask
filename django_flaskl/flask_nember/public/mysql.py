
from settings import Config
import  pymysql
# 注意 args 参数可以传空值[]
class Mysqls(object):
    def __init__(self):
         # 读取配置文件
        self.connect()

    def connect(self):
        self.conn =Config.POOL.connection()
        self.cursor=self.conn.cursor(cursor=pymysql.cursors.DictCursor)

   # 获取所以数据
    def get_all(self,sql,args):
         self.cursor.execute(sql,args)
         res = self.cursor.fetchall()
         return  res

   # 获取一行数据
    def get_one(self,sql,args):
        self.cursor.execute(sql, args)
        res = self.cursor.fetchone()
        return res




   # 添加  就是添加一次提交多次
    def get_mode (self,sql,args):
        self.cursor.execute(sql, args)
        self.conn.commit()

    # 添加并且带返回值
    def get_create(self,sql,args):
        self.cursor.execute(sql,args)
        self.conn.commit()
        return self.cursor.lastrowid
       # python插入记录后取得主键id的方法(cursor.lastrowid和conn.insert_id())

     # 批量加入 以元祖的形式传参数   就是添加一次提交一次
    def mul_mode(self, sql, args):
        # self.cursor.executemany("insert into user (id,name) values (%s,%s)",[(1,"aaa"),(2,"bbb"),(3,"ccc")])  传参方式
        self.cursor.executemany(sql, args)
        self.conn.commit()

    def get_close(self):
           self.cursor.close()
           self.conn.close()



