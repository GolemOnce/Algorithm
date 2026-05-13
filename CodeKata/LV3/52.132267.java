package CodeKata.LV3;

/* [연습 문제] 콜라 문제 */

class Solution {
    public int solution(int a, int b, int n) {
        int answer = 0;
        while (n >= a) {
            answer += n / a * b;
            n = n % a + (n / a) * b;
        }
        return answer;
    }
}