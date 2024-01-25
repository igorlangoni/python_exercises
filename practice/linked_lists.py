# Defining a Linked List
class LinkedList:
    def __init__(self, nodes=None):
        self.head = None # a linked list only need a head(first element) to be initialized
        # Alternatively, we can implement the below piece of code to facilitate creation of l-lists
        # It's possible then to instanciate an object with the nodes as parameters,e.g: l-list = LinkedList('a','b','c')
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    # a repr method to help with visualization
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("none")
        return " --> ".join(nodes)
    
    # Traversing a L-List (Iterating) This method allows for iteration over the l-list
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
    
    # Inserting Nodes (Beggining of the l-list)
    def add_first(self, node):
        node.next = self.head
        self.head = node
    
    # Inserting Nodes (End of the l-list)
    def add_last(self, node):
        if self.head is None: # checks self.head is None, aka last node.  
            self.head = node
            return
        for current_node in self: # Iterates the whole l-list until it finishes, raising an exception
            pass
        current_node.next = node # After the for loop ends (at the (not for long)last node), we add the new node to the end
    
    # Inserting Nodes (Middle of the l-list - the 'after an existing node' approach- )
    def add_after(self, target_node_data, new_node):
        if self.head is None: # checks if l-list is empty
            raise Exception("Empty L-List")
        
        for node in self:   # Iterates over L-List until finding the target node.
            if node.data == target_node_data:
                new_node.next = node.next # First: takes target's next node and assigns it as new node's next
                node.next = new_node #  Second: assigns the new node as target's next
                return
        
        raise Exception(f"Node with data {target_node_data} not found") # In case the target value doesnt exist in L-List
    
     # Inserting Nodes (Middle of the l-list - the 'before an existing node' approach- )
    def add_before(self, target_node_data, new_node):
        if self.head is None: # Checks if l-list is empty
            raise Exception("Empty L-List")
        
        if self.head.data == target_node_data: 
            return self.add_first(new_node) # If target is first node, we use add_first()
        
        prev_node = self.head # We create a prev variable that will be assigned each node that we iterate over
        for node in self:   
            if node.data == target_node_data: # When we reach the target node we work in 2 steps:
                prev_node.next = new_node   # First, we assign the new_node as the previous one's next
                new_node.next = node        # Second, we assing the current_node(target) as next to the new_node
                return
            prev_node = node # At each iteration where the node is NOT the target, we assing this node as prev
        
        raise Exception(f"Node with data {target_node_data} not found") # In case the target value doesnt exist in L-List
    
    # Removing Nodes
    def remove_node(self, target_node_data):
        if self.head is None: # Check for empty list
            raise Exception('Empty L-List')
        
        if self.head.data == target_node_data: # If target is first node, we make the next(second) node as the new head
            self.head = self.head.next
            return 
        
        prev_node = self.head # Much like inserting before a target node, we have to iterate over the l-list keeping track of the prev node
        for node in self:
            if node.data == target_node_data: # When we reach the target data, we need to assign its 'next node' as the next node of the prev node
                prev_node.next = node.next
                return
            prev_node = node
        
        raise Exception(f"Node with data {target_node_data} not found") # In case the target value doesnt exist in L-List


# Creating a Node class, to be used for each Node of the l-list
class Node:
    def __init__(self, data): # it is initialized with 2 values: the actual value of the node(data) and the value of the next node
        self.data = data
        self.next = None
    
    def __repr__(self):
        return self.data



llist = LinkedList()
first_node = Node('a')
llist.head = first_node
second_node = Node('b')
first_node.next = second_node
third_node = Node('c')
second_node.next = third_node


tests_llink = LinkedList(['a','b','c', 'd'])
tests_llink.print()

