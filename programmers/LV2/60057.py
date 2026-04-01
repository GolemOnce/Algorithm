# [2020 KAKAO BLIND RECRUITMENT] 문자열 압축

def solution(s):
    answer = len(s)
    # 자르는 간격 1 ~ 문자열의 길이//2 설정
    for stride in range(1, ((len(s) + 1) // 2) + 1):
        # 이전 문자열, 중복수 카운트
        com_str = ''
        cnt = 1
        # 현재 문자열
        new_str = ''
        # 자르는 간격(stride) 단위로 for문
        for i in range(0, len(s), stride):
            cur_str = s[i:i + stride]
            # 직전 문자열과 같다면 cnt추가
            if com_str == cur_str:
                com_str = cur_str
                cnt += 1
            # 직전 문자열과 다르면 cnt(2이상일시), 직전 문자열 추가하고 cnt 초기화, 문자열 갱신
            else:
                if cnt > 1:
                    new_str += str(cnt)
                new_str += com_str
                cnt = 1
                com_str = cur_str
        # 자투리 문자열 추가
        if cnt > 1:
            new_str += str(cnt)
        new_str += com_str

        # answer와 만들어진 문자열 길이 비교해서 짧은쪽으로 갱신
        answer = min(answer, len(new_str))
    return answer

# ------------------------------------ #
# 프로그래머스 좋아요 1등 코드
def compress(text, tok_len):
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
    res = []
    cur_word = words[0]
    cur_cnt = 1
    for a, b in zip(words, words[1:] + ['']):
        if a == b:
            cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)

def solution(text):
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])

a = [
    "aabbaccc",
    "ababcdcdababcdcd",
    "abcabcdede",
    "abcabcabcabcdededededede",
    "xababcdcdababcdcd",

    'aaaaaa',
]

for x in a:
    print(solution(x))
