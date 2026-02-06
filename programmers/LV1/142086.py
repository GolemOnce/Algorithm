# [연습문제] 가장 가까운 같은 글자
# s의 각 위치마다 자신보다 앞에 나왔으면서, 자신과 가장 가까운 곳에 있는 같은 글자의 위치

def solution(s):
    answer = []
    dic = {}
    for i,st in enumerate(s): 
        if st not in dic:
            answer.append(-1)
        else:
            answer.append(i - dic[st])
        dic[st] = i
    return answer

print(solution("banana"))