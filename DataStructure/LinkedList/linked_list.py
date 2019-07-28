class Node(object):
    def __init__(self, node_data):
        self.data = node_data
        self.next_node = None

    def __del__(self):
        pass

class LinkedList(object):
    def __init__(self):
        self.head_node = None

    def create_node(self,node_data):
        new_node = Node(node_data)
        return new_node

    def destroy_node(self):
        self.head_node = None

    def append_node(self, new_node):
        if not self.head_node:
            self.head_node = new_node
        else:
            node_tail = self.head_node
            while node_tail.next_node is not None:
                node_tail = node_tail.next_node
            node_tail.next_node = new_node

    def insert_node(self, current_node, new_node):
        new_node.next_node = current_node.next_node
        current_node.next_node = new_node

    def insert_new_head(self, new_head):
        if self.head_node is None:
            self.head_node = new_head
        else:
            new_head.next_node = self.head_node
            self.head_node = new_head

    def remove_node(self, remove_node):
        if self.head_node == remove_node:
            self.head_node = remove_node.next_node
        else:
            current_node = self.head_node
            while not current_node and current_node.next_node != remove_node:
                current_node = current_node.next_node

            if not current_node:
                current_node.next_node = remove_node.next_node
                del remove_node

    def get_node_at(self, location):
        count = 0
        current_node = self.head_node
        while current_node is not None and count != location:
            current_node = current_node.next_node
            count = count + 1
        return current_node

    def get_node_count(self):
        count = 0
        current_node = self.head_node
        while current_node is not None:
            current_node = current_node.next_node
            count = count + 1
        return count