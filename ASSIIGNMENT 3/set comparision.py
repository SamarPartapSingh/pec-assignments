set1 = set([1, 2, 3, 4, 5])
set2 = set([2, 4, 6, 8])
set3 = set([1, 5, 9, 13, 17])

print(set1.intersection(set2))

print(set1.intersection(set2.intersection(set3)))

print(set1.intersection(set2).union(set2.intersection(set3).union(set3.intersection(set1))))

print(set([1,2,3,4,5,6,7,8,9,10]).difference(set1))

print(set([1,2,3,4,5,6,7,8,9,10]).difference(set1.union(set2.union(set3))))