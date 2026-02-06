# [2024 KAKAO WINTER INTERNSHIP] 도넛과 막대 그래프
# 도넛 모양 그래프, 막대 모양 그래프, 8자 모양 그래프들
# 1개 이상의 정점, 정점들을 연결하는 방향 간선들로 이루어짐
# 크기가 n인 도넛 모양 그래프는 n개의 정점과 n개의 간선
# 크기가 n인 막대 모양 그래프는 n개의 정점과 n-1개의 간선
# 크기가 n인 8자 모양 그래프는 2n+1개의 정점과 2n+2개의 간선
# 그래프의 간선 정보가 주어지면 생성한 정점의 번호와 정점을 생성하기 전 도넛 모양 그래프의 수, 막대 모양 그래프의 수, 8자 모양 그래프의 수를 구해야 합니다.

# [[2, 3], [4, 3], [1, 1], [2, 1]] -> [2, 1, 1, 0]
# [[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]
#  -> [4, 0, 1, 2]

# 도넛 -> 정점에서 나가는 선 개수 - (막대 + 8자 그래프 수)
# 막대 -> 1개 가고 안옴
# 8자 -> 2개 가고 2 ~ 3개 옴
# 2개 이상 가는데 안돌아오는거 -> 추가 정점
def solution(edges):
    sdic = {}
    edic = {}
    new, stick, eight = 0, 0, 0
    for i in edges:
        sdic[i[0]] = 0
        edic[i[1]] = 0

    for i in edges:
        sdic[i[0]] += 1
        edic[i[1]] += 1

    slist = sorted(sdic.items(), reverse = True)
    elist = sorted(edic.items(), reverse = True)

    loop = max(slist[0][0], elist[0][0])
    for i in range(1, loop + 1):
        if i not in sdic:
            sdic[i] = 0
        if i not in edic:
            edic[i] = 0
            
    for i in range(1, loop + 1):
        if sdic[i] > 1 and edic[i] == 0:
            new = i
        elif sdic[i] == 0 and edic[i] == 1:
            stick += 1
        elif sdic[i] == 2 and edic[i] == 3:
            eight += 1
        elif sdic[i] == 2 and edic[i] == 2:
            eight += 1
    donut = sdic[new] - stick - eight
    return [new, donut, stick, eight]

print(solution([[2, 3], [4, 3], [1, 1], [2, 1]]))


# 온몸 비틀기 최적화... defaultdict함수 활용
from collections import defaultdict

# 지피티
def solution2(edges):
    outdeg = defaultdict(int)
    indeg = defaultdict(int)
    nodes = set()

    for a, b in edges:
        outdeg[a] += 1
        indeg[b] += 1
        nodes.add(a); nodes.add(b)

    new = next(v for v in nodes if indeg[v] == 0 and outdeg[v] >= 2)

    stick = sum(1 for v in nodes if outdeg[v] == 0)

    eight = sum(1 for v in nodes if outdeg[v] == 2 and indeg[v] >= 2)

    donut = outdeg[new] - stick - eight
    return [new, donut, stick, eight]

# 제미나이
def solution3(edges):
    # 정점별 [나가는 수, 들어오는 수]를 저장할 딕셔너리
    # 노드 번호가 100만까지 갈 수 있으므로 리스트 대신 딕셔너리 사용
    counts = {} 
    
    for a, b in edges:
        if a not in counts: counts[a] = [0, 0]
        if b not in counts: counts[b] = [0, 0]
        
        counts[a][0] += 1 # Out-degree 증가
        counts[b][1] += 1 # In-degree 증가
        
    created_node = 0
    donut_cnt = 0
    bar_cnt = 0
    eight_cnt = 0
    
    # 딕셔너리의 키(정점)를 바로 순회 (range 불필요)
    for node, (out_d, in_d) in counts.items():
        # 1. 생성한 정점: 들어오는 건 없고(0), 나가는 건 2개 이상 (문제 조건상 그래프 합 >= 2)
        if in_d == 0 and out_d >= 2:
            created_node = node
        
        # 2. 막대 그래프: 나가는 선이 없는(0) 정점이 존재하면 막대 그래프임
        # (생성 정점이 이 끝점과 연결되어 in_d가 2가 될 수도 있으므로 in_d는 체크하지 않음)
        elif out_d == 0:
            bar_cnt += 1
            
        # 3. 8자 그래프: 나가는 선이 2개인 정점 (단, 생성 정점은 제외)
        # (8자 그래프의 중심점은 항상 out=2, in>=2 입니다)
        elif out_d == 2:
            eight_cnt += 1
            
    # 4. 도넛 그래프: 생성 정점의 총 연결 수 - (막대 수 + 8자 수)
    donut_cnt = counts[created_node][0] - bar_cnt - eight_cnt
    
    return [created_node, donut_cnt, bar_cnt, eight_cnt]