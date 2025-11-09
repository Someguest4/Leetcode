class TreeNode:
    def __init__(self, left, right, value):
        self.left = left
        self.right = right
        self.value = value


tree = TreeNode(
    TreeNode(
        TreeNode(None, None, 2),
        TreeNode(None, None, 7),
        5),
    TreeNode(
        TreeNode(None, None, 12),
        TreeNode(None, None, 17),
        15),
    10)

def find_big_small_number(tree, n):
    result = None
    node = tree
    while node:
        if node.value <= n:
            node = node.right
        else:
            if not result or node.value < result:
                result = node.value
            node = node.left
    return result

print(find_big_small_number(tree, 16))
print(find_big_small_number(tree, 100))
print(find_big_small_number(tree, 0))
print(find_big_small_number(tree, 5))
print(find_big_small_number(tree, 7))

