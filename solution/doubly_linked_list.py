class DoubleNode:
    def __init__(self: object, value: object, key: object) -> None:
        """Constructor.

        Parameters
        ----------
        value : object, required
            Value of the node.

        key : object, required
            The key for the node in the hash map.
        """

        self.value: object = value
        self.key: object = key
        self.next: DoubleNode = None
        self.previous: DoubleNode = None


class DoublyLinkedList:
    def __init__(self: object) -> None:
        """Constructor.
        """
        self.head: DoubleNode = None
        self.tail: DoubleNode = None

    def append(self, node: DoubleNode) -> None:
        """Append node to an existing linked list.

        Parameters
        ----------
        node : DoubleNode, required
           The node to append.
        """

        if self.head is None:
            self.head = node
            self.tail: DoubleNode = self.head
        else:
            self.tail.next = node
            self.tail.next.previous = self.tail
            self.tail = self.tail.next
        return

    def prepend(self, node: DoubleNode) -> None:
        """Prepend node to an existing linked list.

        Parameters
        ----------
        node : DoubleNode, required
           The node to prepend.
        """
        if self.head is None:
            self.head = node
            self.tail: DoubleNode = self.head
        else:
            node.next = self.head
            self.head.previous = node
            self.head = node

    def to_list(self: object) -> None:
        """Convert linked list to list with the values of each node.
        """

        out: list = []
        node: DoubleNode = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out

    def move_item_to_head(self: object, node_to_move: DoubleNode) -> None:
        """Move item within linked list to its head.
        Pass only a node where you are sure that it exists in the cache.

        Parameters
        ----------
        node_to_move : DoubleNode, required
            The node to move
        """

        #print(f"Node to move has value: '{node_to_move.value}'...")
        if node_to_move is self.head:
            #print("Node is head...")
            return
        elif node_to_move is self.tail:
            #print("Node is tail...")
            node_to_move.previous.next = None
            self.tail = node_to_move.previous
            self.head.previous = node_to_move
            node_to_move.next = self.head
            self.head = node_to_move
        else:
            #print("Node is somewhere between head and tail or does not exist in linked list...")
            node_to_move.previous.next = node_to_move.next
            node_to_move.next.previous = node_to_move.previous
            self.head.previous = node_to_move
            node_to_move.next = self.head
            self.head = node_to_move
        #print(f"Move item to head: {self.to_list()}...")
