import unittest
from DataStructure.DoubleLinkedList.double_linked_list import DoubleLinkedList

class TestDoubleLinkedList(unittest.TestCase):
    def test_double_linked_list(self):
        double_linked_list = DoubleLinkedList()
        # create node and append
        for i in range(0, 5):
            new_node = double_linked_list.create_node(i)
            double_linked_list.append_node(new_node)
        self.assertEqual(double_linked_list.get_node_count(), 5)

        # check appended nodes data
        for i in range(0, 5):
            current_node = double_linked_list.get_node_at(i)
            self.assertEqual(current_node.data, i)

        # check insert data
        current_node = double_linked_list.get_node_at(2)
        new_node = double_linked_list.create_node('a')
        double_linked_list.insert_node(current_node, new_node)
        current_node = double_linked_list.get_node_at(2)
        self.assertEqual(current_node.next_node.data, new_node.data)
        self.assertEqual(double_linked_list.get_node_count(), 6)

        double_linked_list.destroy_node()
        self.assertEqual(double_linked_list.head_node, None)


if __name__ == '__main__':
    unittest.main()
