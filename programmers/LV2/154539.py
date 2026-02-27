# [연습문제] 뒤에 있는 큰 수 찾기

# 정수로 이루어진 배열 numbers 주어짐
# 각 원소들에 대해 자신보다 뒤에 있는 숫자 중에서 자신보다 크면서 가장 가까이 있는 수를 '뒷 큰수'라고 함
# 뒷 큰수가 존재하지 않으면 -1
# numbers의 요소 수, 값이 모두 100만 이하라 O(nlogn)까지는 사용 가능할듯
# 브루트 포스(O(n*2))는 시간복잡도 초과로 불가능

# stack 하나 만들어서 보관하는 방식(stack) 생각했었지만 인덱스 아닌 값을 넣는 방식 생각
# 시간복잡도 O(n*n)으로 생각해 하지 않았다.. 
# 생각해보니 stack의 마지막 요소는 무조건 이전 요소 값보다 작기때문에 stack[-1]만 비교하고 넘어가면 O(n) * O(1)으로 해결 가능
# 좀 더 꼼꼼히 생각해 볼 필요가 있을 듯
def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    for idx, val in enumerate(numbers):
        while stack and numbers[stack[-1]] < val:
            answer[stack.pop()] = val
        stack.append(idx)

    return answer