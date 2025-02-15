def calcualte_time(stations: list[tuple[int, int, int, int]], stations_num: int, target_t: int) -> None:
    graph = [[] for _ in range(stations_num + 1)]
    unique_costs = sorted(set(C for _, _, C, _ in stations))

    for x, y, c, t in stations:
        graph[x].append((y, c, t))
        graph[y].append((x, c, t))
    
    left = 0
    right = len(unique_costs) - 1
    output = 0
    
    while left <= right:
        mid = (left + right) // 2
        if dijkstra(graph, stations_num, unique_costs[mid], target_t):
            output = unique_costs[mid]
            right = mid - 1
        else:
            left = mid + 1
    
    print(output)


def dijkstra(graph, s: int, max_cost: int, max_time: int) -> bool:
    INF = float("inf")
    times = [INF] * (s + 1)
    times[1] = 0
    pq = [(0, 1)]

    while pq:
        pq.sort()
        current_time, u = pq.pop()
        
        if current_time > times[u]:
            continue
        
        for v, cost, travle_time in graph[u]:
            if cost > max_cost:
                continue
            
            new_time = current_time + travle_time
            if new_time < times[v]:
                times[v] = new_time
                pq.append((new_time, v))
    
    return times[s] <= max_time
    


t = int(input())

for _ in range(t):
    s, l, m = map(int, input().split())
    stations = [tuple(map(int, input().split())) for _ in range(l)]
    calcualte_time(stations, s, m)
        

        