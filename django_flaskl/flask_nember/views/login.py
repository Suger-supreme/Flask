
from ..public.mysql import Mysqls
from ..public.md5 import md5
from flask import Blueprint,redirect,render_template,session,request
lg = Blueprint('loghe',__name__)
@lg.route('/login/',methods=["GET","POST"])
def user():
    if request.method=="GET":
        return  render_template("login.html")
    username=request.form.get("user")
    print(username)
    pwd=request.form.get("pwd")

    obj=Mysqls()
    data = obj.get_one("select id,supname from userinfo where  user=%s and pwd=%s",(username,pwd))
    if not data:
         return render_template('login.html', error='用户名密码错误')
    session['user_info'] = {'id':data['id'],'supname':data['supname']}
    return redirect('/home/')

@lg.route('/logout/')
def logout():
   if 'user_info' in session:
       del  session['user_info']
   return redirect('/login/')