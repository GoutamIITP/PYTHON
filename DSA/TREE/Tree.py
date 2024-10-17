''' Write a pyhton code with create a tree:
    => count no of node which having only one chile 
    => Display all node which having even number 
    => Count How many node which having exactly two child'''

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self, root= None) -> None:
        self.root = root

    def Num_of_node_one_child(self, node):
        if node is None:
            return 0
        count = 0
        if (node.left is None and node.right is not None) or (node.left is not None and node.right is None):
            count +=1
        return count + self.Num_of_node_one_child(node.left) + self.Num_of_node_one_child(node.right)
          
    def node_even(self, node):
        if node is None:
            return 0
        if node.data % 2 == 0:
            print(node.data, end = " ")
        
        self.node_even(node.left)
        self.node_even(node.right)
    def node_with_two_child(self, node):
        if node is None:
            return 0
        count = 0
        if (node.left is not None and node.right is not None):
            count +=1
        return count + self.node_with_two_child(node.left) + self.node_with_two_child(node.right)
    



root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(8)
root.right.right = Node(18)

tree = Tree(root)

print("Nodes with only one child:", tree.Num_of_node_one_child(root))

# Display nodes with even data
print("Even nodes in the tree:")
tree.node_even(root)

# Count nodes with exactly two children
print("\nNodes with exactly two children:", tree.node_with_two_child(root))