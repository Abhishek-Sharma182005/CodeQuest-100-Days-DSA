def inorder(index, tree):
    if index >= len(tree) or tree[index] is None:
        return []
    left = inorder(2 * index + 1, tree)
    root = [tree[index]]
    right = inorder(2 * index + 2, tree)
    return left + root + right

user_input = input("Enter binary tree in level order (use -1 for None): ").split()
nodes = [int(x) for x in user_input]
inorder_result = inorder(0, nodes)
print("Inorder Traversal:", ' '.join(map(str, inorder_result)))