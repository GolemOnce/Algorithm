# [연습문제] 디펜스 게임

# 보유병사 n명으로 연속되는 적의 공격을 순서대로 막는 게임

# 병사 n명 - 매 라운드 enemy[i]마리 적
# 남은 병사 수 < 다음 라운드 적 수 -> 게임 오버

# 무적권 k번 사용 가능 (병사 소모 x)
# 막을 수 있는 라운드 return. 무적권을 언제 사용할 것인가가 포인트.
# emeny for문 돌면서 크기순 저장, 0보다 작아지는 시점에서 지금까지 중 가장 큰 수 라운드에서 무적권 사용

# 힙큐 사용
import heapq
def solution(n, k, enemy):
    answer = len(enemy)
    q = []

    for round, val in enumerate(enemy):
        n -= val
        heapq.heappush(q, -val) # 가장 큰 수를 활용해야 하기 때문에 음수로 저장 (pop할때 가장 작은 값이 pop됨)
        if n < 0:
            if k > 0:
                n -= heapq.heappop(q) # 음수로 저장했기 때문에 "+="가 아닌 "-="
                k -= 1
            else:
                answer = round
                break

    return answer

print(solution(7, 3, [4, 2, 4, 5, 3, 3, 1]))

# 힙큐를 안다면 매우 쉽게 풀 수 있다
# 하지만 몰랐기 때문에 큐를 직접 구현을 해야하나 생각했었지만, 검색 찬스로 힙큐 사용