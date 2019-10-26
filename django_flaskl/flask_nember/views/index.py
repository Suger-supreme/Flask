
from ..public.mysql import Mysqls
from ..public.md5 import md5
from flask import Blueprint,redirect,render_template,session,request
dex= Blueprint('aaaasQWQaa',__name__)


@dex.before_request
def process_request():
    if not session.get("user_info"):
        return redirect("/login/")
    return None




@dex.route('/home/')
def show():
    return render_template("homes.html")





@dex.route('/user_list/')
def user_list():
     obj=Mysqls()
     data=obj.get_all("SELECT id,user,supname FROM userinfo", [])
     return  render_template("user.html",data_list=data)







@dex.route('/detail/<int:nid>/')
def detail(nid):
    obj = Mysqls()
    record_list = obj.get_all("SELECT id,line,ctime FROM record where user_id=%s", (nid,))
    print(record_list)
    return  render_template("edit.html",record_list=record_list )








#
# @dex.route('/uploads/',methods=["GET","POST"])
# def uploads():
#     if request.method=="GET":
#            return  render_template("uploads.html")
#     from werkzeug.datastructures import FileStorage
#     file_obj = request.files.get('code')
#     print(file_obj.filename)    # 上传的文件名
#     print(file_obj.stream)        # 上传的文件内容  内容是封装到对象里面的
#     # file_obj.save("lalal")           # 上传文件进行保存
#     # file_obj.save(file_obj.filename)  # 上传文件进行保存
#     file_path = os.path.join("files", file_obj.filename)    # 上传的路径     获取上传文化写到入到本地服务器
#     file_obj.save(file_path)     # 从file_obj.stream中读取内容，写入到文件
#     return  "aaa"
#
# 3. 解压文件
# """
# import shutil
# shutil._unpack_zipfile(r"E:\wupeiqi\s9\homework-晓强\homework\files\luffy-vue简单示例（一）.zip",r"E:\wupeiqi\s9\homework-晓强\homework\xxx")
#
#                              参数: 解压 文件     解压到指定目
# """
#



import shutil
import  os,uuid
@dex.route('/uploads/',methods=["GET","POST"])
def uploads():
    if request.method=="GET":
           return  render_template("uploads.html")
    from werkzeug.datastructures import FileStorage
    file_obj = request.files.get('code')

    # 1. 检查上传文件后缀名
    name_ext = file_obj.filename.rsplit('.', maxsplit=1)     # 切开是一个列表  ['aa', 'txt']
    if len(name_ext) != 2:     #   没有后缀
        return "请上传zip压缩文件"
    if name_ext[1] != 'zip':
        return "请上传zip压缩文件"


     # """
     #  # 2. 接收用户上传文件,并写入到服务器本地.
     #  file_path = os.path.join("files",file_obj.filename)
     #  # 从file_obj.stream中读取内容，写入到文件
     #  file_obj.save(file_path)
     #
     #  # 3. 解压zip文件
     #  import shutil
     #  # 通过open打开压缩文件，读取内容再进行解压。
     #  shutil._unpack_zipfile(file_path,'xsadfasdfasdf')
     #  """
   # 2+3, 接收用户上传文件，并解压到指定目录
    target_path = os.path.join('upfile', str(uuid.uuid4()))     # files\91b25a49-fdc1-4059-8022-10b1e96ad218    使用uuid是为了防止上传文件重复
    shutil._unpack_zipfile(file_obj.stream, target_path)




      # aa = os.walk(r"C:\Users\86173\Desktop\22\2\项目配置")
    # for base_path, folder_list, file_list in aa:
    #     print(base_path)
    #     print(folder_list)
    #     print(file_list)
    #
    # os.walk - - 是你所要遍历的目录的地址, 返回的是一个三元组(root, dirs, files)。
    #
    # base_path
    # 所指的是当前正在遍历的这个文件夹的本身的地址
    # folder_list
    # 是一个
    # list ，内容是该文件夹中所有的目录的名字(不包括子目录)
    # file_list
    # 同样是
    # list, 内容是该文件夹中所有的文件(不包括子目录)




    # 4. 遍历某目录下的所有文件  统计代码行数数
    # for item in os.listdir(target_path):
    #     print(item)
    total_num = 0
    for base_path, folder_list, file_list in os.walk(target_path):
        print(base_path,"111")
        print(folder_list,"222")
        print(file_list,"333")

        for file_name in file_list:
            file_path = os.path.join(base_path, file_name)
            file_ext = file_path.rsplit('.', maxsplit=1)
            print(file_ext,"22222222")
            if len(file_ext) != 2:
                continue
            if file_ext[1] != 'py':
                continue
            file_num = 0
            with open(file_path, 'rb') as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    if line.startswith(b'#'):
                        continue
                    file_num += 1
            total_num += file_num
    print(total_num,"总数哈哈哈")


    import datetime
    ctime = datetime.date.today()
    print(total_num, ctime, session['user_info']['id'])
    obj = Mysqls()
    data = obj.get_one("select id from record where ctime=%s and user_id=%s",(ctime,session['user_info']['id']))
    if data:
        return "今天已经上传"

    obj.get_mode("insert into record(line,ctime,user_id)values(%s,%s,%s)", (total_num, ctime, session['user_info']['id']))
    return "上传成功了"














