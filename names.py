import time
start_time = time.time()
f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()
f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()
names = names_1 + names_2
#----RUNTIME COMPLEXITY

import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack
from doubly_linked_list import *

class BinarySearchTree:
        def __init__(self, value):
                self.value = value
                self.left = None
                self.right = None

        def insert(self, value):
                if self == None:
                        BinarySearchTree(value)
                elif self.value < value:
                        if self.right == None:
                                self.right = BinarySearchTree(value)
                        else:
                                return self.right.insert(value)
                else:
                        if self.left == None:
                                self.left = BinarySearchTree(value)
                        else:
                                return self.left.insert(value)


        # Return True if the tree contains the value
        # False if it does not
        def contains(self, target):
                if self == None:
                        return False
                elif self.value == target:
                        return True
                elif self.value < target:
                        if self.right:
                                return self.right.contains(target)
                        return False
                else:
                        if self.left:
                                return self.left.contains(target)
                        return False


        # Return the maximum value found in the tree
        def get_max(self):
                if self == None:
                        return None
                elif self.right == None:
                        return self.value
                else:
                        return self.right.get_max()

        # Call the function `cb` on the value of each node
        # You may use a recursive or iterative approach
        def for_each(self, cb):
                cb(self.value)
                if self.left:
                        self.left.for_each(cb)
                if self.right:
                        self.right.for_each(cb)

        def in_order_print(self, node):
                dfts = Stack()
                order = []
                current = node
                dfts.push(current)
                while dfts.len() > 0:
                        order.append(dfts.storage.head.value.value)
                        dfts.pop()
                        if current.right != None:
                                dfts.push(current.right)
                        if current.left != None:
                                dfts.push(current.left)
                        if dfts.storage.head != None:
                                current = dfts.storage.head.value
                for i in sorted(order):
                        print(i)

        def bft_print(self, node):
                bfts = Queue()
                current = node
                bfts.enqueue(node)
                while bfts.len() > 0:
                        print(current.value)
                        bfts.dequeue()
                        if current.left:
                                bfts.enqueue(current.left)
                        if current.right:
                                bfts.enqueue(current.right)
                        if bfts.storage.head != None:
                                current = bfts.storage.head.value
        def dft_print(self, node):
                dfts = Stack()
                current = node
                dfts.push(current)
                while dfts.len() > 0:
                        print(dfts.storage.head.value.value)
                        dfts.pop()
                        if current.left:
                                dfts.push(current.left)
                        if current.right:
                                dfts.push(current.right)
                        if dfts.storage.head != None:
                                current = dfts.storage.head.value



        def pre_order_dft(self, node):
                global stacka
                current = node
                stacka.push(current)
                while stacka.len() > 0:
                        print(current.value)
                        stacka.pop()
                        if current.left != None:
                                self.pre_order_dft(current.left)
                        if current.right != None:
                                self.pre_order_dft(current.right)
                if current == None:
                        return

        # Print Post-order recursive DFT
        def post_order_dft(self, node):
                current = node
                if current.left:
                        self.post_order_dft(current.left)
                if current.right:
                        self.post_order_dft(current.right)
                print(current.value)
'''
I suspect that because it includes two for loops that both fully complete 
(ie. no chopping-up of one list like we had that one week) then i suspect this original solution is O(n^2),
where n represents a list, and the exponent representing number of lists.
'''
stacka = Stack()
duplicates = []
#for name_1 in names_1:
#    for name_2 in names_2:
#        if name_1 == name_2:
#            duplicates.append(name_1)
find = BinarySearchTree(names_1[0])
names_1.pop(0)
for i in names_1:
        find.insert(i)
for i in names_2:
        if find.contains(i):
                duplicates.append(i)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

