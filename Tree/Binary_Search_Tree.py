class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

def insert(node, value):
    if node is None:
        return Node(value)

    if value > node.value:
        node.right = insert(node.right, value)
    else:
        node.left = insert(node.left, value)
    return node

def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.value)
        inorder(node.right)

def search(node, value):
    if node is None:
        return False

    if node.value == value:
        return True
    elif node.value > value:
        return search(node.left, value)
    else:
        return search(node.right, value)

def min_value(node):
    current = node
    while node.left is not None:
        current = node.left
    return current

def remove(node, value):
    if node is None:
        return node

    if value < node.value:
        node.left = remove(node.left, value)
    elif value > node.value:
        node.right = remove(node.right, value)
    else:
        if node.left is None:
            return  node.right
        elif node.right is None:
            return  node.left

        temp = min_value(node.right)
        node.value = temp.value
        node.right = remove(node.right, temp.value)
    return node


if __name__ == "__main__":
    root = None
    root = insert(root, 3)
    root = insert(root, 6)
    root = insert(root, 7)
    root = insert(root, 5)
    root = insert(root, 2)
    root = insert(root, 1)
    root = insert(root, 10)
    print(inorder(root))
    root  = remove(root, 6)
    print(inorder(root))


