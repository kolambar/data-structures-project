class Node:
    """Класс для узла односвязного списка"""
    def __init__(self, data):
        self.data = data
        self.next_node = None

    def __repr__(self):
        return f'data {self.data} next_node {self.next_node}'



class LinkedList:
    """Класс для односвязного списка"""
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        data = Node(data)
        if self.head:
            new_node = data
            new_node.next_node = self.head
            self.head = new_node
        else:
            self.head = data
            self.tail = data

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        self.tail.next_node = Node(data)
        self.tail = self.tail.next_node

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f'{str(node.data)} -> '
            node = node.next_node

        ll_string += 'None'
        return ll_string

    def to_list(self) -> list:
        """Возвращает все данные в виде списка"""
        lst = []
        lst.append(self.head.data)  # считывает данные из head
        step = self.head.next_node
        while step:  # считывает данные дальше
            lst.append(step.data)
            step = step.next_node
        return lst

    def get_data_by_id(self, id):
        """Ищет блок с указанным id"""
        if self.head.data['id'] == id:
            return self.head.data
        else:
            step = self.head.next_node
            while step:
                # обрабатывает ошибку, если какой-то блок поврежден
                try:
                    if step.data['id'] == id:
                        return step.data
                    else:
                        step = step.next_node
                except TypeError:
                    print('Данные не являются словарем или в словаре нет id.')
                    step = step.next_node
