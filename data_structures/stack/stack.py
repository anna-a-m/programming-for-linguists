"""
Programming for linguists

Implementation of the data structure "Stack"
"""


from typing import Iterable


class Stack:
    """
    Stack Data Structure
    """
    # pylint: disable=missing-module-docstring
    def __init__(self, data: Iterable = None, n_stop: int = 1):
        self.data = list(data) if data else []
        self.stop = n_stop

    def push(self, element):
        """
        Add the element ‘element’ at the top of stack
        :param element: element to add to stack
        """
        if len(self.data) < self.stop:
            self.data.append(element)
        else:
            raise IndexError('The stack is full')

    def pop(self):
        """
        Delete the element on the top of stack
        """
        if self.data:
            self.data.pop(-1)
        else:
            raise ValueError

    def top(self):
        """
        Return the element on the top of stack
        :return: the element that is on the top of stack
        """
        if self.data:
            return self.data[-1]
        else:
            raise ValueError

    def size(self) -> int:
        """
        Return the number of elements in stack
        :return: Number of elements in stack
        """
        return len(self.data)

    def empty(self) -> bool:
        """
        Return whether stack is empty or not
        :return: True if stack does not contain any elements
                 False if stack contains elements
        """
        return not bool(self.data)
