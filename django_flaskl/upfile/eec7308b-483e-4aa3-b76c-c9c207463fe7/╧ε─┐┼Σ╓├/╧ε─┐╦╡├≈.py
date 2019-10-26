import django

django.get_version()


  01. 创建项目:    输入 django-admin startproject Web


  02.查看创建项目的结构:    tree .  /F



  E:\>CD E:\Studypython\Django\web_Django

E:\Studypython\Django\web_Django>django-admin startproject webpython




E:\Studypython\Django\web_Django>tree .  /F
文件夹 PATH 列表
卷序列号为 3018-9A66
E:\STUDYPYTHON\DJANGO\WEB_DJANGO
└─webpython
    │  manage.py    
    │
    └─webpython
            settings.py   项目的配置文件       % 目前修改

            urls.py    项目的url声明           % 目前修改

            wsgi.py   项目与wsgi兼容的web服务器入口    

            __init__.py  一个空文件 它告诉python这个项目 应该被看做一python包



配置数据库 :     
             注意django 默认使用SQLite 数据库

             要使用mysql 数据库 在settings 文件中  通过DATABASES 选项进行数据库配置

             



04.配置mysql:

             python 3.x 中安装的是 PyMySQL
 
             在__init__文件中写入两行代码 :  import pymysql

                                             pymysql.install_as_MySQLdb()




05.settings中配置mysql:


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
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "a1",
        'USER': "root",
        'PASSWORD':'root',
        'HOST':'localhost',
        'PORT':'3306',

    }
}


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '数据库名(你得先在mysql中创建数据库)',
        'USER':'mysql用户名（如root）',
        'PASSWORD':'密码（如123456789）',
        'HOST':'域名（127.0.0.1或localhost）',
        'PORT':'端口号（3306）',
    }
}

06.创建应用  ： 在一个项目中 可以创建多个应用 每个应用进行一种业务处理

                打开黑屏终端进入webpython 目录下的 webpython 目目录


                执行  python manage.py startapp  myapp