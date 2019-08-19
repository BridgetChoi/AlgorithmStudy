
class Node(object):
    def __init__(self, node_data):
        self.data = node_data
            self.next_node = None
                self.prev_node = None

class Stack(object):
    def __init__(self):
    self.bottom_node = None
    self.top_node = None
        
    def _create_node(self, node_data):
        new_node = Node(node_data)
        return new_node
                
    def _append_node(self, new_node):
        if self.bottom_node is None:
            self.bottom_node = new_node
            self.top_node = Node(None)

            self.bottom_node.next_node = self.top_node
            self.top_node.prev_node = self.bottom_node
        else:
            new_node.next_node = self.top_node
            new_node.prev_node = self.top_node.prev_node
            self.top_node.prev_node.next_node = new_node
            self.top_node.prev_node = new_node
                                                        
    def _remove_node(self):
        if self.top_node is not None and self.top_node.prev_node is not None:
            if self.top_node.prev_node == self.bottom_node:
                self.bottom_node = None
                self.top_node = None
            else:
                remove_node = self.top_node.prev_node
                remove_node.prev_node.next_node = self.top_node
                self.top_node.prev_node = remove_node.prev_node
                remove_node = None
                                                                                                
    def push(self, node_data):
        new_node = self._create_node(node_data)
        self._append_node(new_node)

    def pop(self):
        self._remove_node()
                                                                                                                
    def print_nodes(self):
        current_node = self.bottom_node
        text = ''
        while current_node is not self.top_node:
            text = u'{} -> {}'.format(text, current_node.data)
            current_node = current_node.next_node
        print(text)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.print_nodes()
stack.pop()
stack.pop()
stack.print_nodes()
stack.pop()
stack.pop()
stack.print_nodes()
stack.pop()
stack.print_nodes()
stack.pop()
