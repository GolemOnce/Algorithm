package CodeKata.LV2;

/* [연습문제] 문자열 다루기 기본 */

class Solution {
    public boolean solution(String s) {
        char[] sarr = s.toCharArray();
        int len = sarr.length;
        if (len != 4 && len != 6){
            return false;
        }

        for (int i = 0 ; i < len ; i++){
            if (sarr[i] < '0' || sarr[i] > '9') {
                return false;
            }
         }
        return true;
    }
}

// 정규 표현식 활용
class Solution2 {
  public boolean solution(String s) {
        if (s.length() == 4 || s.length() == 6) return s.matches("(^[0-9]*$)");
        return false;
  }
}