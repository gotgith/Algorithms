from heapq import heappush
from heapq import heappop

class LazyPrimMST:
    def __init__(self, graph):
        self._G = graph
        self._pq = []
        # 记录节点的状态
        self._marked = [False] * self._G.V()
        # 存储v-1条边
        self._mst = []
        #最小生成树的权
        self._mst_weight = None
        self._visit(0)
        while self._pq:
            # 最小堆
            e = heappop(self._pq)
            # 判断横切边的俩个点是否在一个阵营
            if self._marked[e.v()] == self._marked[e.w()]:
                continue
            self._mst.append(e)
            # 找到新的结点
            if not self._marked[e.v()]:
                self._visit(e.v())
            else:
                self._visit(e.w())
        # 把最小生成树的最小权值设置为_mst中第一个元素的权值
        self._mst_weight = self._mst[0].wt()
        for each in self._mst[1:]:
            self._mst_weight += each.wt()

    # 返回最小生成树的所有边
    def mst_edges(self):
        return self._mst

    # 返回生成的最小生成树的权值
    def result(self):
        return self._mst_weight

    def _visit(self, v):
        #判断v还未被访问
        assert not self._marked[v]
        self._marked[v] = True
        for e in self._G[v]:
            if not self._marked[e.other(v)]:
                heappush(self._pq, e)