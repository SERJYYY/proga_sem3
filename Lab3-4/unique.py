class Unique(object):
    def __init__(self, items, **kwargs):
        self.cur = 0
        self.ignore_case = kwargs.get("ignore_case", False)
        self.data = []
        if self.ignore_case:
            for el in items:
                if el not in self.data and type(el) is not str:
                    self.data.append(el)
                elif type(el) is str and el.lower() not in self.data:
                    self.data.append(el.lower())
        else:
            for el in items:
                if el not in self.data:
                    self.data.append(el)

    def __next__(self):
        if self.cur < len(self.data):
            self.cur += 1
            return self.data[self.cur - 1]
        raise StopIteration

    def __iter__(self):
        return self


if __name__ == '__main__':
    arr = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    # arr = [1,2,2,3,3,1]
    it = Unique(arr, ignore_case=True)
    for el in it:
        print(el)