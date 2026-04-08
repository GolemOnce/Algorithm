/* [연습문제] 약수의 합 */

class Solution {
    public int solution(int n) {
        int answer = 0;
        double sqrt = Math.sqrt(n);
        for (int i = 1; i < (int)sqrt + 1; i++) {
            if (n % i == 0) {
                answer += i;
                answer += n/i;
            }
        }
        if (sqrt == (int)sqrt) {
            answer -= (int)sqrt;
        }
        
        return answer;
    }
}

class Solution2 {
    public int solution(int n) {
        int answer = 0;
        for (int i = 1; i < n + 1; i++) {
            if (n % i == 0) {
                answer += i;
            }
        }
        return answer;
    }
}