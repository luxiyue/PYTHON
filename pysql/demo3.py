import pymysql

# 打开数据库连接(ip,用户名，密码,数据库实例)
db = pymysql.connect("localhost", "root", "root", "mp")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# sql = """
# insert into aa values (2,1.1,"wdwd")
# """

sql = " insert into aa values (%s,%s, '%s' )" % (5,2.1,'oio')


try:
    #执行sql
    cursor.execute(sql)
    #提交到数据库执行
    db.commit()
    print("操作成功！！！")
except:
    #如果发生错误则回滚
    db.rollback()
    print("添加失败，已经回滚！")


#关闭数据库
cursor.close()