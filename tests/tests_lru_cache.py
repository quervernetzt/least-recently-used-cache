import unittest
import random
from solution.doubly_linked_list import DoubleNode, DoublyLinkedList
from solution.lru_cache import LRUCache


class TestCasesLRUCache(unittest.TestCase):
    def execute_tests_remove_tail_without_nodes(self) -> None:
        # Arrange
        cache: LRUCache = LRUCache(5)

        # Act and Assert
        self.assertFalse(cache.remove_tail())

    def execute_tests_remove_tail_with_nodes(self) -> None:
        # Arrange
        doubly_linked_list: DoublyLinkedList = DoublyLinkedList()
        first_node: DoubleNode = DoubleNode(1, 1)
        second_node: DoubleNode = DoubleNode(2, 2)
        third_node: DoubleNode = DoubleNode(3, 3)
        fourth_node: DoubleNode = DoubleNode(4, 4)

        doubly_linked_list.append(first_node)
        doubly_linked_list.append(second_node)
        doubly_linked_list.append(third_node)
        doubly_linked_list.append(fourth_node)

        cache: LRUCache = LRUCache(5)
        cache.doubly_linked_list = doubly_linked_list
        cache.hash_table = {
            first_node.key: first_node,
            second_node.key: second_node,
            third_node.key: third_node,
            fourth_node.key: fourth_node
        }

        # Act and Assert
        # print("--------------------")
        self.assertTrue(cache.remove_tail())
        # print("--------------------")
        self.assertTrue(cache.remove_tail())
        # print("--------------------")
        self.assertTrue(cache.remove_tail())
        # print("--------------------")
        self.assertTrue(cache.remove_tail())
        # print("--------------------")
        self.assertFalse(cache.remove_tail())
        # print("--------------------")
        self.assertFalse(cache.remove_tail())
        # print("--------------------")

    def execute_tests_lru_cache_capacity_is_zero_add_single_item(self) -> None:
        # Arrange
        cache: LRUCache = LRUCache(0)

        # Act and Assert
        self.assertEqual(cache.set(1, 1), None)
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(2), -1)

    def execute_tests_lru_cache_capacity_is_greater_zero_add_single_item(self) -> None:
        # Arrange
        cache: LRUCache = LRUCache(5)

        # Act and Assert
        self.assertEqual(cache.set(1, 1), None)
        self.assertEqual(cache.get(1), 1)
        self.assertEqual(cache.get(2), -1)

    def execute_tests_lru_cache_capacity_is_greater_zero_add_multiple_items_up_to_capacity(self) -> None:
        # Arrange
        cache: LRUCache = LRUCache(5)

        # Act and Assert
        self.assertEqual(cache.set(1, 1), None)
        self.assertEqual(cache.set(2, 2), None)
        self.assertEqual(cache.set(3, 3), None)
        self.assertEqual(cache.set(4, 4), None)
        self.assertEqual(cache.set(3, 3), None)
        self.assertEqual(cache.set(5, 5), None)
        #print("----------")
        self.assertEqual(cache.get(1), 1)
        self.assertEqual(cache.get(2), 2)
        self.assertEqual(cache.get(4), 4)
        self.assertEqual(cache.get(3), 3)
        self.assertEqual(cache.get(4), 4)
        self.assertEqual(cache.get(1), 1)
        self.assertEqual(cache.get(5), 5)
        self.assertEqual(cache.get(6), -1)

    def execute_tests_lru_cache_capacity_is_greater_zero_add_multiple_items_over_capacity(self) -> None:
        # Arrange
        cache: LRUCache = LRUCache(3)

        # Act and Assert
        self.assertEqual(cache.set(1, 1), None)
        self.assertEqual(cache.set(2, 2), None)
        self.assertEqual(cache.set(3, 3), None)
        self.assertEqual(cache.set(4, 4), None)
        self.assertEqual(cache.set(3, 3), None)
        self.assertEqual(cache.set(5, 5), None)
        #print("----------")
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(2), -1)
        self.assertEqual(cache.get(4), 4)
        self.assertEqual(cache.get(3), 3)
        self.assertEqual(cache.get(4), 4)
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(5), 5)
        self.assertEqual(cache.get(6), -1)
    
    def execute_tests_lru_cache_capacity_is_greater_zero_add_multiple_items_over_capacity_random(self) -> None:
        # Arrange
        cache: LRUCache = LRUCache(1000)
        random_list: list = list(range(100000))
        random_list.extend(list(range(100000)))
        random.shuffle(random_list)
        added_keys: list = []
        
        # Act and Assert
        for i in random_list:
            self.assertEqual(cache.set(i, i), None)
            
            if i not in added_keys:
                added_keys.append(i)
                if len(added_keys) > 1000:
                    added_keys.pop(0)
        
        for added_key in added_keys:
            self.assertEqual(cache.get(added_key), added_key)
        
        for i in random_list:
            if i not in added_keys:
                self.assertEqual(cache.get(i), -1)
