/* [연습문제] 가운데 글자 가져오기 */

class Solution {
    public String solution(String s) {
        String answer = "";
        int half = s.length() / 2;
        if (s.length() % 2 == 0) {
            answer = s.substring(half - 1, half + 1);
        } else {
            answer = s.substring(half, half + 1);
        }
        return answer;
    }
}

// int/int = int인 점을 활용해 시작인덱스, 끝인덱스 설정 
class Solution2 {
    public String solution(String s) {
        return s.substring((s.length()-1)/2, s.length()/2 + 1);
    }
}