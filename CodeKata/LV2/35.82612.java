package CodeKata.LV2;

/* [위클리 챌린지] 부족한 금액 계산하기 */

class Solution {
    public long solution(int price, int money, int count) {
        long answer = 0;
        for (int i = 1; i < count + 1; i++) {
            answer += price * i;
        }
        
        return answer < money ? 0 : answer - money;
    }
}

// 등차수열의 합 + Math.max()활용
class Solution2 {
    public long solution(int price, int money, int count) {
        return Math.max(price * ((long)count * ((long)count + 1) / 2) - (long)money, 0);
    }
}