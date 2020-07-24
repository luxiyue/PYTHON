import os
fileinfo = os.stat("a.txt")
print("文件完整路劲：",os.path.abspath("a.txt"))
#输出文件的基本信息
print("索引号：",fileinfo.st_ino)
print("设备名:",fileinfo.st_dev)
print("文件大小：",fileinfo.st_size,"字节")
print("最后一次访问时间",fileinfo.st_atime)
print("最后一次修改的时间:",fileinfo.st_mtime)
print("最后一次状态变化的时间：",fileinfo.st_ctime)