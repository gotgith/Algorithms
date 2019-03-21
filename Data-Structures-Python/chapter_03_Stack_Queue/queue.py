from chapter_02_Array.array import Array
from chapter_03_Stack_Queue.base import QueueBase


class ArrayQueue(QueueBase):
    def __init__(self, capacity=0):
        self._array = Array(capacity)

    #查看长度
    def get_size(self):
        return self._array.get_size()

    #查看是否为空
    def is_empty(self):
        return self._array.is_empty()

    def get_capacity(self):
        return self.get_capacity()

    #进队
    def enqueue(self, e):
        self._array.add_last(e)

    #出队
    def dequeue(self):
        return self._array.remove_first()

    #查询
    def get_front(self):
        return self._array.get_first()

    def __str__(self):
        return str('<chapter_03_Stack_Queue.queue.ArrayQueue> : {}'
                   .format(self._array))

    def __repr__(self):
        return self.__str__()




if __name__ == '__main__':
    array = ArrayQueue()
