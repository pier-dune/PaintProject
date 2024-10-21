class Point:
    def __init__(self, coords=(0, 0)):
        self.x = coords[0]
        self.y = coords[1]

    def __add__(self, other):
        return Point((self.x + other.x, self.y + other.y))

    def __sub__(self, other):
        return Point((self.x - other.x, self.y - other.y))

    def to_tuple(self):
        tuple_point = (self.x, self.y)
        return tuple_point

    def __str__(self):
        return f"({self.x}, {self.y})"

