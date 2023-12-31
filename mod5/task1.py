class Node:
    """
    Вспомогательный класс для узлов списка
    """
    def __init__(self, data):
        self.data = data  # храним информацию
        self.pref = None  # ссылка на предыдущий узел

class Stack:
    """
    Основной класс для стека
    """

    def __init__(self):
        self.end = None  # ссылка на конец стека

    def pop(self):
        """
        возвращение последнего элемента из списка с удалением его из списка
        """
        if (self.end == None):
            return
        val = self.end.data
        self.end = self.end.pref
        return val

    def push(self, val):
        """
        добавление элемента val в конец списка
        """
        node = Node(val)
        node.pref = self.end
        self.end = node
        pass

    def print(self):
        """
        вывод на печать содержимого стека
        """
        curr = self.end
        while curr != None:
            print(curr.data)
            curr = curr.pref
        pass
