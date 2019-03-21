class Array:
    def __init__(self, arr=None, capacity=10):
        if isinstance(arr, list):
            self._data = arr[:]
            self._size = len(arr)
            return
        #创建一个容量为capacity的空间，值都为None
        self._data = [None] * capacity
        self._size = 0

    def get_size(self):
        return self._size

    def get_capacity(self):
        return len(self._data)

    def is_empty(self):
        return self._size == 0

    #向所有元素后添加一个新元素
    def add_last(self, e):
        self.add(self._size, e)

    # 向所有元素前添加一个新元素
    def add_first(self, e):
        self.add(0, e)

    #在制定位置插入元素
    def add(self, index, e):
        if not 0 <= index <= self._size:
            raise ValueError(
                'add failed. Require index >= 0 and index <= array sise.')
        if self._size == len(self._data):
            if self._size == 0:
                self._resize(1)
            else:
                self._resize(2 * len(self._data))
        #range(start, stop, step)，从后往前
        for i in range(self._size - 1, index - 1, -1):
            self._data[i + 1] = self._data[i]
        self._data[index] = e
        self._size += 1

    #获取
    def get(self, index):
        if not 0 <= index < self._size:
            raise ValueError('get failed. Index is illegal.')
        return self._data[index]

    def get_last(self):
        return self.get(self._size - 1)

    def get_first(self):
        return self.get(0)

    #修改
    def set(self, index, e):
        if not 0 <= index < self._size:
            raise ValueError('set failed. Index is illegal.')
        self._data[index] = e

    #查询是否存在
    def contains(self, e):
        for i in range(self._size):
            if self._data[i] == e:
                return True
        return False

    #查找数组中元素e的索引，若不存在则返回-1
    def find(self, e):
        for i in range(self._size):
            if self._data[i] == e:
                return i
        return -1

    #删除，从右往左，覆盖操作，最后一个元素查询条件不会通过
    def remove(self, index):
        if not 0 <= index < self._size:
            raise ValueError('remove failed. Index is illegal.')
        ret = self._data[index]
        for i in range(index + 1, self._size):
            self._data[i - 1] = self._data[i]
        self._size -= 1
        # len(self._data)如果为1，len(self._data) // 2就会为0，不合理。
        if (self._size == (len(self._data) // 4) and (len(self._data) // 2) != 0):
            self._resize(len(self._data) // 2)
        return ret

    #删除第一个元素
    def remove_first(self):
        return self.remove(0)

    #删除最后一个元素
    def remove_last(self):
        return self.remove(self._size - 1)

    #删除指定元素
    def remove_element(self, e):
        index = self.find(e)
        if index != -1:
            self.remove(index)

    #开辟一个新的空间
    def _resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data

    #交换索引i和索引j俩个元素的位置
    def swap(self, i, j):
        if i < 0 or i >= self._size or j < 0 or j >= self._size:
            raise ValueError('Index is illegal.')
        self._data[i], self._data[j] = self._data[j], self._data[i]

    #格式化字符串的函数 str.format()，它增强了字符串格式化的功能。
    #基本语法是通过 {} 和 : 来代替以前的 % 。
    #format 函数可以接受不限个参数，位置可以不按顺序。
    def __str__(self): #返回一个好看的字符串
        return str('<chapter_02_Array.array.Array> : {}, capacity: {}'
            .format(self._data[:self._size], self.get_capacity()))

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    arr = Array()

    for i in range(10):
        arr.add_last(i)
    print(arr)
    #arr.add_last('zhe')
    # arr.add_last('wang')
    # arr.add_last('zwang')

    arr.add(1, 'lalal')
    print(arr)

    arr.remove_element('lalal')
    print(arr)

    arr.add_first(-1)
    print(arr)

    arr.remove_element(4)
    print(arr)

    arr.remove_element(1)
    print(arr)
    arr.remove_element(2)
    arr.remove_element(3)
    arr.remove_element(5)
    arr.remove_element(6)
    arr.remove_element(7)
    arr.remove_element(8)
    print(arr)
