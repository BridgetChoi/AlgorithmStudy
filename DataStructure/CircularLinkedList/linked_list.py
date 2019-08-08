class Node(object):
    def __init__(self, node_data):
        self.data = node_data
        self.next_node = None
        self.prev_node = None

class CircularLinkedList(object):
    def __init__(self):
        self.head_node = None
        self.tail_node = None
    
    def create_node(self, node_data):
        new_node = Node(node_data)
        return new_node
    
    def destroy_node(self):
        self.head_node = None
    
    def append_node(self, new_node):
        if self.head_node is None:
            self.tail_node = self.create_node(None)
            self.head_node = new_node
            
            self.head_node.next_node = self.tail_node
            self.head_node.prev_node = self.tail_node
            
            self.tail_node.next_node = self.head_node
            self.tail_node.prev_node = self.head_node
        else:
            tail_node = self.tail_node
            new_node.next_node = tail_node
            new_node.prev_node = tail_node.prev_node
            tail_node.prev_node.next_node = new_node
            tail_node.prev_node = new_node

def insert_node(self, new_node, index):
    current_node = self.head_node
        if current_node is None:
            self.append_node(new_node)
    else:
        index = index - 1
            while current_node.next_node != self.tail_node and index >= 0:
                current_node = current_node.next_node
                index = index - 1
        new_node.next_node = current_node.next_node
            new_node.prev_node = current_node
            current_node.next_node.prev_node = new_node
            current_node.next_node = new_node

def remove_node(self, index):
    current_node = self.head_node
        if current_node is not None:
            index = index - 1
            while current_node.next_node != self.tail_node and index >= 0:
                current_node = current_node.next_node
                index = index - 1
            
            if current_node == self.head_node:
                self.tail_node.next_node = current_node.next_node
                current_node.next_node.prev_node = self.tail_node
                self.head_node = current_node.next_node
            else:
                current_node.prev_node.next_node = current_node.next_node
                current_node.next_node.prev_node = current_node.prev_node
            current_node = None
                
                def print_node(self):
                    current_node = self.head_node
                        print_text = ''
                            if current_node is not None:
                                while current_node.data != None:
print_text = u'{} {}'.format(print_text, current_node.data)
current_node = current_node.next_node
    return print_text


circular_linked_list = CircularLinkedList()

new_node = circular_linked_list.create_node(10)
circular_linked_list.append_node(new_node)
print(circular_linked_list.print_node())

new_node = circular_linked_list.create_node(20)
circular_linked_list.append_node(new_node)
print(circular_linked_list.print_node())

new_node = circular_linked_list.create_node(30)
circular_linked_list.append_node(new_node)
print(circular_linked_list.print_node())

new_node = circular_linked_list.create_node(40)
circular_linked_list.insert_node(new_node, 1)
print(circular_linked_list.print_node())

new_node = circular_linked_list.create_node(50)
circular_linked_list.insert_node(new_node, 0)
print(circular_linked_list.print_node())

circular_linked_list.remove_node(2)
print(circular_linked_list.print_node())

circular_linked_list.remove_node(0)
print(circular_linked_list.print_node())

circular_linked_list.remove_node(0)
print(circular_linked_list.print_node())

circular_linked_list.remove_node(0)
print(circular_linked_list.print_node())

circular_linked_list.remove_node(0)
print(circular_linked_list.print_node())

circular_linked_list.remove_node(0)
print(circular_linked_list.print_node())
