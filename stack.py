class Stack:
    """docstring for Stack ^_^"""

    def __init__(self):
        self.stack = []

    def size(self):
        """Проверяем размер стека"""
        return len(self.stack)

    def push(self, value):
        """Пушим значение в стек"""
        self.stack.append(value)

    def pop(self):
        """Возвращаем значение из стека с удалением"""
        if self.stack:
            return self.stack.pop()
        else:
            raise IndexError("Попытка удалить элемент из пустого стека")

    def top(self):
        """Возвращаем значение из стека без удаления"""
        if self.stack:
            return self.stack[-1]
        else:
            raise IndexError("Попытка обратиться к верхнему элементу пустого стека")

    def clear(self):
        """Очищаем стек"""
        self.stack = []

    def __str__(self):
        """Выводим стек"""
        return str(self.stack)


if __name__ == '__main__':
    stack = Stack()

    # Добавляем элементы в стек
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("Стек после добавления элементов:", stack)

    # Показываем верхний элемент
    print("Верхний элемент:", stack.top())

    # Удаляем элемент из стека
    stack.pop()
    print("Стек после удаления элемента:", stack)

    # Очищаем стек
    stack.clear()
    print("Стек после очистки:", stack)

    # Проверка размера
    print("Размер стека:", stack.size())