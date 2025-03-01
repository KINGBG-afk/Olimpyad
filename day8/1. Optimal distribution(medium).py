"""
В една компания има n уникални роли, които могат да бъдат разпределени на екипи. Всеки екип трябва да се състои от точно k роли,
като някои от тях могат да се повтарят. Ако бележим екипа като (r1,r2,…,rk), трябва да е r1≤r2≤⋯≤rk.
Вашата задача е да намерите лексикографския номер на даден екип.

Input Format

На първия ред се подават числата n и k, където: n е броят на уникалните роли.
k е броят на ролите в екипа (1≤k≤n+k−1≤30) На втория ред се подават k цели числа r1,r2,…,rk, които представляват идентификаторите на ролите в екипа.
Те са подредени във възходящ ред.

Constraints

0≤ri≤n−1

1≤k≤n+k−1≤30

Output Format

Изведете лексикографския номер на екипа, като номерацията започва от 1.

Sample Input 0

3 2 
1 2 
Sample Output 0

5
Explanation 0

Комбинациите с повторения за {0,1,2} и k=2 в лексикографски ред:

0 0

0 1

0 2

1 1

1 2

2 2 Комбинацията 1 2 е пета поред.

Sample Input 1

4 3 
1 1 3 
Sample Output 1

13
Explanation 1

Комбинациите с повторения за {0,1,2,3}и k=3

0 0 0

0 0 1

0 0 2

0 0 3

0 1 1

0 1 2

0 1 3

0 2 2

0 2 3

0 3 3

1 1 1

1 1 2

1 1 3

Комбинацията 113 е единадесета поред.
"""

from itertools import combinations_with_replacement

def distribution(k: int, pattern: tuple[int]) -> int:
    elem = []
    for comb in combinations_with_replacement(range(k + 1), k):
        elem.append(comb)
        if comb == pattern:
            break
    
    return len(elem)
        
n, k = map(int, input().split())
pattern = tuple(map(int, input().split()))

print(distribution(k, pattern))
