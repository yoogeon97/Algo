import sys
sys.stdin = open('input.txt')

def paper_cut(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    return paper_cut(n-1) + paper_cut(n-2) * 2

    