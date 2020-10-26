class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)


class BST:
    def __init__(self):
        self.root = None

    def add(self, value):
        traversal_path = ''
        if self.root is None:
            self.root = Node(value)
        else:
            buffer = self.root
            while buffer is not None:
                if value < buffer.value:
                    traversal_path += 'L'
                    if buffer.left is None:
                        buffer.left = Node(value)
                        break
                    else:
                        buffer = buffer.left
                else:
                    traversal_path += 'R'
                    if buffer.right is None:
                        buffer.right = Node(value)
                        break
                    else:
                        buffer = buffer.right
        return traversal_path + '*'


if __name__ == '__main__':
    lst = list(map(int, input("Enter Input : ").split()))
    tree = BST()
    for item in lst:
        print(tree.add(item))