# [연습문제] 달리기 경주
# 이름 불리면 추월
# 시작순서 / 추월자

# 딕셔너리 아이디어 바로 생각해냈지만 나를 의심해서 시간 너무 오래 걸림
def solution(players, callings):
    dic = {} # 사람 : 등수

    for i in range (len(players)):
        dic[players[i]] = i

    for i in callings:
        my_rank = dic[i]
        front_man = players[my_rank - 1]

        players[my_rank - 1], players[my_rank] = players[my_rank], players[my_rank - 1]

        dic[i] -= 1
        dic[front_man] += 1
    
    return players

print(solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]))



# 단순하게 생각 - 시간 초과
# > index함수의 시간 복잡도 n(O)(순회하며 찾음) 사실상 2중 for문(보통 10만개 이상 사용X)
# def solution(players, callings):
#     answer = []

#     for i in callings:
#         pi = players.index(i)
#         players[pi-1], players[pi] = players[pi], players[pi-1]
#     answer = players    
#     return answer