# [2022 KAKAO BLIND RECRUITMENT] 양궁대회

# 라이언vs어피치
# 전 대회 우승자인 라이언 패널티
# 어피치 n발 쏘고 라이언 n발 쏨
# k점을 어피치가 a발 맞추고, 라이언이 b발 맞혔을 때, 더 많은 화살을 k점에 맞힌 선수가 k점을 가져감 a==b인 경우 어피치가 가져감
# 여러발 맞춰도 k점만 가져감

# 어피치가 n발을 다 쏜 상태에서, 라이언이 가장 큰 점수차로 이기기 위한 사격 분포를 구하라
# 어피치의 사격 결과 info[0] = 10점
# dp1
def solution(n, info_A):
    info_L = [0] * 11
    arrow_L = [i+1 for i in info_A[:-1]]
    rate = [[10-index,(2-(hit==1))*(10-index),hit] for index,hit in enumerate(arrow_L)]
    rate.sort(key=lambda x:x[0])    
    dp = [[0,[],11] for _ in range(n+1)]
    for a,b,c in rate:
        for x in range(n,c-1,-1):
            if dp[x-c][0]+b > dp[x][0] or (dp[x-c][0]+b == dp[x][0] and dp[x-c][2] < dp[x][2]):
                dp[x][0] = dp[x-c][0]+b
                dp[x][1] = dp[x-c][1]+[a]
                dp[x][2] = min(dp[x][1])
    for i in dp[n][1]:
        info_L[10-i] = arrow_L[10-i]
    info_L[-1] = n-sum(info_L)        
    answer = sum(((l>a)-(a>l))*(10-index) for index,(a,l) in enumerate(zip(info_A,info_L)))
    return info_L if answer>0 else [-1]

print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))

#dp2
def solution(n, info):
    counterpart_score = sum((10-i) for i in range(10) if info[i])
    # 어피치의 점수의 총합
    dp = [[0,[]] for _ in range(n+1)]
    # 총 점수, 점수를 얻은 칸 위치 리스트 n은 들어간 화살 갯수
    for i in range(10):
        c = info[i]
        # 상대방이 맞춘 화살이 있다면
        if c != 0:
            for j in range(n-c):
                # 내가 점수를 얻어서 상대방의 점수가 줄어든 경우 (10-i) * 2 추가
                if (j==0 or dp[j][0]) and dp[j][0]+2*(10-i)>= dp[j+c+1][0] and 10-i not in dp[j][1]:
                    dp[j+c+1][0] = dp[j][0]+2*(10-i)
                    dp[j+c+1][1]=dp[j][1].copy()
                    dp[j+c+1][1].append(10-i)
        else:
            # 상대방이 맞춘 화살이 없어서 하나만 투자해도 점수를 얻을 수 있는 경우 (10-i) 추가
            for j in range(n):
                if (j==0 or dp[j][0]) and dp[j][0]+(10-i) >= dp[j+1][0] and 10-i not in dp[j][1]:
                    dp[j+1][0] = dp[j][0]+(10-i)
                    dp[j+1][1]=dp[j][1].copy()
                    dp[j+1][1].append(10-i)

    # dp = [[0,[]],[6,[6]],[18,[9]],[24,[9,6]],[34,[9,8]],[40,[9,8,6]]]
    max_comb = max(dp, key= lambda x:x[0])
    if max_comb[0] <= counterpart_score:
        return [-1]

    ans = [0]*11

    for num in max_comb[1]:
        ans[10-num] = info[10-num]+1

    ans[10] = max(0,n-sum(ans))

    return ans

# dfs
def solution(n, info):
    global answer, result

    def score(ryan):
        s = 0
        for i in range(11):
            if ryan[i] == info[i] == 0:
                continue
            if ryan[i] > info[i]:
                s += 10 - i
            else:
                s -= 10 - i
        return s

    def dfs(idx, left, ryan):
        global answer, result
        if idx == -1 and left:
            return
        if left == 0:
            s = score(ryan)
            if result < s:
                answer = ryan[:]
                result = s
            return
        for i in range(left, -1, -1):
            ryan[idx] = i
            dfs(idx-1, left-i, ryan)
            ryan[idx] = 0

    answer = [0 for _ in range(11)]
    result = 0
    dfs(10, n, [0 for _ in range(11)])
    return answer if result != 0 else [-1]