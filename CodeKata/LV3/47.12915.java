package CodeKata.LV3;

/* [연습문제] 문자열 내 마음대로 정렬하기 */

import java.util.*;

class Solution {
    public String[] solution(String[] strings, int n) {
        return Arrays.stream(strings)
                     .sorted(Comparator.comparingInt((String s) -> s.charAt(n))   // 1차 정렬 기준: n번째 문자
                                       .thenComparing(Comparator.naturalOrder())) // 2차 정렬 기준: 전체 문자열 사전순
                     .toArray(String[]::new);
    }
}