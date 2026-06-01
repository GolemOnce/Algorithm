package CodeKata.LV3;

/* [연습문제] 덧칠하기 */

class Solution {
    public int solution(int n, int m, int[] section) {
        int answer = 0;
        int roller = 0;
        for (int i: section) {
            if (i >= roller) {
                roller = m + i;
                answer++;
            }
        }
        return answer;
    }
}