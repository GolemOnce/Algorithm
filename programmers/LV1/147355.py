# [연습문제] 크기가 작은 부분 문자열
# 숫자로 이루어진 문자열 t, p
# t의 부분문자 중 p보다 작은 수가 나오는 횟수 return

def solution(t, p):
    answer = 0
    
    for i in range(len(t) - len(p) + 1):
        if int(t[i:len(p) + i]) <= int(p):
            answer += 1
        
    return answer

print(solution("3141592", "271"))