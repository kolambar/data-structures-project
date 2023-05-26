"""Здесь надо написать тесты с использованием unittest для модуля queue."""
from src.queue import Queue
import unittest


class TestNode(unittest.TestCase):

    def test_enqueue(self):
        queue = Queue()
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')
        assert queue.head.data == 'data1'
        assert queue.head.next_node.data == 'data2'
        assert queue.tail.data == 'data3'
        assert queue.tail.next_node is None

    def test___str__(self):
        assert str(Queue()) == ""

        queue = Queue()
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')

        assert str(queue) == "data1\ndata2\ndata3"
