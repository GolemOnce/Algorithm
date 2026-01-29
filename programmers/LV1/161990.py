# [연습문제] 바탕화면 정리

# 바탕화면의 상태를 나타낸 문자열 배열 wallpaper
# (세로 좌표, 가로 좌표)로 표현. 빈칸은 ".", 파일이 있는 칸은 "#"
# 최소 드래그 거리 시작점(lux, luy), 끝점 (rdx, rdy) (lux,luy,rdx,rdy) retrun하기
# lux는 row가 가장 작은 거, luy는 col이 가장 작은 거
# rdx는 row가 가장 큰 거 +1 , rdy는 col이 가장 큰 거 + 1

def solution(wallpaper):
    answer = []
    height, width = len(wallpaper), len(wallpaper[0])
    lux, luy, rdx, rdy = height, width, 0, 0

    for row in range(height):
        for col in range(width):
            if wallpaper[row][col] == '#':
                lux, luy, rdx, rdy = min(row, lux), min(col, luy), max(row + 1, rdx), max(col + 1, rdy)
    answer = [lux, luy, rdx, rdy]
    return answer



# 조금 더 최적화 (max, min 대체)
def solution3(wallpaper):
    answer = []
    height, width = len(wallpaper), len(wallpaper[0])
    lux, luy, rdx, rdy = height, width, 0, 0

    for row in range(height):
        for col in range(width):
            if wallpaper[row][col] == '#':
                if row < lux : lux = row
                if col < luy : luy = col
                if row + 1 > rdx : rdx = row + 1
                if col + 1 > rdy : rdy = col + 1
    answer = [lux, luy, rdx, rdy]
    return answer

# pythonic for문 enumerate + if 원소 in 배열
# enumerate()는 (인덱스, 원소) tuple 만들어줌 enumerate(배열, start=1) 처럼 인덱스 조절도 가능
def solution2(wallpaper):
    answer = []
    height, width = len(wallpaper), len(wallpaper[0])
    lux, luy, rdx, rdy = height, width, 0, 0

    for ri, row in enumerate(wallpaper):
        for ci, val in enumerate(row):
            if val == '#':
                if ri < lux : lux = ri
                if ci < luy : luy = ci
                if ri + 1 > rdx : rdx = ri + 1
                if ci + 1 > rdy : rdy = ci + 1
    return [lux, luy, rdx, rdy]


print(solution2([".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."]))