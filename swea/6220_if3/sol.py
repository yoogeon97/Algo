import sys
sys.stdin = open('input.txt')

tc = int(input())

for tc in range(1, T+1):
    char = input()

    if char.islower():
        print(f'#{tc} {char} 는 소문자입니다.')
    else:
        print(f'#{tc} {char} 는 대문자입니다.')