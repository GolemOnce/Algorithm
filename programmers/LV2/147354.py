# [연습문제] 테이블 해시 함수

# 2차원 행렬. 열은 컬럼을 나타내고, 행은 튜플
# col번째 컬럼의 값을 기준으로 오름차순 정렬을 하되, 만약 그 값이 동일하면 기본키인 첫 번째 컬럼의 값을 기준으로 내림차순 정렬
# S_i를 i 번째 행의 튜플에 대해 각 컬럼의 값을 i 로 나눈 나머지들의 합으로 정의
# row_begin ≤ i ≤ row_end 인 모든 S_i를 누적하여 bitwise XOR 한 값을 해시 값으로서 반환
# [[2,2,6],[1,5,10],[4,2,9],[3,8,3]], 2, 2, 3
# 4,2,9 -> 2,2,6 -> 1,5,10 -> 3,8,3 S_2 = 2%2 2%2 6%2, S_3 = 1%3 5%3 10%3

def solution(data, col, row_begin, row_end):
    answer = 0

    sorted_data = sorted(data, key=lambda x: (x[col-1], -x[0]))

    for i in range(row_begin, row_end + 1):
        s_i = 0
        for j in sorted_data[i-1]:
            s_i += j % i
        answer = answer ^ s_i
    return answer

print(solution([[2,2,6],[1,5,10],[4,2,9],[3,8,3]], 2, 2, 3))