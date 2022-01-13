""" 生成式 """

# 列表生成式
list1 = ['simon_dsb','tom_dsb','jack','rose_dsb']
# new_list = []
# for name in list1:
#     if name.endswith('dsb'):
#         new_list.append(name)
# print(new_list)
new_list = [name for name in list1 if name.endswith('dsb')]
print(new_list)

# 把所有的小写字母全变成大写
list2 = [name.upper()for name in list1]
list3 = [name.title()for name in list1]
print(list2)
print(list3)
# 去掉名字中的_
list4 = [name.replace('_','')for name in list1]
print(list4)
