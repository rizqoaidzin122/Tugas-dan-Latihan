class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

def print_tree(node, level=0):
    if node is None:
        return
    print("  " * level + str(node.data))
    for child in node.children:
        print_tree(child, level + 1)

# Contoh penggunaan
root = TreeNode("A")
child1 = TreeNode("B")
child2 = TreeNode("C")
child3 = TreeNode("D")
root.add_child(child1)
root.add_child(child2)
root.add_child(child3)

child1.add_child(TreeNode("E"))
child1.add_child(TreeNode("F"))

child2.add_child(TreeNode("G"))

print_tree(root)