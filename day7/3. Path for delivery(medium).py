"""
В голям град, една компания за доставки стои пред предизвикателството да оптимизира В голям град,
една компания за доставки се сблъсква с предизвикателството да оптимизира маршрутите на своите куриери.
Ежедневно трябва да се съставя план за доставка на пратки до различни адреси, целящ минимизация на времето за доставка.
Компанията разполага с централен склад и мрежа от улици, които свързват различните квартали на града.
Вашата задача е да изработите ефективен маршрут от склада до всеки адрес.

Input Format

На първия ред се подава броят на тестовите примери T. За всеки тест:

Първият ред съдържа две цели числа N и M, които описват броя на кварталите и броя на улиците съответно.

Следват M реда, всеки от които съдържа три числа U, V и W, описващи улица от квартал U към квартал V с време за преминаване W минути.

Последният ред на всеки тест съдържа числото S, указващо номера на квартала, където се намира складът.

Constraints

1 ≤ T ≤ 10

2 ≤ N ≤ 100

1 ≤ M ≤ 500

1 ≤ U, V ≤ N

1 ≤ W ≤ 100

U ≠ V

Output Format

За всеки тест изведете на стандартния изход минималното общо време в минути,
необходимо за обхождане на всички адреси от склада,използвайки оптимизиран маршрут

Sample Input 0

1
4 4
1 2 5
2 3 2
3 4 8
1 4 10
1
Sample Output 0

22
Explanation 0

Обяснение: Най-кратките пътища от склада (квартал 1) до всеки друг квартал са с обща дължина 22 минути:
от квартал 1 до квартал 2 е 5 минути, до квартал 3 е 7 минути (през квартал 2), и до квартал 4 е 10 минути директно от квартал 1
"""

import heapq


def costs(n, edges, start) -> int:
    graph = {i: [] for i in range(1, n + 1)}
    for u, v, w in edges:
        graph[u].append((w, v))
        graph[v].append((w, u))

    min_heap = [(0, start)]
    distances = {i: float("inf") for i in range(1, n + 1)}
    distances[start] = 0

    while min_heap:
        cur_dist, node = heapq.heappop(min_heap)

        if cur_dist > distances[node]:
            continue

        for cost, neighbor in graph[node]:
            new_dist = cur_dist + cost
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(min_heap, (new_dist, neighbor))

    return sum(distances.values())


for _ in range(int(input())):
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    start = int(input())

    print(costs(n, edges, start))
