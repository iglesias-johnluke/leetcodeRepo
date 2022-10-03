'''
doubly linkedlist, with dummy tail, head for removal
map keys to Nodes
linkedlist of least accessed keys

get() returns value if key is in map, moves node to end of list
put(), 
    updates map if key exists, moves node to end of list
    else:
        if capacity not reached:
            size += 1
        else: #capacity reached
            remove head of list
            remove key from map
        
        append node to list
        insert into map
'''
class Node:
    def __init__(self):
        self.val = None
        self.next = None
        self.prev = None
    

class LRUCache:

    def __init__(self, capacity: int):
        self.map = {}
        self.capacity = capacity
        self.size = 0
        self.dummyHead = Node()
        self.dummyTail = Node()
        self.dummyHead.next = self.dummyTail
        self.dummyTail.prev = self.dummyHead
        
    def removeNode(self, node):
        prev = node.prev
        nex = node.next
        prev.next = nex
        nex.prev = prev
        
        node.next = None
        node.prev = None
        
    def pushNode(self, node, tail):
        prev = tail.prev
        prev.next = node
        node.prev = prev
        node.next = tail
        tail.prev = node

    def get(self, key: int) -> int:
        if key in self.map.keys():
            self.removeNode(self.map[key])
            self.pushNode(self.map[key], self.dummyTail)
            return self.map[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map.keys():
            self.map[key].val = value
            self.removeNode(self.map[key])
            self.pushNode(self.map[key], self.dummyTail)
        else:
            if  self.size < self.capacity :
                self.size += 1
            else: #at capacity
                nodeToDelete = self.dummyHead.next
                self.removeNode(nodeToDelete)
                for k, v in self.map.items():
                    if v == nodeToDelete:
                        del self.map[k] #need key of node to delete
                        break
            newNode = Node()
            newNode.val = value
            self.map[key] = newNode
            self.pushNode(newNode, self.dummyTail)
                
                
                


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)