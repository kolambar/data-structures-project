"""Здесь надо написать тесты с использованием unittest для модуля stack."""
from src.stack import Node, Stack
import unittest


class TestNode(unittest.TestCase):

    def test___init__(self):
        n1 = Node(5, None)
        self.assertEqual(n1.data, 5)
        self.assertEqual(n1.next_node, None)

    def test_push(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')

        self.assertEqual(stack.top.data, 'data2')
        self.assertEqual(stack.top.next_node.data, 'data1')

    def test_pop(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        data = stack.pop()
        self.assertEqual(stack.top.data, 'data1')
        self.assertEqual(data, 'data2')


    def test___str__(self):
        stack = Stack()
        stack.push('data1')
        self.assertEqual(str(stack), 'data1')
