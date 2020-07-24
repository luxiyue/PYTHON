import pymysql

# 打开数据库连接(ip,用户名，密码,数据库实例)
db = pymysql.connect("localhost", "root", "root", "mp")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

#SQL更新语句
sql = "Update aa set id=99 where sname = '%s'" % ("oio")

try:
    #执行SQL语句
    cursor.execute(sql)
    #提交到数据
    db.commit()
    print("修改成功！！！")
except:
    #发生错误时回滚
    db.rollback()
    print("操作失败，且已经回滚了")

# 关闭数据库连接
db.close()
