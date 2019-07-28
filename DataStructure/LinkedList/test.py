import unittest
from DataStructure.LinkedList.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    def test_linked_list(self):
        linked_list = LinkedList()

        for i in range(0, 5):
            new_node = linked_list.create_node(i)
            linked_list.append_node(new_node)
        self.assertEqual(linked_list.get_node_count(), 5)

        new_node = linked_list.create_node('a')
        linked_list.insert_new_head(new_node)
        self.assertEqual(linked_list.head_node.data, new_node.data)
        self.assertEqual(linked_list.get_node_count(), 6)

        current_node = linked_list.get_node_at(2)
        new_node = linked_list.create_node(3000)
        linked_list.insert_node(current_node, new_node)
        self.assertEqual(linked_list.get_node_count(), 7)
        self.assertEqual(current_node.next_node.data, new_node.data)

        linked_list.destroy_node()
        self.assertEqual(linked_list.head_node, None)

if __name__ == '__main__':
    unittest.main()
