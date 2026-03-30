# [2019 카카오 개발자 겨울 인턴십] 튜플

# 카카오답게 문제 해석에 시간이 좀 들었다
def solution(s):
    answer = []
    s = s.replace("{{", "").replace("}}", "").split('},{')
    s.sort(key=lambda x: len(x))
    
    for i in s:
        temp = list(map(int, i.split(",")))
        for j in temp:
            if j not in answer:
                answer.append(j)
                
    return answer