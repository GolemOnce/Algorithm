# [월간 코드 챌린지 시즌2] 괄호 회전하기

# 특별한거 없음
def solution(s):
    answer = 0
    # 올바른 괄호 문자열 체크
    def is_right(st):
        stack = []
        for i in st:
            if not stack and i in [']', '}', ')']:
                return 0
            if i in ['[', '{', '(']:
                stack.append(i)
            elif i == ']' and stack[-1] == '[':
                stack.pop()
            elif i == '}' and stack[-1] == '{':
                stack.pop()
            elif i == ')' and stack[-1] == '(':
                stack.pop()
            else:
                break
        return 1 if not stack else 0
    # 회전
    for i in range(0, len(s)):
        ro_s = s[i + 1:] + s[0:i + 1]
        answer += is_right(ro_s)
    return answer