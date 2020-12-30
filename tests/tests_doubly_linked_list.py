import unittest
from solution.doubly_linked_list import DoubleNode, DoublyLinkedList


class TestCasesDoublyLinkedList(unittest.TestCase):
    def execute_tests_move_item_to_head_without_nodes(self) -> None:
        # Arrange
        doubly_linked_list: DoublyLinkedList = DoublyLinkedList()
        first_node: DoubleNode = DoubleNode(1, 1)

        # Act and Assert
        self.assertRaises(
            AttributeError, doubly_linked_list.move_item_to_head, first_node)

    def execute_tests_move_item_to_head_with_nodes(self) -> None:
        # Arrange
        doubly_linked_list: DoublyLinkedList = DoublyLinkedList()
        first_node: DoubleNode = DoubleNode(1, 1)
        second_node: DoubleNode = DoubleNode(2, 2)
        third_node: DoubleNode = DoubleNode(3, 3)
        fourth_node: DoubleNode = DoubleNode(4, 4)
        fifth_node: DoubleNode = DoubleNode(5, 5)

        doubly_linked_list.append(first_node)
        doubly_linked_list.append(second_node)
        doubly_linked_list.append(third_node)
        doubly_linked_list.append(fourth_node)

        # Act and Assert
        #print("--------------------")
        self.assertEqual(
            doubly_linked_list.move_item_to_head(first_node), None)
        #print("--------------------")
        self.assertEqual(
            doubly_linked_list.move_item_to_head(second_node), None)
        #print("--------------------")
        self.assertEqual(
            doubly_linked_list.move_item_to_head(third_node), None)
        #print("--------------------")
        self.assertEqual(
            doubly_linked_list.move_item_to_head(fourth_node), None)
        #print("--------------------")
        self.assertRaises(
            AttributeError, doubly_linked_list.move_item_to_head, fifth_node)

    def execute_tests_move_item_to_head_with_nodes_many(self) -> None:
        # Arrange
        doubly_linked_list: DoublyLinkedList = DoublyLinkedList()

        number_of_nodes: int = 1000
        nodes: list = []
        for i in range(number_of_nodes):
            node: DoubleNode = DoubleNode(i, i)
            nodes.append(node)
            doubly_linked_list.append(node)

        # Act and Assert
        for node in nodes:
            self.assertEqual(
                doubly_linked_list.move_item_to_head(node), None)
