# [Summer/Winter Coding(~2018)] 스킬트리

# 
def solution(skill, skill_trees):
    answer = 0
    for skill_set in skill_trees:
        cur_skill = 0
        able = True
        for sk in skill_set:
            if sk in skill:
                if skill.index(sk) == cur_skill:
                    cur_skill += 1
                else:
                    able = False
                    break
        if able:
            answer += 1
    
    return answer

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))