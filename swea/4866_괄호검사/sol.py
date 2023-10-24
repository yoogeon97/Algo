import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(T):
    text = input()
    stack = []
    for i in text:
        if i == "{" or i == "(":
            stack.append(i)
        elif stack and i == "}" and stack[-1] == "{":
            stack.pop()
        elif stack and i == ")" and stack[-1] == "(":
            stack.pop()
        elif i == "}" or i == ")":
            stack.append(i)

    if stack:               # stack의 길이 0이 아닐때 : 오답
        answer = 0          
    else:                   # stack의 길이가 0 : 정답
        answer = 1          

    print(f"#{t+1}", answer)