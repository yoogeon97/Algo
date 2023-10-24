import sys
sys.stdin = open('input.txt')

T = 10

for test_case in range(1,11):
    result = 0
    houseCount = int(input())
    house = list(map(int , input().split()))
    for i in range(2, houseCount-2):
        arMax = max(house[i-1],house[i-2],house[i+1],house[i+2])
        if house[i] > arMax:
            result += ( house[i] - arMax )

    print("#{} {}".format(test_case,result))