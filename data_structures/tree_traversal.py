class Node():
    name = None
    left = None
    right = None
    
    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right = right

    def in_order(self, node):
        # left, root, right, at each node
        if node != None:
            # visit left
            self.in_order(node.left)
            # print self (root)
            print(node.name)
            # finally, visit right
            self.in_order(node.right)

    def pre_order(self, node):
        # visit current node, then child nodes, left to right
        if node != None:
            print(node.name)
            self.pre_order(node.left)
            self.pre_order(node.right)

    def post_order(self, node):
        # visit current AFTER child nodes
        if node != None:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.name)

'''
          root
    child1    child2
            child3
'''

child1 = Node('child1', None, None)
child3 = Node('child3', None, None)
child2 = Node('child2', child3, None)
root = Node('root', child1, child2)

print('in order')
root.in_order(root)
print('pre-order')
root.pre_order(root)
print('post-order')
root.post_order(root)
