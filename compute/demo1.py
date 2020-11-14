'''
1-2020  需要多少个字符2
'''
def two():
    count = 0
    for i in range(1,2021):
        stringtemp = str(i)
        count += stringtemp.count("2")
    return count
i = two()
print(i)
