创建应用  ：

         在一个项目中可以创建多个项目  每个应用进行一种业务处理

06.创建应用  ： 在一个项目中 可以创建多个应用 每个应用进行一种业务处理

                打开黑屏终端进入webpython 目录下的 webpython 目目录


                执行  python  manage.py  startapp  myApp
                


      myApp 目录说明:  
                     admin.py       站点匹配
                    
                 
                     models.py       模型
                    
                     views.py        视图

                  
       激活应用 ： 在setting文件中将myApp添加到 INSTALLED_APPS选项中

       INSTALLED_APPS = [

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myApp'
     ]

# 上面是配djiango文件  下面是具体操作
  
    1 定义模型  :       概述 有一个数据表 就对应一个，模型   引入from django.db import models   模型要继承model.Modle类

                     在models.py文件中定义模型 

                        class Grades(models.Model):

                           gname    =    models.CharField(max_length=20)   # 最长20个字节

                           gdate    =    models.DateTimeaField()    # 时间类型

                           ggirlnum =    models.IntegerField()   

                           gboynum  =    models.IntegerField()

                           isDelete =    models.BooleanField(default=False)      
                           
                        # 
                        class Student(models.Model):

                           sname   = models.CharField(max_length=20)

                           sgender = models.BooleanField(default=True)

                           sage    = models.IntegerField()

                           scontend= models.CharField(max_length=20)

                           isDelete= models.BooleanField(default=False)
                            # 关联外键
                           sgrade  =  models.ForeignKey("Grades")

                          # 注意不要定义主键 在生成自动添加 并且值也自动增加


2生成数据表：       生成迁移文件  --- 执行：   python  manage.py  makemigrations   
                                         是在migrations目录下生产一个迁移文件 此时数据库中还没有生成数据表

                                D:\learnPython\py13\Web_Django\webpython>python  manage.py  makemigrations
                                Migrations for 'myApp':
                                  myApp\migrations\0001_initial.py
                                    - Create model Grades
                                    - Create model Student



                   执行迁移文件----执行 python manage.py migrate   相当于执行sql语句创建了数据表

                                     D:\learnPython\py13\Web_Django\webpython>python manage.py migrate
                                    System check identified some issues:

                                    WARNINGS:
                                    ?: (mysql.W002) MySQL Strict Mode is not set for database connection 'default'
                                            HINT: MySQL's Strict Mode fixes many data integrity problems in MySQL, such as data truncation upon insertion, by escalating warnings into errors. It is strongly recommended you activate it. See: https://docs.djangoproject.com/en/1.11/ref/databases/#mysql-sql-mode
                                    Operations to perform:
                                      Apply all migrations: admin, auth, contenttypes, myApp, sessions
                                    Running migrations:
                                      Applying contenttypes.0001_initial... OK
                                      Applying auth.0001_initial... OK
                                      Applying admin.0001_initial... OK
                                      Applying admin.0002_logentry_remove_auto_add... OK
                                      Applying contenttypes.0002_remove_content_type_name... OK
                                      Applying auth.0002_alter_permission_name_max_length... OK
                                      Applying auth.0003_alter_user_email_max_length... OK
                                      Applying auth.0004_alter_user_username_opts... OK
                                      Applying auth.0005_alter_user_last_login_null... OK
                                      Applying auth.0006_require_contenttypes_0002... OK
                                      Applying auth.0007_alter_validators_add_error_messages... OK
                                      Applying auth.0008_alter_user_username_max_length... OK
                                      Applying myApp.0001_initial... OK
                                      Applying sessions.0001_initial... OK

到这里了Web     因该执行下面了py14

3测试数据表操作        进入到 python shell   ---------------
                               
                                      执行    :   python manage.py shell

                                              D:\learnPython\py13\Web_Django\webpython>python manage.py shell
                                              D:\learnPython\py13\Web_Django\webpython>python manage.py shell
                                                Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
                                                Type "help", "copyright", "credits" or "license" for more information.
                                                (InteractiveConsole)
                                                >>>


                                    引入包：       from myapp.models import Grades,Students

                                                 from django.utils import timezone

                                                 from datetime import *

                        
                                    查询所有数据: 类名.objects.all()

                                                 例如： Grades.objects.all()


                                    添加数据：   本质:就是创建一个模型类的对象实例

                                                 例如：    grade1=Grades()

                                   grade1.gname="python01"

                                   grade1.gdate=datetime(year=2017,month=1,day=15)

                                   grade1.ggirlnum=6000

                                   grade1.gboynum=800

                                   grade1.save()  # 保存


									mysql> select * from myapp_grades;
									+----+----------+---------------------+----------+---------+----------+
									| id | gname    | gdate               | ggirlnum | gboynum | isDelete |
									+----+----------+---------------------+----------+---------+----------+
									|  1 | python01 | 2017-01-14 16:00:00 |     6000 |     800 |        0 |
									+----+----------+---------------------+----------+---------+----------+
									1 row in set (0.00 sec)
									                
 
                                     查看某个对象      类名.objects.get(pk=2)
                                                     
                                                                  例如: Grades.objects.get(pk=2)

                                     修改数据              模型对象.属性=新值
                                                                                             例如: grade2.gboynum=11111
                                         grade2.save()


                                     修改数据           模型对象.delete()
                                                                例如: grade2.delete()





                                                       注意: 物理删除 数据库中的表里的数据被删除了


                                                        stu=Students()
                                                        stu.sname="张三"
                                                        stu.sgender=False
                                                        stu.sage=20
                                                        stu.scontend="喜欢喝牛奶了啊哈哈啊哈"
                                                        stu.sgrade=grade1   # 关联 对象
                                                        stu.save()



                                    关联对象 ：  获取关联对象集合   ：
                                                                        需求  获取python 班级的所有学生

                                                                        对象名.关联的类名_set.all()

                                                                        例如： grade1.students_set.all()
                                                                        
                                                                        
                                  创建一个邓家佳属于python01班级      
                                                                  
                                            列如:  stu3=grade1.students_set.create(sname=u'邓家佳',sgender=True,scontend='我是一个演员啊',sage=36)


















 4 启动服务器         格式: python manage.py runserver ip：port

               ip 可以不写   不写的话代表本地ip

                                      端口默认是8000

                                      执行  python manage.py runserver   开启djiango服务器

                                      http://127.0.0.1:8000/
                                      
                                      说明 ： 这是一个纯python 写的轻量级web服务器 仅仅开发测视使用









5站点管理(Admin)                  概述:  01 内容发布     负责添加    修改  删除内容

                                      02 公告访问   

                                   配置Admin应用 :

                                             在setting文件中的INSTALLED_APPS中添加
                        'django.contrib.admin',  默认是自动添加


                                 创建管理员用户:  

                                     执行:  python  manage.py  createsuperuser

                                       例如用户名 loverto
                                       密码      1234567890a
                                       http://127.0.0.1:8000/admin/

                                       汉化:  在setting文件中修改成

                                             LANGUAGE_CODE = 'zh-Hans'

                                             TIME_ZONE = 'Asia/Shanghai'

                                管理数据表:

                                           在myApp文件中修改admin 文件
                                            from .models import Grades,Student

                                            # 注册:
                                            admin.site.register(Grades)
                                            admin.site.register(Student) 


                              自定义管理界面 :

                                         属性说明（列表页）: 
                                                             list_dispaly=[]     显示字段
                                                             list_filter=[]     过滤字段
                                                             search_fields=[]   搜索字段
                                                             list_per_page=     分页


                                         添加修改页属性:

                                                          fields=[]    是来规定的属性的先后顺序
                                                          fieldsets=[]   给属性分组

                                                             fields 和 fieldsets不能同时使用




                       