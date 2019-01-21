#-*-coding:utf8 -*-
def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in Processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

if __name__ == '__main__':
    #新建图
    graph = {}
    graph['start']['a'] = 6
    graph['start']['b'] = 2
    graph['a']['fin'] = 1
    graph['b']['a'] = 3
    graph['b']['fin'] = 2
    graph['fin'] = {}
    #新建开销表
    infinity = float('inf')
    costs = {}
    costs['a'] = 6
    costs['b'] = 2
    costs['fin'] = infinity
    #新建父节点表
    parents = {}
    parents['a'] = 'start'
    parents['b'] = 'start'
    parents['fin'] = None
    #新建一个数组存放处理过的节点
    processed = []
    #在未处理的节点中找出开销最小的节点
    node = find_lowest_cost_node(costs)
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
    #最终路径就是fin到它的父节点 然后依次查询
