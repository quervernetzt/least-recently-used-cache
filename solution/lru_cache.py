from solution.doubly_linked_list import DoubleNode, DoublyLinkedList


class LRUCache(object):
    def __init__(self: object, capacity: int) -> None:
        """Constructor.

        Parameters
        ----------
        capacity : int, required
            Maximum size of the cache.
        """

        # The actual cache
        self.doubly_linked_list: DoublyLinkedList = DoublyLinkedList()
        # Stores key:node pairs for fast retrieval
        self.hash_table: dict = {}
        self.max_size_cache: int = capacity
        self.current_size_cache: int = 0

    def get(self: object, key: object) -> object:
        """Get the value for a key in the cache.
        The element got is put as head of the linked list.

        Parameters
        ----------
        key : object, required
            The key for the value to retrieve.

        Returns
        ----------
        object
            Returns the value for the key if the key exists.
            Otherwise it returns -1.
        """

        #print(f"Get value for key '{key}'...")
        if key in self.hash_table:
            #print("Key exists...")
            node_for_key: DoubleNode = self.hash_table[key]
            if self.current_size_cache > 1:
                self.doubly_linked_list.move_item_to_head(node_for_key)
            return self.hash_table[key].value
        else:
            #print("Key does not exist...")
            return -1

    def set(self, key: object, value: object) -> None:
        """Add a new element to the cache (if not exists).
        If already in cache just move node to head of linked list.
        If it does not exist but exceeds capacity remove oldest node, then add new one.

        Parameters
        ----------
        key : object, required
            The key for the value to retrieve.

        Returns
        ----------
        object
            Returns the value for the key if the key exists.
            Otherwise it returns -1.
        """

        #print(f"Try to add node with key '{key}' and value '{value}'...")
        if self.max_size_cache == 0:
            #print(f"Maximum capcity of cache is zero...")
            return
        else:
            if key in self.hash_table:
                #print(f"Key '{key}' already exists...")
                node_for_key: DoubleNode = self.hash_table[key]
                if node_for_key.value == value:
                    #print("No value update...")
                    return
                else:
                    # print(
                    #     f"Value update from '{node_for_key.value}' to '{value}'...")
                    node_for_key.value = value

                if self.current_size_cache > 1:
                    self.doubly_linked_list.move_item_to_head(node_for_key)
            else:
                #print(f"Key '{key}' does not exist...")
                new_node: DoubleNode = DoubleNode(value, key)

                if self.doubly_linked_list.head is None:  # Init
                    # Add node
                    self.doubly_linked_list.head = new_node
                    self.doubly_linked_list.tail = new_node
                    self.hash_table[key] = new_node
                    self.current_size_cache += 1
                    # print(
                    #     f"Node is first node in linked list. Number of elements in cache is now '{self.current_size_cache}'...")
                elif self.current_size_cache == self.max_size_cache:  # Cache full
                    #print("Cache is full, removing least recently used node...")
                    removed_tail: bool = self.remove_tail() # TODO: add key to node properties
                    if removed_tail:  # should always be true
                        self.current_size_cache -= 1
                        # Add node
                        self.doubly_linked_list.prepend(new_node)
                        self.hash_table[key] = new_node
                        self.current_size_cache += 1
                        # print(
                        #     f"Added node. Number of elements in cache is now '{self.current_size_cache}'...")
                elif self.current_size_cache >= 0 and self.current_size_cache < self.max_size_cache:
                    # Add node
                    self.doubly_linked_list.prepend(new_node)
                    self.hash_table[key] = new_node
                    self.current_size_cache += 1
                    # print(
                    #     f"Added node. Number of elements in cache is now '{self.current_size_cache}'...")
                else:
                    raise Exception(
                        f"current_size_cache is '{self.current_size_cache}'...")

    def remove_tail(self: object) -> bool:
        """Remove tail node from linked list and hash map.

        Returns
        ----------
        bool
            Boolean if a node has been removed.
        """

        if self.doubly_linked_list.tail:
            #print("Tail exists...")
            current_tail: DoubleNode = self.doubly_linked_list.tail
            if self.doubly_linked_list.tail is self.doubly_linked_list.head:
                self.doubly_linked_list.head = None
                self.doubly_linked_list.tail = None
            else:
                self.doubly_linked_list.tail.previous.next = None
                self.doubly_linked_list.tail = self.doubly_linked_list.tail.previous
            del self.hash_table[current_tail.key]
            current_tail = None
            #print(f"Removed tail: {self.doubly_linked_list.to_list()}...")
            return True
        else:
            #print("No tail exists...")
            return False
