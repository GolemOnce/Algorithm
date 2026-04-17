# [스택/큐] 프로세스

from collections import deque
def solution(priorities, location):
    answer = 0
    last_idx = len(priorities) - 1
    q = deque(priorities)
    while(q):
        p = q.popleft()
        if (all(p >= x for x in q)):
            if location == 0:
                return answer + 1
            else:
                answer += 1
                last_idx -= 1
        else:
            q.append(p)
        location -= 1
        if location < 0:
            location = last_idx
    return answer

# 튜플로 재정의해서 푸는 아이디어 - 생각은 했던 것
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer