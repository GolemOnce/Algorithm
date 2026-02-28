# [월간 코드 챌린지 시즌3] 없는 숫자 더하기
def solution(numbers):
    answer = 0
    for i in range(0, 10):
        if i not in numbers:
            answer += i
    return answer

print(solution([1,2,3,4,6,7,8,0]))

# numbers의 모든 숫자는 다르다는 제한사항... 쉬운 문제도 꼼꼼히 보자
def solution2(numbers):
    return 45 - sum(numbers)

print(solution2([1,2,3,4,6,7,8,0]))