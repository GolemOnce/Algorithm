# [힙(Heap)] 더 맵게

# heapq에 대한 이해
import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while(True):
        a = heapq.heappop(scoville)
        if a >= K: return answer
        if scoville:
            b = heapq.heappop(scoville)
            c = a + b * 2
            heapq.heappush(scoville, c)
            answer += 1
        else:
            break
    return -1