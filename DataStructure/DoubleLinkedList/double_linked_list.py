class Node(object):
    def __init__(self, node_data):
        self.data = node_data
        self.prev_node = None
        self.next_node = None

class DoubleLinkedList(object):
    def __init__(self):
        self.head_node = None

    def create_node(self, node_data):
        new_node = Node(node_data)
        return new_node

    def destroy_node(self):
        self.head_node = None

    def append_node(self, new_node):
        if self.head_node is None:
            self.head_node = new_node
        else:
            node_tail = self.head_node
            while node_tail.next_node is not None:
                node_tail = node_tail.next_node
            node_tail.next_node = new_node
            new_node.prev_node = node_tail

    def insert_node(self, current_node, new_node):
        new_node.next_node = current_node.next_node
        new_node.prev_node = current_node

        if current_node.next_node is not None:
            current_node.next_node.prev_node = new_node
        current_node.next_node = new_node

    def remove_node(self, remove_node):
        if self.head_node == remove_node:
            self.head_node = remove_node.next_node
            if self.head_node is not None:
                self.head_node.prev_node = None
            remove_node.next_node = None
            remove_node.prev_node = None
        else:
            temp_node = remove_node
            if remove_node.prev_node is not None:
                remove_node.prev_node.next_node = temp_node.next_node
            if remove_node.next_node is not None:
                remove_node.next_node.prev_node = temp_node.prev_node
            remove_node.next_node = None
            remove_node.prev_node = None

    def get_node_at(self, index):
        index = index - 1
        current_node = self.head_node
        while current_node is not None and index >= 0:
            current_node = current_node.next_node
            index = index - 1
        return current_node

    def get_node_count(self):
        count = 0
        current_node = self.head_node
        while current_node is not None:
            current_node = current_node.next_node
            count = count + 1
        return count
