#################
#               #
# Problem Set 0 #
#               #
#################


#
# Setup
#
from typing import Counter


class BinaryTree:
    def __init__(self, root):
        self.root: BTvertex = root
 
class BTvertex:
    def __init__(self, key):
        self.parent: BTvertex = None
        self.left: BTvertex = None
        self.right: BTvertex = None
        self.key: int = key
        self.size: int = int

#
# Problem 1a
#

# Input: BTvertex v, the root of a BinaryTree of size n
# Output: Up to you
# Side effect: sets the size of each vertex n in the
# ... tree rooted at vertex v to the size of that subtree
# Runtime: O(n)
def calculate_sizes(v):
    # Your code goes here
    print("hi")
    root = BTvertex(v)
    root.size = 1
    print(root.key)
    print(root.right.key)
    if (root.left):
        counter += 1
        root.size = counter
        print(root.size)
    elif (root.right):
        counter += 1
        root.size = counter
        print (root.size)
    else:
        return root.size
    
    
calculate_sizes(4)

#
# Problem 1c
#

# Input: BTvertex r, the root of a size-augmented BinaryTree T
# ... of size n and height h
# Output: A BTvertex that, if removed from the tree, would result
# ... in disjoint trees that all have at most n/2 vertices
# Runtime: O(h)
def find_vertex(r): 
    # Your code goes here
    pass
