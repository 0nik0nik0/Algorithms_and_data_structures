def find_min_value_node(node: Node) -> Node:
        """
        Метод позволяет найти узел с минимальным значением в дереве, начиная с заданного узла.
        :param node: Узел, с которого начать поиск
        :return: Узел с минимальным значением
        """
        current = node
        while current.left is not None:
            current = current.left
        return current