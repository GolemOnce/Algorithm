# t초동안 1초당 x체력회복 t*x, t초 꽉 채우면 +y
# 공격 받으면 체력 닳고 힐 끊김, 체력 0되면 죽음, 최대 체력 있음

def solution(bandage, health, attacks):
    attack_count = 0
    bandage_count = 1
    my_health = health
    for i in range(attacks[-1][0] + 1):
        if i == attacks[attack_count][0]:
            my_health -= attacks[attack_count][1]
            attack_count += 1
            bandage_count = 1
            if my_health <= 0:
                return -1
        else:
            my_health += bandage[1]
            if bandage_count == bandage[0]:
                my_health += bandage[2]
                bandage_count = 0
            bandage_count += 1
            if my_health > health:
                my_health = health
    return my_health


print(solution([1, 1, 1], 5, [[1, 2], [3, 2]]))