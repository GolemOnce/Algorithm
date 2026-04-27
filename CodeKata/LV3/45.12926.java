package CodeKata.LV3;

/* [연습문제] 시저 암호 */

class Solution {
    public String solution(String s, int n) {
        StringBuilder answer = new StringBuilder();
        for (char i: s.toCharArray()) {
            if ((i >= 65) && (i <= 90)) {
                i += n;
                if (i > 90) i -= 26;
            } else if ((i >= 97) && (i <= 122)) {
                i += n;
                if (i > 122) i -= 26;
            }
            answer.append(i);
        }
        return answer.toString();
    }
}