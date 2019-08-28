from flask import Flask
from flask import Flask,request,render_template
import student_dao
import tkinter

import tkinter.messagebox
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('login.html')
@app.route('/login2')
def login2():
    return render_template('login2.html')
@app.route('/adds')
def adds():
    return render_template('welcome_admin.html')
@app.route('/addb')
def addb():
    return render_template('addbook.html')
@app.route('/addBFail')
def addBFail():
    result=student_dao.loadBookAll()
    return render_template('index2.html',results=result)

@app.route('/select', methods=['GET', 'POST'])
def select():
    number= request.form.get('username')
    print('sssssss'+number)
    results=student_dao.student_num(int(number))
    if results==None:
        tkinter.messagebox.showinfo('提示', '尚未注册')
        return render_template('login.html')
    else:
        results = student_dao.loadBookAll()
        return render_template('index2.html', results=results,re=number)
@app.route('/selectp', methods=['GET', 'POST'])
def selectp():
    number= request.form.get('username')
    password= request.form.get('password')
    print('aaaaa'+number)
    print('aaaaa'+password)
    results=student_dao.admin_num(int(number))
    print("555"+str(results))
    if results==None:
        tkinter.messagebox.showinfo('提示', '尚未注册')
        return render_template('login2.html')
    for item in results:
        if item[0]==password:
           print(item[0])
           print("33333333333")
           return render_template('welcome_admin.html')
        else:
          tkinter.messagebox.showinfo('提示', '密码错误')
          return render_template('login2.html')
@app.route('/addStudent',methods=['GET','POST'])
def addStudent():
    num = request.form.get('number')
    print(num)
    name = request.form.get('name')
    sex = request.form.get('sex')
    grade = request.form.get('grade')
    results=student_dao.selectS(num)
    print("QQQ"+str(results))
    if str(results)=="()":
      student_dao.insert_student(num, name,sex,grade)
      return render_template('success.html')
    else:
      return render_template('fail.html')

@app.route('/add1success',methods=['GET','POST'])
def add1suceess():
    return render_template('welcome_admin.html')
@app.route('/addBook',methods=['GET','POST'])
def addBook():
    num = request.form.get('number')
    print(num)
    name = request.form.get('name')
    price = request.form.get('price')
    author = request.form.get('author')
    results=student_dao.selectB(num)
    print("QQQ"+str(results))
    if str(results)=="()":
      student_dao.insert_student(num, name,price,author)
      return render_template('success2.html')
    else:
      return render_template('fail2.html')
@app.route('/add2success',methods=['GET','POST'])
def add2suceess():
    return render_template('addbook.html')
@app.route('/selectR',methods=['GET','POST'])
def selectR():
    type = request.form.get('type')
    if type=="number":
        number=request.form.get('content')
@app.route('/selectBook',methods=['GET','POST'])
def selectBook():
    number2 = request.args['numberS']
    name = request.form.get('name')
    print(name)
    results = student_dao.loadBook(name)
    print("DDDDD"+str(results))
    return render_template('index2.html', results=results,re=number2)
@app.route('/jieyue')
def jieyue():
    number = request.args['number']
    number2=request.args['numberS']
    results=student_dao.selectBS(number)
    print(str(results))
    if str(results) == "(('已借阅',),)":
        return render_template('yijieyue.html')
    else:
       student_dao.updateS(number,number2)
       results = student_dao.loadBookAll()
    print(results)
    return render_template('index2.html', results=results,re=number2)
@app.route('/selectRead')
def selectRead():
    number2 = request.args['numberS']
    results=student_dao.selectSRead(number2)
    return render_template('selectBS.html', results=results, re=number2)
@app.route('/s')
def s():
    number2 = request.args['numbers']
    results=student_dao.selectSRead(number2)
    return render_template('index2.html', results=results, re=number2)
if __name__ == '__main__':
    app.run()
