"""
Programming for linguists

Implementation of the data structure "Queue"
"""

from typing import Iterable


# pylint: disable=invalid-name
class Queue_:
    """
    Queue Data Structure
    """

    # pylint: disable=unused-argument,missing-module-docstring
    def __init__(self, data: Iterable = (), max_size: int = None, rank: tuple = ()):
        self.data = []
        self.rank = rank
        if max_size and len(self.rank) < max_size:
            while not len(self.rank) == max_size:
                self.rank += (0,)
        elif not max_size and data:
            self.rank = tuple([0] * len(data))
        if max_size and data:
            for i in range(max_size):
                self.data.insert(self.rank[i], data[i])
        elif data:
            for i, element in enumerate(data):
                self.data.insert(self.rank[i], element)
        self.stop = max_size

    def put(self, element):
        """
        Add the element ‘element’ at the end of queue_
        :param element: element to add to queue_
        """
        if len(self.data) < self.stop:
            self.data.insert(0, element)
        else:
            raise AssertionError

    def get(self):
        """
        Remove and return an item from queue_
        """
        if self.data:
            return self.data.pop(-1)
        else:
            raise AssertionError

    def empty(self) -> bool:
        """
        Return whether queue_ is empty or not
        :return: True if queue_ does not contain any elements.
                 False if the queue_ contains elements
        """
        return not self.data

    # pylint: disable=no-self-use
    def full(self) -> bool:
        """
        Return whether queue_ is full or not
        :return: True if queue_ is full.
                 False if queue_ is not full
        """
        return len(self.data) == self.stop

    def size(self) -> int:
        """
        Return the number of elements in queue_
        :return: Number of elements in queue_
        """
        return len(self.data)

    def top(self):
        """
        Return the first element in queue_
        :return: Item from queue_
        """
        return self.data[-1]

    # pylint: disable=no-self-use
    def capacity(self) -> int:
        """
        Return the maximal size of queue_
        :return: Maximal size of queue_
        """
        return self.stop


if __name__ == '__main__':
    Q = Queue_(data=['Ann', 'Lisa', 'Clara', 'Astrid', 'cat', 'dog', 'mouse'], max_size=7, rank=(0, 0, 2, 1, 3, 0))
    Q1 = Queue_(data=['Ann', 'Lisa', 'Clara', 'Astrid', 'cat', 'dog', 'mouse'], max_size=7)
    for i in range(7):
        print(Q.get(), '\t', Q1.get())
