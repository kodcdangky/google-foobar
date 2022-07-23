def bellman_ford(times):
    min_cost = [[float("inf") for _ in times] for _ in times]
    previous = [[None for _ in times] for _ in times]
    for index, _ in enumerate(min_cost):
        min_cost[index][index] = 0

    for node, _ in enumerate(times):
        for _ in times[:-1]:
            for step, costs in enumerate(times):
                for dest, cost in enumerate(costs):
                    if min_cost[node][dest] > min_cost[node][step] + cost:
                        min_cost[node][dest] = min_cost[node][step] + cost
                        previous[node][dest] = step

    for step, costs in enumerate(times):
        for dest, cost in enumerate(costs):
            if min_cost[0][dest] > min_cost[0][step] + cost:
                return float("-inf"), None

    return min_cost, previous


def solution(times, time_limit):
    min_cost, previous = bellman_ford(times)
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
                tracer = next_node
                while tracer != node:
                    if tracer in range(1, len(times) - 1):
                        visited.add(tracer)
                    tracer = previous[node][tracer]

                node = next_node
                budget -= cost
                break
        else:
            break
    return sorted(map(lambda node: node - 1, visited))
