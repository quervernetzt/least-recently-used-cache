from tests.tests_doubly_linked_list import TestCasesDoublyLinkedList
from tests.tests_lru_cache import TestCasesLRUCache
from solution.lru_cache import LRUCache


if __name__ == "__main__":
    ###################################
    # Tests
    ###################################
    tests_doubly_linked_list_instance: TestCasesDoublyLinkedList = TestCasesDoublyLinkedList()
    tests_lru_cache_instance: TestCasesDoublyLinkedList = TestCasesLRUCache()

    tests_doubly_linked_list_instance.execute_tests_move_item_to_head_without_nodes()
    tests_doubly_linked_list_instance.execute_tests_move_item_to_head_with_nodes()
    tests_doubly_linked_list_instance.execute_tests_move_item_to_head_with_nodes_many()
    tests_lru_cache_instance.execute_tests_remove_tail_without_nodes()
    tests_lru_cache_instance.execute_tests_remove_tail_with_nodes()
    tests_lru_cache_instance.execute_tests_lru_cache_capacity_is_zero_add_single_item()
    tests_lru_cache_instance.execute_tests_lru_cache_capacity_is_greater_zero_add_multiple_items_up_to_capacity()
    tests_lru_cache_instance.execute_tests_lru_cache_capacity_is_greater_zero_add_multiple_items_over_capacity()
    tests_lru_cache_instance.execute_tests_lru_cache_capacity_is_greater_zero_add_multiple_items_over_capacity_random()

    ###################################
    # Demo
    ###################################
    our_cache: LRUCache = LRUCache(5)

    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)

    print(our_cache.get(1))     # returns 1
    print(our_cache.get(2))      # returns 2
    # returns -1 because 9 is not present in the cache
    print(our_cache.get(9))

    our_cache.set(5, 5)
    our_cache.set(6, 6)

    # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
    print(our_cache.get(3))
