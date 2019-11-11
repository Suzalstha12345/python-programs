# #iteration in dictionaries
# maths = {'john':88.0,'sam':77.0}
# for key in maths.keys():
#     print(key)
# maths = {'john':88.0,'sam':77.0}
# for value in maths.values():
#     print(value)

#add key and value to exixting dictionary
# d = {'no1':10, 'no2':20}
# print(d)
# d2 = {'no3':30, 'no4':30}
# d.update(d2)
# print(d)

#concatinate multiple dictionaries
# dict1 = {'no1':10, 'no2':20}
# dict2 = {'no3':10, 'no4':20}
# dic4 = {}
# for d in (dict1, dict2):
#      dic4.update(d)
# print(dic4)

#check weather key is present or not
dict = {}
key1 = 'something'
if key1 in dict:
    print('key is present in the dictionary')
else:
    print('key is not present in the dictionary')
