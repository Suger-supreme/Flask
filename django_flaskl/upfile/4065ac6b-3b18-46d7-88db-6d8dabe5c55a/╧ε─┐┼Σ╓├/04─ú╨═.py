1 模型(models):
               01 Django中对各种数据库提供了很好的支持 django为这些数据库提供了统一的调用api可以根据不同的业务需求选择数据库



               02 配置数据:

                       注意:一个模型类在数据库中对应一张表

                       在settings文件中修改
                                     DATABASES = {
											    'default': {
											      # 'ENGINE': 'django.db.backends.sqlite3',
											        'ENGINE': 'django.db.backends.mysql',
											        'NAME': "class",   数据名
											        'USER': "root",  用户
											        'PASSWORD':'root',密码
											        'HOST':'localhost', 数据库的ip
											        'PORT':'3306',   端口

											    }
											}


                       在__init__.py文件中写入:   import pymysql

                                                 pymysql.install_as_MySQLdb()



               03 开发流程    就是(增 删 改 查)






2 ORM(对象关系映射):   
                   任务:

	                   01 根据对象的类型生成结构表

	                   02 将对象 列表的操作转换为sql语句

	                   03 将sql语句查询到的结果转换对象 ， 列表

	              优点: 
	                  极大的减轻了开发人员的工作量   不需要修改代码






3 定义模型:

           01模型  属性  表  字段间关系   
               一个模型类在数据库中对应一张表,在模型中定义的属性,对应该模型中的一个字段
 
           02 定义属性:


           03元选项 ：
                      在模型类中定义Meta类 用于设置元信息

                      class Meta:

                      	   db_table=""     定义数据表名(推荐使用小写 数据表默认项目小写 类名)

                      	   ordering=[]  对象默认排序字段  获取对象列表时使用
                      	   ordering=['id']     升序
                      	   ordering=['-id']    降序


          04模型成员:
                    类属性：    objects    是Manage类型的一个对象 作用是数据库进行交互

                    创建对象(objects ): 当定义模型类是没有指定管理器 则Django为模型创建一个名为objects的管理器


                    自定义管理器:

                                

                   



