class CustomDataStructure:
    def __init__(self):
        self.data = []

    def set(self, i, x):
        if i < 0:
            raise ValueError("Index cannot be negative.")
        elif i < len(self.data):
            self.data[i] = x
        else:
            self._resize_and_set(i, x)

    def _resize_and_set(self, i, x):
        new_data = [None] * (i - len(self.data) + 1)
        self.data += new_data
        self.data[i] = x

    def get(self, i):
        if 0 <= i < len(self.data):
            return self.data[i]
        else:
            raise IndexError("Index out of range.")
