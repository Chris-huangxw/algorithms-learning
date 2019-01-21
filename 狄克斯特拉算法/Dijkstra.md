# 狄克斯特拉算法
Dijkstra's 算法包含4个步骤:  
1. 找出最便宜得节点, 即可在最短时间内到达得节点
2. 更新该节点的邻居的开销
3. 重复这个过程直到图中所有的节点都这样做了
4. 计算最终路径
# 例子
起点--(6)-->A  
起点--(2)-->B  
B--(3)-->A  
A--(1)-->终点  
B--(5)-->终点  
## 第一步
找到最便宜的节点, 站在起点可以走到A, 也可以走到B, 但是去往A需要6分钟, 去往B需要2分钟. 去往其他节点的时间还不知道.  
所以先选择去最短路径B节点  
## 第二步
计算经B节点前往其各个邻居所需的时间  
从B节点到A节点的开销为5分钟, 比原来的开销小, 所以更新去A节点的开销为5分钟  
对于B节点的邻居, 如果找到了前往它的更短路径, 那么就更新其开销.  
这里我们发现去往终点的开销变成了7分钟  
## 第三步
重复前面第一步第二步的操作, 直到所有的节点都运行了Dijkstra's 算法
## 第四步
计算最终路径
# 术语
Dijkstra's 算法对于图中每一条边都关联了数字, 这个称为weight.  
带权重的图为加权图, 不带权重的图称为非加权图  
前者可以使用Dijkstra's 算法(仅限于有向无环图), 后者可以使用广度优先搜索  
# 换钢琴
Rama想用一本乐谱换钢琴  
Alex可以用海报换乐谱, 或者用乐谱+5美元换黑胶唱片  
Amy可以用吉他=海报+30美元/黑胶唱片+15美元, 或者黑胶唱片换架子鼓  
Bee可以用钢琴换架子鼓或者吉他  
问Rama如何用最小的代价换到钢琴?  
和之前的步骤一样, 计算每一个节点到各个邻居的开销, 关键理念就是 找到图中最便宜的节点, 并确保没有到该节点的更便宜的路径  
```
乐谱 --> 海报
乐谱 --> 黑胶唱片+5
选择 海报
计算海报邻居的开销
海报 --> 吉他+30
海报 --> 架子鼓+35
选择吉他
吉他 --> 钢琴+40
选择架子鼓
架子鼓 --> 钢琴+35
```
上面的只是一个思路 最终要在每个节点要都要运行Dijkstra's 算法.  
# 负权边
当图的边 weight存在负值的时候, 就不能使用Dijkstra's算法. 因为这个时候会发现已经处理完的节点开销更新了.  
**这个时候需要使用贝尔曼-福德算法**  
# 代码实现
这里我们总共需要三个散列表, 一个存图的信息, 一个存开销信息, 一个存父节点信息  
这里使用例子中的图, 起点、A、B、终点  
```
graph = {}
graph['start']['a'] = 6
graph['start']['b'] = 2
graph['a']['fin'] = 1
graph['b']['a'] = 3
graph['b']['fin'] = 2
graph['fin'] = {}
#终点没有任何邻居
```
我们还需要一个表来存开销信息, 在起点我们直到去往a和b的开销, 但是我们还不知道去往终点的开销所以是无穷大  
```
infinity = float('inf')
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity
```  
一个表用来存放父节点的散列表, 用于选择最终路径  
```
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None
```  
同时我们还需要一个数组来存放已经处理过的节点 **processed = []**  
```python
def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in Processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs)
#在未处理的节点中找出开销最小的节点
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
    #遍历该节点所有的邻居
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    #将当前节点标记为已处理
    node = find_lowest_cost_node(costs)
    #找出接下来要处理的节点
```
# 小节
* 广度优先搜索用于非加权图中查找最短路径
* Dijkstra's算法用于在加权图中查找最短路径
* 仅当权重为正时 Dijkstra's算法才有效
* 如果图中包含负权边, 则需要使用贝尔曼-福德算法
