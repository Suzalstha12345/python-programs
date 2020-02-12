from copy import deepcopy

tup = ([], 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
newTup = deepcopy(tup)
newTup[0].append("Mine")

print(newTup)

