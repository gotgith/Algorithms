from chapter_03_Stack_Queue.base import QueueBase
from chapter_03_Stack_Queue.queue import ArrayQueue

class LoopQueue(QueueBase):
    def __init__(self, capacity=8):
        """浪费一个空间
        (tail + 1) % c == front"""
        self._data = [None] * (capacity + 1)
        self._front = 0
        self._tail = 0
        self._size = 0

    #有效容量
    def get_capacity(self):
        return len(self._data) - 1

    def is_empty(self):
        return self._front == self._tail

    def get_size(self):
        return self._size

    def enqueue(self, e):
        if (self._tail + 1) % len(self._data) == self._front:
            self._resize(self.get_capacity() * 2)
        self._data[self._tail] = e
        #取余，循环队列
        self._tail = (self._tail + 1) % len(self._data)
        self._size += 1

    def dequeue(self):
        # 使用循环队列出队时间复杂度为O(1)
        if (self.is_empty()):
            raise ValueError('Can not dequeue from an empty queue.')
        ret = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if self._size == self.get_capacity() // 4 and \
                self.get_capacity() // 2 != 0:
            self._resize(self.get_capacity() // 2)
        return ret

    def get_front(self):
        if self.is_empty():
            raise ValueError('Can not get_front from an empty queue.')
        return self._data[self._front]

    def _resize(self, new_capacity):
        new_data = [None] * (new_capacity + 1)
        for i in range(self._size):
            #把数据放到new_data中，仔细体会，循环遍历
            #_data中front不一定在0k开始，所有有front个偏移
            new_data[i] = self._data[(i + self._front) % len(self._data)]
        self._data = new_data
        self._front = 0
        self._tail = self._size

    def __str__(self):
        if self._tail >= self._front:
            return str('<chapter_03_Stack_Queue.queue.LoopQueue> '
                ': front {} tail,'' capacity: {}'
                       .format(self._data[self._front:self._tail],
                        self.get_capacity()))
        else:
            # presentation purpose only
            return str('<chapter_03_Stack_Queue.queue.LoopQueue> : '
                       'front {} tail, capacity: {}'
                       .format(str(self._data[self._front:] +
                                  self._data[:self._tail]),
                                    self.get_capacity()))

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    # queue = LoopQueue()
    # queue.enqueue(1)
    # queue.enqueue(4)
    # queue.enqueue(3)
    # queue.enqueue(0)
    # queue.enqueue(10)
    # queue.enqueue(10)
    # queue.enqueue(10)
    # queue.enqueue(10)
    # print(queue)
    #
    #
    # queue.dequeue()
    # queue.enqueue(3)
    # print(queue)
    # queue.dequeue()
    # print(queue)
    # queue.dequeue()
    # queue.enqueue(3)
    # print(queue)
    # queue.dequeue()
    # print(queue)

    from time import time
    from random import randint

    def test_enqueue(queue, op_count):
        #开始时间
        start_time = time()
        for i in range(op_count):
            queue.enqueue(randint(1, 2000))
        for i in range(op_count):
            queue.dequeue()
            #结束减去开始时间
        return time() - start_time

    # def test_dequeue(queue, op_count):
    #     start_time = time()
    #     for i in range(op_count):
    #         queue.dequeue()
    #     return time() - start_time

    #入队和出队的操作次数
    op_count = 100000
    array_queue = ArrayQueue()
    loop_queue = LoopQueue()

    print('ArrayQueue enqueue: ', test_enqueue(array_queue, op_count))
    print('LoopQueue enqueue: ', test_enqueue(loop_queue, op_count))

    # print('ArrayQueue dequeue: ', test_dequeue(array_queue, op_count))
    # print('LoopQueue dequeue: ', test_dequeue(loop_queue, op_count))