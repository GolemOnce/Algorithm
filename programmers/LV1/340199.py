def solution(wallet, bill):
    answer = 0

    while(True):
        if put_in(wallet, bill):
            break
        folding(bill)
        answer += 1
    return answer
    
def put_in(wallet, bill):
    if (wallet[0] >= bill[0] and wallet[1] >= bill[1]) or (wallet[0] >= bill[1] and wallet[1] >= bill[0]):
        return True

def folding(bill):
    if bill[0] > bill[1]:
        bill[0] = bill[0]//2
    else:
        bill[1] = bill[1]//2
    return bill