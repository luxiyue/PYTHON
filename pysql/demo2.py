import pymysql

# 打开数据库连接(ip,用户名，密码,数据库实例)
db = pymysql.connect("localhost", "root", "root", "mp")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

cursor.execute("Drop table if exists AA")

#使用预处理语句创建表
sql = """
create table AA(
id int primary key,
Income float,
sname varchar(10)
)
"""

cursor.execute(sql)
print("创建成功！！！")
cursor.close()