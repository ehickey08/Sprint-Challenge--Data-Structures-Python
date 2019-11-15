import time

from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

'''
Binary Search Tree: took 0.048 seconds
duplicates = []
bst = BinarySearchTree(names_1[0])
for name in names_1[1:]:
    bst.insert(name)

for name_2 in names_2:
    if bst.contains(name_2):
        duplicates.append(name_2)
'''


'''
This took 5.5 seconds
duplicates = []
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)
'''

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

