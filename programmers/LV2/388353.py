# [2025 프로그래머스 코드챌린지 1차 예선] 지게차와 크레인

# 세로로 n 줄, 가로로 m줄 총 n x m개
# 알파벳 하나는 접근 가능 컨테이너만, 알파벳 두 개는 그 종류 모든 컨테이너를 꺼냄
# 모든 요청을 순서대로 완료한 후 남은 컨테이너의 수를 return 
# 접근 가능 여부 판단 - BfS?

def fork(storage, container):
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    list = []

    for i in range(1, len(storage) - 1):
        for j in range(1, len(storage[0]) - 1):
            if storage[i][j] == container:
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    if storage[nx][ny] == "0":
                        list.append((i, j))
                        break
    
    for i, j in list:
        storage[i][j] = "0"
        is_outside(storage, i, j)

def crane(storage, container):
    for i in range(1, len(storage) - 1):
        for j in range(1, len(storage[0]) - 1):
            if storage[i][j] == container:
                storage[i][j] = "1"
                is_outside(storage, i, j)

def is_outside(storage, row, col):
    dr, dc = (1, -1, 0 ,0), (0, 0, 1, -1)
    outside = False

    for i in range(4):
        nr, nc = row + dr[i], col + dc[i]
        if storage[nr][nc] == "0":
            storage[row][col] = "0"
            outside = True
            break
    
    if outside:
        for i in range(4):
            nr, nc = row + dr[i], col + dc[i]
            if storage[nr][nc] == '1':
                storage[nr][nc] = '0'
                is_outside(storage, nr, nc)

def solution(storage, requests):
    answer = 0

    storage = [list("0" + i + "0") for i in storage]
    storage.insert(0, list("0" * len(storage[0])))
    storage.append(list("0" * len(storage[0])))

    for i in requests:
        if len(i) == 1:
            fork(storage, i)
        else:
            crane(storage, i[0])

    for i in range(1, len(storage) - 1):
        for j in range(1, len(storage[0]) - 1):
            if storage[i][j] not in ["0", "1"]:
                answer += 1

    return answer

            
print(solution(["AZWQY", "CAABX", "BBDDA", "ACACA"], ["A", "BB", "A"]))