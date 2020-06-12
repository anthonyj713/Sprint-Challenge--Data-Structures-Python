import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements

# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


class Name:
    def __init__(self, names):
        self.names = names
        self.left = None
        self.right = None
  
    def insert(self, names):
        if names < self.names:
            if self.left is None:
                self.left = Name(names)
            else:
                self.left.insert(names)
        elif names >= self.names:
            if self.right is None:
                self.right = Name(names)
            else:
                self.right.insert(names)
       
    def contains(self, names):
        if self.names == names:
            return True
        if self.names < names:
            if self.right is None:
                return False
            else:
                return self.right.contains(names)
        if self.names > names:
            if self.left is None:
                return False
            else:
                return self.left.contains(names)

tree = Name(names_1[0])
for name in names_1:
    tree.insert(name)

for name in names_2:
    # for list 2 compared to tree 1
    if tree.contains(name):
        duplicates.append(name)
    
end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
