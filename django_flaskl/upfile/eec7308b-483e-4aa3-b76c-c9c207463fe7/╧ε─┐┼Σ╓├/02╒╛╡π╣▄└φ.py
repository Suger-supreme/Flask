
5站点管理(Admin)     概述:  01 内容发布     负责添加    修改  删除内容

                         02 公告访问   

                                                配置Admin应用 :

                                                                  在setting文件中的INSTALLED_APPS中添加
                            'django.contrib.admin',  默认是自动添加


                                                 创建管理员用户:  
                                                 
                         D:\learnPython\py14\web_Django\Web>python  manage.py  createsuperuser
                                                                 执行:  python  manage.py  createsuperuser

                                                                     例如用户名: loverto            (lovertao)
                                                                     密码 :1234567890a             (1234567890lv)
                           http://127.0.0.1:8000/admin/

                                                  汉化:  在setting文件中修改成

                                             LANGUAGE_CODE = 'zh-Hans'
                                             TIME_ZONE = 'Asia/Shanghai'

                                                管理数据表:

                                                           在myApp文件中修改admin 文件
                                            from .models import Grades,Students

                                            # 注册:
                                            admin.site.register(Grades)
                                            admin.site.register(Student) 


                                               自定义管理界面 : 例如
									from django.contrib import admin
									from .models import Grades,Students
									
									
									# 自定义管理界面
									class GradesAdmin(admin.ModelAdmin):
			
									     # 列表页属性
									     list_display= ['pk','gname','gdate','ggirlnum','gboynum','isDelete']    # 显示字段
									     list_filter= ['gname']    # 过滤字段
									     search_fields= ['gname']  # 搜索字段
									     list_per_page=5           # 分页
									     									
									     # 添加修改页属性  注意: fields 和 fieldsets不能同时使用
									     # fields=[]        # 是来规定的属性的先后顺序
									     # 
									     fieldsets=[  # 给属性分组
									              ("aa",{"fields":['ggirlnum','gboynum']}),
									              ("bb",{"fields":['gname','gdate','isDelete']}),
									     ]     																		
									 # 注册:
									admin.site.register(Grades,GradesAdmin)
									admin.site.register(Students)
									
									
									                 
									                                                      
                                                                
                                               

                                               属性说明（列表页）: 
                                                             list_dispaly=[]     显示字段
                                                             list_filter=[]     过滤字段
                                                             search_fields=[]   搜索字段
                                                             list_per_page=     分页




                                               添加修改页属性:

                                                          fields=[]    是来规定的属性的先后顺序
                                                          fieldsets=[]   给属性分组
                                           
                                                          fields 和 fieldsets不能同时使用
                                                        
                                                        
                                                        
                                                        
                                                        
                                                        
                                                        
                                                          
                                                对象关联使用                需求 ： 就是在创建一个班级时可以直接添加几个学生
												class StudentsInfo(admin.TabularInline):
												
												           model=Students
												           extra=2
                                                inlines= [StudentsInfo]    # 意思创建班级时在附带两个学生  意思加俩行
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                               布尔值显示问题(性别):     
                                                   def aa(self): # 布尔值显示问题(性别):
												        if self.sgender:
												            return "男"
												        else:
												            return "女"
												    aa.short_description="性别"    # 设置页面列的名称
												
												
												
												
												    def bb(self): # 布尔值显示问题(是否删除):
												        if self.isDelete:
												            return True 
												        else:
												            return False
												    bb.short_description="是否删除"    # 设置页面列的名称
												    
												    
												    
						# 页面执行动作的位置
						                  actions_on_top=False
    									  actions_on_top=True
												    

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
// admin 站点 页面布局   完整  使用装饰器注册
 
 from django.contrib import admin
from .models import Grades,Students


# 意思创建班级时在附带两个学生
class StudentsInfo(admin.TabularInline):

           model=Students
           extra=2

# 自定义管理界面
class GradesAdmin(admin.ModelAdmin):

     inlines= [StudentsInfo]    # 意思创建班级时在附带两个学生  意思加俩行

     # 列表页属性
     list_display= ['pk','gname','gdate','ggirlnum','gboynum','isDelete']    # 显示字段
     list_filter= ['gname']    # 过滤字段
     search_fields= ['gname']  # 搜索字段
     list_per_page=5           # 分页       表示5数据个一页

     # 添加修改页属性  注意: fields 和 fieldsets不能同时使用
     # fields=[]        # 是来规定的属性的先后顺序
     # 
     fieldsets=[  # 给属性分组
              ("aa",{"fields":['ggirlnum','gboynum']}),
              ("bb",{"fields":['gname','gdate','isDelete']}),
     ]     

 # 注册:
admin.site.register(Grades,GradesAdmin)

          

@admin.register(Students)

class StudentsAdmin(admin.ModelAdmin):

    def aa(self): # 布尔值显示问题(性别):
        if self.sgender:
            return "男"
        else:
            return "女"
    aa.short_description="性别"    # 设置页面列的名称

    def bb(self): # 布尔值显示问题(是否删除):
        if self.isDelete:
            return 1
        else:
            return 0
    bb.short_description="是否删除"    # 设置页面列的名称


    list_display=['pk','sname','sage',aa,'scontend','sgrade',bb]
    list_per_page=3   

# 页面执行动作的位置
    actions_on_top=False
    actions_on_bottom=True


 # 注册:
#admin.site.register(Students,StudentsAdmin)



                      