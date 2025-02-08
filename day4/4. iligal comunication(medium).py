"""
В една корпорация съществува сложна мрежа от комуникации между служители. 
Тази мрежа може да бъде представена като неориентиран граф, където всеки връх представлява служител,
а всяко ребро представлява директна комуникация между двама служители.

Компанията подозира, че някои служители са част от незаконна комуникационна верига (цикъл).
Задачата ви е да проверите дали съществува такъв цикъл и, ако съществува, да изведете един от тях.

Input Format

На първия ред се въвеждат две цели числа N и M — броят на служителите и броят на директните комуникации. 
Следват M реда, всеки от които съдържа две цели числа u и v, които представляват, 
че служител u комуникира директно със служител v.

Constraints

1≤N≤100 000

0≤M≤200 000

Гарантира се, че входните данни са валидни.

Output Format

Ако съществува незаконна комуникационна верига (цикъл), изведете "YES" на първия ред.
На втория ред изведете списък с идентификаторите на служителите, образуващи цикъла, започвайки и завършвайки с един и същ служител.

Ако няма цикъл, изведете "NO".

Sample Input 0

6 6 
1 2 
2 3 
3 4 
4 5 
5 2 
5 6 
Sample Output 0

YES 
2 3 4 5 2 
Sample Input 1

4 2 

1 2 

3 4 
Sample Output 1

NO 
"""

class Graph:
    def __init__(self, directed=False) -> None:
        self.directed = directed
        self.adj_list = dict()

    def add_node(self, node) -> None:
        if node not in self.adj_list:
            self.adj_list[node] = set()

    def add_edge(self, from_node, to_node) -> None:
        if from_node not in self.adj_list:
            self.add_node(from_node)
        if to_node not in self.adj_list:
            self.add_node(to_node)

        self.adj_list[from_node].add(to_node)
        if not self.directed:
            self.adj_list[to_node].add(from_node)

    def get_neighbours(self, node):
        return self.adj_list.get(node, set())

    def dfs(self, node, visited, parent, cycle, path) -> bool:
        visited.add(node)
        path.append(node)

        for neighbor in self.get_neighbours(node):
            if neighbor not in visited:
                if self.dfs(neighbor, visited, node, cycle, path):
                    return True
            elif neighbor != parent:
           
                cycle_index = path.index(neighbor)
                cycle.extend(path[cycle_index:])
                cycle.append(neighbor)  
                return True
        path.pop()
        return False

    def find_cycle(self) -> list | None:
        visited = set()
        cycle = []
        path = []

        for node in self.adj_list:
            if node not in visited:
                if self.dfs(node, visited, None, cycle, path):
                    return cycle

        return None

def find_illegal_com(graph: Graph) -> None:
    cycle = graph.find_cycle()

    if cycle:
        print("YES")
        print(" ".join(map(str, cycle)))
    else:
        print("NO")


n, m = map(int, input().split())

graph = Graph()

for _ in range(m):
    line = input().strip()
    if line:
        u, v = map(int, line.split())
        graph.add_edge(u, v)

find_illegal_com(graph)
