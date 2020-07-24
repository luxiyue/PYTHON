import os
import shutil

# print(os.getcwd())#输出当前目录
# print(os.path.abspath(r"a.txt"))#绝对路径
# print(os.path.abspath(r"wwww"))#乱写也可以
#
# print(os.path.join("W:\dw","aaa"))#拼接路径
#
# #判端目录是否存在
# print(os.path.exists(os.getcwd()))
# print(os.path.exists("D:\\AAAAAAAAA"))


path= "E:\\文件\\python\\IO\\b"
#创建目录
# if not os.path.exists(path):
#     os.mkdir(path)
#     print("目录创建成功！")
# else:
#     print("该目录已经存在！")
#如果想要创建多级目录就用mkdirs

#删除目录
# os.rmdir(path)#注意rmdir只能删除空目录
#如果想要删去非空目录：
# shutil.rmtree(path)

#遍历目录
# tuples = os.walk("E:\文件\python\IO")  #该函数只能在Windows 和UNIX 操作吸引上生效
# for i in tuples:
#     print(i)
# for root,dirs,files in os.walk("E:\文件\python\IO",topdown=True):
#     print(root)
#     print(dirs)
#     print(files)
#     for i in files:
#         print(i)


#删除文件
# path="b.txt"
# if os.path.exists(path):
#     os.remove("b.txt")
#     print("文件删除完毕")
# else:
#     print("文件不存在！！")


#文件目录的重命名：
# src = "E:\\文件\\python\\IO\\b.txt"
# dst = "E:\\文件\\python\\IO\\pp.txt"
# if os.path.exists(src):
#     os.rename(src,dst)
#     print("文件重命名完成！！")
# else:
#     print("文件不存在！！！")



#运行电脑上的软件
os.system(u"G:\\qqmusic\\QQMusic.exe")