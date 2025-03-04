class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        """Добавить потомка"""
        self.children.append(child_node)

    def print_tree(self, level=0):
        """Вывести дерево на экран"""
        print(" " * level * 2 + str(self.value))
        for child in self.children:
            child.print_tree(level + 1)

# Создаём дерево
root = TreeNode("Родитель")
child1 = TreeNode("Ребёнок 1")
child2 = TreeNode("Ребёнок 2")

root.add_child(child1)
root.add_child(child2)

child1.add_child(TreeNode("Внук 1"))
child1.add_child(TreeNode("Внук 2"))

child2.add_child(TreeNode("Внук 3"))

root.print_tree()
