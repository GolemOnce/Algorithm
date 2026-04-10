# [정렬] H-Index

# enumerate(iterable, start=0) : 속성에서 start = i로 idx 시작점 조절이 가능함(정수 입력만 가능, 람다식X)
def solution(citations):
    answer = 0
    citations.sort(reverse = True)
    for idx, val in enumerate(citations, start = 1):
        if val >= answer:
            answer += 1
            if citations[answer-1] < answer:
                answer -= 1
                break
        else:
            break
    return answer

# 진짜 아이디어 신기하다... 이해는 됨
def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer