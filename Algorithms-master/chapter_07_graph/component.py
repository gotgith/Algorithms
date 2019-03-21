'''
计算连通分量
每一次深度优先遍历都会把所有相连接的节点遍历一遍，用来求连通分量
'''
class Component:
    """Only for dense graph"""
    def __init__(self, graph):
        self._graph = graph
        #是否被访问过
        self._visited = [False] * graph.V()
        #连通分量
        self._ccount = 0
        #俩个点是否相连，相连的节点id相同，在同一个连通分量里面
        self._id = [-1] * graph.V()
        for i in range(graph.V()):
            if not self._visited[i]:
                #deep first search
                #与i相连接所有节点遍历一次
                self._dfs(i)
                self._ccount += 1

    def count(self):
        return self._ccount

    def _dfs(self, v):
        self._visited[v] = True
        #在同一个连通分量值相同
        self._id[v] = self._ccount
        for i in self._graph[v]:
            if not self._visited[i]:
                #若没有访问过，继续访问下一个节点
                self._dfs(i)

    #判断俩个节点是否相连
    def is_connected(self, v, w):
        assert 0 <= v < self._graph.V()
        assert 0 <= w < self._graph.V()
        return self._id[v] == self._id[w]