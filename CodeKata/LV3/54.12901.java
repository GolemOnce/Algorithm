package CodeKata.LV3;

/* [연습문제] 2016년 */

class Solution {
    public String solution(int a, int b) {
        String[] answer = {"SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"};
        // 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30
        int[] month = {3, 1, 3, 2, 3, 2, 3, 3, 2, 3, 2};
        int n_add = 0;
        for (int i = 0; i < (a - 1); i++) {
            n_add += month[i];
        }
        
        return answer[(n_add + b + 4) % 7];
    }
}