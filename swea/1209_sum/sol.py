import sys
sys.stdin = open('input.txt')

T = 10

for test_case in range(1, 11):
    answer = 0
    t = int(input())

    array = [list(map(int, input().split())) for _ in range(100)]
    # 행렬 전치
    trans_array = list(map(list, zip(*array)))
    # ↘ 대각선의 합
    left_right = sum([array[i][i] for i in range(100)])
    # ↙ 대각선의 합
    right_left = sum([array[i][99 - i] for i in range(100)])

    for i in range(100):
        answer = max(answer, max(sum(array[i]), sum(trans_array[i])))

    answer = max(answer, max(left_right, right_left))

    print('#' + str(test_case), answer)