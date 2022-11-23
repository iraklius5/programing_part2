from book import Book


class Node:
    def __init__(self, data: Book):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data: Book):
        if self.data:
            if data.name < self.data.name:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data.name > self.data.name:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def find(self, value):
        if value < self.data.publication:
            if self.left is None:
                return str(value) + " is not found"
            return self.left.find(value)
        elif value > self.data.publication:
            if self.right is None:
                return str(value) + " is not found"
            return self.right.find(value)
        else:
            print(self.data)
            if self.left is not None:
                self.left.find(value)
            if self.right is not None:
                self.right.find(value)

    def delete(self, value):
        if value < self.data.author:
            if self.left is None:
                return str(value) + " is not found"
            self.left.delete(value)
        elif value > self.data.author:
            if self.right is None:
                return str(value) + " is not found"
            self.right.delete(value)
        else:
            self.data = self.right
            if self.left is not None:
                self.left.delete(value)
            if self.right is not None:
                self.right.delete(value)

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data),
        if self.right:
            self.right.print_tree()

    def __str__(self):
        return "None"