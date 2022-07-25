from copy import deepcopy
from itertools import permutations


def floyd_warshall(times):
    min_cost = deepcopy(times)

    for step, _ in enumerate(min_cost):
        for start, _ in enumerate(min_cost):
            for dest, _ in enumerate(min_cost):
                if min_cost[start][dest] > min_cost[start][step] + min_cost[step][dest]:
                    min_cost[start][dest] = min_cost[start][step] + min_cost[step][dest]

    for node, _ in enumerate(min_cost):
        if min_cost[node][node] < 0:
            return float("-inf")

    return min_cost


def solution(times, time_limit):
    min_cost = floyd_warshall(times)
    if min_cost == float("-inf"):
        return list(range(len(times) - 2))

    nodes = len(times) - 2
    for visiting in reversed(range(nodes + 1)):
        for path in permutations(range(1, len(times) - 1), visiting):
            last_node = 0
            budget = time_limit
            for node in path:
                budget -= min_cost[last_node][node]
                last_node = node
            budget -= min_cost[last_node][len(times) - 1]
            if budget >= 0:
                return sorted(map(lambda node: node - 1, path))
    return None
