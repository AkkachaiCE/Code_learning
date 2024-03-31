class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negatibe integer.")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("n must be a non-negatibe integer.")
        if self._size + n > self._capacity:
            raise ValueError("Exceed the cookie's capacity")
        self._size = self._size + n

    def withdraw(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("n must be a non-negatibe integer.")
        if self._size < n:
            raise ValueError("Not enough cookie to withdraw")
        self._size = self._size - n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
