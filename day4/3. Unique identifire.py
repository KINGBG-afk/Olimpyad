"""
В онлайн платформа се регистрират N потребители, 
като всяко потребителско име трябва да получи уникален числов идентификатор. 
На платформата съществуват M уникални потребителски имена (M≤N), 
и всяко от тях трябва да бъде съпоставено с уникално число от 0 до M−1. Вашата задача е да напишете програма, която позволява:

Бързо да намерите числовия идентификатор за дадено потребителско име.

Бързо да намерите потребителското име по даден числов идентификатор.

Input Format

На първия ред се подава числото T — броят на тестовите примери (1≤T≤100).

За всеки тест:

На първия ред се подава числото N (1≤N≤10^5) — броят на потребителските имена.

На следващите N реда се въвеждат потребителските имена.

След това:

На следващия ред се подава числото Q — броят на заявки (1≤Q≤10^5).

Следват Q реда, всеки съдържащ или потребителско име, или числов идентификатор.

Constraints

-1≤T≤100
1≤N≤10^5 1≤Q≤10^5

Output Format

За всяка заявка изведете съответното число или низ.

Sample Input 0

1 
10 
Alice 
Bob 
Alice 
Charlie 
Bob 
Diana 
Alice 
Charlie 
Eve 
Diana 
5 
Alice 
0 
4 
Charlie 
3 
Sample Output 0

0
Alice
Eve
2
Diana
Explanation 0

Уникални потребителски имена: Alice, Bob, Charlie, Diana, Eve.

Съпоставяне:

Alice → 0
Bob → 1
Charlie → 2
Diana → 3
Eve → 4

Обработване на заявките:

Потребителското име Alice съответства на числовия идентификатор 0.

Числовият идентификатор 0 съответства на потребителското име Alice.

Числовият идентификатор 4 съответства на потребителското име Eve.

Потребителското име Charlie съответства на числовия идентификатор 2.

Числовият идентификатор 3 съответства на потребителското име Diana.
"""


def identifier(names: list[str], names_nums: list[str]) -> list:
    name_to_id = {name: i for i, name in enumerate(names)}
    id_to_name = {i: name for i, name in enumerate(names)}

    output = []

    for i in names_nums:
        if i.isdigit():
            output.append(id_to_name[int(i)])
        else:
            output.append(name_to_id[i])

    return output


t = int(input())

for _ in range(t):
    n = int(input())

    names = sorted(set(input().strip() for _ in range(n)))

    q = int(input())
    names_nums = [input().strip() for _ in range(q)]

    results = identifier(names, names_nums)
    
    for res in results:
        print(res)
