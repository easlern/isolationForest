class Leaf:
    def __init__(self, locationAsArray, item):
        self.LocationAsArray = locationAsArray
        self.Item = item
        self.Depth = None

    def __str__(self):
        return str(self.LocationAsArray) + ' ' + str(self.Item)

    def __lt__(self, other):
        return str(other.Item) < str(self.Item)