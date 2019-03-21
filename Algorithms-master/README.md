## play-with-data-structures

Python implementation of imooc course [学习算法思想，修炼编程内功](http://coding.imooc.com/class/71.html), thanks for that great course (instructor [liuyubobobo](https://github.com/liuyubobobo)) !

Any pull-request is welcome:)

Any quesitons please email to wangzhe.dut@gmail.com


### Some course notes

1. 选择排序
- 从当前未排序的序列中选择最小的值


2. 插入排序
- 将当前处理的元素插入到前面排好的位置上，对于近乎有序的数组复杂度为O(n), can be used for shell sort.


3. 冒泡排序
- move the largest element to the end of the array everytime


4. Merge sort
- 需要O(n)的空间复杂度
- 小数据使用insertion_sort
- 也可以自底向上归并排序, 可以在nlog(n)时间内对链表进行排序（因为不需要用到数组索引）!!!


5. 快速排序
- 对近乎有序的数组排序效率很差，退化成O(n^2)。解决方案：随机化选择pivot
- 对重复元素多的数组排序效率很差。解决方案：双路（三路）快排
- 双路排序是分出了大于和小于pivot_value的两部分，三路排序是加上了等于pivot_value的部分


6. Heap sort
- shift up
- shift down
- heapify 所有的叶子节点可以看成是最大堆，第一个非叶子节点是最后一个叶子节点的index除以2（index // 2），对每一个非叶子节点（反向）进行shift_down即可
- 一个个插入空堆，时间复杂度是O(nlogn)，heapify是O(n) !!!! 因为上来就抛弃了近乎一半的叶子节点
- 可以原地堆排序优化（空间优化），空间复杂度O(1)
- 现将最大的值放在数组最后一个位置，再与第一个位置交换并shift_down
- 快排额外空间是O(logn)
- 插入，归并是稳定排序；快排和堆排是不稳定排序，可以自定义比较函数，让排序算法不存在稳定性问题。
- 索引堆（Index Heap）新建一个索引数组，不用移动原始数组，而改变索引数组即可（典型的空间换时间策略），适合于复杂元素数组（move cost比较大的）
- 应用场景：动态优先级的情况
- 多路归并排序: 比如4路，每次将4个元素推入堆中，n路归并退化成堆排序
- d叉堆(d-ary heap)：每个元素可以有3个孩子
- 思路：最大最小队列（同时维护一个最大堆和一个最小堆）
- 二项堆，斐波那契堆


7. 二分查找
- 对于有序的数列才能使用二分查找
- floor and ceil


8. 并查集
- 解决的是连接问题（而不是路径问题），少了很多信息，因此可以更高效的回答。
- 并查集的操作时间复杂度近乎是O(1)的


9. Graph
- 无向图（Undirected Graph）
- 有向图（Directed Graph）
- 无权图（Unweighted Graph）
- 有权图（Weighted Graph）
- 图的连通性（图中的点不一定都是连在一起的）
- 自环边（self-loop）
- 平行边（parallel-edges）
- 简单图（没有自环边和平行边）
- 图的表示：邻接矩阵（Adjacency Matrix，适合稠密图）,邻接表（Adjacency Lists，适合稀疏图）
- DFS -> 稀疏图（邻接表）：O(V+E)
- DFS -> 稠密图（邻接矩阵）：O(V^2)
- 广度优先：在加入队列之前时刻判断是否应该加入队列，可以用来找最短距离，先遍历到的点的距离一定小于等于后遍历到的点的距离
- 广度优先复杂度和深度优先的复杂度一致
- flood fill算法（PS抠图）
- 二分图(买方，卖方，路径是达成交易的价格)
- 带权图(weighted graph)


9. Minimum Span Tree
- 是否存在一棵树，能够连接所有的点，并且路径之和最小？
- 带权无向图（连通图）
- 找V-1条边，连接V个顶点，总权值最小
- Cut Property(切分定理),把图中的节点分成两部分，成为一个切分
- 横切边（连接两个切分的边）
- 给定任意切分，横切边中权值最小的边必然属于最小生成树
- Prim算法:从任意一个点开始，加上weight最小的边（到一个最小堆中）和节点，类似贪心思路, 优化后从O(logE)到O(ElogV)
- Kruskal：扫描所有的边（从小到大），只要不能变成环，就是一条边 O(ElogE)


10. 最短路径问题
- 单源最短路径：single source shortest path
- 有权图的松弛操作：找到一条更短的路径（尽管可能多经过了点，更“松”的路径）.
- 每遍历一个点，都考虑一下经过这个点是否可能让路径长度更低。
- dijkstra:有向图单源最短路径算法(图中不能有负权边), O(ElogV),求的是起始点到所有点最短的路径
- 处理负权边（有时候会产生负权环 -> 会导致没有最短路径）
- Bellman-Ford （前提图中不能负权环，但该算法可以判断图中是否有负权环）, O(EV)
- 如果一个图没有负权环，从一点到另一个点的最短路径，最多经过的V个顶点，有V-1条边。否则，存在顶点经过了两次，即存在负权环。
- 依旧找最短的边，但是此时最短边并不能保证全局最短（因为有负权），可以对所有的点进行第二次松弛操作。
- 理论上对所有的点进行V-1次松弛操作，理论上就找到了从原点到其他所有点的最短路径。如果还可以继续松弛，即说明图中有负权环。
- 有向无环图（DAG）可以用拓扑排序O(V+E)
- Floyed算法O(V^3),处理无负权环的图，动态规划思想

11. 杂项
- 分治
- 贪心
- 递归回溯
- DP