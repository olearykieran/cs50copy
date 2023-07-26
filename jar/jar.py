def main():
    print(str(jar))

class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Must be a non-negative int")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return self._size * '🍪'

    def deposit(self, n):
        self._size += n
        if self._size > self._capacity:
            raise ValueError("Capacity exceeded")

    def withdraw(self, n):
        self._size -= n
        if self._size < 0:
            raise ValueError("No cookies in jar")


    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

jar = Jar()
jar.deposit(12)
jar.withdraw(3)

main()
