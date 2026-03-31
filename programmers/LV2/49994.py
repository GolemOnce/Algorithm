# [Summer/Winter Coding(~2018)] 방문 길이

def solution(dirs):
    visited = set()
    x, y = 0, 0
    for i in dirs:
        px, py = x, y
        if i == 'U' and y < 5:
            y += 1
        elif i == 'D' and y > -5:
            y -= 1
        elif i == 'R' and x < 5 :
            x += 1
        elif i == 'L' and x > -5:
            x -= 1
        else:
            continue
        visited.add(tuple(sorted(((px, py), (x, y)))))
    return len(visited)


# U, D, R, L를 딕셔너리로 정리, 양방향 모두 기록하고 /2하는 아이디어 좋은 듯
def solution(dirs):
    s = set()
    d = {'U': (0,1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    x, y = 0, 0
    for i in dirs:
        nx, ny = x + d[i][0], y + d[i][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            s.add((x,y,nx,ny))
            s.add((nx,ny,x,y))
            x, y = nx, ny
    return len(s)//2
