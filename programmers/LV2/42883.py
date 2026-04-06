# [탐욕법(Greedy)] 큰 수 만들기

# 그렇게 어려운 문제가 아닌데.. 너무 어렵게 접근했었는듯

def solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)