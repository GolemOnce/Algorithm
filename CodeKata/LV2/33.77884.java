package CodeKata.LV2;

/* [월간 코드 챌린지 시즌2] 약수의 개수와 덧셈 */

class Solution {
    public int solution(int left, int right) {
        int answer = 0;
        for (int i = left; i < right + 1; i++) {
            if ((int)Math.sqrt(i) == Math.sqrt(i)) {
                answer -= i;
            } else {
                answer += i;
            }
        }
        return answer;
    }
}