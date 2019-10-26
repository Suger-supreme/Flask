




1  视图 (views):



         01 概述 ： 

            作用: 视图接收web请求 并响应web请求

            本质： 视图就是一个python 中的函数


            响应：   网页 -------------重定向

                                      错误视图   404     500


                     json数据


        02 url配置：
                   配置流程:
                           定制根级url配置文件  ssettings文件中的 例如:   ROOT_URLCONF = 'webpython.urls' 默认配置好了的




                   urlpatterns : 一个url实例的列表

                                url对象 :     正则表达式                 例如： url(r'^$',views.index),
                                                                              url(r'^student$',views.students),

                                              视图名称

                                              名称


                  url匹配注意事项：    如果想要从url中获取一个值 需要对正则加小括号

                                      匹配正则前方不需要加反斜杠

                                      则在需要加r表示字符字符串不转义


                  引入其他url配置：

                                 在应用中创建urls.py文件 定义应用的url配置 在工程urls.py文件中使用include()方法

                                                                           例如：

                                                                             url(r'^admin/', admin.site.urls),
                                                                             url(r'^', include('myApp.urls')),

                                 url(r'^', include('myApp.urls',namespace="myapp"))




2 URL的反向解析：

               概述: 如果在视图 模板中使用了硬编码 在url配置发送改变时 动态生成连接的地址

               解决思路: 在使用用链接 通过url配置的名称 动态生成url1地址

               作用: 使用url模板



          





3  视图函数：

        01 定义视图 :
                    本质:一个函数

                    视图参数：     request请求对象实例  

                                  通过正则表达式获取参数

                    位置:         一般 在views文件下




        02 错误视图         404视图            早不到网页时就是早不到url

                                              {{request_path}} 导致错误的网址

                                              在templates(模板)下定义404.html



                          配置404页面:         在settings.py文件中

                                               DEBUG = True      如果为True 永远也不会调用404页面
                                               ALLOWED_HOSTS = []





                           500视图             在视图代码中出现错误（服务器代码）


                           400视图             错误出现在客服端的操作




4 request对象(请求):

                    概述: 服务器接收http请求后 会根据报文创建HttpRequest对象

                          视图的第一个参数就是 HttpRequest 对象

                          djiango 创建的  之后调用视图传递给视图
                 
                   request(属性)

                           path   请求的完整的路径(不包括域名和端口)

                           method    表示请求的方式  get   post

                           encoding  表示是浏览器提交的数据编码方式 一般是utf-8

                           GET       类似于字典的对象 它包含了get请求的所有参数

                           POST     类似于字典的对象 包含了post请求的所有参数

                           FILES   类似于字典的对象  它是包含了所有上传的文件

                           COOKIES   就是字典 包含所有cookies

                           sesion   类似于字典的对象  表示当前对话

                           方法:
                                   is_ajax()   如果是通过xmlHttpRequest 发起的   返回True   







5 QueryDict对象:

                request对象中GET POST   都属于QueryDict对象

                方法:

                       get()          作用: 根据键值获取                    只能获取一个值 

                                                例如:  www.lover.aa/abc?a=1&b=2&c=3


                       getlist()           将建的值以列表的形式返回           获取多个值
                                                 
                                                 例如:  www.lover.aa/abc?a=1&b=2&c=3










6 GET属性:

           获取浏览器传递给服务器的数据
           http://127.0.0.1:8000/lover/get1

           http://127.0.0.1:8000/lover/get1?a=1&b=2&c=3

            # #01 获取GET传递的数据
            def get1(request):
                # http://127.0.0.1:8000/lover/get1?a=1&b=2&c=3
                # 1 2 3
                 a=request.GET.get('a')
                 b=request.GET.get('b')
                 c=request.GET.get('c')
                 return HttpResponse(a+" "+b+" "+c)





              #02获取GET传递的数据(键值获取)
              def get2 (request):
                  a=request.GET.getlist('a')
                  a1=a[0]
                  a2=a[1]

                  c=request.GET.get('c')
                  return HttpResponse(a1+" "+a2+" "+c)








      










7 POST属性:   使用表单模拟psot数据

             post 注释掉settings中
             MIDDLEWARE = [
                  'django.middleware.security.SecurityMiddleware',
                  'django.contrib.sessions.middleware.SessionMiddleware',
                  'django.middleware.common.CommonMiddleware',
                  # 'django.middleware.csrf.CsrfViewMiddleware',
                  'django.contrib.auth.middleware.AuthenticationMiddleware',
                  'django.contrib.messages.middleware.MessageMiddleware',
                  'django.middleware.clickjacking.XFrameOptionsMiddleware',
              ]
         


              # POST

              # 01显示页面
              def showreg(request):
                  return render(request,"html_app/02regist.html")

              #02获取表单注册信息  服务器返回数据
              def reg(request):
                   name=request.POST.get("aa")
                   sex=request.POST.get("sex")
                   age=request.POST.get("age")
                   hobby=request.POST.get("hobby")

                   print(name)
                   print(sex)
                   print(age)
                   print(hobby)
                   return HttpResponse("POST")









8 HttpResponse(对象):

                  概念: 给浏览器返回数据

                  request 对象是由django创建的    HttpResponse 对象是程序员创建的


                   用法:  

                       1 不掉用模板直接返回数据
                          def index(request):
                                return HttpResponse("欢迎老到djiango的页面啊哈哈哈哈哈1111111111111111111111111111111")



                       2 掉用模板 使用render方法:
                                          
                                         01 原型 : render(request,templatesName [content])


                                         02 作用:  结合数据模板  返回html对象


                                         03 参数:   
                                                request    请求对象

                                                templatesName  模板路径

                                                [context]       传递需要渲染模板上的数据




                                          04 实例：
                                               def showreg(request):
                                                         return render(request,"html_app/02regist.html")


                       3  属性:

                                   content  表示返回的内容

                                   charset 编码格式

                                   status code   状态   200  304 404

                                   content.type   指定输出MIME类型


                       4 方法:

                                  init     使用页面内容实例化HttpResponse对象


                                  weite:(content) 以文件的写入

                                  flush  以文件的形式刷新缓存区


                                  set_cookie(key.value="max_age=Nome.expnise=None")


                                  delete_cookie(key):
                                                    删除: COOKIE

                                                    注意 ：一个不存在的key什么都没有发身


                                  HttpResponseRedirect 子类:    功能      重定向     服务器端跳转

                                             from django.http import HttpResponseRedirect

                                            """# 重定向 方法二
                                            from django.shortcuts import redirect
                                            def red1(request):
                                                return redirect('/lover/red2')
                                            def red2(request):
                                                return HttpResponse("我是重定向后的视图。。。。。。。。。。。。。")"""
                                             

                                  JSonResponse子类：  返回json数据  一般是异步请求(is_ajax)

                                                       __init__(self,data)    注意data是字典对象

                                                       注意类型为Content-type类型为appliction/json








            5 sessions(保持状态):
                                01 Http 是无状态的   每一次请求都是新的亲求 不记得上一次请求

                                02 客服端于服务器端的一次通信会话

                                03 存储的方式 :  cookie存在客服端  

                                                session存在服务器端 存储的session_id 就是key存储在服务端

                                04 状态保持的目的 ：  在一段时间跟踪请求者的状态 可以实现跨页面访问当前的数据

                                注意： 不同的请求者不会共享这个数据  请求者是一一对用的


                                启用session   在setting文件中 默认是启用的

                                              INSTALLED_APPS ['django.contrib.sessions',]

                                             MIDDLEWARE ['django.contrib.sessions.middleware.SessionMiddleware',]

                                启用session 后 每个HttpRequest对象都有一个session对象 类似于字典的对象


                                get(key,default=None)      根据这个方法获取session值

                                clear()                 清空会话

                                flush()     删除当前的会话的cookie


                                设置session过期时间:
                                        request.session.set_expiry(100)   #设置session过期时间   默认是秒
                                       set_expiry(value)

                                       时间对象

                                       0   就是关闭浏览器就过期了

                                       如果不设置时间 两周自动过期了








                                def main(request):
                                       username=request.session.get('name',"默认游客")
                                       return render(request,"html_app/03main.html",{'username':username})
                                  def login(request):
                                      return render(request,"html_app/04login.html")

                                  def showmain(request):

                                      username=request.POST.get('username')
                                      request.session.set_expiry(100)   #设置session过期时间   默认是秒
                                      print(username)
                                      # 存储session
                                      request.session['name']=username
                                      return redirect('/lover/main')

                                  # 删除session



                                  from django .contrib.auth import logout
                                  def quit(request):
                                         logout(request)

                                         # request.session.clear()
                                         
                                         # request.session.flush()

                                         return redirect('/lover/main')






9 使用redis缓存session    下载    pip install django-redis-sessions

                     # 使用redis缓存session 
                      SESSION_ENGINE='redis_sessions.session'
                      SESSION_REDIS_HOST='localhost'
                      SESSION_REDIS_PORT=6379
                      SESSION_REDIS_DB=0
                      SESSION_REDIS_PASSWORD='lvtao'
                      SESSION_REDIS_PREFIX='session'


























