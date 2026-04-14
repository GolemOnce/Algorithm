/* [연습문제] 서울에서 김서방 찾기 */

// String은 객체이기 때문에 "=="로 비교하면 안됨(주소값 비교) 문자열 비교는 .equals()쓰기
// return부분도 +로 문자열 연결 시 문자열 객체를 매번 새로 만들기 때문에 StringBuilder를 쓰는 게 더 좋다.
class Solution {
    public String solution(String[] seoul) {
        String answer = "";
        for (int i = 0; i < seoul.length; i++) {
            if (seoul[i].equals("Kim")) return "김서방은 " + i + "에 있다";
        }
        return answer;
    }
}