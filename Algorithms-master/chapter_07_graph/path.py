'''
寻路算法
每访问一个节点，存储一下所访问的节点是从那个节点过来的from
'''
class Path:
    def __init__(self, graph, s):
        # s : source
        self._G = graph
        assert 0 <= s < self._G.V()
        # s是从哪里起步
        self._s = s
        self._from = [-1] * self._G.V()
        self._visited = [False] * self._G.V()
        self._dfs(s)

    def has_path(self, w):
        """从s到w有没有路径"""
        assert 0 <= w < self._G.V()
        return self._visited[w]

    def path(self, w):
        """从s到w点的路径，倒推的过程"""
        assert 0 <= w < self._G.V()
        s = []
        p = w
        #一直推到了源节点，源节点的值仍然为-1
        while p != -1:
            s.append(p)
            p = self._from[p]
        return s

    def _dfs(self, v):
        self._visited[v] = True
        for i in self._G[v]:
            if not self._visited[i]:
                # 进入节点前，记录一下访问的i节点是从v过来的
                self._from[i] = v
                self._dfs(i)

    def show_path(self, w):
        """打印从s到w点的路径"""
        vec = self.path(w)
        print('start ' + ' -> '.join(
            str(i) for i in vec[::-1]) + ' end')