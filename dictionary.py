# crate a dictionary with key 'rollno' and add list of rollnos , similaryly add 'name' key and add 5 names in that key
# dict = {'rollno': [1, 2, 3, 4], 'name': ['rohil', 'sujal', 'prasamsha', 'samir']}
# roll = dict['rollno']
# nam = dict['name']
# data = input('enter your rollno')
# temp = 0
# for i in range(len(roll)):
#     if roll[i] == data:
#         temp=i
# print(nam[temp])

#print key and its value as square of its keys
# d=dict()
# for x in range(1,5):
#     d[x] = x ** 2
# print(d)

#merge dictionary
# d1 = {'a':100, 'b':200}
# d2 = {'x':300, 'y':200}
# d = d1.copy()
# d.update(d2)
# print(d)

#create a dict, add datas like roll.no,name, marks, along with gender, now i want to print all the names and marks whose gender is male, how would you do that ?
d1 = {'roll':[1,2,3,4],'names':['jajo','rohila','suzal','nimesh'],'age':[18,23,45,56],'gen':['male','female','male','male']}
for i in range(len(d1['roll'])):
        if d1['gen'][i] == 'male':
            print(d1['age'][i])
            print(d1['names'][i])