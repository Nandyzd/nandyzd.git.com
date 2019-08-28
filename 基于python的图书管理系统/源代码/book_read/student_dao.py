
import pymysql

#查询学生密码
def student_num(number):
    db = pymysql.connect(host='localhost', user='root', passwd='root', db='book', port=3306,
                         charset='utf8')
    conn = db.cursor()  # 获取指针以操作数据库
    conn.execute('set names utf8')
    sql ="select password from student_t where student_num=%d" % number#查询所有信息
    print(sql)
    a ='00000'
    try:
        conn.execute(sql)
        # 执行sql语句
        one = conn.fetchone()
        return one
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()
        return a
    # 关闭数据库连接
    db.close()
#查询管理员密码
def admin_num(number):
    db = pymysql.connect(host='localhost', user='root', passwd='root', db='book', port=3306,
                         charset='utf8')
    conn = db.cursor()  # 获取指针以操作数据库
    conn.execute('set names utf8')
    sql ="select password from admin_t where admin_num=%d" % number#查询所有信息
    print(sql)
    a ='00000'
    try:
        conn.execute(sql)
        # 执行sql语句
        one = conn.fetchall()
        return one
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()
        return a
    # 关闭数据库连接
    db.close()
#插入学生信息
def insert_student(num,name,sex,grade):
    db = pymysql.connect(host='localhost', user='root', passwd='root', db='book', port=3306,
                         charset='utf8')
    conn = db.cursor()  # 获取指针以操作数据库
    conn.execute('set names utf8')
    password="1111111"
    t=(int(num),name,sex,grade,password)
    sql = "INSERT INTO student_t(student_num,student_name,sex,grade,password) values('%d','%s','%s','%s','%s')" % t # 查询所有信息
    print(sql)
    a = '00000'
    try:
        conn.execute(sql)
        # 执行sql语句
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()
    # 关闭数据库连接
    db.close()
def selectS(num):
    db = pymysql.connect(host='localhost', user='root', passwd='root', db='book', port=3306,
                         charset='utf8')
    conn = db.cursor()  # 获取指针以操作数据库
    conn.execute('set names utf8')
    sql = "select * from student_t where student_num=%d" % int(num)  # 查询所有信息
    print(sql)
    a = '00000'
    try:
        conn.execute(sql)
        # 执行sql语句
        one = conn.fetchall()
        return one
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()
        return a
    # 关闭数据库连接
    db.close()
def selectB(num):
    db = pymysql.connect(host='localhost', user='root', passwd='root', db='book', port=3306,
                         charset='utf8')
    conn = db.cursor()  # 获取指针以操作数据库
    conn.execute('set names utf8')
    sql = "select * from book_t where book_num=%d" % int(num)  # 查询所有信息
    print(sql)
    a = '00000'
    try:
        conn.execute(sql)
        # 执行sql语句
        one = conn.fetchall()
        return one
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()
        return a
    # 关闭数据库连接
    db.close()
#插入图书信息
def insert_student(num,name,price,author):
    db = pymysql.connect(host='localhost', user='root', passwd='root', db='book', port=3306,
                         charset='utf8')
    conn = db.cursor()  # 获取指针以操作数据库
    conn.execute('set names utf8')
    state="未借阅"
    student_num=0
    t=(name,int(num),price,state,author,student_num)
    sql = "INSERT INTO book_t(book_name,book_num,price,state,author,student_num) values('%s','%d','%s','%s','%s','%d')" % t
    print(sql)
    a = '00000'
    try:
        conn.execute(sql)
        # 执行sql语句
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()
    # 关闭数据库连接
    db.close()
def selectR_s(num):
    db = pymysql.connect(host='localhost', user='root', passwd='root', db='book', port=3306,
                         charset='utf8')
    conn = db.cursor()  # 获取指针以操作数据库
    conn.execute('set names utf8')
    sql = "select b_num from book_student where s_num=%d" % int(num)
    print(sql)
    a = '00000'
    try:
        conn.execute(sql)
        # 执行sql语句
        one = conn.fetchall()
        db.commit()
        db.close()
        for item in one:
            sql2 = "select bool_name,state from book_t where s_num=%d" % int(item[0])
            conn.execute(sql2)
            one = conn.fetchall()
            db.commit()

    except:
        # 发生错误时回滚
        db.rollback()
        return a
    # 关闭数据库连接
    db.close()
def loadBook(name):
    # 连接数据库
    db = pymysql.connect(host='localhost', user='root', passwd='root', db='book', port=3306,
                         charset='utf8')
    conn = db.cursor()  # 获取指针以操作数据库
    conn.execute('set names utf8')
    sql = "select * from book_t where book_name='%s'"%(name)
    print(sql)
    try:
        conn.execute(sql)
        # 执行sql语句
        result=conn.fetchall()
        return result
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()
        return
    # 关闭数据库连接
    db.close()
def loadBookAll():
    # 连接数据库
    db = pymysql.connect(host='localhost', user='root', passwd='root', db='book', port=3306,
                         charset='utf8')
    conn = db.cursor()  # 获取指针以操作数据库
    conn.execute('set names utf8')
    sql = "select * from book_t"#查询所有信息
    print(sql)
    try:
        conn.execute(sql)
        # 执行sql语句
        result=conn.fetchall()
        return result
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()
        return
    # 关闭数据库连接
    db.close()
def updateS(number,number1):
    # 连接数据库
    db = pymysql.connect(host='localhost', user='root', passwd='root', db='book', port=3306,
                         charset='utf8')
    conn = db.cursor()  # 获取指针以操作数据库
    conn.execute('set names utf8')
    str="已借阅"
    t=(str,int(number1),int(number))
    sql = "update book_t set state = '%s',student_num='%d' where book_num = '%d'" % t
    print(sql)
    try:
        conn.execute(sql)
        # 执行sql语句
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()
    # 关闭数据库连接
    db.close()
def selectBS(number):
    db = pymysql.connect(host='localhost', user='root', passwd='root', db='book', port=3306,
                         charset='utf8')
    conn = db.cursor()  # 获取指针以操作数据库
    conn.execute('set names utf8')
    sql = "select state from book_t where book_num='%d'" %int(number) # 查询所有信息
    print(sql)
    try:
        conn.execute(sql)
        # 执行sql语句
        result = conn.fetchall()
        return result
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()
        return
    # 关闭数据库连接
    db.close()
def selectSRead(number):
    db = pymysql.connect(host='localhost', user='root', passwd='root', db='book', port=3306,
                         charset='utf8')
    conn = db.cursor()  # 获取指针以操作数据库
    conn.execute('set names utf8')
    sql = "select * from book_t where student_num='%d'" %int(number) # 查询所有信息
    print(sql)
    try:
        conn.execute(sql)
        # 执行sql语句
        result = conn.fetchall()
        return result
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()
        return
    # 关闭数据库连接
    db.close()