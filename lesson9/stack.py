class Stack():
    def __init__(self):
        self._stack = []

    def push(self, v):
        self._stack.append(v)

    def pop(self):
        if len(self._stack) == 0:
            raise IndexError('Empty stack')
        else:
            self._stack.pop()

    def head(self):
        return self._stack[-1]