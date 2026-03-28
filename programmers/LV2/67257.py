# [2020 카카오 인턴십] 수식 최대화
# 우선순위를 재정의해 절대값이 가장 큰 수 찾기
from itertools import permutations
import copy
def solution(expression):
    answer = 0
    op_list = []
    num_list = []
    tmp_num = ''
    for i in expression:
        if i == '*' or i == '+' or i == '-':
            num_list.append(int(tmp_num))
            tmp_num = ''
            op_list.append(i)
        else:
            tmp_num += i
    num_list.append(int(tmp_num))
    for a, b, c in permutations(['*', '+', '-'], 3):
        cur_op_list = copy.deepcopy(op_list)
        cur_num_list = copy.deepcopy(num_list)
        while(a in cur_op_list):
            idx = cur_op_list.index(a)
            if a == '*':
                cur_num_list[idx] = cur_num_list[idx] * cur_num_list[idx+1]
            elif a == '+':
                cur_num_list[idx] = cur_num_list[idx] + cur_num_list[idx+1]
            else:
                cur_num_list[idx] = cur_num_list[idx] - cur_num_list[idx+1]
            cur_num_list[idx+1] = cur_num_list[idx]
            del cur_num_list[idx]
            del cur_op_list[idx]
        while(b in cur_op_list):
            idx = cur_op_list.index(b)
            if b == '*':
                cur_num_list[idx] = cur_num_list[idx] * cur_num_list[idx+1]
            elif b == '+':
                cur_num_list[idx] = cur_num_list[idx] + cur_num_list[idx+1]
            else:
                cur_num_list[idx] = cur_num_list[idx] - cur_num_list[idx+1]
            cur_num_list[idx+1] = cur_num_list[idx]
            del cur_num_list[idx]
            del cur_op_list[idx]
        while(c in cur_op_list):
            idx = cur_op_list.index(c)
            if c == '*':
                cur_num_list[idx] = cur_num_list[idx] * cur_num_list[idx+1]
            elif c == '+':
                cur_num_list[idx] = cur_num_list[idx] + cur_num_list[idx+1]
            else:
                cur_num_list[idx] = cur_num_list[idx] - cur_num_list[idx+1]
            cur_num_list[idx+1] = cur_num_list[idx]
            del cur_num_list[idx]
            del cur_op_list[idx]
        answer = max(answer, abs(cur_num_list[0]))
    return answer

print(solution("100-200*300-500+20"))

def solution(expression):
    operations = [('+', '-', '*'), ('+', '*', '-'), ('-', '+', '*'), ('-', '*', '+'), ('*', '+', '-'), ('*', '-', '+')]
    answer = []
    for op in operations:
        a = op[0]
        b = op[1]
        temp_list = []
        for e in expression.split(a):
            temp = [f"({i})" for i in e.split(b)]
            temp_list.append(f'({b.join(temp)})')
        answer.append(abs(eval(a.join(temp_list))))
    return max(answer)