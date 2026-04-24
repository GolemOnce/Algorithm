package CodeKata.LV3;

/* [연습문제] 이상한 문자 만들기 */

class Solution {
    public String solution(String s) {
        StringBuilder sb = new StringBuilder();
        int idx = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == ' ') {
                sb.append(" ");
                idx = 0;
            } else {
                sb.append(idx % 2 == 0 ? Character.toUpperCase(s.charAt(i)) : Character.toLowerCase(s.charAt(i)));
                idx += 1;
            }
            System.out.println(sb.toString());
        }
        return sb.toString();
    }
}