# [월간 코드 챌린지 시즌1] 쿼드압축 후 개수 세기

# 분할 정복

def solution(arr):
    n = len(arr)

    def quadtree(i, j, k, arr, n, answer):
        key = arr[i][j]

        cut_arr = [arr[x][j:j+k] for x in range(i, i+k)]

        if all(row == [key] * k for row in cut_arr):
            answer[key] += 1
        else:
            k//=2
            quadtree(0, 0, k, cut_arr, n, answer)
            quadtree(k, 0, k, cut_arr, n, answer)
            quadtree(0, k, k, cut_arr, n, answer)
            quadtree(k, k, k, cut_arr, n, answer)

    answer = [0, 0]
    quadtree(0, 0, n, arr, n, answer)

    return answer