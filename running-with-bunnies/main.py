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

    for node, _ in enumerate(times):
        for step, costs in enumerate(times):
            for dest, cost in enumerate(costs):
                if min_cost[node][dest] > min_cost[node][step] + cost:
                    return float("-inf")

    return min_cost, previous


def solution(times, time_limit):
    min_cost, previous = bellman_ford(times)
    if min_cost == float("-inf"):
        return list(range(len(times) - 2))

    unique_bunnies = set()
    time_remaining = time_limit
    node = 0
    while True:
        for next_node, cost in sorted(
            enumerate(min_cost[node][1:-1], start=1),
            key=lambda index_and_cost: index_and_cost[1],
        ):
            if (
                next_node not in unique_bunnies
                and time_remaining - cost - min_cost[next_node][-1] >= 0
            ):
                tracker_node = next_node
                while tracker_node != node:
                    if tracker_node in range(1, len(times) - 1):
                        unique_bunnies.add(tracker_node)
                    tracker_node = previous[node][tracker_node]

                node = next_node
                time_remaining -= cost
                break
        else:
            break
    return sorted(map(lambda index: index - 1, unique_bunnies))
