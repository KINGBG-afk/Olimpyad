"""
Правителството планира изграждането на пътна мрежа, която да свърже всички градове в дадена област.
Всяка двойка градове може да бъде свързана с път, като строителството на всеки път има определена цена.
Целта е да се намери оптималният начин за изграждане на пътната мрежа така, че:

Всички градове да бъдат свързани.

Общите разходи за строителство да бъдат минимални.

Да не се строят излишни пътища (т.е. да се избягват цикли).

Input Format:
Първият ред съдържа едно цяло число t (1≤t≤10) — броят на тестовите случаи.

За всеки тестов случай:
Първият ред съдържа две цели числа n и m (2≤n≤10^4,1≤m≤10^5), където:

n: броят на градовете.

m: броят на възможните пътища между градовете.

Следват m реда, като всеки ред съдържа три цели числа a,b,c:

a и b (0 ≤ a,b

c (1 ≤ c ≤ 10^6): разходът за изграждане на този път.

Constraints

Брой на тестовите случаи:

1 ≤ t ≤ 10

Брой на градовете (върховете):

2 ≤ n ≤ 10^4

Брой на възможните пътища (ребра):

1 ≤ m ≤ 10^5

Номерация на градовете:

0 ≤ a,b

Разход за изграждане на път (тегло на реброто):

1 ≤ c ≤ 10^6

Output Format

За всеки тестов случай изведете:

На първия ред: минималния общ разход за изграждане на пътната мрежа.

На следващите n−1 реда: двойките градове a и b, които са свързани чрез път.

Ако няма начин да се свържат всички градове, изведете -1.

Sample Input 0

1
4 5
0 1 1
0 2 2
0 3 3
1 2 4
2 3 5
Sample Output 0

6
0 1
0 2
0 3
"""


# kurskal algorithm
def connetions(n: int, roads: list[list[int]]) -> tuple[int, list] | tuple[-1, list]:
    roads.sort(key=lambda x: x[2])
    parent = list(range(n))

    def find(x: int) -> int:
        while parent[x] != x:
            x = parent[x]
        return x

    def union(x: int, y: int) -> bool:
        root_x = find(x)
        root_y = find(y)

        if root_x != root_y:
            parent[root_x] = root_y
            return True
        return False

    ls = []
    total_cost = 0

    for city_a, city_b, cost in roads:
        if union(city_a, city_b):
            ls.append((city_a, city_b))
            total_cost += cost

    # check if all cities are conneted
    if len(ls) == n - 1:
        return total_cost, ls
    else:
        return -1, []


t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    # n = cities
    # m = roads

    roads = []

    for _ in range(m):
        city_a, city_b, cost = map(int, input().split())
        roads.append((city_a, city_b, cost))

    total_cost, ls = connetions(n, roads)

    if total_cost == -1:
        print(-1)
    else:
        print(total_cost)

        for city_a, city_b in ls:
            print(city_a, city_b)
