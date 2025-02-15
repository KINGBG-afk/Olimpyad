def invert(num: int, indexes: list[int]) -> int:
    num = bin(num)[2:]
    num = list(num[::-1])

    for i in indexes:
        num[i - 1] = "1" if num[i - 1] == "0" else "0"

    return int("".join(num[::-1]), 2)


for _ in range(int(input())):
    num = int(input())

    indexes = []
    for _ in range(int(input())):
        indexes.append(int(input()))

    print(invert(num, indexes))
