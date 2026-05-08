package CodeKata.LV3;

/* [연습문제] 가장 가까운 같은 글자 */

import java.util.*;

class Solution {
    public int[] solution(String s) {
        int[] answer = new int[s.length()];
        Map <Character, Integer> map = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            char al = s.charAt(i);
            int idx = map.getOrDefault(al, -1);
            if (idx == -1) {
                answer[i] = -1;
            } else {
                answer[i] = i - idx;
            }
            map.put(al, i);
        }
        return answer;
    }
}