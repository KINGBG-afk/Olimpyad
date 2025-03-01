"""
Инженер-проектант трябва да определи разстоянието от предложен строителен обект до съществуващ път.
Пътят се представя като отсечка с краища A и B в координатната система,
а обектът е представен като точка X. Ваша задача е да намерите дължината на перпендикуляра от точката X до правата,
на която лежи отсечката AB, независимо дали перпендикулярът пада вътре или извън отсечката.

Input Format

На първия ред се подава числото T — броят на тестовите примери - За всеки тестов пример:
Един ред съдържа 6 цели числа: xA,yA,xB,yB,xX,yX които представляват координатите на точките A, B и X.

Constraints

1≤T≤1000

Output Format

За всеки тестов пример изведете дължината на перпендикуляра от X до AB с точност до два знака след десетичната точка.

Sample Input 0

2 
0 0 4 0 2 3 
1 1 3 3 2 0 
Sample Output 0

3.00 
1.41 
Explanation 0

Първи тест:

Отсечката AB е хоризонтална линия от (0,0) до (4,0), а точката X е (2,3). Разстоянието от точка X до AB е 3.00.

Втори тест:

Отсечката AB е диагонал от (1,1) до (3,3), а точката X е (2,0). Разстоянието е 1.41.

------------------------------------------------------------------------------

OLD CODE:
def min_dist(xA: int, yA: int, xB: int, yB: int, xX: int, yX: int) -> float:
    a = sqrt((xB - xX) ** 2 + (yB - yX) ** 2)
    b = sqrt((xA - xX) ** 2 + (yA - yX) ** 2)
    c = sqrt((xA - xB) ** 2 + (yA - yB) ** 2)

    P = a + b + c

    p = P / 2

    S = sqrt(p * (p - a) * (p - b) * (p - c))
    
    if c == 0:
        return dist((xX, yX), (xA, yA))

    return (2 * S) / c
"""




from math import sqrt
from math import dist


def min_dist(xA: int, yA: int, xB: int, yB: int, xX: int, yX: int) -> float:
    if xA == xB and yA == yB:
        return dist((xX, yX) , (xA, yA))
    numerator = abs((yB - yA) * xX - (xB - xA) * yX + xB * yA - yB * xA)
    denominator = dist((xA, yA), (xB, yB))
    perpendicular_distance = numerator / denominator

    def dot_product(x1: int, y1: int, x2: int, y2: int) -> int:
        return x1 * x2 + y1 * y2

    def vector_length(x: int, y: int) -> float:
        return sqrt(x**2 + y**2)

    ABx = xB - xA
    ABy = yB - yA

    AXx = xX - xA
    AXy = yX - yA

    BXx = xX - xB
    BXy = yX - yB

    dot_product_AB_AX = dot_product(ABx, ABy, AXx, AXy)
    dot_product_AB_AB = dot_product(ABx, ABy, ABx, ABy)

    if dot_product_AB_AX < 0:
        return vector_length(AXx, AXy)
    elif dot_product_AB_AX > dot_product_AB_AB:
        return vector_length(BXx, BXy)

    return perpendicular_distance


res = []
for _ in range(int(input())):
    xA, yA, xB, yB, xX, yX = map(float, input().split())
    res.append(f"{min_dist(xA, yA, xB, yB, xX, yX):.2f}")

for r in res:
    print(r)
