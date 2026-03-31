# [2020 KAKAO BLIND RECRUITMENT] 괄호 변환

# 뭔가... 뇌빼고 따라가면 된다고 해서 뇌빼고 로직만 짰더니 진짜로 통과가 됨...
def solution(p):
    answer = ''
    # 올바른 문자열 판별
    tmp_str = []
    for i in p:
        if i == '(':
            tmp_str.append(i)
        elif i == ')' and tmp_str:
            tmp_str.pop()
    if not tmp_str:
        return p
    
    # u, v로 쪼개기
    u, v = '', ''
    dic = {'(' : 0, ')' : 0}
    for i in range(len(p)):
        dic[p[i]] += 1
        if dic['('] == dic[')']:
            u = p[0:i + 1]
            v = p[i + 1:]
            break
    # u의 올바름 판별 후, v 재귀
    while(u):
        if u[0] == '(':
            answer += u
            u = ''
            answer += solution(v)
        else:
            tmp = '('
            tmp += solution(v)
            tmp += ')'
            u = u[1:-1]
            for i in u:
                if i == '(':
                    tmp += ')'
                else:
                    tmp += '('
            answer += tmp
            u = ''
    return answer

print(solution("(()())()"))
print(solution("()))((()"))