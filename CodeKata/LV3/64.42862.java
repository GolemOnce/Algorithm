package CodeKata.LV3;

/* [탐욕법(Greedy)] 체육복 */

import java.util.*;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = 0;
        int[] clothes = new int[n];
        Arrays.fill(clothes, 1);
        for (int i: lost) clothes[i - 1]--;
        for (int i: reserve) clothes[i - 1]++;
        
        for (int i = 0; i < n; i++) {
            if (clothes[i] == 0) {
                // 앞사람
                if (i > 0 && clothes[i - 1] == 2) {
                    clothes[i]++;
                    clothes[i - 1]--;
                // 뒷사람
                } else if (i < n - 1 && clothes[i + 1] == 2) {
                    clothes[i]++;
                    clothes[i + 1]--;
                }
            }
            if (clothes[i] > 0) answer++;
        }
        return answer;
    }
}
