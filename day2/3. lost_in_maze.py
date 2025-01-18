"""
Един авантюрист се е изгубил в мистериозен лабиринт.
Лабиринтът може да бъде представен като матрица с клетки, където някои клетки са проходими, а други са блокирани.
Целта е авантюристът да намери път от входа до изхода на лабиринта.

Input Format

На първия ред се подава броят на тестовите примери T.
За всеки тест: Първият ред съдържа две числа N и M, указващи съответно броя на редовете и колоните на матрицата на лабиринта.
Следващите N реда съдържат по M символа, където: '.' означава проходима клетка, '#' означава блокирана клетка,
'S' означава началната позиция на авантюриста, 'E' означава изхода на лабиринта.

Constraints

1 ≤ T ≤ 10

1 ≤ N, M ≤ 50

Output Format

За всеки тестов пример, на нов ред, изведете "Yes" ако съществува път от 'S' до 'E', и "No" ако такъв път не съществува.

Sample Input 0

2
3 4
S...
#.#.
...E
3 3
S#E
###
...
Sample Output 0

Yes
No
"""


def lost_in_maze(maze: list, start: tuple[int, int], end: tuple[int, int]) -> str:
    position = [
        (0, -1),
        (-1, 0),
        (1, 0),
        (0, 1),
    ]
    searched = set()
    to_search = [start]

    while to_search:
        current = to_search.pop(0)
        if current == end:
            return "Yes"

        searched.add(current)

        for pos in position:
            nx = current[0] + pos[0]
            ny = current[1] + pos[1]

            if (
                0 <= nx < len(maze)
                and 0 <= ny < len(maze[0])
                and (nx, ny) not in searched
                and maze[nx][ny] != "#"
            ):
                to_search.append((nx, ny))

    return "No"


t = int(input())
results = []

for _ in range(t):
    n, m = map(int, input().split())
    maze = [input().strip() for _ in range(n)]

    start = end = None

    for i in range(n):
        for j in range(m):
            if maze[i][j] == "S":
                start = (i, j)
            if maze[i][j] == "E":
                end = (i, j)

    results.append(lost_in_maze(maze, start, end))

for res in results:
    print(res)
