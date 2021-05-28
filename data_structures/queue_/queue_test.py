"""
Programming for linguists

Tests for Queue class.
"""

import unittest

from data_structures.queue_.queue_ import Queue_


class QueueTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementation of Stack
    """

    def test_new_queue_is_empty(self):
        """
        Create an empty Queue.
        Test that its size is 0.
        """
        queue = Queue_()
        self.assertTrue(queue.empty())
        self.assertEqual(queue.size(), 0)

    def test_new_queue_with_max_number_is_empty(self):
        """
        Create an empty Queue with specified maximal size.
        Test that its size is 0.
        """
        queue = Queue_(max_size=10)
        self.assertTrue(queue.empty())
        self.assertEqual(queue.size(), 0)

    def test_new_queue_from_tuple(self):
        """
        Create a Queue from an iterable object.
        Check that the size of queue_ equals to the size of the given tuple.
        """
        data = (1, None, [], Queue_())
        queue = Queue_(data=data)
        self.assertFalse(queue.empty())
        self.assertEqual(queue.size(), len(data))
        self.assertFalse(queue.full())
        for value in data:
            test_value = queue.get()
            self.assertEqual(test_value, value)
        self.assertTrue(queue.empty())
        self.assertEqual(queue.size(), 0)

    def test_new_queue_from_tuple_with_max_size(self):
        """
        Create an empty Queue from the given data and put elements to queue_.
        """
        data = (1, None, [], Queue_())
        queue = Queue_(data=data, max_size=len(data) - 2)
        self.assertFalse(queue.empty())
        self.assertEqual(queue.size(), len(data) - 2)
        self.assertTrue(queue.full())
        for value in data[:-2]:
            test_value = queue.get()
            self.assertEqual(test_value, value)
        self.assertTrue(queue.empty())
        self.assertEqual(queue.size(), 0)

    def test_call_get_of_empty_queue_raised_error(self):
        """
        Create an empty Queue.
        Test that call of get function raises Assertion error
        """
        queue = Queue_()
        self.assertRaises(AssertionError, queue.get)

    def test_call_put_of_fully_queue_raised_error(self):
        """
        Create a Queue with maximum size=0.
        Test that call of put function raises Assertion error
        """
        queue = Queue_(max_size=1)
        queue.put(0)
        self.assertRaises(AssertionError, queue.put, 1)

    def test_call_full_of_not_full_queue(self):
        """
        Create a Queue with 0 elements.
        Test that call of full-function returns False
        """
        data = ()
        queue = Queue_(data)
        self.assertFalse(queue.full())
        self.assertEqual(queue.capacity(), None)
