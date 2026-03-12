# [연습문제] 택배상자

# 1 ~ n 순서로 전달
# 트럭에 싣지 못하면 stack에 저장

# 원본 배열 건드리지 않고 인덱스로만 접근
def solution(order):
    answer = 0
    stack = [0]
    boxes = [0]
    for i in range(len(order),0 , -1):
        boxes.append(i)
    while(boxes[-1] != 0 or stack[-1] == order[answer]):
        if boxes[-1] == order[answer]:
            boxes.pop()
            answer += 1
        elif stack[-1] == order[answer]:
            stack.pop()
            answer += 1
        else:
            stack.append(boxes.pop())
        if answer == len(order):
            break
    return answer

# print(solution([4, 3, 1, 2, 5]))
print(solution([5, 4, 3, 2, 1]))

# 일단 stack으로 옮기고 stack[-1]만 order와 비교
def solution2(order):
    answer = 0

    stack = []
    for i in range(1, len(order) + 1):
        stack.append(i)

        while stack and stack[-1] == order[answer]:
            stack.pop()
            answer += 1

    return answer

print(solution2([5, 4, 3, 2, 1]))
