package CodeKata.LV2;

/* [연습문제] 문자열 내림차순으로 배치하기 */

import java.util.*;

class Solution {
    public String solution(String s) {
        char[] sList = s.toCharArray();
        Arrays.sort(sList);
        int left = 0, right = sList.length - 1;
        while(left < right) {
            char tmp = sList[left];
            sList[left++] = sList[right];
            sList[right--] = tmp;
        }
        return new String(sList);
    }
}