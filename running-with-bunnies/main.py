from copy import deepcopy


def floyd_warshall(times):
    min_cost = deepcopy(times)
    next_in_path = [[None for _ in times] for _ in times]
    for node, _ in enumerate(next_in_path):
        for next_node, _ in enumerate(next_in_path[node]):
            next_in_path[node][next_node] = next_node

    for step, _ in enumerate(min_cost):
        for start, _ in enumerate(min_cost):
            for dest, _ in enumerate(min_cost):
                if min_cost[start][dest] > min_cost[start][step] + min_cost[step][dest]:
                    min_cost[start][dest] = min_cost[start][step] + min_cost[step][dest]
                    next_in_path[start][dest] = next_in_path[start][step]

    for node, _ in enumerate(min_cost):
        if min_cost[node][node] < 0:
            return float("-inf"), None

    return min_cost, next_in_path


def solution(times, time_limit):
    min_cost, next_in_path = floyd_warshall(times)
    if min_cost == float("-inf"):
        return list(range(len(times) - 2))

    visited = set()
    budget = time_limit
    node = 0
    while True:
        for next_node, cost in sorted(
            enumerate(min_cost[node][1:-1], start=1),
            key=lambda index_and_cost: index_and_cost[1],
        ):
            if (
                next_node not in visited
                and budget - cost - min_cost[next_node][-1] >= 0
            ):
                tracer = node
                while True:
                    if tracer in range(1, len(times) - 1):
                        visited.add(tracer)
                    if tracer == next_node:
                        break
                    tracer = next_in_path[tracer][next_node]

                node = next_node
                budget -= cost
                break
        else:
            break
    return sorted(map(lambda node: node - 1, visited))
