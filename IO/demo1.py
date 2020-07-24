# file = open("a.txt",'r',encoding="UTF-8")
# print(file.read())

# file = open("a.txt","w",encoding="UTF-8")#w表示覆盖  a表示追加
# file.write("11111")
# file.close()

# with open('a.txt') as file:
#     print(file.read())

# with open("a.txt",'r',encoding="UTF-8") as file:
#     file.seek(3)# 将指针移动到三字符长度的地方
#     string = file.read(3)#往后读取三个字符 ,如果不写参数则读取后面的所有信息
#     print(string)


# with open('a.txt','r',encoding="UTF-8") as file:
#     num  = 0
#     while True:
#         num += 1
#         line = file.readline()
#         if line =='':
#             break
#         print(num,line,end='\n')


# with open("a.txt",'r',encoding="UTF-8") as file:
#     message = file.readlines()#这个和read()方法的不同之处在于，这个会将读取到的数据封装成列表
#     print(message)
#     for m in message:
#         print(m)

