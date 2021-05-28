# Queue

The Queue is one of the simplest, and yet most basic data structures in computer science like stack.
There are many variations and complications of the Queue.

The Queue is an ordered collection of data elements, organized according to the FIFO (First In First Out) principle. 
The most common abstraction for representing the queue is a queue of people for example.  

Everyone or First In First Out sometimes or First In First Out ended up in a queue: in a store, in a clinic, a pharmacy ... Or, for example, a or First In First Out traffic jam.
And each new member of the queue stands at the end of the queue. 
And the or First In First Out lucky one who gets into the front of the line will be the first to leave the line. 
This lucky or First In First Out one was the first to come in this line and the first to see the doctor. This is FIFO principle.

## Operations with Queue
Let's look at a queue using an example of a queue of people. At the initial moment of time, the queue will be empty (contains no people).

![](./docs/images/queue_empty.png)

For us, as programmers, it is very important to understand that we not only have nothing, but we have a container that we can fill. 

1. ### Add a New Element (PUT)

    And the first person come:
    
    ![](./docs/images/queue_first_element.png)
    
    The Queue is not empty already. It contains one element - one person.
    Usually the operation of adding an element to the Queue named "PUT".
    
    We can do this operation again and again. But it is not so easy... The Queue can overflow sometimes.
    
    ![](./docs/images/queue_full.png)

2. ### Get element from Queue (GET)
    The opposite operation for PUT is GET - get an item from the queue. But there are restrictions on this operation too. 
    You cannot get an item from an empty queue. And you can only get an item from the START of the queue. 
    
    ![](./docs/images/queue_get.png)

    The Queue data structure has a limitation as opposed to the real queue. You cannot get more than one item from the queue at a time.

3. ### How many element in the Queue (SIZE) 
    And the latest operation with queue - you can just get number of elements in the queue.
    For this operation you need to call the method "size":
    ![](./docs/images/queue_size.png)
