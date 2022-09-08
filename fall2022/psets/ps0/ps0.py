#################
#               #
# Problem Set 0 #
#               #
#################


#
# Setup
#


#from turtle import left, right


class BinaryTree:
    def __init__(self, root):
        self.root: BTvertex = root
 
class BTvertex:
    def __init__(self, key):
        self.parent: BTvertex = None
        self.left: BTvertex = None
        self.right: BTvertex = None
        self.key: int = key
        self.size: int = None

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
    if v == None:
        return 0
    v.size = calculate_sizes(v.left) + calculate_sizes(v.right) + 1
    return(v.size)


    

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
    if r != 0:
        tree_sz = r.size 
    else:
        tree_sz = 0
    def vertex_finder(r):
        if r is None:
            return r
        if r.left != 0:
            l_subtree_sz = r.left.size
        else: 
            l_subtree_sz = 0
        if r.right != 0:
            r_subtree_sz = r.right.size
        else:
            r_subtree_sz = 0
        parent_subtree_sz = tree_sz - r.size
        n = l_subtree_sz + r_subtree_sz + parent_subtree_sz + 1
        if max(l_subtree_sz, r_subtree_sz, parent_subtree_sz) <= n/2:
            return r
        else:
            if l_subtree_sz >= r_subtree_sz:
                return vertex_finder(r.left)
            else:
                return vertex_finder(r.right)
    return vertex_finder(r)
   
