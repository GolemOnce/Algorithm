package CodeKata.LV3;

/* [연습문제] 크기가 작은 부분 문자열 */

class Solution {
    public int solution(String t, String p) {
        int answer = 0;
        for (int i = 0; i < t.length() - p.length() + 1; i++) {
            if (Long.parseLong(p) >= Long.parseLong(t.substring(i, i + p.length()))) answer++;
        }
        return answer;
    }
}