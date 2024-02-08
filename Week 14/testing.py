from AVL_tree import Node
root = Node(5)
to_add = [3, 8, 2, 4, 7, 11, 1, 6, 10, 12, 9, 13]
# root = Node(4)
# to_add = [3,2,1,6,5]
for i in to_add:
    root.insert(i)
root.show_tree()

nodeToFind = Node(8)
print(nodeToFind.get_height())

# root.print_tree()
