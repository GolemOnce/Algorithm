# [2022 KAKAO BLIND RECRUITMENT] 주차 요금 계산

# 입차, 출차 기록으로 차량별 주차 요금 계산

from collections import defaultdict
import math
def solution(fees, records):
    answer = []
    dic = defaultdict(list)
    def str_to_time(time):
        hr = int(time[0:2]) * 60
        mi = int(time[3:5])
        return hr + mi
    # 딕셔너리 담기
    for i in records:
        time, car, inout = i.split(' ')
        dic[car] += [time]
    # 기록이 홀수 = out이 없다, '23:59' out 마지막에 추가, 문제에서 in > out 순서 보장해줌
    for key, value in dic.items():
        if len(value) % 2 == 1:
            dic[key].append('23:59')
        parking = 0 # 누적 주차시간
        parking_bill = 0 # 주차 요금

        # 주차기록에 따라 주차시간 누적
        for i in range(len(value) - 1, 0, -2):
            parking += str_to_time(value[i]) - str_to_time(value[i-1])    
        
        # 초과시간 계산
        over = 0        
        if parking >= fees[0]:
            over = parking - fees[0]
            parking -= fees[0]
        parking_bill += fees[1] + math.ceil(over/fees[2]) * fees[3]
        # 차량 번호와 요금 튜플 저장 (정렬용)
        answer.append((key, parking_bill))
    answer.sort(key=lambda x: x[0]) # 차량 번호 기준 정렬
    
    return [i[1] for i in answer] # 1열(요금)만 return
