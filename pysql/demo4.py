import pymysql

# 打开数据库连接(ip,用户名，密码,数据库实例)
db = pymysql.connect("localhost", "root", "root", "mp")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

#SQl查询语句
sql = "select *from aa where id >= %s" % (3)

try:
    #执行sql语句
    cursor.execute(sql)
    #获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        id = row[0]
        Income = row[1]
        sname = row[2]
        print(" id=%s,Income=%s,sname=%s " % (id,Income,sname)  )
except:
    print("Error: unable to fetch data")

#关闭数据库链接
db.close()



