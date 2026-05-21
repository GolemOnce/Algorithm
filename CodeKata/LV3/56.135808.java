package CodeKata.LV3;

/* [연습문제] 과일 장수 */

import java.util.*;

class Solution {
    public int solution(int k, int m, int[] score) {
        int answer = 0;
        Arrays.sort(score);
        int idx = score.length - 1;
        int remain = score.length;
        while(remain >= m) {
            answer += score[idx - m + 1] * m;
            idx -= m;
            remain -= m;
        }
        
        return answer;
    }
}