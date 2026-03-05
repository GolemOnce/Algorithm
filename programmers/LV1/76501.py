# [월간 코드 챌린지 시즌2] 음양 더하기
 
# [4,7,12], [true,false,true] true양수, false 음수

# 한 줄 코딩 각이 나와서 해보았다.
def solution(absolutes, signs):

    return sum(i if j else -i for i, j in zip(absolutes, signs))

print(solution([4,7,12], [True,False,True]))

# 평범하게 했으면 이렇게 했을 듯
def solution(absolutes, signs):
    answer = 0
    for i, j in zip(absolutes,signs):
        if j:
            answer += i
        else:
            answer -= i
    return answer

print(solution([4,7,12], [True,False,True]))