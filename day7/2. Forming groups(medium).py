"""
В една компания се организира състезание, в което служителите трябва да формират отбори.
Дадени са n служители, всеки със собствено име. Вашата задача е да помогнете на организаторите да изберат всички възможни екипи от точно k души.

Всеки отбор трябва да бъде изведен в лексикографски ред на имената на участниците. Освен това, всички отбори трябва да бъдат сортирани лексикографски.

Input Format

На първия ред се подават две числа n и k (1≤k≤n≤10)

Следват n реда с имената на служителите, по едно име на ред. Имената са стрингове, съставени само от латински букви, с дължина до 20 символа.

Constraints

1≤k≤n≤10

Output Format

Изведете всички възможни екипи от точно k души,
по един на ред. Във всеки ред имената трябва да бъдат подредени лексикографски, а самите редове трябва да бъдат сортирани лексикографски.

Sample Input 0

3 2
Ivan
Ana
Galya
Sample Output 0

Ana Galya
Ana Ivan
Galya Ivan
"""

from itertools import combinations


def generate_teams(n: int, k: int, names: list[str]) -> None:
    names.sort()
    groups = combinations(names, k)

    for group in groups:
        print(" ".join(group))


n, k = map(int, input().split())
names = []
for _ in range(n):
    names.append(input().strip())

generate_teams(n, k, names)
