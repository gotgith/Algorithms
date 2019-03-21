#创建一个稠密图
class DenseGraph:
    def __init__(self, n, directed):
        # n表示图的节点数
        self._n = n
        # m表示图的边数
        self._m = 0
        self._directed = directed
        #实现一个n阶二维矩阵
        self._g = [[False] * n for _ in range(n)]

    def V(self):
        return self._n

    def E(self):
        return self._m

    def add_edge(self, v, w):
        """顶点v和顶点w连接"""
        assert 0 <= v < self._n
        assert 0 <= w < self._n
        #因为有边的情况下，不做任何处理，就排除了平行边
        if (self.has_edge(v, w)):
            return
        #若是有向图，只需要执行下面这一句话
        self._g[v][w] = True
        if not self._directed:
            #无向图所加条件
            self._g[w][v] = True
        self._m += 1

    #判断v和w之间是否有边
    def has_edge(self, v, w):
        assert 0 <= v < self._n
        assert 0 <= w < self._n
        return self._g[v][w]

    def __iter__(self):
        yield from self._g

    def __len__(self):
        return self._n

    def __getitem__(self, v):
        assert 0 <= v < self._n
        return self._g[v]

    def __str__(self):
        ret = ['<DenseGraph object>:']
        for v in range(len(self._g)):
            # b、d、o、x分别是二进制、十进制、八进制、十六进制
            ret.append('{:2d}: '.format(v) +
                       ' '.join('{:2d}'.format(w) for w in self._g[v]))
        return '\n'.join(ret)

    def __repr__(self):
        return self.__str__()

    @classmethod
    def from_local_file(cls, directed, filename):
        with open(filename, 'r') as f:
            rows = f.read()
        rows = rows.split('\n')
        data = [[int(j) for j in each_row_str.split()]
                for each_row_str in rows]
        graph = cls(n=len(data), directed=directed)
        for v in range(len(data)):
            #读取数据，构成图
            for w in data[v]:
                graph.add_edge(v, w)
        return graph