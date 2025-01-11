"""
Организатор на събития иска да провери дали записите в неговия дневник са структурирани правилно. Всеки събитиен блок е ограден с кръгли скоби (),
като всяка отваряща скоба трябва да има съответната затваряща. Трябва да се провери дали всеки блок е правилно затворен и последователен.

Input Format:
На първия ред се подава броят на тестовите примери T. За всеки тест:

Единствен ред съдържащ низ от кръгли скоби ().

Constraints

1 ≤ T ≤ 100

Дължината на низа за всеки тест не превишава 100 000 символа.

Output Format

За всеки тест, на нов ред изведете "Valid" ако записите са коректно структурирани или "Invalid", ако има грешки.

Sample Input 0

3
(()(()))
(()())
(()()))(
Sample Output 0

Valid
Valid
Invalid
"""


def is_valid(s: str) -> None:
    stack = []
    brackets_map = {")": "(", "]": "[", "}": "{"}

    for char in s:
        if char in brackets_map:
            top_element = stack.pop() if stack else "#"
            if brackets_map[char] != top_element:
                print("Invalid")
                return
        else:
            stack.append(char)

    print("Valid")


n_strings = int(input())

brackets = []
for _ in range(n_strings):
    s_brackets = input()
    brackets.append(s_brackets)

for string in brackets:
    is_valid(string)
