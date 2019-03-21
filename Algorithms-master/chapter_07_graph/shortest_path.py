'''
广度优先遍历实现无权图的最短路径
'''
from collections import deque

class ShortestPath:
    def __init__(self, graph, s):
        self._G = graph
        assert 0 <= s < self._G.V()
        # s是从哪里起步
        self._s = s
        self._from = [-1] * self._G.V()
        self._visited = [False] * self._G.V()
        # order数组记录从s到每一个点的最短距离
        self._ord = [-1] * self._G.V()
        self._bfs()

    def has_path(self, w):
        """从s到w有没有路径"""
        assert 0 <= w < self._G.V()
        return self._visited[w]

    def path(self, w):
        """从s到w点的路径"""
        assert 0 <= w < self._G.V()
        s = []
        p = w
        while p != -1:
            s.append(p)
            p = self._from[p]
        return s

    def show_path(self, w):
        """打印从s到w点的路径"""
        vec = self.path(w)
        print('start ' +  ' -> '.join(str(i) for i in vec[::-1]) + ' end')

    #查询从s到w的最短路径长度
    def length(self, w):
        assert 0 <= w < self._G.V()
        return self._ord[w]

    def _bfs(self):
        queue = deque()
        queue.append(self._s)
        self._visited[self._s] = True
        while queue:
            """ 移除并返回最左边的元素 """
            curr = queue.popleft()
            #删除元素相邻节点
            for i in self._G[curr]:
                if not self._visited[i]:
                    queue.append(i)
                    self._visited[i] = True
                    #从curr走到i节点
                    self._from[i] = curr
                    self._ord[i] = self._ord[curr] + 1
