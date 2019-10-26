




1 视图基本使用 :     
               
               概述:在djiango中视图对应web请求进行回应




               视图定义：
                       from django.http import HttpResponse
                       def index(request):
                        return HttpResponse("欢迎老到djiango的页面啊哈哈哈哈哈")



               配置url: 修改webpyton文件下的urls.py文件
                          from django.conf.urls import url,include
                          from django.contrib import admin
                          urlpatterns = [
                          url(r'^admin/', admin.site.urls),
                          url(r'^', include('myApp.urls')),]




                        在myApp应用目录下创建一个urls.py文件
                        from django.conf.urls import url
                            from . import views
                            urlpatterns = [
                                url(r'^$',views.index )
                            ]


2 创建模板目录：
                概述 ： 模板是html页面   可以根据视图中传递过来的数据进行填充
                创建模板那： 创建templates目录  在目录下创建对应项目的模板目录(webpython/templates/myApp)   
         
         
         
                配置模板路径 修改settings.py文件下的        TEMPLATES
                                                'DIRS': [os.path.join(BASE_DIR,'templates')],
         
         
                定义了两个html模板       grades.html      students.html
                
                                     模板的语法:   
                                      
                                                               语法1  {{输出值,可以是变量,一个可以是对象.属性}}
                             
                                                                语法2  {%执行代码段%}
  -------------------------------------------------------------------------------------------------------------------------------                                                              
                                 http://127.0.0.1:8000/grades:                           
                                                              
                
                                                                               写: grades.html 模板 如下：
                                                        
										<!DOCTYPE html>
										<html>
											<head>
												<meta charset="UTF-8">
												<title>班级信息</title>
											</head>
											<body>
												 <h1>班级信息列表</h1>
												 <ul>
												 	{% for i in grades%}
												 	<li>
												 		<a href="#">{{i.gname}}</a>
												 	</li>
												 	{%endfor%}
												 </ul>
											</body>
										</html>
          定义视图:如下: 配置url
        
                            url(r'^grades$',views.grades),
                            
                        
                            from .models import Grades
							def grades (request):
							
							    # 01 在模型中去取数据(从模型中取出数据相当于数据库中)
							     a=Grades.objects.all()
							
							    #02 将数据传递给模板 模板在渲染页面返回给浏览器
							     return render(request,'myapp/01grades.html',{"grades":a})
							
							     pass

  -------------------------------------------------------------------------------------------------------------------------------                                                              
                 http://127.0.0.1:8000/student: 
                 
                                  写: student.html 模板 如下：
                                  
                                  <!DOCTYPE html>
									<html>
										<head>
											<meta charset="UTF-8">
											<title>学生信息</title>
										</head>
										<body>
											<h1>学生信息列表</h1>
											 <ul>
											 	 {%for s in students%}
											 	 <li>
											 		{{s.sname}}-----{{s.scontend}}
											 	 </li>
											 	 {%endfor%}
											 </ul>
										</body>
									</html>


                    定义视图:如下: 配置url
                    
                    
               url(r'^student$',views.students), 
               
                   
				#02 学生
				from .models import  Students
				def students (request):
				    # 01 在模型中去取数据(从模型中取出数据相当于数据库中)
				     b=Students.objects.all()
				    #02 将数据传递给模板 模板在渲染页面返回给浏览器
				     return render(request,'myapp/02students.html',{"students":b})
				     pass       
    -------------------------------------------------------------------------------------------------------------------------------                                            