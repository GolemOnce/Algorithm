/* [연습문제] 콜라츠 추측 */

// int형 오버플로우 -> long캐스팅 필요
class Solution {
    public int solution(long num) {
        int answer = 0;
        while(num != 1) {
            if (answer > 500) return -1;
            if (num % 2 == 0) {
                num /= 2;
            } else {
                num = num * 3 + 1;
            }
            answer++;
        }
        return answer;
    }
}