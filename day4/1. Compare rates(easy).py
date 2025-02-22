"""
В университет се съхраняват данни за курсовете, които студентите са записали. 
Всеки студент има уникален набор от курсове. 
За целите на академичния анализ, трябва да се направи сравнение между курсовете на двама студенти, за да се види:

Всички курсове, които поне един от студентите е записал.

Курсовете, които и двамата студенти са записали.

Курсовете, които само първият студент е записал.

Курсовете, които са записани от един от студентите, но не и от двамата.

Input Format

На първия ред се подава числото T — брой на тестовите примери )

За всеки тест:

Първият ред съдържа две числа N1 и N2 — броят на курсовете, записани от първия и втория студент

Следващият ред съдържа N1 цели числа — идентификатори на курсовете, записани от първия студент.

Следващият ред съдържа N2 цели числа — идентификатори на курсовете, записани от втория студент.

Constraints

1≤T≤100 1≤N1,N2≤1000

Output Format

За всеки тест изведете четири резултата на нови редове:

Всички курсове, записани от поне един от двамата студенти.

Курсовете, записани и от двамата студенти.

Курсовете, записани само от първия студент.

Курсовете, записани от единия, но не и от другия студент.

Sample Input 0

1 
5 4 
1 2 3 4 5 
3 4 5 6 
Sample Output 0

1 2 3 4 5 6 
3 4 5 
1 2 
1 2 6 
"""

def compare(n1: list[int], n2: list[int]) -> tuple[list[int], list, list, list]:
    set1 = set(n1)
    set2 = set(n2)

    return (
        sorted(set1 | set2),
        sorted(set1 & set2),
        sorted(set1 - set2),
        sorted(set1 ^ set2),
    )


t = int(input())

cases = []
for _ in range(t):
    _, _ = map(str, input().split())
    student1 = list(map(int, input().split()))
    student2 = list(map(int, input().split()))
    cases.append((student1, student2))

for res in cases:
    result = compare(res[0], res[1])
    for r in result:
        print(*r)
