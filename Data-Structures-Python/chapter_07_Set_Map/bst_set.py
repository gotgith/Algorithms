from chapter_06_BST.bst import BST
from chapter_07_Set_Map.base import SetBase

#实现的二分搜索树本身就支持集合
class BSTSet(SetBase):
    def __init__(self):
        self._bst = BST()

    def get_size(self):
        return self._bst.size()

    def is_empty(self):
        return self._bst.is_empty()

    def add(self, e):
        return self._bst.add(e)

    def contains(self, e):
        return self._bst.contains(e)

    def remove(self, e):
        return self._bst.remove(e)


if __name__ == '__main__':
    words = ''
    with open('./shakespeare.txt', 'r') as f:
        words = f.read()
    words = words.split()

    from time import time
    start_time = time()
    bst_set = BSTSet()
    for word in words:
        #add不重复
        bst_set.add(word)

    print('Total words: ', len(words))
    print('Unique words: ', bst_set.get_size())
    print('Contains word "they": ', bst_set.contains('they'))
    #耗时三秒
    print('Total time: {} seconds'.format(time() - start_time))