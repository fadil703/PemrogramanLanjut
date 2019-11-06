from queue import *
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_left(self, value):
        if self.left_child == None:
            self.left_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.left_child = self.left_child
            self.left_child = new_node

    def insert_right(self, value):
        if self.right_child == None:
            self.right_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.right_child = self.right_child
            self.right_child = new_node

    #depth first search

    def pre_order(self):
        print(self.value)

        if self.left_child:
            self.left_child.pre_order()

        if self.right_child:
            self.right_child.pre_order()

    def in_order(self):
        if self.left_child:
            self.left_child.in_order()

        print(self.value)

        if self.right_child:
            self.right_child.in_order()

    def post_order(self):
        if self.left_child:
            self.left_child.post_order()

        if self.right_child:
            self.right_child.post_order()

        print(self.value)

    def bfs(self): #breadth first search
        queue = Queue()
        queue.put(self)

        while not queue.empty():
            current_node = queue.get()
            print(current_node.value)

            if current_node.left_child:
                queue.put(current_node.left_child)

            if current_node.right_child:
                queue.put(current_node.right_child)

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_node(self, value):
        if value <= self.value and self.left_child:
            self.left_child.insert_node(value)
        elif value <= self.value:
            self.left_child = BinarySearchTree(value)
        elif value > self.value and self.right_child:
            self.right_child.insert_node(value)
        else:
            self.right_child = BinarySearchTree(value)

    def find_node(self, value):
        if value < self.value and self.left_child:
            return self.left_child.find_node(value)
        if value > self.value and self.right_child:
            return self.right_child.find_node(value)

        return value == self.value


    def remove_node(self, value, parent):
        if value < self.value and self.left_child:
            return self.left_child.remove_node(value, self)
        elif value < self.value:
            return False
        elif value > self.value and self.right_child:
            return self.right_child.remove_node(value, self)
        elif value > self.value:
            return False
        else:
            if self.left_child is None and self.right_child is None and self == parent.left_child:
                parent.left_child = None
                self.clear_node()
            elif self.left_child is None and self.right_child is None and self == parent.right_child:
                parent.right_child = None
                self.clear_node()
            elif self.left_child and self.right_child is None and self == parent.left_child:
                parent.left_child = self.left_child
                self.clear_node()
            elif self.left_child and self.right_child is None and self == parent.right_child:
                parent.right_child = self.left_child
                self.clear_node()
            elif self.right_child and self.left_child is None and self == parent.left_child:
                parent.left_child = self.right_child
                self.clear_node()
            elif self.right_child and self.left_child is None and self == parent.right_child:
                parent.right_child = self.right_child
                self.clear_node()
            else:
                self.value = self.right_child.find_minimum_value()
                self.right_child.remove_node(self.value, self)

            return True

    def clear_node(self):
        self.value = None
        self.left_child = None
        self.right_child = None 

    def find_minimum_value(self):
        if self.left_child:
            return self.left_child.find_minimum_value()
        else:
            return self.value

    def pre_order_traversal(self):
        print(self.value)

        if self.left_child:
            self.left_child.pre_order_traversal()

        if self.right_child:
            self.right_child.pre_order_traversal()

    def in_order_traversal(self):
        if self.left_child:
            self.left_child.in_order_traversal()

        print(self.value)

        if self.right_child:
            self.right_child.in_order_traversal()