class Stack:
    def __init__(self):
        self.items = []  # Используем список для хранения элементов

    def push(self, item):
        """Добавить элемент в стек"""
        self.items.append(item)

    def pop(self):
        """Удалить и вернуть верхний элемент"""
        if not self.is_empty():
            return self.items.pop()
        return "Стек пуст"

    def peek(self):
        """Посмотреть верхний элемент без удаления"""
        if not self.is_empty():
            return self.items[-1]
        return "Стек пуст"

    def is_empty(self):
        """Проверить, пуст ли стек"""
        return len(self.items) == 0

    def size(self):
        """Получить количество элементов в стеке"""
        return len(self.items)


# ✅ Тестируем стек
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print(stack.pop())  # 30
print(stack.peek())  # 20
print(stack.size())  # 2
