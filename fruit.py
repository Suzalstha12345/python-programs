#create a 3 sets of fruits, with random items, now, i need to get data how many items among the sets are repeated,
# how many of them are unique, in total get all the unrepeated items
a = {'banana', 'pineapple', 'apple'}
b = {'apple', 'straberry', 'mango'}
c = {'banana', 'apple', 'grape'}
print(a.intersection(b).intersection(c))
print(a.symmetric_difference(b).symmetric_difference(c))
print(len(a))