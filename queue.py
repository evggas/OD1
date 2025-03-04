class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Добавить элемент в конец очереди"""
        self.items.append(item)

    def dequeue(self):
        """Удалить и вернуть первый элемент"""
        if not self.is_empty():
            return self.items.pop(0)
        return "Очередь пуста"

    def is_empty(self):
        """Проверить, пуста ли очередь"""
        return len(self.items) == 0

    def size(self):
        """Получить количество элементов в очереди"""
        return len(self.items)

# Тестируем очередь
queue = Queue()
queue.enqueue("Аня")
queue.enqueue("Боря")
queue.enqueue("Вика")

print(queue.dequeue())  # "Аня"
print(queue.size())  # 2
