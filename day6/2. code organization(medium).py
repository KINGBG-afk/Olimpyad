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
