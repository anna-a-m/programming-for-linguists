"""
Programming for linguists

Implementation of the data structure "Queue"
"""

from typing import Iterable


class _QueueConstructor:
    """"
    Queue Constructor from given data
    """

    def __init__(self, elements, priorities):
        self.elements = elements
        self.priorities = priorities

    @staticmethod
    def _check_type(storage):
        """
        Check whether the params 'elements' and 'priorities' are of right type
        :param storage: iterable object
        :return: True if storage is an iterable object
        """
        return isinstance(storage, Iterable)

    def _check_priorities(self):
        """
        Check whether param 'priorities' contains integers only
        :return: True if 'priorities' contains integers only
        """
        return (len([p for p in self.priorities if isinstance(p, int) and not isinstance(p, bool)])
                == len(self.priorities))

    def _check_length(self):
        """
        Check whether length of params 'elements' and 'priorities' are equal
        :return: True if they are of the same length
        """
        return len(self.elements) == len(self.priorities)

    @staticmethod
    def _find_place(queue, prior_value):
        """
        Find index of 1st element on the right in the queue
        :param queue: list with tuples (element, priority)
        :param prior_value: int
        :return:    index (int) if there is an element on the right
                    None if there is not
        """
        for el, p in queue:
            if p <= prior_value:
                index = queue.index((el, p))
                break
        else:
            index = None
        return index

    def create_queue(self):
        """
        Create queue as list with tuples (element, priority)
        :return: list
        """
        queue = []
        if self._check_type(self.elements) and self._check_type(self.priorities) and self._check_priorities():
            for el, p in zip(self.elements, self.priorities):
                if not queue:
                    queue.append((el, p))
                else:
                    ind = self._find_place(queue, p)
                    if ind is None:
                        queue.append((el, p))
                    else:
                        queue.insert(ind, (el, p))
        elif not self._check_priorities():
            raise TypeError('"priorities" should contain only integers')
        else:
            raise TypeError('attributes "elements" and "priorities" should be of type list')
        if not self._check_length():
            raise ValueError('length of "elements" and "priorities" should be equal')
        return queue


# pylint: disable=invalid-name
class QueueDS:
    """
    Queue Data Structure
    """

    # pylint: disable=unused-argument,missing-module-docstring
    def __init__(self, elements=(), priorities: Iterable = (), max_size: int = None):
        if not priorities:
            priorities = [0] * len(elements)
        self.data = _QueueConstructor(elements, priorities).create_queue()
        self.max_size = max_size
        if max_size is not None:
            self.data = self.data[::-1][:max_size][::-1]

    def put(self, element, priority: int = 0):
        """
        Add the element ‘element’ at the end of queue_
        :param element: element to add to queue_
        :param priority: priority of the given element
        """
        if self.max_size is None or len(self.data) < self.max_size:
            for el, p in self.data:
                if p <= priority:
                    self.data.insert(self.data.index((el, p)), (element, priority))
                    break
            else:
                self.data.insert(0, (element, priority))
        else:
            raise AssertionError('queue is full')

    def get(self):
        """
        Remove and return an item from queue_
        """
        if self.data:
            return self.data.pop(-1)[0]
        else:
            raise AssertionError('queue is empty')

    def get_prioritized(self):
        """
        Remove and return an item from queue_
        """
        if self.data:
            return self.data.pop(-1)
        else:
            raise AssertionError('queue is empty')

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
        return len(self.data) == self.max_size

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
        return self.data[-1][0]

    def top_prioritized(self):
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
        return self.max_size


if __name__ == '__main__':
    # creating queue from list
    Q_list = QueueDS(elements=['Ninth', 'Tenth', 'Eleventh', 'Twelfth'], priorities=[1, 0, 2, 3])
    # creating queue from dict
    Q_dict = QueueDS(elements={'Ninth': 1, 'Tenth': 3, 'Eleventh': 3, 'Twelfth': 3}, priorities=[1, 0, 2, 3],
                     max_size=3)
    # creating queue from str
    Q_str = QueueDS(elements='Doctor Who', priorities=[2, 0, 3, 3, 0, 1, 4, 1, 3, 0])
    Q_str_1 = QueueDS('(1-4)/3')
    for Q in [Q_list, Q_dict, Q_str, Q_str_1]:
        for _ in range(Q.size()):
            print(Q.get_prioritized())
        print()
