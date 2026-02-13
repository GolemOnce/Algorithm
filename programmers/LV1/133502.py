# [연습문제] 햄버거 만들기

# 정해진 순서(아래서부터, 빵 – 야채 – 고기 - 빵)로 쌓인 햄버거만 포장
# 1,2,3,1 이 되면 빵 제조
# stack에 쌓고 1,2,3,1 되면 pop

def solution(ingredient):
    answer = 0
    stack = []

    for i in ingredient:
        stack.append(i)
        if len(stack) >= 4:
            if stack[-1] == 1 and stack[-2] == 3 and stack[-3] == 2 and stack[-4] == 1:
                for _ in range(4):
                    stack.pop()
                answer += 1

    return answer

print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))
print(solution([1, 3, 2, 1, 2, 1, 3, 1, 2]))

# if문 정제 - 슬라이싱은 인덱스에러 나지 않기 때문에 [-4:]로 바로 접근
def solution2(ingredient):
    answer = 0
    stack = []

    for i in ingredient:
        stack.append(i)
        if stack[-4:] == [1, 2, 3, 1]:
            for _ in range(4):
                stack.pop()
            answer += 1

    return answer
