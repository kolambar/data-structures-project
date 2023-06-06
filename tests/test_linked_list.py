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

    def test_to_list(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 0, 'username': 'serebro'})
        ll.insert_at_end({'id': 3, 'username': 'mosh_s'})

        lst = ll.to_list()
        assert lst[0] == {'id': 0, 'username': 'serebro'}
        assert lst[1] == {'id': 3, 'username': 'mosh_s'}

    def test_get_data_by_id(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 0, 'username': 'serebro'})
        ll.insert_at_end({'id': 3, 'username': 'mosh_s'})

        user_data = ll.get_data_by_id(0)
        assert user_data == {'id': 0, 'username': 'serebro'}