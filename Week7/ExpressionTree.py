class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            curr = self.root
            while True:
                if data < curr.data:
                    if curr.left is None:
                        curr.left = Node(data)
                        break
                    curr = curr.left
                else:
                    if curr.right is None:
                        curr.right = Node(data)
                        break
                    curr = curr.right
        return self.root

    def max(self):
        if self.root is None:
            return
        curr = self.root
        while curr.right is not None:
            curr = curr.right
        return curr.data

    def min(self):
        if self.root is None:
            return
        curr = self.root
        while curr.left is not None:
            curr = curr.left
        return curr.data

    def mult(self, k, multiplier):  # bfs then multiply
        q = Queue()
        q.enqueue(self.root)
        while not q.is_empty():
            curr = q.dequeue()
            if curr.data > k:
                curr.data = curr.data*multiplier
            if curr.left is not None:
                q.enqueue(curr.left)
            if curr.right is not None:
                q.enqueue(curr.right)

    def bfs(self):
        if self.root is None:
            return "Empty Tree"
        q = Queue()
        q.enqueue(self.root)
        out = "Breadth : "
        while not q.is_empty():
            curr = q.dequeue()
            out += str(curr.data) + ' '
            if curr.left is not None:
                q.enqueue(curr.left)
            if curr.right is not None:
                q.enqueue(curr.right)
        return out

    def print_tree(self, node, level=0):
        if node is not None:
            self.print_tree(node.right, level + 1)
            print('     ' * level, node)
            self.print_tree(node.left, level + 1)


ino = "Infix : "
pre = "Prefix : "


def inorder(curr):
    global ino
    if curr is not None:
        if curr.left is not None or curr.right is not None:  # not leaf
            ino += "("
        inorder(curr.left)
        ino += str(curr.data)
        inorder(curr.right)
        if curr.left is not None or curr.right is not None:  # not leaf
            ino += ")"


def preorder(curr):
    global pre
    if curr is not None:
        pre += str(curr.data)
        preorder(curr.left)
        preorder(curr.right)


if __name__ == '__main__':
    exp = input("Enter Postfix : ")
    ExpressionTree = BST()
    s = Stack()
    for character in exp:
        if character in '+-*/':
            op1 = s.pop()
            op2 = s.pop()
            s.push(Node(character, op2, op1))
        else:
            s.push(Node(character))
    print("Tree :")
    ExpressionTree.root = s.pop()
    ExpressionTree.print_tree(ExpressionTree.root)
    print("--------------------------------------------------")
    inorder(ExpressionTree.root)
    print(ino)
    preorder(ExpressionTree.root)
    print(pre)