#!/usr/bin/env python3

from linkedlist import LinkedList, Node

def main():
    ll = LinkedList()
    for i in range(1, 10):
        ll.insert(i)
    
    print("LinkedList: ", ll) 
    print("LinkedList length: ", len(ll))
    ll.delete(2)
    print("LinkedList after deleting node 2: ", ll)
    print("Find LinkedList node 1: ", ll.find(1)) 

if __name__ == "__main__":
    main()