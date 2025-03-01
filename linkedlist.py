from typing import Any, Iterator

class Node:
    def __init__(self, value: Any) -> None:
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, head=None) -> None:
        self.head = head
        self.count = 0 if head is None else 1
        
    def __str__(self) -> str:
        if not self.head:
            return "Empty LinkedList"
        return "-->".join(str(value) for value in self)
    
    def __repr__(self) -> str:
        values = list(self)
        return f"LinkedList([" + ", ".join(str(v) for v in values) + "])"
    
    def __len__(self) -> int:
        return self.count
    
    def __iter__(self) -> Iterator:
        current = self.head
        while current:
            yield current.value
            current = current.next
            
    def insert(self, value: Any) -> None:
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.count += 1
        
    def find(self, value: Any) -> Node:
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None
    
    def delete(self, value: Any) -> bool:
        # empty case
        if not self.head:
            return False

        # head case
        if self.head.value == value:
            self.head = self.head.next
            self.count -= 1
            return True

        # non-head case
        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                self.count -= 1
                return True
            current = current.next
        return False