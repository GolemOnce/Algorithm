package CodeKata.LV3;

/* [연습문제] 기사단원의 무기 */

class Solution {
    public int solution(int number, int limit, int power) {
        int answer = 0;
        for (int i = 1; i < number + 1; i++) {
            int weapon = div(i);
            if (weapon > limit) answer += power;
            else answer += weapon;
        }
        return answer;
    }
        
    public int div(int number) {
        int num = 0;
        for (int i = 1; i < number + 1; i++) {
            if (i*i > number) {
                return num;
            }
            if (i*i == number) {
                num++;
                return num;
            } else if (number % i == 0) {
                num += 2;
            }
        }
        return num;
    }
}