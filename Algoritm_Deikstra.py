#Первая практическая реализация Алгоритма Дейкстры

def find_lowest_cost_node(cost):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node




graph = {}
# Создаем графы
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2

# пример печати графов
# print(graph['start'].keys())
# print(graph['start']['a'])

graph['a'] = {}
graph['a']['fin'] = 1
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5
graph['fin'] = {}

#хэш таблица стоимостей

infinity = float('inf')
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

# хэш таблица родителей

parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

processed = []

#собственно алгоритм

node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if cost[n] > new_cost:
            cost[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)
