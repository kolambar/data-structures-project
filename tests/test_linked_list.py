"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
from src.linked_list import Node, LinkedList
import unittest


class TestNode(unittest.TestCase):

    def test_insert_beginning(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        assert str(ll) == "{'id': 1} -> None"
        ll.insert_beginning({'id': 2})
        assert str(ll) == "{'id': 2} -> {'id': 1} -> None"


    def test_insert_at_end(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        ll.insert_at_end({'id': 2})
        assert str(ll) == "{'id': 1} -> {'id': 2} -> None"

    def test_Node(self):
        test_block = Node({'id': 1})
        assert str(test_block) == "data {'id': 1} next_node None"