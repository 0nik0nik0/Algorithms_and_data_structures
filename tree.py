""" 
Доработать бинарное дерево с семинара, добавить подсчет количества элементов, вывод всего дерева на экран, удаление элемента.
"""


from typing import Any


class Node:
    """
    Класс -  узел в бинарном древе.
    Каждый узел обладает значением (value), левым (left) и правым (right) потомком.
    None - нет потомка.
    """

    def __init__(self, value: int):
        """
        Конструктор для Node
        :param value: целое число
        """
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        """
        Метод создает узел, левого и правого потомка(при наличии).
        :return: String
        """
        result = f'значение нашего узла: {self.value}'
        if self.left:
            result += f' значение левого: {self.left.value}'
        if self.right:
            result += f' значение правого: {self.right.value}'
        return result


class BinaryTree:
    """
    Класс -  бинарное древо.
    """

    def __init__(self, root_value):
        """
        Конструктор класса.
        :param root_value: корневой узел
        """
        self.root = Node(root_value)

    def add(self, *values: int) -> None:
        """
        Метод добавляет новый узел в древо.
        :param values: Целое число
        """
        for value in values:
            result = self.search(self.root, value)

            if result[0] is None:
                new_node = Node(value)
                if value > result[1].value:
                    result[1].right = new_node
                else:
                    result[1].left = new_node

    @staticmethod
    def min_node_search(node: Node) -> Node:
        """
        Метод поиска мин узла в древе.
        :param node: узел начала поиска
        :return: узел с мин значением
        """
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete_node(self, root_value: Node, value: int) -> Node | None | Any:
        """
        Удаляет узел из древа.
        :param root_value: корневой узел древа
        :param value: удалямое значение
        :return: корневой узел древа после удаления
        """

        if root_value is None:
            return root_value

        if value < root_value.value:
            root_value.left = self.delete_node(root_value.left, value)
        elif value > root_value.value:
            root_value.right = self.delete_node(root_value.right, value)
        else:
            if root_value.left is None:
                return root_value.right
            elif root_value.right is None:
                return root_value.left

            min_value_node = self.min_node_search(root_value.right)
            root_value.value = min_value_node.value
            root_value.right = self.delete_node(
                root_value.right, min_value_node.value)

        return root_value

    def delete_element(self, *values: int) -> None:
        """
        Удаление элемента из древа.
        :param values: Целые числа
        :return: None
        """
        for value in values:
            self.root = self.delete_node(self.root, value)

    def search(self, node: Node, value: int, parent=None) -> tuple:
        """
        Метод поиска узла в бинарном дереве(выдает узел + родитель).
        Если узла нет, выдает None и узел, просмотренный последним.
        :param node: узел начала поиска
        :param value: искомый узел
        :param parent: родитель
        :return: узел + родитель
        """
        if node is None or value == node.value:
            return node, parent
        if value > node.value:
            return self.search(node.right, value, node)
        if value < node.value:
            return self.search(node.left, value, node)

    def count_elements(self, node: Node = None) -> int:
        """
        Метод подсчета эл. в древе
        :param node: Начальный узел. Если None, то начинаем с root.
        :return: Кол-во эл в древе.
        """
        if node is None:
            node = self.root
        count = 1
        if node.left is not None:
            count += self.count_elements(node.left)
        if node.right is not None:
            count += self.count_elements(node.right)
        return count

    def show_tree(self, node: Node, level=0) -> None:
        """
        Метод вывода древа в консоль.
        :param node: Начальный узел. Если None, то начинаем с root.
        :param level: Расположение узла в древе
        :return: None
        """
        if node is not None:
            self.show_tree(node.right, level + 1)
            print(f"{' ' * 7 * level} #{'=' * 2}|{node.value}|")
            self.show_tree(node.left, level + 1)


bt = BinaryTree(5)
root = bt.root

bt.add(10)
bt.add(15)
bt.add(3)
bt.add(4)
bt.add(8, 7, 12, 2, 34, 27, 1) 
bt.delete_element(34, 15)

print(f"Total numder of elemets in binary tree = {bt.count_elements()}")
bt.show_tree(bt.root)
