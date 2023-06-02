class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        que = Node(data, None)
        if not self.head:
            self.head = que
            self.tail = que
        else:
            self.tail.next_node = Node(data, None)
            self.tail = self.tail.next_node

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        if self.head:
            inf = self.head.data
            self.head = self.head.next_node
            return inf
        else:
            return None

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        i = self.head
        info = ''
        while i:
            info += str(i.data) + '\n'
            i = i.next_node
        return info[:-1]



