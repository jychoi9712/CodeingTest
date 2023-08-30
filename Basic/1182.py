# 문제
# N개의 정수로 이루어진 수열이 있을 때, 크기가 양수인 부분수열 중에서 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정수의 개수를 나타내는 N과 정수 S가 주어진다. (1 ≤ N ≤ 20, |S| ≤ 1,000,000) 둘째 줄에 N개의 정수가 빈 칸을 사이에 두고 주어진다. 주어지는 정수의 절댓값은 100,000을 넘지 않는다.

# 출력
# 첫째 줄에 합이 S가 되는 부분수열의 개수를 출력한다.

# 예제 입력 1 
# 5 0
# -7 -3 -2 5 8
# 예제 출력 1 
# 1

import sys
input = sys.stdin.readline

N, S = map(int, input().split())
array = list(map(int,input().split()))
array.sort()
result = []
visited = []
count = 0

def bf(num):
    if sum(result) == S and len(result) != 0:
        # print(result)
        global count
        count += 1

    if len(result)==N:
        return
    
    for i in range(num,N):
        if len(result) != 0:
            if i in visited:
                continue
            if result[len(result)-1] > array[i]:
                continue

        result.append(array[i])
        visited.append(i)
        bf(i)
        visited.pop()
        result.pop()

bf(0)
print(count)