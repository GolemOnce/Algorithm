# [연습문제] 호텔 대실

# 누적합 사용하지 않는 방식으로 하고싶었음

# https://gwon-s.tistory.com/30 참고
def solution(book_time):
    # 분단위(정수형)으로 변환
    def str_to_time(time):
        hr, mi = map(int, time.split(":"))
        return hr * 60 + mi

    # 시작시간, 종료+청소시간 분단위 정수형으로 변환 후 정렬
    book_list = sorted([(str_to_time(start), str_to_time(end) + 10) for start, end in book_time])

    # 방마다 끝나는 시간 저장
    room = [0]

    for start, end in book_list:
        for i in range(len(room)):
            if room[i] <= start:
                room[i] = end
                break
        else:
            room.append(end)

    return len(room)

print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))

# 누적합 (2중 for문)
def solution(book_time):
    time_table = [0 for _ in range(60 * 24)]
    for start, end in book_time:
        start_minutes = 60 * int(start[:2]) + int(start[3:])
        end_minutes = 60 * int(end[:2]) + int(end[3:]) + 10

        if end_minutes > 60 * 24 - 1:
            end_minutes = 60 * 24 - 1

        for i in range(start_minutes, end_minutes):
            time_table[i] += 1
    return max(time_table)

# 누적합 (단일 for문)
def solution3(book_time):
    time_table = [0 for _ in range(60 * 24)]
    for start, end in book_time:
        start_minutes = 60 * int(start[:2]) + int(start[3:])
        end_minutes = 60 * int(end[:2]) + int(end[3:]) + 10

        if end_minutes > 60 * 24 - 1:
            end_minutes = 60 * 24 - 1

        time_table[start_minutes] += 1
        time_table[end_minutes] -= 1
    
    room = 0
    for i in range(len(time_table)):
        room += time_table[i]
        time_table[i] = room

    return max(time_table)

print(solution3([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))
