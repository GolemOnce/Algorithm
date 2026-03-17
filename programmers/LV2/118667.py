# [2022 KAKAO TECH INTERNSHIP] 두 큐 합 같게 만들기

# 길이가 같은 2개의 큐.
# 하나를 골라 pop하고 다른 큐에 insert 
# 각 큐의 원소 합이 같을 때까지 반복 횟수
from collections import deque
def solution(queue1, queue2):
    answer = 0
    queue1, queue2 = deque(queue1), deque(queue2)
    sum1 = sum(queue1)
    objective = (sum(queue1) + sum(queue2)) / 2
    limit = (len(queue1) + len(queue2)) * 3 - 3
    while (answer <= limit):
        if sum1 == objective:
            return answer
        if sum1 < objective:
            que2 = queue2.popleft()
            sum1 += que2
            queue1.append(que2)
        else:
            que1 = queue1.popleft()
            sum1 -= que1
            queue2.append(que1)
        answer += 1
        
    return answer if sum1 == objective else -1

print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
print(solution([1, 2, 1, 2], [1, 10, 1, 2]))
print(solution([1, 10, 1, 2], [1, 2, 1, 2]))