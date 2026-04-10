/* [연습문제] 문자열을 정수로 바꾸기 */

// parseInt쓰면 한 줄 컷 (+,-도 알아서 처리해줌)
class Solution {
    public int solution(String s) {
        return Integer.parseInt(s);
    }
}

// 원리 구현에 가깝게
class Solution {
    public int solution(String s) {
        int answer = 0;
        boolean is_minus = false;
        for (int i = 0; i < s.length(); i++) {
            char number = s.charAt(i);
            if (number == '-') is_minus = true;
            else if (number == '+') continue;
            else answer = answer * 10 + ((int)(number - '0'));
        }
        return (is_minus? -1 : 1) * answer;
    }
}