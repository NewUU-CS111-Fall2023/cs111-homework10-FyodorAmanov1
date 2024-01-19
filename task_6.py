import heapq

def network_delay_time(times, n, k):
    graph = {}
    for u, v, w in times:
        if u not in graph:
            graph[u] = []
        graph[u].append((v, w))

    # Dijkstra's algorithm to find shortest paths
    distances = {node: float('inf') for node in range(1, n + 1)}
    distances[k] = 0
    priority_queue = [(0, k)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        if current_node in graph:
            for neighbor, weight in graph[current_node]:
                new_distance = current_distance + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(priority_queue, (new_distance, neighbor))

    max_distance = max(distances.values())

    # Check if all nodes are reachable
    if any(distance == float('inf') for distance in distances.values()):
        return -1

    return max_distance
