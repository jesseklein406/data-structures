[![Build Status](https://travis-ci.org/jesseklein406/data-structures.svg?branch=bst2)](https://travis-ci.org/jesseklein406/data-structures)

#Data Structures Assignments
####Jesse Klein & Muoi Ly


###Queue Data Structures Assignment
Access 'queue.py' for the class Queue and create a queue to hold data.
The test file for the module is 'test_queue.py'.


###Linked List Assignment
Use LinkedList class from link_list.py to implement a singly linked list


###Stack Assignment
Use Stack class from stack.py to implement the class and its methods, push(value) and pop(). The Stack class inherets methods from LinkedList using composition. We referred to Learn Python the Hard Way for implementing composition: http://learnpythonthehardway.org/book/ex44.html


###Doubly Linked List Data Structures Assignment
Access 'dll.py' for the class Dll and create a doubly linked list to hold data.
The test file for the module is 'test_dll.py'.


###Binary Heap Data Structures Assignment
Access 'binheap.py' for the class Binheap and create a doubly linked list to hold data.
The test file for the module is 'test_binheap.py'.


###Priority Queue Data Structures Assignment
Access 'priorityq.py' for the class PriorityQ and create a doubly linked list to hold data.
The test file for the module is 'test_priorityq.py'. This assignment heavily uses code from
the previous binary heap assignment.


###Simple Graph Assignment
Access 'simple_graph.py' for the class G and create a graph object to hold data.
The test file for the module is 'test_simple_graph.py'. This assignment heavily uses code from
the previous binary heap assignment. Thanks to Martin Broadhurst for a great resource. http://www.martinbroadhurst.com/graph-data-structures.html


###Graph Traversal Assignment
Access 'simple_graph.py' for traversal methods for the class G.
The test file for the module is 'test_graph_traversal.py'. I referred to [Wikipedia](https://en.wikipedia.org/wiki/Graph_traversal) for this assignment.


###Graph with Weighted Edges Assignment
Access 'simple_graph.py' to implement weighted edges for the class G and Node class.
The test file for the module is 'test_weighted_edges.py'.

###Graph Algorithms for Shortest Path Assignment
Access 'simple_graph.py' for shortest path algorithms for the class G.
The test file for the module is 'test_shortest_path.py'.

The two algorithms I chose were Dijkstra's and Bellman-Ford's. 
I referred to [Wikipedia](https://en.wikipedia.org/wiki/Shortest_path_problem) for this assignment. Specifically, I implemented the methods used in the pseudocode for my two algorithms from the articles for the algorithms [here](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm) and [here](https://en.wikipedia.org/wiki/Bellman–Ford_algorithm).

Dijkstra's algorithm will always find the shortest path with as few iterations as possible because it cherry picks the least weighted path to execute on first. Thus the path may continue to retain priority if its total weight keeps undercutting other paths. Bellman-Ford's can execute on negative weights as well as check for runaway de-weighting. Beyond those special casesm Dijkstra's is optimal.