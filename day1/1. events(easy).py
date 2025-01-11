"""
В едно училище се организират различни клубни събития и лотарии.
Училището иска да изчисли броя на различните начини, по които могат да бъдат избрани участници за определено събитие и награди за лотарията.
Вие сте назначени да напишете програма, която пресмята броя на възможните комбинации.

Input Format:
На първия ред се задава броят T на тестовите примери 1≤T≤20,000

Всеки тест се състои от един ред с четири цели числа:

P: Броят на участниците, които трябва да бъдат избрани.

R: Броят на наградите, които трябва да бъдат разпределени.

N: Общият брой на наличните участници.

M: Общият брой на наличните награди.

Constraints

1 ≤ T ≤ 20000 — Брой тестови примери.

1 ≤ R,P ≤ 15— Брой избрани събития от общия набор.

1 ≤ N,M ≤ 1000— Общият брой налични събития и подаръци.

Output Format

За всеки тест изведете броя на възможните комбинации от участници и награди.

Sample Input 0

2
3 2 10 5
4 3 20 10
Sample Output 0

1200
581400
"""

import math


def events(tests: list) -> list:
    results = []

    for test in tests:
        P, R, N, M = test

        if P > N or R > M:
            results.append(0)
            continue

        # number of ways to select studens
        ways_to_select = math.factorial(N) // (
            math.factorial(P) * math.factorial(N - P)
        )

        # numbes of ways to distribute rewords
        ways_to_distribute = math.factorial(M) // (
            math.factorial(R) * math.factorial(M - R)
        )

        results.append(ways_to_select * ways_to_distribute)

    return results


T = int(input())

tests = []

for _ in range(T):
    P, R, N, M = map(int, input().split())
    tests.append((P, R, N, M))

for result in events(tests):
    print(result)
