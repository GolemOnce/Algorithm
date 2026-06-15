package CodeKata.LV3;

/* [연습문제] 숫자 짝꿍 */

class Solution {
    public String solution(String X, String Y) {
        StringBuilder sb = new StringBuilder();
        
        for (int i = 9; i >= 0; i--) {
            String s = String.valueOf(i);
            int cnt = Math.min(
                X.length() - X.replace(s, "").length(),
                Y.length() - Y.replace(s, "").length()
            );
            for (int j = 0; j < cnt; j++) {
                sb.append(i);
            }
        }
        
        if (sb.length() == 0) return "-1";
        
        String result = sb.toString();
        if (result.charAt(0) == '0') return "0";
        
        return result;
    }
}

// 시간초과
class Solution2 {
    public String solution(String X, String Y) {
        String answer = "";
        for (int i = 9; i > 0; i--) {
            int cnt = Math.min(counting(X, String.valueOf(i)), counting(Y, String.valueOf(i)));
            for (int j = 0; j < cnt; j++) {
                answer += String.valueOf(i);
            }
        }

        if (answer.length() == 0) {
            return "-1";
        } else if (answer.length() == counting(answer, "0")) {
            return "0";
        } else return answer;
    }

    public int counting(String st, String num) {
        int count = (st.length() - st.replaceAll(num, "").length()) / num.length();
        return count;
    }
}