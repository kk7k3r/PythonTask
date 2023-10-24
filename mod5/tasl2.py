class Node:
    """
    Вспомогательный класс для узлов списка
    """
    def __init__(self, data):
        self.data = data  # храним информацию
        self.nref = None  # ссылка на следующий узел
        self.pref = None  # Ссылка на предыдущий узел


class Queue:
    """
    Основной класс
    """

    def __init__(self):
        self.start = None  # ссылка на начало очереди
        self.end = None  # ссылка на конец очереди

    def pop(self):
        """
        возвращаем элемент val из начала списка с удалением из списка
        """
        if (self.start == None):
            return
        val = self.start.data
        self.start = self.start.nref
        return val

    def push(self, val):
        """
        добавление элемента val в конец списка
        """
        curr = Node(val)
        if (self.end != None):
            self.end.nref = curr
            curr.pref = self.end
            self.end = curr
        else: 
            self.start = curr
            self.end = curr

        pass

    def insert(self, n, val):
        """
        вставить элемент val между элементами с номерами n-1 и n
        """
        curr = Node(val)
        if (n == 0):
            curr.nref = self.start
            self.start = curr
            return
        nref = self.start
        pref = self.start
        while n != 0:
            if nref == None:
                break
            pref = nref
            nref = nref.nref
            n -= 1
        curr.pref = pref
        curr.nref = nref
        pref.nref = curr
        if nref != None:
            nref.pref = curr
        pass

    def print(self):
        """
        вывод на печать содержимого очереди
        """
        curr = self.start
        while curr != None:
            print(curr.data)
            curr = curr.nref
        pass
    
queue = Queue()
queue.push(1)
queue.push(2)
queue.push(3)
queue.push(4)
queue.pop()
queue.insert(-1, 8)
queue.print()