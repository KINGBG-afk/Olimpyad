"""
В село Мирно живеят двама съседи, чиито настроения винаги са противоположни.
Когато единият е щастлив, другият е тъжен и обратно.
Напишете програма, която по дадени темпераментите на двамата съседи за деня, определя дали те са в противоположни настроения.
Щастието се означава с положителни числа, а тъгата с отрицателни числа.

Жокер:

Задачата да се реши с побитови операции.

Input Format

Програмата трябва да може да обработва при едно изпълнение няколко тестови примера.
Броят T на тестовете ще бъде зададен на първия ред на стандартния вход.
За всеки тестов пример на отделен ред са зададени две цели числа A и B.

Constraints

• 1 ≤ T ≤ 10 • -10^18 < A ≤ 10^18 • -10^18 ≤ B ≤ 10^18

Output Format

За всеки тестов случай програмата трябва да изведе на един ред "Opposite", ако съседите са в противоположни настроения, или "Same", ако настроенията им са еднакви.

Sample Input 0

3
10000000000 -10000000000
9999999999 9999999999
-10000000000 -9999999999
Sample Output 0

Opposite
Same
Same
"""


def opposite(person1: int, person2: int) -> bool:
    if (person1[0] == "-" and person2[0] != "-") or (person2[0] == "-" and person1[0] != "-"):
        return True
    return False
 


t = int(input())

cases = []
for _ in range(t):
    person1, person2 = map(str, input().split())
    cases.append((person1, person2))

for people in cases:
    result = opposite(people[0], people[1])
    
    if result:
        print("Opposite")
    else:
        print("Same")
