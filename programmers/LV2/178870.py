# [연습문제] 연속된 부분 수열의 합
# 비내림차순으로 정렬된 수열, 기존 수열에서 임의의 두 인덱스의 원소와 그 사이의 원소를 모두 포함하는 부분 수열이어야 합니다.
# 부분 수열의 합은 k, 합이 k인 부분 수열이 여러 개인 경우 길이가 짧은 수열
# 5 <= sequence <= 1,000,000, 5 <= k <= 1,000,000,000
# 2중 반복문 사용시 시간 초과날듯 (브루트포스) -> 투 포인터
# [1, 1, 1, 2, 3, 4, 5], 5
#투 포인터
def solution(sequence, k):
    answer = []
    value, length = 0, len(sequence) + 1
    end = 0  # 투 포인터
    c_length = 1   
    for start in range(len(sequence)):
        c_length -= 1
        while value < k and end < len(sequence):
            value += sequence[end]
            end += 1
            c_length += 1
        # 부분 합이 k, 길이가 더 짧을 때 갱신
        if value == k and c_length < length:
            length = c_length
            answer = [start, end - 1]

        value -= sequence[start]
            
    return answer


# 브루트포스
def wrong_solution(sequence, k):
    answer = []
    value, length = 0, len(sequence) + 1
    for i in range(length):
        value = 0
        for j in range(i, length):
            value += sequence[j]
            c_len = j - i + 1
            if value == k and c_len < length:
                answer = [i, j]
                length = c_len
            elif value > k:
                break
    return answer 


# print(solution([1, 2, 3, 3, 6, 6, 12], 12))
# print(solution([2, 2, 2, 2, 2], 6))
# print(solution([1, 1, 1, 2, 3, 4, 5], 5))
print(solution([1,1,1,1,1,1,1], 7))